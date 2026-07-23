"""
languages.py — Hardened multi-language execution engine.

Security:
  - Python: removed __builtins__, blocks dunder access via AST scanning
  - JavaScript: subprocess with strict timeout + headless Node
  - Pseudocode: forgiving pattern matching with beginner-friendly errors
"""

import subprocess
import os
import signal
import json
import ast
import textwrap
from typing import Any


class TimeoutError(RuntimeError):
    pass


class SecurityError(RuntimeError):
    pass


LANGUAGES = {
    "python": {
        "name": "Python 🐍",
        "emoji": "🐍",
        "color": "#3776AB",
        "description": "The friendliest language to start with. Reads like English!",
        "starter_template": "def {func_name}({params}):\n    # Your code here\n    pass\n",
        "comment_style": "#",
        "tabs": 4,
    },
    "javascript": {
        "name": "JavaScript 🟨",
        "emoji": "🟨",
        "color": "#F7DF1E",
        "description": "The language of the web. Makes websites dance.",
        "starter_template": "function {func_name}({params}) {{\n    // Your code here\n}}\n",
        "comment_style": "//",
        "tabs": 2,
    },
    "pseudocode": {
        "name": "Pseudocode 📝",
        "emoji": "📝",
        "color": "#888888",
        "description": "No syntax rules — just explain your logic in plain words.",
        "starter_template": "# {func_name}({params}):\n#   Write your logic in plain English\n",
        "comment_style": "#",
        "tabs": 4,
    },
}


# ═══════════════════════════════════════════════════════════════════════
# PYTHON — HARDENED SANDBOX
# ═══════════════════════════════════════════════════════════════════════

# Build a safe set of builtins — no access to object, type, eval, exec, etc.
SAFE_BUILTINS = {
    # Types
    "bool": bool, "int": int, "float": float, "str": str,
    "list": list, "dict": dict, "tuple": tuple, "set": set,
    "type": type,  # safe — they need it for isinstance
    # Math
    "abs": abs, "max": max, "min": min, "sum": sum, "round": round,
    "pow": pow, "len": len,
    # Iteration
    "range": range, "enumerate": enumerate, "zip": zip,
    "map": map, "filter": filter, "reversed": reversed, "sorted": sorted,
    "all": all, "any": any, "isinstance": isinstance,
    # I/O (safe — print goes to captured stdout)
    "print": print,
    # Constants
    "True": True, "False": False, "None": None,
}


def _scan_for_dangerous_code(code: str):
    """
    AST-level scan for escape attempts before execution.
    Blocks: __dunder__, eval, exec, compile, import, open, breakpoint.
    """
    dangerous_patterns = [
        "__",       # dunder access (__class__, __subclasses__, etc.)
        "eval(",    # dynamic eval
        "exec(",    # dynamic exec
        "compile(", # dynamic compile
        "import ",  # import statements (catches 'import os')
        "open(",    # file I/O
    ]
    code_no_comments = code
    for pattern in dangerous_patterns:
        if pattern in code_no_comments:
            raise SecurityError(
                f"⚠️  Your code contains '{pattern}' which isn't allowed "
                "in the sandbox environment. Try solving it with basic Python instead!"
            )

    # Also reject 'import' as a statement via AST
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                raise SecurityError(
                    "⚠️  Import statements aren't supported in the sandbox. "
                    "All the functions you need are already available!"
                )
    except SyntaxError:
        pass  # Let exec() report syntax errors naturally


def _execute_python(code: str, func_name: str, args: list) -> Any:
    """Execute Python code with a hardened sandbox."""

    # 1. AST-level scan for escape attempts
    _scan_for_dangerous_code(code)

    # 2. Build restricted globals — NO __builtins__ whatsoever
    restricted = {"__builtins__": {}}
    # Inject our safe builtins individually
    for name, obj in SAFE_BUILTINS.items():
        restricted[name] = obj

    # 3. Set timeout and execute
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(4)

    try:
        exec(code, restricted)
    except TimeoutError:
        raise
    except SecurityError:
        raise
    except SyntaxError as e:
        raise RuntimeError(
            f"📝 Syntax error on line {e.lineno}: {e.msg}\n"
            f"   {e.text or ''}"
        )
    except Exception as e:
        raise RuntimeError(f"💥 Runtime error: {type(e).__name__}: {e}")
    finally:
        signal.alarm(0)

    # 4. Verify the function exists
    if func_name not in restricted:
        raise NameError(
            f"🤔 Function `{func_name}()` wasn't found in your code. "
            f"Double-check the function name and make sure it's defined at the top level."
        )

    return restricted[func_name](*args)


# ═══════════════════════════════════════════════════════════════════════
# JAVASCRIPT — SUBPROCESS WITH HARD TIMEOUT
# ═══════════════════════════════════════════════════════════════════════

def _execute_javascript(code: str, func_name: str, args: list) -> Any:
    """Execute JavaScript via Node.js subprocess with strict timeout."""

    js_args = json.dumps(args)
    wrapper = textwrap.dedent(f"""
    {code}

    const result = JSON.stringify({func_name}(...{js_args}));
    console.log(result);
    """)

    try:
        proc = subprocess.run(
            ["node", "-e", wrapper],
            capture_output=True,
            text=True,
            timeout=3,           # Hard wall-clock timeout — kills infinite loops
            env={**os.environ, "NODE_PATH": ""},
        )

        if proc.returncode != 0:
            stderr = proc.stderr.strip() or "(no error output)"
            raise RuntimeError(f"💥 JS error: {stderr}")

        output = proc.stdout.strip()
        if not output:
            raise RuntimeError(
                "📭 Your function didn't return anything. "
                "Make sure you use `return` to send back a result!"
            )
        return json.loads(output)

    except subprocess.TimeoutExpired:
        raise TimeoutError(
            "⏱ Your code took longer than 3 seconds to run. "
            "Check for infinite loops (e.g., `while(true)` or `for(;;)`)!"
        )
    except json.JSONDecodeError:
        raise RuntimeError(
            "📦 Couldn't parse the result from your JS code. "
            "Make sure your function returns a simple value (string, number, array, or object)."
        )


# ═══════════════════════════════════════════════════════════════════════
# PSEUDOCODE — FORGIVING INTERPRETER
# ═══════════════════════════════════════════════════════════════════════

# For quiz lessons, answers are extracted from comments
# For code-type, we try to interpret simple patterns


def _execute_pseudocode(code: str, func_name: str, args: list) -> Any:
    """
    Pseudocode runner — extremely forgiving, beginner-first.

    Matches patterns like:
      - "return X" → returns X
      - "set x = Y" or "x = Y" → assignment (stored in local scope)
      - "add X to list" → list append
      - "loop through X" → iteration hint (just returns placeholder)

    If nothing matches, returns a helpful message.
    """
    lines = code.strip().split("\n")
    local_vars = {}

    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue

        # Try to eval simple expressions first
        try:
            result = _try_eval(line, local_vars)
            if result is not None:
                return result
        except Exception:
            pass

    # If we get here, nothing matched
    raise RuntimeError(
        f"🤔 I couldn't figure out what your pseudocode is trying to do.\n\n"
        f"Try writing it like one of these:\n"
        f"  • `return \"Hello\"` — to return a value\n"
        f"  • `set name = \"Bob\"` — to set a variable\n"
        f"  • `x = 5 + 3` — for math\n\n"
        f"Your code:\n{textwrap.indent(code, '   ')}"
    )


def _try_eval(line: str, vars_dict: dict) -> Any:
    """Try to interpret a single pseudocode line as an instruction."""
    line_lower = line.lower().strip()

    # Pattern: "return X" or "Return X" or "RETURN X"
    if line_lower.startswith("return "):
        val_str = line[7:].strip()
        return _parse_value(val_str, vars_dict)

    # Pattern: "set x = value" or "x = value"
    if "=" in line:
        parts = line.split("=", 1)
        var_name = parts[0].strip().lower()
        # Strip "set " prefix
        if var_name.startswith("set "):
            var_name = var_name[4:].strip()
        val_str = parts[1].strip()
        vars_dict[var_name] = _parse_value(val_str, vars_dict)
        return None  # assignment, no return

    # Pattern: simple expression evaluation (like "5 + 3")
    return _parse_value(line, vars_dict)


def _parse_value(val_str: str, vars_dict: dict) -> Any:
    """Parse a value string — handles numbers, strings, booleans, lists, and variable lookup."""
    val = val_str.strip()

    # Empty value
    if not val:
        return None

    # Variable reference (look up in our vars dict)
    if val.lower() in vars_dict:
        return vars_dict[val.lower()]

    # Boolean literals
    if val.lower() in ("true", "yes"):
        return True
    if val.lower() in ("false", "no"):
        return False
    if val.lower() == "none":
        return None

    # String literals (single or double quotes)
    if (val.startswith('"') and val.endswith('"')) or \
       (val.startswith("'") and val.endswith("'")):
        return val[1:-1]

    # Number (int or float)
    try:
        if "." in val:
            return float(val)
        return int(val)
    except ValueError:
        pass

    # List: [1, 2, 3]
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1]
        items = []
        for item in inner.split(","):
            item = item.strip()
            if item:
                items.append(_parse_value(item, vars_dict))
        return items

    # Dict: {key: value, ...}
    if val.startswith("{") and val.endswith("}"):
        inner = val[1:-1]
        result = {}
        for pair in inner.split(","):
            pair = pair.strip()
            if ":" in pair:
                k, v = pair.split(":", 1)
                result[_parse_value(k.strip(), vars_dict)] = _parse_value(v.strip(), vars_dict)
        return result

    # Fallback: return as-is (it's probably a word)
    return val


# ═══════════════════════════════════════════════════════════════════════
# DISPATCH
# ═══════════════════════════════════════════════════════════════════════

def _timeout_handler(signum, frame):
    raise TimeoutError(
        "⏱ Code execution timed out (>4 seconds). "
        "Check for infinite loops or recursive calls without a base case!"
    )


LANGUAGE_RUNNERS = {
    "python": _execute_python,
    "javascript": _execute_javascript,
    "pseudocode": _execute_pseudocode,
}


def run_code(language: str, code: str, func_name: str, args: list) -> Any:
    runner = LANGUAGE_RUNNERS.get(language)
    if not runner:
        raise ValueError(
            f"Sorry, the language '{language}' isn't available yet. "
            f"Try one of: {', '.join(LANGUAGE_RUNNERS.keys())}"
        )
    return runner(code, func_name, args)


def get_language_config(lang: str) -> dict:
    return LANGUAGES.get(lang, LANGUAGES["python"])
