from dataclasses import dataclass
from PIL.ImageColor import colormap as ColorMap
import re


@dataclass
class Color(int):
    """Class that provides color value representation and functionality."""

    def __str__(self):
        return hex(self)

    @staticmethod
    def from_string(color: str):
        # rgb = ColorMap.get(color)
        # if rgb:
        # TODO:
        # tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

        c: Color = int.__new__(Color, int(color.lstrip("#").lower(), 16))
        return c

    def to_rgb(self) -> str:
        return f"#{self:06x}"
