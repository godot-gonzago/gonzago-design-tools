from numbers import Number
from typing import TypeVar

NumberT = TypeVar("NumberT", bound=Number)


def clamp(value: NumberT, min_value: NumberT, max_value: NumberT) -> NumberT:
    return min_value if value < min_value else max_value if value > max_value else value


def clamp01(value: float) -> float:
    return clamp(value, 0.0, 1.0)


def clamp8bit(value: int) -> int:
    return clamp(value, 0, 255)


class RangedValue:
    def __init__(
        self, min_value: NumberT, max_value: NumberT, default: NumberT | None = None
    ):
        self.min_value = min_value
        self.max_value = max_value
        self.default = default

    def __set_name__(self, _, name: str) -> None:
        self.name = name

    def __get__(self, obj: object, objtype=None) -> NumberT:
        # getattr(obj, self.name, self.default)
        if not obj: return self.default
        return obj.__dict__[self.name]

    def __set__(self, obj: object, value: NumberT) -> None:
        # setattr(obj, self.name, clamp(value, self.min_value, self.max_value))
        obj.__dict__[self.name] = clamp(value, self.min_value, self.max_value)

    #def __delete__(self, obj: object) -> None:
    #    del obj.__dict__[self.name]
