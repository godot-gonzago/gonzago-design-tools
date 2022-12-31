import re
from math import sqrt
from typing import NamedTuple


class Color(NamedTuple):
    r: float
    g: float
    b: float
    a: float = 1.0

    @classmethod
    def from_hex_string(cls, color: str):
        if re.match("#[a-f0-9]{3}$", color):
            return Color(
                int(color[1] * 2, 16) / 255.0,
                int(color[2] * 2, 16) / 255.0,
                int(color[3] * 2, 16) / 255.0,
            )
        if re.match("#[a-f0-9]{4}$", color):
            return Color(
                int(color[1] * 2, 16) / 255.0,
                int(color[2] * 2, 16) / 255.0,
                int(color[3] * 2, 16) / 255.0,
                int(color[4] * 2, 16) / 255.0,
            )
        if re.match("#[a-f0-9]{6}$", color):
            return Color(
                int(color[1:3], 16) / 255.0,
                int(color[3:5], 16) / 255.0,
                int(color[5:7], 16),
            )
        if re.match("#[a-f0-9]{8}$", color):
            return Color(
                int(color[1:3], 16) / 255.0,
                int(color[3:5], 16) / 255.0,
                int(color[5:7], 16) / 255.0,
                int(color[7:9], 16) / 255.0,
            )
        raise ValueError

    def to_hex_string(self, include_alpha: bool = False, shorten: bool = False) -> str:
        return f"#{int(self.r * 255):02x}{int(self.g * 255):02x}{int(self.b * 255):02x}"

    def get_length(self, include_alpha: bool = False) -> float:
        sum: float = self.r**2 + self.g**2 + self.b**2
        if include_alpha:
            sum += self.a**2
        return sqrt(sum)


# Color names api: https://github.com/meodai/color-names
