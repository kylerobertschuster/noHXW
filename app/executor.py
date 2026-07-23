"""
executor.py — Multi-language, multi-type code execution engine.

Supports:
  - type: code → run function with inputs, compare to expected
  - type: quiz → compare answer (case-insensitive trimmed)
  - type: debug → same as code, but the starter code has bugs
"""

from .languages import run_code, LANGUAGE_RUNNERS
from typing import Any
import re


def run_test(code: str, func_name: str, test_input: list,
             expected: Any, language: str = "python",
             lesson_type: str = "code") -> dict:
    """Run a single test case and return result metadata."""

    if lesson_type == "quiz":
        return _run_quiz_test(code, func_name, test_input, expected)

    try:
        if language not in LANGUAGE_RUNNERS:
            return {
                "passed": False,
                "input": test_input,
                "expected": expected,
                "actual": None,
                "error": f"Language '{language}' not available on this system 😅",
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
    except Exception as e:
        return {
            "passed": False,
            "input": test_input,
            "expected": expected,
            "actual": None,
            "error": str(e),
        }


def _run_quiz_test(code: str, func_name: str, test_input: list,
                   expected: Any) -> dict:
    """Quiz tests — extract answer from comment or code."""
    # Quiz answers are in comments: # Q1: answer
    # We extract the answer from the student's code
    # If they just wrote the answer word, compare it
    lines = code.strip().split("\n")
    for line in lines:
        line = line.strip()
        # Remove comment markers
        clean = re.sub(r'^[#//]+\s*', '', line).strip().lower()
        # Check if this looks like an answer
        expected_clean = str(expected).lower().strip()
        if clean == expected_clean:
            return {
                "passed": True,
                "input": test_input,
                "expected": expected,
                "actual": expected,
                "error": None,
            }
        # Check for "Q1: answer" pattern
        if ':' in clean:
            parts = clean.split(':', 1)
            answer = parts[1].strip()
            if answer == expected_clean:
                return {
                    "passed": True,
                    "input": test_input,
                    "expected": expected,
                    "actual": expected,
                    "error": None,
                }

    return {
        "passed": False,
        "input": test_input,
        "expected": expected,
        "actual": None,
        "error": "Couldn't find the right answer. Make sure you wrote it clearly!",
    }


def get_function_name(code: str, lesson_id: str) -> str:
    """Try to extract the function name from code, fall back to lesson_id."""
    # Python: `def func_name(`
    m = re.search(r'def\s+(\w+)\s*\(', code)
    if m:
        return m.group(1)
    # JS: `function func_name(`
    m = re.search(r'function\s+(\w+)\s*\(', code)
    if m:
        return m.group(1)
    return lesson_id
