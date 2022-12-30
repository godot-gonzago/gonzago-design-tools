from numbers import Number
from typing import TypeVar

NumberT = TypeVar("NumberT", bound=Number)


def clamp(value: NumberT, min_value: NumberT, max_value: NumberT) -> NumberT:
    return min_value if value < min_value else max_value if value > max_value else value


def clamp01(value: float) -> float:
    return clamp(value, 0.0, 1.0)


def clamp8bit(value: int) -> int:
    return clamp(value, 0, 255)
