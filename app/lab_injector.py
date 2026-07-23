"""
lab_injector.py — The full K.A.H.M.F. curriculum & beyond.

Tracks:
  🐍 Python Path — from zero to hero
  🟨 JavaScript Journey — web wizardry
  📝 Pseudo Prep — logic without syntax

Lesson types: code, quiz, debug, refactor, fill_blank
"""

LESSONS = [
    # ═══════════════════════════════════════════════════════════════════
    # TRACK 1: 🐍 PYTHON PATH — Absolute Beginner
    # ═══════════════════════════════════════════════════════════════════

    # ── 01: Hello, World! ───────────────────────────────────────────
    {
        "id": "hello_world",
        "track": "🐍 Python Path",
        "track_order": 1,
        "type": "code",
        "title": "01: Hello, World! 🌍",
        "languages": ["python", "pseudocode"],
        "description": (
            'The ancient ritual of every programmer: print "Hello, World!"\n\n'
            "Bro KAHMF says: 'This is like a baby's first word, but for computers. Say hi!'"
        ),
        "starter_code": {
            "python": "def hello_world():\n    # Return the string \"Hello, World!\"\n    pass\n",
            "pseudocode": "# hello_world():\n#   Return \"Hello, World!\"\n",
        },
        "tests": [
            {"input": [], "expected": "Hello, World!"},
        ],
        "hints": [
            "Use `return \"Hello, World!\"` — yes, with the quotes!",
            "Strings need quotes in Python. Both single `'` and double `\"` work.",
        ],
        "xp_bonus": 10,
    },

    # ── 02: Variable Vibes ──────────────────────────────────────────
    {
        "id": "variable_vibes",
        "track": "🐍 Python Path",
        "track_order": 2,
        "type": "code",
        "title": "02: Variable Vibes 🎯",
        "languages": ["python", "javascript", "pseudocode"],
        "description": (
            "Variables are like labeled boxes where you store stuff!\n\n"
            "Create three variables:\n"
            "- `name` = your name as a string\n"
            "- `age` = your age as a number\n"
            "- `height` = your height in meters (float, like 1.75)\n\n"
            "Return them as a list: `[name, age, height]`"
        ),
        "starter_code": {
            "python": "def variable_vibes():\n    # Your variables here\n    pass\n",
            "javascript": "function variable_vibes() {\n    // Your variables here\n}\n",
            "pseudocode": "# variable_vibes():\n#   Set name, age, height\n#   Return them as a list\n",
        },
        "tests": [
            {"input": [], "expected": ["Bro KAHMF", 25, 1.85]},
        ],
        "hints": [
            "Strings: `name = \"YourName\"`",
            "Numbers: `age = 25` (no quotes!)",
            "Floats: `height = 1.75` (with decimal point)",
            "Return a list: `return [name, age, height]`",
        ],
        "xp_bonus": 10,
    },

    # ── 03: String Theory ───────────────────────────────────────────
    {
        "id": "string_theory",
        "track": "🐍 Python Path",
        "track_order": 3,
        "type": "code",
        "title": "03: String Theory 🧵",
        "languages": ["python"],
        "description": (
            "Strings have powers! Write a function that takes a word and returns:\n"
            "1. The word in ALL CAPS\n"
            "2. The word in lowercase\n"
            "3. The length of the word\n"
            "4. The first character\n\n"
            "Return as a list: `[upper, lower, length, first_char]`"
        ),
        "starter_code": "def string_theory(word):\n    # Your string magic here\n    pass\n",
        "tests": [
            {"input": ["KAHMF"], "expected": ["KAHMF", "kahmf", 5, "K"]},
            {"input": ["Bro"], "expected": ["BRO", "bro", 3, "B"]},
        ],
        "hints": [
            "Use `word.upper()` for uppercase, `word.lower()` for lowercase",
            "Use `len(word)` for length",
            "Use `word[0]` for the first character",
        ],
        "xp_bonus": 15,
    },

    # ── 04: Number Crunch ───────────────────────────────────────────
    {
        "id": "number_crunch",
        "track": "🐍 Python Path",
        "track_order": 4,
        "type": "code",
        "title": "04: Number Crunch 🔢",
        "languages": ["python", "javascript", "pseudocode"],
        "description": (
            "Write a function `number_crunch(a, b)` that returns a DICT with:\n"
            "- `'sum'`: a + b\n"
            "- `'diff'`: a - b\n"
            "- `'prod'`: a × b\n"
            "- `'quot'`: a ÷ b (as a float)\n"
            "- `'power'`: a raised to the power of b\n\n"
            "Bro says: 'Math is just spicy pattern recognition.'"
        ),
        "starter_code": {
            "python": "def number_crunch(a, b):\n    # Your calculations here\n    pass\n",
            "javascript": "function number_crunch(a, b) {\n    // Your calculations here\n}\n",
            "pseudocode": "# number_crunch(a, b):\n#   Return {sum: a+b, diff: a-b, ...}\n",
        },
        "tests": [
            {"input": [10, 3], "expected": {"sum": 13, "diff": 7, "prod": 30, "quot": 10/3, "power": 1000}},
            {"input": [2, 8], "expected": {"sum": 10, "diff": -6, "prod": 16, "quot": 0.25, "power": 256}},
        ],
        "hints": [
            "Addition: `a + b`, Subtraction: `a - b`",
            "Multiplication: `a * b`, Division: `a / b`",
            "Power: `a ** b` in Python, `Math.pow(a, b)` in JS",
        ],
        "xp_bonus": 20,
    },

    # ── 05: Truth or Dare ───────────────────────────────────────────
    {
        "id": "truth_or_dare",
        "track": "🐍 Python Path",
        "track_order": 5,
        "type": "code",
        "title": "05: Truth or Dare 🤔",
        "languages": ["python"],
        "description": (
            "Write `truth_or_dare(age)` that returns:\n"
            "- `'You can drive! 🚗'` if age >= 16\n"
            "- `'You can vote! 🗳️'` if age >= 18\n"
            "- `'You're a senior dev! 👴'` if age >= 65\n"
            "- `'You're a kiddo! 👶'` otherwise\n\n"
            "Return ONLY the FIRST matching message (age >= 16 AND age >= 18? Return the 18 one!)"
        ),
        "starter_code": "def truth_or_dare(age):\n    # Your logic here\n    pass\n",
        "tests": [
            {"input": [10], "expected": "You're a kiddo! 👶"},
            {"input": [16], "expected": "You can drive! 🚗"},
            {"input": [18], "expected": "You can vote! 🗳️"},
            {"input": [25], "expected": "You can vote! 🗳️"},
            {"input": [70], "expected": "You're a senior dev! 👴"},
        ],
        "hints": [
            "Use `if` / `elif` / `else` — check the BIGGEST age first (65), then 18, then 16, then else.",
            "Order matters! Check 65 first, then 18, then 16, then else.",
        ],
        "xp_bonus": 25,
    },

    # ── 06: Loop Dreams ─────────────────────────────────────────────
    {
        "id": "loop_dreams",
        "track": "🐍 Python Path",
        "track_order": 6,
        "type": "code",
        "title": "06: Loop Dreams 🔄",
        "languages": ["python", "javascript"],
        "description": (
            "Write `loop_dreams(n)` that returns a dict:\n"
            "- `'numbers'`: list from 1 to n\n"
            "- `'evens'`: list of even numbers from 1 to n\n"
            "- `'squares'`: dict where key=number, value=number²\n"
            "- `'sum'`: sum of all numbers from 1 to n\n\n"
            "Bro says: 'Loops are like groundhog day, but productive!'"
        ),
        "starter_code": {
            "python": "def loop_dreams(n):\n    # Your loops here\n    pass\n",
            "javascript": "function loop_dreams(n) {\n    // Your loops here\n}\n",
        },
        "tests": [
            {"input": [5], "expected": {"numbers": [1,2,3,4,5], "evens": [2,4], "squares": {1:1,2:4,3:9,4:16,5:25}, "sum": 15}},
            {"input": [3], "expected": {"numbers": [1,2,3], "evens": [2], "squares": {1:1,2:4,3:9}, "sum": 6}},
        ],
        "hints": [
            "Use `range(1, n + 1)` for numbers 1 through n",
            "Check even: `x % 2 == 0`",
            "Build the squares dict: `squares[x] = x ** 2`",
            "Sum: use `sum(numbers)` or accumulate in the loop",
        ],
        "xp_bonus": 30,
    },

    # ── 07: List-icool ──────────────────────────────────────────────
    {
        "id": "listicool",
        "track": "🐍 Python Path",
        "track_order": 7,
        "type": "code",
        "title": "07: List-icool 📋",
        "languages": ["python"],
        "description": (
            "Write `listicool(items)` that takes a list of numbers and returns:\n"
            "- `'first'`: first element\n"
            "- `'last'`: last element\n"
            "- `'sorted'`: the list sorted ascending\n"
            "- `'reversed'`: the list reversed\n"
            "- `'middle'`: remove first AND last, return the rest\n"
            "- `'has_duplicates'`: True if any value appears more than once"
        ),
        "starter_code": "def listicool(items):\n    # Your list magic\n    pass\n",
        "tests": [
            {"input": [[3, 1, 4, 1, 5]], "expected": {"first": 3, "last": 5, "sorted": [1,1,3,4,5], "reversed": [5,1,4,1,3], "middle": [1,4,1], "has_duplicates": True}},
            {"input": [[7, 2, 9]], "expected": {"first": 7, "last": 9, "sorted": [2,7,9], "reversed": [9,2,7], "middle": [2], "has_duplicates": False}},
        ],
        "hints": [
            "First: `items[0]`, Last: `items[-1]`",
            "Sorted: `sorted(items)`, Reversed: `list(reversed(items))` or `items[::-1]`",
            "Middle: `items[1:-1]` (slicing!)",
            "Check duplicates: `len(items) != len(set(items))`",
        ],
        "xp_bonus": 35,
    },

    # ── 08: Dictionary Dazzle ───────────────────────────────────────
    {
        "id": "dict_dazzle",
        "track": "🐍 Python Path",
        "track_order": 8,
        "type": "code",
        "title": "08: Dictionary Dazzle 📖",
        "languages": ["python"],
        "description": (
            "Write `dict_dazzle(records)` that takes a list of (name, score) tuples.\n"
            "Return a dict:\n"
            "- `'passed'`: names with score >= 50\n"
            "- `'failed'`: names with score < 50\n"
            "- `'average'`: average score (rounded to 1 decimal)\n"
            "- `'top_student'`: name of the person with the highest score\n"
            "- `'honors'`: count of students with score >= 80"
        ),
        "starter_code": "def dict_dazzle(records):\n    # Your analysis here\n    pass\n",
        "tests": [
            {"input": [[("Alice",95),("Bob",42),("Charlie",78),("Diana",88)]], "expected": {"passed":["Alice","Charlie","Diana"],"failed":["Bob"],"average":75.8,"top_student":"Alice","honors":3}},
            {"input": [[("Eve",30),("Frank",49)]], "expected": {"passed":[],"failed":["Eve","Frank"],"average":39.5,"top_student":"Eve","honors":0}},
        ],
        "hints": [
            "Loop through records: `for name, score in records:`",
            "Use `round(average, 1)` for one decimal place",
            "Find top student: track max score and corresponding name",
        ],
        "xp_bonus": 40,
    },

    # ── 09: Function Junction ────────────────────────────────────────
    {
        "id": "function_junction",
        "track": "🐍 Python Path",
        "track_order": 9,
        "type": "code",
        "title": "09: Function Junction 🔧",
        "languages": ["python"],
        "description": (
            "Write `function_junction(x)` that:\n"
            "1. Defines INNER function `double(n)` that returns n * 2\n"
            "2. Defines INNER function `triple(n)` that returns n * 3\n"
            "3. Returns a dict with:\n"
            "   - `'doubled'`: double(x)\n"
            "   - `'tripled'`: triple(x)\n"
            "   - `'applied'`: apply both: double(triple(x))\n\n"
            "Bro says: 'Functions inside functions? That's function-ception!'"
        ),
        "starter_code": "def function_junction(x):\n    # Define your inner functions\n    pass\n",
        "tests": [
            {"input": [5], "expected": {"doubled": 10, "tripled": 15, "applied": 30}},
            {"input": [10], "expected": {"doubled": 20, "tripled": 30, "applied": 60}},
        ],
        "hints": [
            "Define `def double(n): return n * 2` INSIDE function_junction",
            "Define `def triple(n): return n * 3` inside too",
            "Call them: `double(x)`, `triple(x)`, `double(triple(x))`",
        ],
        "xp_bonus": 35,
    },

    # ── 10: Error? I Barely Know Her! ───────────────────────────────
    {
        "id": "error_handling",
        "track": "🐍 Python Path",
        "track_order": 10,
        "type": "code",
        "title": "10: Error? I Barely Know Her! 🛡️",
        "languages": ["python"],
        "description": (
            "Write `safe_divide(a, b)` that:\n"
            "- Returns `a / b` normally\n"
            "- If `b` is 0, returns `\"Can't divide by zero, bro! 🤯\"`\n"
            "- If `a` or `b` is a string, returns `\"Numbers only, please! 🔢\"`\n\n"
            "Use try/except! Don't use if/else for the zero check."
        ),
        "starter_code": "def safe_divide(a, b):\n    # Try to divide, catch errors\n    pass\n",
        "tests": [
            {"input": [10, 2], "expected": 5.0},
            {"input": [10, 0], "expected": "Can't divide by zero, bro! 🤯"},
            {"input": [10, "hi"], "expected": "Numbers only, please! 🔢"},
        ],
        "hints": [
            "Use `try:` to attempt `a / b`",
            "Catch `ZeroDivisionError` for division by zero",
            "Catch `TypeError` for wrong types",
        ],
        "xp_bonus": 40,
    },

    # ── 11: Debug: Broken Calculator ─────────────────────────────────
    {
        "id": "debug_calc",
        "track": "🐍 Python Path",
        "track_order": 11,
        "type": "debug",
        "title": "11: DEBUG: Broken Calculator 🐛🔧",
        "languages": ["python"],
        "description": (
            "This code is SUPPOSED to add two numbers and return the result.\n"
            "But it's BROKEN. Fix the bugs!\n\n"
            "Bro says: 'Debugging is like being a detective in a crime movie "
            "where YOU are also the criminal.'"
        ),
        "starter_code": "def broken_add(a, b):\n    result = a - b  # <- BUG! Wrong operator\n    print(\"The result is\" result)  # <- BUG! Missing comma\n    return result\n    print(\"Done!\")  # <- BUG! Unreachable code\n",
        "tests": [
            {"input": [3, 5], "expected": 8},
            {"input": [10, 20], "expected": 30},
        ],
        "hints": [
            "Hint 1: Look at the operator on line 2. Are we adding or subtracting?",
            "Hint 2: The print statement needs a comma between its arguments",
            "Hint 3: Code AFTER a return statement never runs!",
        ],
        "xp_bonus": 30,
    },

    # ── 12: FizzBuzz ────────────────────────────────────────────────
    {
        "id": "fizzbuzz",
        "track": "🐍 Python Path",
        "track_order": 12,
        "type": "code",
        "title": "12: The One and Only FizzBuzz 🎯",
        "languages": ["python", "javascript"],
        "description": (
            "THE classic coding challenge. Write `fizzbuzz(n)` that returns a LIST of strings:\n"
            "- Numbers 1 to n\n"
            "- Multiples of 3 → `'Fizz'`\n"
            "- Multiples of 5 → `'Buzz'`\n"
            "- Multiples of BOTH → `'FizzBuzz'`\n"
            "- Otherwise → the number as a string\n\n"
            "Bro says: 'Every dev has to pass the FizzBuzz gauntlet. Let's go!'"
        ),
        "starter_code": {
            "python": "def fizzbuzz(n):\n    result = []\n    for i in range(1, n + 1):\n        # Your logic here\n        pass\n    return result\n",
            "javascript": "function fizzbuzz(n) {\n    let result = [];\n    for (let i = 1; i <= n; i++) {\n        // Your logic here\n    }\n    return result;\n}\n",
        },
        "tests": [
            {"input": [15], "expected": ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]},
            {"input": [5], "expected": ["1","2","Fizz","4","Buzz"]},
        ],
        "hints": [
            "Check `i % 15 == 0` FIRST (divisible by both 3 and 5)",
            "Then `i % 3 == 0` for Fizz",
            "Then `i % 5 == 0` for Buzz",
            "Otherwise: `str(i)`",
        ],
        "xp_bonus": 50,
    },

    # ═══════════════════════════════════════════════════════════════════
    # TRACK 2: 🟨 JAVASCRIPT JOURNEY
    # ═══════════════════════════════════════════════════════════════════

    # ── JS-01 ────────────────────────────────────────────────────────
    {
        "id": "js_intro",
        "track": "🟨 JavaScript Journey",
        "track_order": 1,
        "type": "code",
        "title": "JS-01: JS Jumpstart 🟨",
        "languages": ["javascript"],
        "description": (
            "Write `js_intro(name)` that returns:\n"
            "`\"Hello {name}! JavaScript is LIT! 🔥\"`\n\n"
            "Bro says: 'JS runs the web, bro. Learn it, live it.'"
        ),
        "starter_code": "function js_intro(name) {\n    // Your code here\n}\n",
        "tests": [
            {"input": ["Bro"], "expected": "Hello Bro! JavaScript is LIT! 🔥"},
        ],
        "hints": [
            "Use string concatenation: `\"Hello \" + name + \"! JavaScript is LIT! 🔥\"`",
            "Or template literals: `` `Hello ${name}! JavaScript is LIT! 🔥` ``",
        ],
        "xp_bonus": 15,
    },

    # ── JS-02 ────────────────────────────────────────────────────────
    {
        "id": "js_arrays",
        "track": "🟨 JavaScript Journey",
        "track_order": 2,
        "type": "code",
        "title": "JS-02: Array Antics 📊",
        "languages": ["javascript"],
        "description": (
            "Write `js_arrays(arr)` that takes an array and returns:\n"
            "- `'length'`: array length\n"
            "- `'first'`: first element\n"
            "- `'last'`: last element\n"
            "- `'reversed'`: copy of array reversed\n"
            "- `'has_null'`: true if any element is null\n"
            "- `'all_numbers'`: true if every element is a number"
        ),
        "starter_code": "function js_arrays(arr) {\n    // Your array magic\n}\n",
        "tests": [
            {"input": [[1, 2, None, 4]], "expected": {"length": 4, "first": 1, "last": 4, "reversed": [4, None, 2, 1], "has_null": True, "all_numbers": False}},
            {"input": [[7, 2, 9]], "expected": {"length": 3, "first": 7, "last": 9, "reversed": [9, 2, 7], "has_null": False, "all_numbers": True}},
        ],
        "hints": [
            "Length: `arr.length`, First: `arr[0]`, Last: `arr[arr.length - 1]`",
            "Reversed: `[...arr].reverse()` (spread to copy first)",
            "Has null: `arr.includes(null)` or `arr.some(x => x === null)`",
            "All numbers: `arr.every(x => typeof x === 'number')`",
        ],
        "xp_bonus": 25,
    },

    # ═══════════════════════════════════════════════════════════════════
    # TRACK 3: 📝 PSEUDO PREP — Logic without Syntax
    # ═══════════════════════════════════════════════════════════════════

    {
        "id": "pseudo_logic",
        "track": "📝 Pseudo Prep",
        "track_order": 1,
        "type": "quiz",
        "title": "P-01: Logic Lanes 🧠",
        "languages": ["pseudocode"],
        "description": (
            "Let's think like a programmer! Answer these logic puzzles.\n"
            "No code needed — just pure brain power.\n\n"
            "Bro says: 'Logic is the secret sauce. Syntax is just the plate it sits on.'"
        ),
        "starter_code": "# Think through each question and submit your answers!\n# Q1: If you have a bucket of water and it's raining,\n# does the water level go up, down, or stay the same?\n# (Answer: \"up\", \"down\", or \"same\")\n",
        "tests": [
            # These are special quiz-type tests
            {"input": [], "expected": "up", "question": "Q1: A bucket's in the rain. Water level goes...?"},
            {"input": [], "expected": "true", "question": "Q2: True or False: A computer needs electricity to think."},
            {"input": [], "expected": "loop", "question": "Q3: What do you call code that repeats? (one word)"},
        ],
        "hints": [
            "Q1: Rain adds water to the bucket. What happens?",
            "Q2: Computers run on...?",
            "Q3: We learned this one! Starts with L...",
        ],
        "xp_bonus": 20,
    },

    # ═══════════════════════════════════════════════════════════════════
    # TRACK 4: 🌟 CHALLENGE MODE — Harder Problems
    # ═══════════════════════════════════════════════════════════════════

    {
        "id": "palindrome",
        "track": "🌟 Challenge Mode",
        "track_order": 1,
        "type": "code",
        "title": "C-01: Palindrome Check 🔄",
        "languages": ["python", "javascript"],
        "description": (
            "Write `is_palindrome(text)` that returns True if the string\n"
            "reads the same forwards and backwards (ignoring case and spaces).\n\n"
            "Examples: 'racecar' → True, 'Race Car' → True, 'hello' → False\n\n"
            "Bro says: 'Palindromes are the sneakers of the word world — they look the same from both sides.'"
        ),
        "starter_code": {
            "python": "def is_palindrome(text):\n    # Your palindrome logic\n    pass\n",
            "javascript": "function is_palindrome(text) {\n    // Your palindrome logic\n}\n",
        },
        "tests": [
            {"input": ["racecar"], "expected": True, "target": "is_palindrome"},
            {"input": ["Race Car"], "expected": True, "target": "is_palindrome"},
            {"input": ["A man a plan a canal Panama"], "expected": True, "target": "is_palindrome"},
            {"input": ["hello"], "expected": False, "target": "is_palindrome"},
            {"input": [""], "expected": True, "target": "is_palindrome"},
        ],
        "hints": [
            "Remove spaces: `text.replace(' ', '')` in Python, `text.replace(/\\s/g, '')` in JS",
            "Make lowercase: `text.lower()` in Python, `text.toLowerCase()` in JS",
            "Compare string to its reverse: `text == text[::-1]` in Python",
        ],
        "xp_bonus": 60,
    },

    {
        "id": "two_sum",
        "track": "🌟 Challenge Mode",
        "track_order": 2,
        "type": "code",
        "title": "C-02: Two Sum 🎯",
        "languages": ["python", "javascript"],
        "description": (
            "Write `two_sum(nums, target)` that finds TWO numbers in the list\n"
            "that add up to the target. Return their INDICES as a list [i, j].\n"
            "Assume exactly one solution exists. Don't use the same element twice.\n\n"
            "Bro says: 'This is THE interview question. Every FAANG dev has sweated over this one.'"
        ),
        "starter_code": {
            "python": "def two_sum(nums, target):\n    # Find the two indices\n    pass\n",
            "javascript": "function two_sum(nums, target) {\n    // Find the two indices\n}\n",
        },
        "tests": [
            {"input": [[2, 7, 11, 15], 9], "expected": [0, 1]},
            {"input": [[3, 2, 4], 6], "expected": [1, 2]},
            {"input": [[3, 3], 6], "expected": [0, 1]},
        ],
        "hints": [
            "Use a double loop: for each i, check every j > i",
            "Or use a dict/hashmap for O(n) solution (bonus!)",
            "In Python: `for i in range(len(nums)): for j in range(i+1, len(nums)):`",
        ],
        "xp_bonus": 80,
    },

    {
        "id": "fibonacci",
        "track": "🌟 Challenge Mode",
        "track_order": 3,
        "type": "code",
        "title": "C-03: Fibonacci 💫",
        "languages": ["python", "javascript"],
        "description": (
            "Write `fibonacci(n)` that returns the n-th Fibonacci number.\n"
            "Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...\n"
            "Each number is the sum of the two before it.\n"
            "fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2...\n\n"
            "Bro says: 'Fibonacci shows up in nature, art, and job interviews. It's the universe's favorite sequence.'"
        ),
        "starter_code": {
            "python": "def fibonacci(n):\n    # Return the nth Fibonacci number\n    pass\n",
            "javascript": "function fibonacci(n) {\n    // Return the nth Fibonacci number\n}\n",
        },
        "tests": [
            {"input": [0], "expected": 0},
            {"input": [1], "expected": 1},
            {"input": [10], "expected": 55},
            {"input": [20], "expected": 6765},
        ],
        "hints": [
            "Use a loop, not recursion (recursion is slow for big numbers!)",
            "Start with a, b = 0, 1 and update in a loop",
            "For each iteration: a, b = b, a + b",
        ],
        "xp_bonus": 70,
    },

    {
        "id": "anagrams",
        "track": "🌟 Challenge Mode",
        "track_order": 4,
        "type": "code",
        "title": "C-04: Anagram Detective 🔍",
        "languages": ["python"],
        "description": (
            "Write `are_anagrams(a, b)` that returns True if the two strings\n"
            "are anagrams (contain the same letters, ignoring spaces and case).\n\n"
            "Examples:\n"
            "- ('listen', 'silent') → True\n"
            "- ('The eyes', 'They see') → True\n"
            "- ('hello', 'world') → False\n\n"
            "Bro says: 'Anagrams are like a remix of the same song. Same ingredients, different arrangement.'"
        ),
        "starter_code": "def are_anagrams(a, b):\n    # Check if a and b are anagrams\n    pass\n",
        "tests": [
            {"input": ["listen", "silent"], "expected": True, "target": "are_anagrams"},
            {"input": ["The eyes", "They see"], "expected": True, "target": "are_anagrams"},
            {"input": ["hello", "world"], "expected": False, "target": "are_anagrams"},
            {"input": ["", ""], "expected": True, "target": "are_anagrams"},
        ],
        "hints": [
            "Remove spaces and lowercase both strings",
            "Sort the characters: `sorted(a) == sorted(b)`",
            "Or use a character counter dict",
        ],
        "xp_bonus": 50,
    },

    # ═══════════════════════════════════════════════════════════════════
    # TRACK 5: 💡 QUIZ CORNER — Concepts & Theory
    # ═══════════════════════════════════════════════════════════════════

    {
        "id": "quiz_cs_basics",
        "track": "💡 Quiz Corner",
        "track_order": 1,
        "type": "quiz",
        "title": "Q-01: CS Basics 💭",
        "languages": ["pseudocode"],
        "description": (
            "Test your computer science fundamentals!\n"
            "Each question expects a short answer.\n\n"
            "Bro says: 'Theory is the foundation. Code is the house. "
            "Let's make sure your foundation is SOLID.'"
        ),
        "starter_code": "# Answer these questions:\n# Q1: What does CPU stand for?\n# Q2: What's faster — RAM or SSD?\n# Q3: True or False: Python is a compiled language\n",
        "tests": [
            {"input": [], "expected": "central processing unit", "question": "What does CPU stand for?"},
            {"input": [], "expected": "ram", "question": "What's faster — RAM or SSD?"},
            {"input": [], "expected": "false", "question": "True or False: Python is a compiled language"},
        ],
        "hints": [
            "CPU = the brain of the computer",
            "RAM is like your desk (fast but small), SSD is like a filing cabinet (slower but big)",
            "Python is an INTERPRETED language, not compiled",
        ],
        "xp_bonus": 30,
    },

    {
        "id": "quiz_web",
        "track": "💡 Quiz Corner",
        "track_order": 2,
        "type": "quiz",
        "title": "Q-02: Web Wizardry 🌐",
        "languages": ["pseudocode"],
        "description": (
            "How well do you know the web?\n\n"
            "Bro says: 'The web is the world's biggest app. Understand it, and you understand everything.'"
        ),
        "starter_code": "# Answer these questions:\n# Q1: What protocol do websites use? (hint: starts with HTTP)\n# Q2: What does HTML stand for?\n# Q3: What CSS property makes text red?\n",
        "tests": [
            {"input": [], "expected": "https", "question": "What protocol do secure websites use? (starts with HTTP)"},
            {"input": [], "expected": "hypertext markup language", "question": "What does HTML stand for?"},
            {"input": [], "expected": "color", "question": "What CSS property makes text red?"},
        ],
        "hints": [
            "Secure websites use HTTP + S (for Secure)",
            "HTML = HyperText Markup Language",
            "CSS uses 'color' (not 'font-color'!)",
        ],
        "xp_bonus": 25,
    },
]


TRACKS = [
    {"id": "python", "name": "🐍 Python Path", "description": "From zero to Python pro. Start here if you're new!", "icon": "🐍"},
    {"id": "javascript", "name": "🟨 JavaScript Journey", "description": "Make the web your playground. JS awaits!", "icon": "🟨"},
    {"id": "pseudocode", "name": "📝 Pseudo Prep", "description": "Logic without syntax. Perfect for absolute beginners!", "icon": "📝"},
    {"id": "challenge", "name": "🌟 Challenge Mode", "description": "Hard problems for when you're feeling spicy!", "icon": "🌟"},
    {"id": "quiz", "name": "💡 Quiz Corner", "description": "Test your CS knowledge! No code needed.", "icon": "💡"},
]


BRO_WISDOM = [
    "The best time to start coding was 10 years ago. The second best time is RIGHT NOW.",
    "Every expert was once a beginner who didn't give up.",
    "Your code will suck at first. Mine did. Everyone's does. Keep going.",
    "Computers are dumb. They only do exactly what you tell them. THAT'S the power.",
    "A bug is just a feature you haven't named yet. (Just kidding — fix your bugs.)",
    "Programming isn't about knowing all the answers — it's about knowing how to find them.",
    "Stack Overflow isn't cheating. It's... collaborative research.",
    "The best code is the code that works. The second best is the code you can read.",
    "Don't compare your chapter 1 to someone else's chapter 20.",
    "Syntax is just typing. LOGIC is the real skill. And logic you can practice anywhere.",
]


def get_all_lessons():
    """Return lesson metadata for frontend listing."""
    result = []
    for l in LESSONS:
        result.append({
            "id": l["id"],
            "track": l["track"],
            "track_order": l["track_order"],
            "type": l["type"],
            "title": l["title"],
            "description": l["description"],
            "languages": l["languages"],
            "num_tests": len(l["tests"]),
            "xp_bonus": l.get("xp_bonus", 10),
        })
    return result


def get_lesson(lesson_id: str):
    """Get a full lesson by ID, including hints and starter code."""
    for l in LESSONS:
        if l["id"] == lesson_id:
            return l
    return None


def get_random_wisdom() -> str:
    import random
    return random.choice(BRO_WISDOM)


def get_tracks():
    return TRACKS
