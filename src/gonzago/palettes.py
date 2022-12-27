from dataclasses import dataclass
from PIL.ImageColor import colormap as ColorMap
import re


@dataclass
class Color:
    """Class that provides color value representation and functionality."""

    value: int = 0

    def __str__(self):
        return hex(self.value)

    @staticmethod
    def from_string(color: str):
        # rgb = ColorMap.get(color)
        # if rgb:
        # TODO:
        # tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return Color(int(color.lstrip("#").lower(), 16))

    def to_rgb(self) -> str:
        return f"#{self.value:06x}"
