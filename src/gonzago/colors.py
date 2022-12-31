from abc import ABC
from dataclasses import dataclass
from math import sqrt
from typing import NamedTuple
from gonzago.math import clamp01

# https://stackoverflow.com/a/70700159
# https://docs.python.org/3/howto/descriptor.html#validator-class
# https://docs.python.org/3/howto/descriptor.html#properties


class Color(NamedTuple):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0

    def clamped(self):
        return Color(clamp01(self.r), clamp01(self.g), clamp01(self.b), clamp01(self.a))

    def get_length(self, include_alpha: bool = False) -> float:
        sum: float = self.r**2 + self.g**2 + self.b**2
        if include_alpha:
            sum += self.a**2
        return sqrt(sum)


# Color names api: https://github.com/meodai/color-names


# https://stackoverflow.com/questions/55973284/how-to-create-self-registering-factory-in-python
# https://realpython.com/primer-on-python-decorators/#registering-plugins
# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration
# https://docs.python.org/3/library/functools.html#functools.singledispatch ???


class ColorFactory:
    pass
