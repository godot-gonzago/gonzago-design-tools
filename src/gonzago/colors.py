from abc import ABC
import colorsys
import re
from dataclasses import dataclass
from typing import NamedTuple, Sequence

from PIL import ImageColor

# https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
# https://docs.python.org/3/library/colorsys.html#module-colorsys
# https://github.com/edaniszewski/colorutils/tree/master/colorutils

# https://developer.mozilla.org/en-US/docs/Web/CSS/color
# <named-color> values: color: red;
# <hex-color> values: color: #090; color: #009900; color: #090a; color: #009900aa;
# <rgb()> values: color: rgb(34, 12, 64, 0.6); color: rgba(34, 12, 64, 0.6);
# <hsl()> values: color: hsl(30, 100%, 50%, 0.6); color: hsla(30, 100%, 50%, 0.6);
# <hwb()> values


# https://docs.python.org/3/library/collections.html#collections.namedtuple
class ColorDec(NamedTuple):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0


RGB32 = NamedTuple("RGB32", r=int, g=int, b=int)
RGBA32 = NamedTuple("RGBA32", r=int, g=int, b=int, a=int)
RGB = NamedTuple("RGB", r=float, g=float, b=float)
RGBA = NamedTuple("RGBA", r=float, g=float, b=float, a=float)
HSV = NamedTuple("HSV", h=float, s=float, v=float)
HSVA = NamedTuple("HSVA", h=float, s=float, v=float, a=float)

ColorChannel = float | int | str


# TODO: Handle alpha via mixin? https://www.residentmar.io/2019/07/07/python-mixins.html https://www.datasciencelearner.com/python-mixin-implementation/
# https://docs.python.org/dev/reference/datamodel.html#customizing-class-creation
class ColorAlphaMixin:
    pass


# https://docs.python.org/3/reference/datamodel.html#slots
# https://docs.python.org/dev/library/abc.html
# https://docs.python.org/dev/reference/datamodel.html#implementing-descriptors
class BaseColor(ABC):
    # __match_args__ = ("left", "center", "right")
    # https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable
    # abc.Hashable?`
    # https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__

    def __int__(self) -> int:
        return ord(self.val)

    def __index__(self):
        return ord(self.val)

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        # return f'({self.x}, {self.y})'
        return ""

    # def __len__(self):
    #    pass

    # https://www.pythontutorial.net/python-oop/python-__repr__/
    # https://www.codingem.com/repr-method-python/
    def __repr__(self):
        # return f'Person(name={self.name}, age={self.age})'
        return ""


# https://zetcode.com/python/magicmethods/
# https://docs.python.org/dev/reference/datamodel.html#specialnames
# https://docs.python.org/dev/reference/datamodel.html#customizing-instance-and-subclass-checks
# __hash__()
# __match_args__


class Color:
    """Class that provides color value representation and functionality."""

    _r: float = 0.0
    _g: float = 0.0
    _b: float = 0.0
    _a: float = 1.0

    # TODO: Type should be something like float (0..1) | int (0..255) | str (if ends in %) where conversion happens
    def __init__(
        self,
        r: ColorChannel = 0.0,
        g: ColorChannel = 0.0,
        b: ColorChannel = 0.0,
        a: ColorChannel = 1.0,
    ):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        return f"Color{{r: {self.r}, g: {self.g}, b: {self.b}, a: {self.a}}}"

    def __str__(self):
        return self.to_hex_rgb()

    # TODO: not always 0..1, h might be 0..360, see https://www.w3schools.com/css/css_colors_hsl.asp
    def _convert_channel(self, value: ColorChannel) -> float | None:
        if isinstance(value, str):
            # if value.endswith("%"):
            #    value = value.removesuffix("%")
            #    if value.isnumeric():
            #        value = float(value) / 100.0
            match: re.Match[str] = re.match(r"(\d+|\d+.\d+)%$", value)
            if match:
                value = float(match.group[0]) / 100.0

        if isinstance(value, int):
            value = value / 255.0

        if isinstance(value, float):
            return 0.0 if value < 0.0 else 1.0 if value > 1.0 else value

        # raise ValueError(f"Cannot convert to color channel: {repr(value)}")
        return None

    # https://www.geeksforgeeks.org/difference-between-attributes-and-properties-in-python/
    # https://github.com/WebJournal/journaldev/tree/master/Python-3/basic_examples
    # https://github.com/WebJournal/journaldev/blob/master/Python-3/basic_examples/hash_function.py
    # https://github.com/WebJournal/journaldev/blob/master/Python-3/basic_examples/not_equal_operator.py

    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, value: ColorChannel) -> None:
        new_value: float = self._convert_channel(value)
        if new_value:
            self._r = new_value

    @property
    def g(self) -> float:
        return self._g

    @g.setter
    def g(self, value: ColorChannel) -> None:
        new_value: float = self._convert_channel(value)
        if new_value:
            self._g = new_value

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: ColorChannel) -> None:
        new_value: float = self._convert_channel(value)
        if new_value:
            self._b = new_value

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: ColorChannel) -> None:
        new_value: float = self._convert_channel(value)
        if new_value:
            self._a = new_value

    @property
    def rgb(self) -> RGB:
        return RGB(self.r, self.g, self.b)

    @property
    def rgb32(self) -> RGB32:
        return RGB32(int(self.r * 255), int(self.g * 255), int(self.b * 255))

    @property
    def hsv(self) -> HSV:
        hsv_value = colorsys.rgb_to_hsv(self.r, self.g, self.b)
        return HSV(hsv_value[0], hsv_value[1], hsv_value[2])

    @hsv.setter
    def hsv(self, value: HSV) -> None:
        rbg_value = colorsys.hsv_to_rgb(value.h, value.s, value.v)
        self.r = rbg_value[0]
        self.g = rbg_value[1]
        self.b = rbg_value[2]

    @classmethod
    def create(cls, color: str | int | Sequence):
        if isinstance(color, str):
            rgb = ImageColor.getrgb(color)
            return cls(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) > 3 else 1.0)

        if isinstance(color, int):
            return cls(
                (color & 0xFF000000) > 24,
                (color & 0x00FF0000) > 16,
                (color & 0x0000FF00) > 8,
                (color & 0x000000FF) > 0,
            )

        if isinstance(color, Sequence):
            if len(color) >= 3:
                return cls(
                    color[0], color[1], color[2], color[3] if len(color) > 3 else 1.0
                )

        raise ValueError(f"Cannot handle color specifier: {repr(color)}")

    def to_hex(self, upper: bool = False) -> str:
        rgb: RGB32 = self.rgb32
        hex_str: str = f"0x{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}"
        return hex_str.upper() if upper else hex_str

    def to_hex_rgb(self, upper: bool = False) -> str:
        rgb: RGB32 = self.rgb32
        hex_rgb: str = f"#{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}"
        return hex_rgb.upper() if upper else hex_rgb
