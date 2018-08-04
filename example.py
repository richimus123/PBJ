# coding=utf-8
"""Example functions and helpers."""


def my_cool_function(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def count_chars(text: str, char_to_count: str) -> int:
    """Count the number of times that 'char_to_count' is found in the 'text'."""
    count = 0
    for char in text:
        if char == char_to_count:
            count += 1
    return count
