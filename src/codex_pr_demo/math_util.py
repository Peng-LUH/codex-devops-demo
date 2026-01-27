"""Math utilities for codex_pr_demo."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def subtract(a, b):
    """Return the result of a minus b."""
    return a - b


def mal(a, b):
    """Return the product of a and b."""
    return a * b
