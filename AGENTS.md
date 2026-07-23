# Simul8r4BroKahmf — Agent Instructions

## Vision
A gamified, personality-driven coding dojo that makes people WANT to learn.
Built for everyone — absolute beginners to seasoned devs.

## Architecture
- `app/main.py` — FastAPI server
- `app/lab_injector.py` — Lesson/quiz/curriculum definitions
- `app/executor.py` — Multi-language sandboxed execution
- `app/state.py` — Gamified state: XP, streaks, achievements, progress
- `app/achievements.py` — Achievement definitions & unlock logic
- `app/languages.py` — Language configs (Python, JS, pseudo)
- `app/static/index.html` — Full gamified frontend

## Personality
"Bro KAHMF" is your coding mentor. Casual, encouraging, uses fun metaphors,
but teaches real CS concepts. He gives different reactions based on score.

## Gamification
- XP: +10 per test pass, -5 per fail, +5 streak bonus, +50 first-of-day
- Levels: 1-100, each requiring more XP
- Streaks: consecutive days of completing at least 1 lesson
- Achievements: triggered by milestones
- Titles: earned at certain levels

## Accessibility
- WCAG AA contrast ratios
- Semantic HTML + ARIA labels
- Keyboard navigable
- Font size controls
- High-contrast & reduced-motion themes
- Screen reader friendly
