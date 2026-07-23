"""
state.py — Gamified session state with XP, streaks, levels, and achievements.

Every learner's journey is tracked like an RPG character.
"""

import uuid
import time
import math
from typing import Optional


# Daily streak window: 36 hours — gives you a 12-hour grace period
STREAK_WINDOW = 36 * 3600


class Player:
    """A player's full profile — like a character sheet."""

    def __init__(self, player_id: Optional[str] = None):
        self.player_id = player_id or str(uuid.uuid4())[:8]
        self.xp: int = 0
        self.level: int = 1
        self.streak: int = 0
        self.last_active: float = 0.0
        self.total_lessons_attempted: int = 0
        self.total_lessons_completed: int = 0
        self.total_score: int = 0
        self.max_lesson_score: int = 0
        self.languages_used: set = set()
        self.quizzes_passed: int = 0
        self.perfect_first_lesson: bool = False
        self.debug_first_try: bool = False
        self.lesson_progress: dict = {}  # lesson_id -> lesson state
        self.achievements: list = []
        self.unlocked_achievements: list = []  # timestamps
        self.settings: dict = {
            "theme": "dark",
            "font_size": 14,
            "reduce_motion": False,
            "high_contrast": False,
            "sound_enabled": True,
        }

    # ── XP & Levels ─────────────────────────────────────────────────

    def add_xp(self, amount: int):
        self.xp += amount
        new_level = self._calc_level()
        leveled_up = new_level > self.level
        self.level = new_level
        return leveled_up

    def _calc_level(self) -> int:
        # Level = floor((XP / 100) ^ (2/3)) + 1
        if self.xp < 100:
            return 1
        return min(100, int((self.xp / 100) ** (2/3)) + 1)

    # ── Streaks ─────────────────────────────────────────────────────

    def tick_streak(self):
        now = time.time()
        if self.last_active == 0:
            self.streak = 1
        else:
            elapsed = now - self.last_active
            if elapsed <= STREAK_WINDOW:
                # Still within the streak window
                days_diff = int(elapsed / 86400)
                if days_diff >= 1:
                    self.streak += 1
                # If less than a day, streak stays the same
            else:
                self.streak = 1  # Reset
        self.last_active = now

    # ── Lesson Tracking ─────────────────────────────────────────────

    def get_lesson_state(self, lesson_id: str) -> dict:
        if lesson_id not in self.lesson_progress:
            self.lesson_progress[lesson_id] = {
                "score": 0,
                "completed": False,
                "attempts": 0,
                "hints_used": 0,
                "best_score": 0,
                "language": None,
            }
        return self.lesson_progress[lesson_id]

    def record_attempt(self, lesson_id: str, language: str,
                       test_results: list, test_score: int,
                       all_passed: bool, lesson_type: str):
        state = self.get_lesson_state(lesson_id)
        state["attempts"] += 1
        state["language"] = language
        state["score"] += test_score
        state["best_score"] = max(state["best_score"], test_score)

        self.total_score += test_score
        self.max_lesson_score = max(self.max_lesson_score, test_score)
        self.total_lessons_attempted += 1
        self.languages_used.add(language)

        if all_passed:
            state["completed"] = True
            self.total_lessons_completed += 1

            # Perfect first lesson check
            if state["attempts"] == 1 and self.total_lessons_attempted == 1:
                self.perfect_first_lesson = True

            # Debug first try
            if lesson_type == "debug" and state["attempts"] == 1:
                self.debug_first_try = True

            # Quiz tracking
            if lesson_type == "quiz":
                self.quizzes_passed += 1

    # ── Hints ───────────────────────────────────────────────────────

    def use_hint(self, lesson_id: str):
        state = self.get_lesson_state(lesson_id)
        state["hints_used"] += 1
        state["score"] -= 3

    # ── Summary ─────────────────────────────────────────────────────

    def summary(self) -> dict:
        from .achievements import get_title
        title = get_title(self.level)
        return {
            "player_id": self.player_id,
            "xp": self.xp,
            "level": self.level,
            "title": title["title"],
            "title_emoji": title["emoji"],
            "streak": self.streak,
            "lessons_attempted": self.total_lessons_attempted,
            "lessons_completed": self.total_lessons_completed,
            "total_score": self.total_score,
            "languages_used": list(self.languages_used),
            "achievements_count": len(self.achievements),
            "next_level_xp": self._calc_level() + 100,
            "settings": self.settings,
        }


# Global in-memory players
_players: dict[str, Player] = {}


def get_or_create_player(player_id: Optional[str] = None) -> Player:
    if player_id and player_id in _players:
        return _players[player_id]
    p = Player(player_id=player_id)
    _players[p.player_id] = p
    return p


def get_player(player_id: str) -> Optional[Player]:
    return _players.get(player_id)
