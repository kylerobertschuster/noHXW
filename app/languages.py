"""
languages.py — Language configurations for multi-language support.

Each language has a runner, syntax demo, personality flavor,
and accessibility notes.
"""

import subprocess
import sys
import os
import tempfile
import signal
import json
from typing import Any


class TimeoutError(RuntimeError):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutError("⏱ Code took too long! (>3s)")


LANGUAGES = {
    "python": {
        "name": "Python 🐍",
        "emoji": "🐍",
        "color": "#3776AB",
        "description": "The friendliest language to start with. Reads like English!",
        "starter_template": "def {func_name}({params}):\n    # Your code here\n    pass\n",
        "comment_style": "#",
        "tabs": 4,
        "bro_tip": "Python's like giving instructions to a very literal friend. Say EXACTLY what you mean.",
    },
    "javascript": {
        "name": "JavaScript 🟨",
        "emoji": "🟨",
        "color": "#F7DF1E",
        "description": "The language of the web. Makes websites dance.",
        "starter_template": "function {func_name}({params}) {{\n    // Your code here\n}}\n",
        "comment_style": "//",
        "tabs": 2,
        "bro_tip": "JS is like a Swiss Army knife — does everything, but sometimes cuts you. Watch those semicolons!",
    },
    "pseudocode": {
        "name": "Pseudocode 📝",
        "emoji": "📝",
        "color": "#888888",
        "description": "No syntax rules — just explain your logic in plain words. Great for beginners!",
        "starter_template": "# {func_name}({params}):\n#   Write your logic in plain English\n#   Example: 'set result = the first item in the list'\n",
        "comment_style": "#",
        "tabs": 4,
        "bro_tip": "Pseudocode is like telling a story about how your code works. No pressure, just vibes.",
    },
}


def _execute_python(code: str, func_name: str, args: list) -> Any:
    """Execute Python code in a restricted sandbox."""
    safe_builtins = {
        "abs": abs, "all": all, "any": any, "bool": bool,
        "dict": dict, "enumerate": enumerate, "float": float,
        "int": int, "isinstance": isinstance, "len": len,
        "list": list, "max": max, "min": min, "print": print,
        "range": range, "round": round, "sorted": sorted,
        "str": str, "sum": sum, "tuple": tuple, "type": type,
        "zip": zip, "map": map, "filter": filter, "reversed": reversed,
        "True": True, "False": False, "None": None,
        "__import__": __import__,
        "open": open,  # needed for file I/O lessons
    }
    restricted = {"__builtins__": safe_builtins}

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(3)

    try:
        exec(code, restricted)
    except TimeoutError:
        raise
    except Exception as e:
        raise RuntimeError(f"💥 Code error: {e}")
    finally:
        signal.alarm(0)

    if func_name not in restricted:
        raise NameError(
            f"🤔 Function `{func_name}()` not found! Double-check the name."
        )
    return restricted[func_name](*args)


def _execute_javascript(code: str, func_name: str, args: list) -> Any:
    """Execute JavaScript code via Node.js."""
    js_args = json.dumps(args)
    wrapper = f"""
{code}

const result = JSON.stringify({func_name}(...{js_args}));
console.log(result);
"""
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(3)

    try:
        proc = subprocess.run(
            ["node", "-e", wrapper],
            capture_output=True, text=True, timeout=3,
            env={**os.environ, "NODE_PATH": ""}
        )
        if proc.returncode != 0:
            raise RuntimeError(f"💥 JS error: {proc.stderr.strip()}")
        output = proc.stdout.strip()
        return json.loads(output)
    except subprocess.TimeoutExpired:
        raise TimeoutError("⏱ JS took too long! (>3s)")
    finally:
        signal.alarm(0)


def _execute_pseudocode(code: str, func_name: str, args: list) -> Any:
    """Pseudocode runner — just parse keywords for simple logic."""
    # For pseudocode, we try to interpret simple patterns:
    # "return X" → returns X
    # "set X = Y" → assignment
    # For now, just try to eval simple returns
    lines = code.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.lower().startswith("return "):
            val = line[7:].strip()
            try:
                return eval(val, {"__builtins__": {}}, {})
            except:
                return val
    return None


LANGUAGE_RUNNERS = {
    "python": _execute_python,
    "javascript": _execute_javascript,
    "pseudocode": _execute_pseudocode,
}


def run_code(language: str, code: str, func_name: str, args: list) -> Any:
    runner = LANGUAGE_RUNNERS.get(language)
    if not runner:
        raise ValueError(f"Language '{language}' not supported yet! Coming soon maybe? 👀")
    return runner(code, func_name, args)


def get_language_config(lang: str) -> dict:
    return LANGUAGES.get(lang, LANGUAGES["python"])
