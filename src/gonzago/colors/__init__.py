# https://inkscape.gitlab.io/inkscape/doxygen-extensions/colors_8py_source.html
# https://github.com/meodai/color-names
# https://en.wikipedia.org/wiki/Web_colors#Extended_colors
# https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
# https://developer.mozilla.org/en-US/docs/Web/CSS/named-color
# https://github.com/ubernostrum/webcolors
# https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
from math import sqrt

from gonzago.colors.data import Color

__all__ = ["Color"]


HEX_COLOR_REGEX_STRING = r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$"

# _NAME_COLOR
# _NAME_PRETTY_NAME
# _COLOR_NAME
# _COLOR_PRETTY_NAME

#def hex_to_rgb(hex):
#    rgb = []
#    for i in (0, 2, 4):
#        decimal = int(hex[i:i+2], 16)
#        rgb.append(decimal)
#    return tuple(rgb)

# https://developer.mozilla.org/en-US/docs/Web/CSS/color
# https://realpython.com/python-property/
# https://docs.python.org/3.11/library/colorsys.html
# class Color:
#    def __init__(
#        self,
#        name: str,
#        description: str | None = None,
#        r: int = 0,
#        g: int = 0,
#        b: int = 0,
#    ) -> None:
#        self.name = name
#        self.description = description
#        self.r = r
#        self.g = g
#        self.b = b


def square_distance(c1: Color, c2: Color) -> float:
    return pow(c2.r - c1.r, 2) + pow(c2.g - c1.g, 2) + pow(c2.b - c1.b, 2)


def distance(c1: Color, c2: Color) -> float:
    return sqrt(square_distance(c1, c2))


# Color spaces?
# Color conversion?
