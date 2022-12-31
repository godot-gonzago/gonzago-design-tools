from abc import ABC
from dataclasses import dataclass
from gonzago.math import clamp01

# https://stackoverflow.com/a/70700159
# https://docs.python.org/3/howto/descriptor.html#validator-class
# https://docs.python.org/3/howto/descriptor.html#properties


class Color:
    def __init__(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, value: float) -> None:
        self._r = clamp01(value)

    @property
    def g(self) -> float:
        return self._g

    @g.setter
    def g(self, value: float) -> None:
        self._g = clamp01(value)

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = clamp01(value)

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = clamp01(value)

    def __str__(self) -> str:
        return f"rgba({self.r},{self.g},{self.b},{self.a})"

    def __repr__(self) -> str:
        return f"Color({self.r},{self.g},{self.b},{self.a})"


# https://stackoverflow.com/questions/55973284/how-to-create-self-registering-factory-in-python
# https://realpython.com/primer-on-python-decorators/#registering-plugins
# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration
# https://docs.python.org/3/library/functools.html#functools.singledispatch ???


class ColorFactory:
    pass
