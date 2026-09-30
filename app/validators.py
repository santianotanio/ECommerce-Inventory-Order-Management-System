"""Input validation and error messages."""
from typing import Optional


def required_text(value: str, field: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError(f"{field} cannot be empty.")
    return value


def positive_int(value: str, field: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"{field} must be a whole number.")
    if number <= 0:
        raise ValueError(f"{field} must be greater than zero.")
    return number


def non_negative_int(value: str, field: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"{field} must be a whole number.")
    if number < 0:
        raise ValueError(f"{field} cannot be negative.")
    return number


def positive_float(value: str, field: str) -> float:
    try:
        number = float(value)
    except ValueError:
        raise ValueError(f"{field} must be a number.")
    if number <= 0:
        raise ValueError(f"{field} must be greater than zero.")
    return round(number, 2)


def optional_status(value: str, allowed) -> str:
    value = value.strip().title()
    if value not in allowed:
        raise ValueError(f"Status must be one of: {', '.join(allowed)}.")
    return value
