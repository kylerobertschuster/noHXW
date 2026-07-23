"""
achievements.py — Badges, milestones, and career progression titles.

Tracks your growth from Green Bean to The KAHMF.
"""

ACHIEVEMENTS = [
    # ── First Steps ─────────────────────────────────────────────────
    {
        "id": "first_code",
        "name": "First Steps 🚶",
        "description": "Submit your first piece of code",
        "icon": "🚶",
        "condition": "lessons_attempted >= 1",
        "xp_reward": 25,
    },
    {
        "id": "perfect_first",
        "name": "Flawless Debut ✨",
        "description": "Pass every test on your very first lesson",
        "icon": "✨",
        "condition": "perfect_first_lesson",
        "xp_reward": 50,
    },
    # ── Streaks ─────────────────────────────────────────────────────
    {
        "id": "streak_3",
        "name": "Consistency Builder 🔥",
        "description": "3-day coding streak",
        "icon": "🔥",
        "condition": "streak >= 3",
        "xp_reward": 50,
    },
    {
        "id": "streak_7",
        "name": "Weekly Warrior ⚔️",
        "description": "7-day coding streak",
        "icon": "⚔️",
        "condition": "streak >= 7",
        "xp_reward": 150,
    },
    {
        "id": "streak_30",
        "name": "Monthly Legend 🏆",
        "description": "30-day coding streak",
        "icon": "🏆",
        "condition": "streak >= 30",
        "xp_reward": 500,
    },
    # ── Mastery ─────────────────────────────────────────────────────
    {
        "id": "lessons_5",
        "name": "Apprentice 📚",
        "description": "Complete 5 lessons",
        "icon": "📚",
        "condition": "lessons_completed >= 5",
        "xp_reward": 75,
    },
    {
        "id": "lessons_10",
        "name": "Journeyman 🎖️",
        "description": "Complete 10 lessons",
        "icon": "🎖️",
        "condition": "lessons_completed >= 10",
        "xp_reward": 150,
    },
    {
        "id": "lessons_25",
        "name": "Artisan 💪",
        "description": "Complete 25 lessons",
        "icon": "💪",
        "condition": "lessons_completed >= 25",
        "xp_reward": 400,
    },
    # ── Score ───────────────────────────────────────────────────────
    {
        "id": "score_100",
        "name": "Century Club 💯",
        "description": "Reach a score of 100 on any single lesson",
        "icon": "💯",
        "condition": "max_lesson_score >= 100",
        "xp_reward": 100,
    },
    {
        "id": "score_500",
        "name": "High Roller 🎲",
        "description": "Reach a total score of 500",
        "icon": "🎲",
        "condition": "total_score >= 500",
        "xp_reward": 300,
    },
    # ── XP & Levels ─────────────────────────────────────────────────
    {
        "id": "level_5",
        "name": "Getting Started 🚀",
        "description": "Reach level 5",
        "icon": "🚀",
        "condition": "level >= 5",
        "xp_reward": 100,
    },
    {
        "id": "level_10",
        "name": "Double Digits 🔟",
        "description": "Reach level 10",
        "icon": "🔟",
        "condition": "level >= 10",
        "xp_reward": 200,
    },
    {
        "id": "level_25",
        "name": "Quarter Century 🎯",
        "description": "Reach level 25",
        "icon": "🎯",
        "condition": "level >= 25",
        "xp_reward": 500,
    },
    # ── Skills ──────────────────────────────────────────────────────
    {
        "id": "debug_master",
        "name": "Bug Hunter 🐛🔫",
        "description": "Complete a debug-type lesson on first try",
        "icon": "🐛",
        "condition": "debug_first_try",
        "xp_reward": 100,
    },
    {
        "id": "polyglot",
        "name": "Polyglot 🗣️",
        "description": "Try lessons in 2+ languages",
        "icon": "🗣️",
        "condition": "languages_used >= 2",
        "xp_reward": 200,
    },
    {
        "id": "quiz_kid",
        "name": "Trivia Champ 🧠",
        "description": "Pass 5 quiz-type lessons",
        "icon": "🧠",
        "condition": "quizzes_passed >= 5",
        "xp_reward": 150,
    },
]


TITLES = [
    {"level": 1,  "title": "Green Bean",          "emoji": "🫘"},
    {"level": 3,  "title": "Code Padawan",        "emoji": "🌱"},
    {"level": 5,  "title": "Apprentice",          "emoji": "🔧"},
    {"level": 8,  "title": "Junior Engineer",     "emoji": "⚡"},
    {"level": 12, "title": "Developer",           "emoji": "💻"},
    {"level": 16, "title": "Proficient Engineer", "emoji": "⚙️"},
    {"level": 21, "title": "Senior Engineer",     "emoji": "🏗️"},
    {"level": 27, "title": "Staff Engineer",      "emoji": "🧠"},
    {"level": 33, "title": "Principal Engineer",  "emoji": "🎯"},
    {"level": 40, "title": "Distinguished Engineer", "emoji": "🌟"},
    {"level": 50, "title": "Fellow",              "emoji": "👑"},
    {"level": 65, "title": "Chief Technology Officer", "emoji": "🏛️"},
    {"level": 80, "title": "Grand Master",        "emoji": "🧙"},
    {"level": 100,"title": "The KAHMF",           "emoji": "🏆"},
]


LEVEL_UP_MESSAGES = {
    "green_bean": [
        "Hey Green Bean! Welcome to the dojo. Every master was once where you are. Let's get to work. 🌱",
        "A fresh face! Welcome, Green Bean. No pressure — just show up and try. That's all it takes.",
        "Green Bean in the house! Don't worry about what you don't know yet. Focus on what's next.",
    ],
    "padawan": [
        "Level 3 — Code Padawan! The force is stirring. Keep practicing, stay curious. 🌱",
        "You're finding your footing, Padawan. The basics are clicking. Now build on them.",
        "A Padawan rises! You've got the fundamentals taking root. Water them daily.",
    ],
    "apprentice": [
        "Level 5 — Apprentice! You've earned your tools. Now learn to wield them. 🔧",
        "Apprentice status unlocked. You know enough to be dangerous — in a good way. Keep going!",
        "The apprentice becomes the... well, still an apprentice. But a PROMISING one!",
    ],
    "junior": [
        "Level 8 — Junior Engineer! You're making real progress. Production code awaits. ⚡",
        "Junior Engineer in the building! You've got the basics mastered. Time to build something real.",
        "You're not so green anymore. Junior Engineer — own it. You've earned it.",
    ],
    "developer": [
        "Level 12 — Developer! Competent, confident, contributing. This is where it gets fun. 💻",
        "You're a Developer now. The patterns are becoming second nature. Trust your instincts.",
        "Developer level achieved. You can build things that work. That's more than most.",
    ],
    "proficient": [
        "Level 16 — Proficient Engineer! You know your stuff. Others are starting to notice. ⚙️",
        "Proficient. It's not just a title — it's what you've become. Solid fundamentals, sharp instincts.",
        "You've graduated from 'figuring it out' to 'knowing it'. Proficient Engineer status.",
    ],
    "senior": [
        "Level 21 — Senior Engineer! You've seen some things. Built some things. Led some things. 🏗️",
        "Senior. People will come to you for answers now. Be patient. Be kind. Lift as you climb.",
        "Senior Engineer — you've got the experience, the judgment, and the battle scars. Wear them proudly.",
    ],
    "staff": [
        "Level 27 — Staff Engineer! You architect solutions and mentor peers. Your impact multiplies. 🧠",
        "Staff Engineer. You don't just write code — you shape how code gets written. Big influence energy.",
        "The Staff level. You're a force multiplier. Every line you write teaches ten others.",
    ],
    "principal": [
        "Level 33 — Principal Engineer! You shape the technical direction. The roadmap follows you. 🎯",
        "Principal. You see around corners. Your decisions echo across the architecture. Lead wisely.",
        "Principal Engineer — you've transcended 'how' and now ask 'why'. Visionary territory.",
    ],
    "distinguished": [
        "Level 40 — Distinguished Engineer! You push boundaries and set standards. Industry weight. 🌟",
        "Distinguished. Your name carries weight. Your patterns become playbooks. Legend status loading...",
        "You've reached Distinguished Engineer. Conferences want your talks. Companies want your wisdom.",
    ],
    "fellow": [
        "Level 50 — Fellow! Thought leader. Industry influencer. You don't follow trends — you set them. 👑",
        "Fellow. The highest technical recognition. You've shaped not just code, but culture.",
        "You're a Fellow now. Your impact is measured in decades, not sprints. Monumental.",
    ],
    "cto": [
        "Level 65 — Chief Technology Officer! Visionary leader. You build the future. 🏛️",
        "CTO. You lead technology strategy. Your vision shapes products, teams, and markets.",
        "Chief Technology Officer — you've gone from writing code to directing how it's written.",
    ],
    "grand_master": [
        "Level 80 — Grand Master! The wisdom keeper. You've seen generations of technology come and go. 🧙",
        "Grand Master. There's little you haven't encountered. Your mentorship creates dynasties.",
        "You've reached Grand Master. Your knowledge isn't just deep — it's foundational.",
    ],
    "kahmf": [
        "Level 100 — THE KAHMF! 🏆 You've completed the journey. You ARE the mentor now.",
        "You've become The KAHMF. The one who started as a Green Bean is now the legend.",
        "🏆 THE KAHMF. Infinite respect. You've finished what you started. Now help others do the same.",
    ],
}


GENERAL_LEVEL_UP = [
    "⬆️ LEVEL UP! You're level {level} now — {title} {emoji}. That's real growth.",
    "Level {level}! {title} unlocked. {emoji} Keep that momentum going.",
    "Ding! 🛎️ Level {level} achieved. Welcome to the {title} club.",
]


BRO_MESSAGES = {
    "welcome": [
        "Welcome to noHXW! I'm your guide — think of me as a senior dev who's seen it all. Let's get started. 🙌",
        "Hey there! Ready to level up your skills? I'll be here with tips, encouragement, and the occasional dad joke.",
        "Welcome to the platform! Every line of code you write here makes you better. Let's go. 🚀",
    ],
    "perfect": [
        "All tests passed! Clean execution — that's how it's done. 🔥",
        "Perfect score! Every test green. You're building solid instincts.",
        "Nailed it. Every single test passed. That's the mark of someone who pays attention to detail.",
        "Flawless run! You're not just writing code — you're writing correct code. That's the real skill.",
    ],
    "good": [
        "Some tests passed — you're on the right track. A few adjustments and you'll have it. 💪",
        "Progress! Not all green yet, but you're moving in the right direction. Debug and try again.",
        "Getting there! Partial pass — the logic is forming, just a few edge cases to catch.",
        "Good effort! You've got the foundation. Now refine and retry. Every attempt teaches something.",
    ],
    "fail": [
        "No tests passed yet — that's totally fine. Every error is data. Read the feedback and iterate. 💡",
        "Don't sweat it. I've seen senior devs fail tests harder than this. Check the error, adjust, retry.",
        "First attempt didn't stick. No shame in that. Debugging is where the real learning happens.",
        "Not quite there, but you're closer than you think. Read the error messages — they tell you exactly what's wrong.",
    ],
    "streak": [
        "{day} day streak! Consistency is the single best predictor of growth. Keep showing up. 🔥",
        "Day {day}! You're building a habit. That's more important than any single lesson.",
        "{day} days in a row. Discipline beats motivation every time. Well done.",
    ],
    "achievement": [
        "Achievement unlocked: {name}! {icon} That's {xp} bonus XP. You're building an impressive portfolio.",
        "New milestone: {name}! Your dedication is paying off. +{xp} XP. 🏅",
        "Badge earned: {name}. These accomplishments add up. Keep collecting them. +{xp} XP",
    ],
    "hint": [
        "Here's a hint to point you in the right direction. Try not to lean on them too much — the struggle is where you grow. 😉",
        "OK, a little nudge. See if you can take it from here:",
        "Tip coming your way. Use it wisely. The goal is to not need the next one.",
    ],
}


def check_achievements(player_state: dict) -> list:
    """Check which achievements should be unlocked. Returns newly unlocked ones."""
    newly_unlocked = []
    for ach in ACHIEVEMENTS:
        if ach["id"] in player_state.get("achievements", []):
            continue
        if _evaluate_condition(ach["condition"], player_state):
            newly_unlocked.append(ach)
    return newly_unlocked


def get_title(level: int) -> dict:
    """Get the title for a given level."""
    best = TITLES[0]
    for t in TITLES:
        if level >= t["level"]:
            best = t
    return best


def get_level_up_message(level: int, title: str, emoji: str) -> str:
    """Get a level-up message appropriate to the user's tier."""
    import random
    if level == 1:
        msg = random.choice(LEVEL_UP_MESSAGES["green_bean"])
    elif level <= 3:
        msg = random.choice(LEVEL_UP_MESSAGES["padawan"])
    elif level <= 5:
        msg = random.choice(LEVEL_UP_MESSAGES["apprentice"])
    elif level <= 8:
        msg = random.choice(LEVEL_UP_MESSAGES["junior"])
    elif level <= 12:
        msg = random.choice(LEVEL_UP_MESSAGES["developer"])
    elif level <= 16:
        msg = random.choice(LEVEL_UP_MESSAGES["proficient"])
    elif level <= 21:
        msg = random.choice(LEVEL_UP_MESSAGES["senior"])
    elif level <= 27:
        msg = random.choice(LEVEL_UP_MESSAGES["staff"])
    elif level <= 33:
        msg = random.choice(LEVEL_UP_MESSAGES["principal"])
    elif level <= 40:
        msg = random.choice(LEVEL_UP_MESSAGES["distinguished"])
    elif level <= 50:
        msg = random.choice(LEVEL_UP_MESSAGES["fellow"])
    elif level <= 65:
        msg = random.choice(LEVEL_UP_MESSAGES["cto"])
    elif level <= 80:
        msg = random.choice(LEVEL_UP_MESSAGES["grand_master"])
    else:
        msg = random.choice(LEVEL_UP_MESSAGES["kahmf"])
    return msg


def xp_for_level(level: int) -> int:
    return int(100 * (level ** 1.5))


def _evaluate_condition(cond: str, state: dict) -> bool:
    if cond == "perfect_first_lesson":
        return state.get("perfect_first_lesson", False)
    if cond == "debug_first_try":
        return state.get("debug_first_try", False)

    parts = cond.split()
    if len(parts) == 3:
        key, op, val = parts
        actual = state.get(key, 0)
        try:
            val = int(val)
        except:
            val = float(val) if '.' in str(val) else val
        if op == ">=":
            return actual >= val
        if op == ">":
            return actual > val
        if op == "==":
            return actual == val
    return False
