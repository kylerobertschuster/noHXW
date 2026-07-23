"""
executor.py — Multi-language, multi-type test execution engine.

Dispatches to hardened language runners in languages.py.
Supports code, quiz, and debug lesson types with clear error messages.
"""

from .languages import run_code, LANGUAGE_RUNNERS, TimeoutError, SecurityError
from typing import Any
import re


def run_test(code: str, func_name: str, test_input: list,
             expected: Any, language: str = "python",
             lesson_type: str = "code") -> dict:
    """Run a single test case with clear, actionable error messages."""

    # ── Quiz type: compare answers case-insensitively ───────────────
    if lesson_type == "quiz":
        return _run_quiz_test(code, expected)

    # ── Code or Debug type: execute and compare ─────────────────────
    try:
        if language not in LANGUAGE_RUNNERS:
            return {
                "passed": False,
                "input": test_input,
                "expected": expected,
                "actual": None,
                "error": (
                    f"😅 The '{language}' runner isn't available on this system. "
                    f"Supported: {', '.join(LANGUAGE_RUNNERS.keys())}"
                ),
            }

        actual = run_code(language, code, func_name, test_input)
        passed = actual == expected
        return {
            "passed": passed,
            "input": test_input,
            "expected": expected,
            "actual": actual,
            "error": None,
        }

    except TimeoutError as e:
        return {
            "passed": False,
            "input": test_input,
            "expected": expected,
            "actual": None,
            "error": str(e),
        }
    except SecurityError as e:
        return {
            "passed": False,
            "input": test_input,
            "expected": expected,
            "actual": None,
            "error": str(e),
        }
    except NameError as e:
        return {
            "passed": False,
            "input": test_input,
            "expected": expected,
            "actual": None,
            "error": str(e),
        }
    except Exception as e:
        return {
            "passed": False,
            "input": test_input,
            "expected": expected,
            "actual": None,
            "error": str(e),
        }


def _run_quiz_test(code: str, expected: Any) -> dict:
    """
    Quiz tests — scan code comments and raw text for the answer.

    Extremely forgiving: checks for the answer word anywhere in the
    code, in comments, or in plain text. Case-insensitive.
    """
    expected_str = str(expected).strip().lower()
    code_lower = code.lower()

    # Check if the expected value appears anywhere in the code
    if expected_str in code_lower:
        return {
            "passed": True,
            "input": [],
            "expected": expected,
            "actual": expected,
            "error": None,
        }

    # Check each line for "answer:" patterns
    for line in code.split("\n"):
        line = line.strip().lower()
        # Remove comment markers
        clean = re.sub(r'^[#//]+\s*', '', line).strip()
        if clean == expected_str:
            return {
                "passed": True,
                "input": [],
                "expected": expected,
                "actual": expected,
                "error": None,
            }
        # Check "Q1: answer" or "answer = x" patterns
        if ':' in clean:
            parts = clean.split(':', 1)
            answer = parts[1].strip()
            if answer == expected_str or answer == f'"{expected_str}"' or answer == f"'{expected_str}'":
                return {
                    "passed": True,
                    "input": [],
                    "expected": expected,
                    "actual": expected,
                    "error": None,
                }

    return {
        "passed": False,
        "input": [],
        "expected": expected,
        "actual": None,
        "error": (
            f"🤔 I couldn't find the right answer in your code.\n\n"
            f"Expected something containing: `{expected}`\n\n"
            f"Try writing it like:\n"
            f"  • `# {expected}` — just put the answer in a comment\n"
            f"  • `{expected}` — or write it directly!\n\n"
            f"💡 Hint: It's case-insensitive, so don't stress about capitalization!"
        ),
    }


def get_function_name(code: str, lesson_id: str) -> str:
    """Try to extract the function name from code, fall back to lesson_id."""
    # Python: def func_name(
    m = re.search(r'def\s+(\w+)\s*\(', code)
    if m:
        return m.group(1)
    # JS: function func_name(
    m = re.search(r'function\s+(\w+)\s*\(', code)
    if m:
        return m.group(1)
    return lesson_id
