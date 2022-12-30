from collections.abc import Iterable
from typing import NamedTuple
from abc import ABC, abstractmethod


class RGBA(NamedTuple):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0


class IColor(ABC):
    @abstractmethod
    def to_rgba(self) -> RGBA:
        pass

    @abstractmethod
    @classmethod
    def from_rgba(cls, rgba: RGBA):
        pass


class Color:
    def __init__(
        self, r: float = 0.0, g: float = 0.0, b: float = 0.0, a: float = 1.0
    ) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __index__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, __o: object) -> bool:
        pass

# https://refactoring.guru/design-patterns/python
