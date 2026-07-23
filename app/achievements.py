"""
achievements.py — Badges, milestones, and titles.

Bro KAHMF tracks your glory and calls you out when you level up.
"""

ACHIEVEMENTS = [
    # ── First Steps ─────────────────────────────────────────────────
    {
        "id": "first_code",
        "name": "Hello, World! 🌍",
        "description": "Submit your first piece of code",
        "icon": "🌍",
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
        "name": "Threepeat 🔥",
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
        "name": "Code Cadet 🎖️",
        "description": "Complete 10 lessons",
        "icon": "🎖️",
        "condition": "lessons_completed >= 10",
        "xp_reward": 150,
    },
    {
        "id": "lessons_25",
        "name": "Senior Dev in Training 💪",
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
    # ── Quirks ──────────────────────────────────────────────────────
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
    {"level": 1, "title": "Script Kiddie", "emoji": "👶"},
    {"level": 3, "title": "Code Explorer", "emoji": "🧭"},
    {"level": 5, "title": "Syntax Samurai", "emoji": "⚔️"},
    {"level": 8, "title": "Loop Master", "emoji": "🔄"},
    {"level": 12, "title": "Function Fanatic", "emoji": "🔧"},
    {"level": 16, "title": "Debug Detective", "emoji": "🔍"},
    {"level": 20, "title": "Algorithm Alchemist", "emoji": "🧪"},
    {"level": 25, "title": "Full Stack Apprentice", "emoji": "📐"},
    {"level": 30, "title": "Code Artisan", "emoji": "🎨"},
    {"level": 40, "title": "System Architect", "emoji": "🏗️"},
    {"level": 50, "title": "Bro KAHMF's Protege", "emoji": "🤝"},
    {"level": 65, "title": "Tech Wizard", "emoji": "🧙"},
    {"level": 80, "title": "Legendary Dev", "emoji": "🌟"},
    {"level": 100, "title": "The KAHMF Himself", "emoji": "👑"},
]


BRO_MESSAGES = {
    "welcome": [
        "YO! Bro KAHMF here! Ready to level up your coding game? 🎮",
        "Ayy, welcome to the dojo! I'm Bro KAHMF — your coding sensei with zero judgment and max hype. 🙌",
        "Hey hey hey! Another future dev in the house! Let's get this bread. 🍞",
    ],
    "perfect": [
        "BRUH. NAILED IT. 🔥🔥🔥 That's how we do!",
        "BOOM! Every test passed. You're not messing around! 💯",
        "HOLY COW that was CLEAN. You're a natural, my friend. 🌟",
        "Wait... did you just... YES YOU DID. Perfect score! I'm taking credit for this. 😎",
    ],
    "good": [
        "Solid work! Some tests passed — we're building momentum! 💪",
        "Not bad at all! Fix a couple things and you'll be golden. 🥇",
        "Progress > perfection. You're moving forward, and that's what counts. 🚀",
        "Hey, Rome wasn't built in a day. Your code, though? Getting there! 🏗️",
    ],
    "fail": [
        "Ayy, don't sweat it! Every error is a lesson in disguise. Let's debug together! 🐛",
        "Bro, I've been coding for YEARS and I still break things daily. Try again! 💪",
        "It's not a fail — it's a first attempt in learning! Let's see what went wrong. 🔍",
        "Remember: the only real failure is giving up. You got this! Try tweaking your approach. 🤝",
    ],
    "level_up": [
        "LEVEL UP! 🎉 You're evolving before my eyes! Next level: {title}!",
        "BOOM! Level {level}! You're officially {title}. That title's gonna look GREAT on a hoodie. 👕",
        "Ding! 🛎️ Level {level} achieved! Welcome to the {title} club. We have cookies (and bugs). 🍪",
    ],
    "streak": [
        "🔥 STREAK ALERT! Day {day}! You're more consistent than my gym attendance (low bar but still).",
        "Day {day} in a row?? You're addicted to learning and I am HERE FOR IT. 🏃‍♂️",
        "Consistency is 🔑 and you're building a KEYCHAINS at this point. Day {day}! 💪",
    ],
    "achievement": [
        "ACHIEVEMENT UNLOCKED: {name}! 🏅 That's {xp} bonus XP! You're a legend!",
        "WOAH! You just unlocked '{name}'! I'm so proud I might cry. 😢 (I won't. But still!)",
        "NEW BADGE: {name}! Your collection is growing! Next stop: world domination. 🌍",
    ],
    "hint": [
        "Okay okay, I'll give you a little help. Don't make it a habit... (jk, ask anytime) 😉",
        "Shh, don't tell anyone I'm giving you hints. Here goes:",
        "A wise person once said... actually it was me, just now. Here's a hint:",
    ],
}


def check_achievements(player_state: dict) -> list:
    """Check which achievements should be unlocked. Returns newly unlocked ones."""
    newly_unlocked = []
    for ach in ACHIEVEMENTS:
        if ach["id"] in player_state.get("achievements", []):
            continue  # already unlocked
        if _evaluate_condition(ach["condition"], player_state):
            newly_unlocked.append(ach)
    return newly_unlocked


def get_title(level: int) -> dict:
    best = TITLES[0]
    for t in TITLES:
        if level >= t["level"]:
            best = t
    return best


def xp_for_level(level: int) -> int:
    """XP required to reach a given level."""
    return int(100 * (level ** 1.5))


def _evaluate_condition(cond: str, state: dict) -> bool:
    # Simple condition evaluator for achievement checks
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
            val = float(val) if '.' in val else val
        if op == ">=":
            return actual >= val
        if op == ">":
            return actual > val
        if op == "==":
            return actual == val
    return False
