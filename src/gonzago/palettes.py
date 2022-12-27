from dataclasses import dataclass
from PIL.ImageColor import colormap as ColorMap
import re


@dataclass
class Color(int):
    """Class that provides color value representation and functionality."""

    def __str__(self):
        return hex(self)

    @classmethod
    def from_string(cls, color: str):
        color = color.lower()
        rgb = ColorMap.get(color)
        #if rgb:
        # TODO:
        #string = string.lstrip('#')
        #tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return Color()

    def to_rgb(self) -> str:
        return f"#{self:06x}"
