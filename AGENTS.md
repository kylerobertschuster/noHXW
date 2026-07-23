# noHXW — Agent Instructions

## Vision
A gamified, career-progressive coding platform that takes learners from
**Green Bean** to **Principal Engineer** and beyond. Enterprise-ready,
accessible, and genuinely engaging.

## Architecture
- `app/main.py` — FastAPI server
- `app/lab_injector.py` — 21 lessons across 5 tracks (Python, JS, Pseudocode, Challenges, Quizzes)
- `app/executor.py` — Multi-language sandboxed execution
- `app/state.py` — Gamified state: XP, streaks, levels, achievements
- `app/achievements.py` — 15 achievements, 14 career titles with progression messages
- `app/languages.py` — Language configs (Python, JS, Pseudocode)
- `app/static/index.html` — Full gamified frontend with ASCII splash

## Career Progression Titles
1. Green Bean → 3. Code Padawan → 5. Apprentice → 8. Junior Engineer →
12. Developer → 16. Proficient Engineer → 21. Senior Engineer →
27. Staff Engineer → 33. Principal Engineer → 40. Distinguished Engineer →
50. Fellow → 65. CTO → 80. Grand Master → 100. The KAHMF

## Gamification
- XP: +10 per test pass, -5 per fail, +xp_bonus on completion
- Levels: 1-100, each requiring more XP
- Streaks: consecutive days of completing at least 1 lesson
- Achievements: 15 badges triggered by milestones
- Titles: 14 unlockable career titles with unique level-up messages

## Accessibility
- WCAG AA contrast ratios
- Semantic HTML + ARIA labels
- Full keyboard navigation
- Font size controls (10px–28px)
- High-contrast & reduced-motion themes
- Screen reader friendly
