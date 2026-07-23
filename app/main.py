"""
main.py — FastAPI server for the gamified coding dojo.

Endpoints:
  All previous endpoints + gamification: XP, streaks, achievements, tracks, wisdom.
"""

from pathlib import Path
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from .lab_injector import get_all_lessons, get_lesson, get_tracks, get_random_wisdom
from .executor import run_test, get_function_name
from .state import get_or_create_player, get_player
from .achievements import check_achievements, get_title, xp_for_level, BRO_MESSAGES
from .languages import get_language_config
import random

app = FastAPI(title="noHXW — No Hardware, No Problem", version="2.0.0", docs_url="/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = Path(__file__).resolve().parent / "static"


# ── Frontend ────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse("<h1>simul8r4brokahmf</h1><p>Frontend loading...</p>")
    return HTMLResponse(index_path.read_text())


# ── Wisdom ──────────────────────────────────────────────────────────────

@app.get("/api/wisdom")
async def wisdom():
    return {"wisdom": get_random_wisdom()}


# ── Player / Session ────────────────────────────────────────────────────

@app.get("/api/player")
async def create_or_get_player(player_id: Optional[str] = None):
    player = get_or_create_player(player_id)
    return {
        "player_id": player.player_id,
        "settings": player.settings,
    }


@app.get("/api/player/{player_id}")
async def get_player_profile(player_id: str):
    player = get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player.summary()


# ── Tracks ──────────────────────────────────────────────────────────────

@app.get("/api/tracks")
async def list_tracks():
    return get_tracks()


# ── Lessons ─────────────────────────────────────────────────────────────

@app.get("/api/lessons")
async def list_lessons(track: Optional[str] = None):
    lessons = get_all_lessons()
    if track:
        lessons = [l for l in lessons if l["track"] == track]
    return lessons


@app.get("/api/lessons/{lesson_id}")
async def lesson_detail(lesson_id: str):
    lesson = get_lesson(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


# ── Submission ──────────────────────────────────────────────────────────

class SubmitPayload(BaseModel):
    player_id: str
    lesson_id: str
    code: str
    language: str = "python"


@app.post("/api/submit")
async def submit_code(payload: SubmitPayload):
    player = get_player(payload.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found. Start a session first!")

    lesson = get_lesson(payload.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    results = []
    test_score = 0
    all_passed = True
    lesson_type = lesson.get("type", "code")

    for test in lesson["tests"]:
        func_name = test.get("target", lesson["id"])
        test_input = test["input"]
        expected = test["expected"]

        result = run_test(
            payload.code, func_name, test_input,
            expected, language=payload.language,
            lesson_type=lesson_type
        )
        results.append(result)

        if result["passed"]:
            test_score += 10
        else:
            test_score -= 5
            all_passed = False

    # Add XP bonus from lesson
    xp_bonus = lesson.get("xp_bonus", 10)
    if all_passed:
        test_score += xp_bonus

    # Track the attempt in player state
    player.record_attempt(
        payload.lesson_id, payload.language,
        results, test_score, all_passed, lesson_type
    )

    # Streak!
    player.tick_streak()

    # Add XP
    xp_gained = test_score if test_score > 0 else 0
    leveled_up = player.add_xp(xp_gained)

    # Check achievements
    new_achievements = check_achievements({
        "lessons_attempted": player.total_lessons_attempted,
        "lessons_completed": player.total_lessons_completed,
        "streak": player.streak,
        "total_score": player.total_score,
        "max_lesson_score": player.max_lesson_score,
        "level": player.level,
        "achievements": player.achievements,
        "perfect_first_lesson": player.perfect_first_lesson,
        "debug_first_try": player.debug_first_try,
        "languages_used": len(player.languages_used),
        "quizzes_passed": player.quizzes_passed,
    })

    for ach in new_achievements:
        player.achievements.append(ach["id"])
        player.add_xp(ach["xp_reward"])

    # Pick a Bro message
    if all_passed:
        bro_msg = random.choice(BRO_MESSAGES["perfect"])
    elif test_score > 0:
        bro_msg = random.choice(BRO_MESSAGES["good"])
    else:
        bro_msg = random.choice(BRO_MESSAGES["fail"])

    # Check for level up message
    level_up_msg = None
    if leveled_up:
        title = get_title(player.level)
        level_up_msg = random.choice(BRO_MESSAGES["level_up"]).format(
            level=player.level, title=title["title"]
        )

    # Streak message
    streak_msg = None
    if player.streak > 1 and player.streak % 1 == 0:
        # Only show streak message occasionally
        if random.random() < 0.3:
            streak_msg = random.choice(BRO_MESSAGES["streak"]).format(day=player.streak)

    # Achievement messages
    achievement_messages = []
    for ach in new_achievements:
        msg = random.choice(BRO_MESSAGES["achievement"]).format(
            name=ach["name"], xp=ach["xp_reward"]
        )
        achievement_messages.append({
            "id": ach["id"],
            "name": ach["name"],
            "description": ach["description"],
            "icon": ach["icon"],
            "message": msg,
        })

    title_info = get_title(player.level)

    return {
        "results": results,
        "score_this_attempt": test_score,
        "xp_gained": xp_gained,
        "all_passed": all_passed,
        "completed": all_passed,
        "player": {
            "level": player.level,
            "title": title_info["title"],
            "title_emoji": title_info["emoji"],
            "xp": player.xp,
            "streak": player.streak,
        },
        "bro_message": bro_msg,
        "level_up_message": level_up_msg,
        "streak_message": streak_msg,
        "new_achievements": achievement_messages,
        "language_config": get_language_config(payload.language),
    }


# ── Hints ───────────────────────────────────────────────────────────────

class HintPayload(BaseModel):
    player_id: str


@app.post("/api/hint/{lesson_id}")
async def get_hint(lesson_id: str, payload: HintPayload):
    player = get_player(payload.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    lesson = get_lesson(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    hints = lesson.get("hints", [])
    state = player.get_lesson_state(lesson_id)
    hint_index = state["hints_used"]

    if hint_index >= len(hints):
        return {"hint": "No more hints! You've squeezed me dry. 😅", "hint_number": hint_index, "total_hints": len(hints)}

    player.use_hint(lesson_id)
    hint = hints[hint_index]
    bro_msg = random.choice(BRO_MESSAGES["hint"])

    return {
        "hint": hint,
        "hint_number": hint_index + 1,
        "total_hints": len(hints),
        "remaining_score": state["score"],
        "bro_message": bro_msg,
    }


# ── Settings ────────────────────────────────────────────────────────────

class SettingsPayload(BaseModel):
    theme: Optional[str] = None
    font_size: Optional[int] = None
    reduce_motion: Optional[bool] = None
    high_contrast: Optional[bool] = None
    sound_enabled: Optional[bool] = None


@app.post("/api/player/{player_id}/settings")
async def update_settings(player_id: str, payload: SettingsPayload):
    player = get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    if payload.theme is not None:
        player.settings["theme"] = payload.theme
    if payload.font_size is not None:
        player.settings["font_size"] = payload.font_size
    if payload.reduce_motion is not None:
        player.settings["reduce_motion"] = payload.reduce_motion
    if payload.high_contrast is not None:
        player.settings["high_contrast"] = payload.high_contrast
    if payload.sound_enabled is not None:
        player.settings["sound_enabled"] = payload.sound_enabled

    return player.settings


# ── Summary ─────────────────────────────────────────────────────────────

@app.get("/api/summary/{player_id}")
async def get_summary(player_id: str):
    player = get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    summary = player.summary()
    # Include lesson-by-lesson breakdown
    lesson_details = []
    for lid, state in player.lesson_progress.items():
        lesson = get_lesson(lid)
        if lesson:
            lesson_details.append({
                "id": lid,
                "title": lesson["title"],
                "score": state["score"],
                "completed": state["completed"],
                "attempts": state["attempts"],
                "hints_used": state["hints_used"],
                "best_score": state["best_score"],
            })

    summary["lesson_details"] = lesson_details
    return summary
