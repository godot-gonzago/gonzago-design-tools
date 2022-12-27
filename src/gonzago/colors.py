import colorsys
import re
from dataclasses import dataclass
from typing import NamedTuple, Sequence

from PIL.ImageColor import colormap as ColorMap

# https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
# https://docs.python.org/3/library/colorsys.html#module-colorsys
# https://github.com/edaniszewski/colorutils/tree/master/colorutils

# https://developer.mozilla.org/en-US/docs/Web/CSS/color
# <named-color> values: color: red;
# <hex-color> values: color: #090; color: #009900; color: #090a; color: #009900aa;
# <rgb()> values: color: rgb(34, 12, 64, 0.6); color: rgba(34, 12, 64, 0.6);
# <hsl()> values: color: hsl(30, 100%, 50%, 0.6); color: hsla(30, 100%, 50%, 0.6);
# <hwb()> values


RGB32 = NamedTuple("RGB32", r=int, g=int, b=int)
RGBA32 = NamedTuple("RGBA32", r=int, g=int, b=int, a=int)
RGB = NamedTuple("RGB", r=float, g=float, b=float)
RGBA = NamedTuple("RGBA", r=float, g=float, b=float, a=float)
HSV = NamedTuple("HSV", h=float, s=float, v=float)
HSVA = NamedTuple("HSVA", h=float, s=float, v=float, a=float)

ColorChannel = float | int | str


# https://zetcode.com/python/magicmethods/
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

    def _convert_channel(self, value: ColorChannel) -> float | None:
        if isinstance(value, str):
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

    # https://www.programiz.com/python-programming/methods/built-in/classmethod
    @classmethod
    def create(cls, color: str | int | Sequence):
        if isinstance(color, str):
            color = color.lower()
            return cls(0, 0, 0, 1)

        if isinstance(color, int):
            return cls(0, 0, 0, 1)

        # if isinstance(color, Sequence):
        #    length: int = len(color)

        # if isinstance(color, RGBA32):
        #    return cls(color.r / 255, color.g / 255, color.b / 255, color.a / 255)
        # if isinstance(color, RGB32):
        #    return cls(color.r, color.g, color.b)
        # if isinstance(color, RGBA):
        #    return cls(color.r, color.g, color.b, color.a)
        # if isinstance(color, RGB):
        #    return cls(color.r, color.g, color.b)

        c = cls(0, 0, 0, 1)
        return c

    @classmethod
    def from_int(cls, color: int):
        c = cls(0, 0, 0, 1)
        return c

    @staticmethod
    def from_string(color: str):
        # rgb = ColorMap.get(color)
        # if rgb:
        # TODO:
        # tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

        color = color.lstrip("#").lower()
        return Color(
            int(color[0:2], 16) / 255.0,
            int(color[2:4], 16) / 255.0,
            int(color[4:6], 16) / 255.0,
        )

    def to_hex(self, upper: bool = False) -> str:
        rgb: RGB32 = self.to_rgb32()
        hex_str: str = f"0x{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}"
        return hex_str.upper() if upper else hex_str

    def to_hex_rgb(self, upper: bool = False) -> str:
        rgb: RGB32 = self.to_rgb32()
        hex_rgb: str = f"#{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}"
        return hex_rgb.upper() if upper else hex_rgb

    # TODO: Make properties?
    def to_rgb32(self) -> RGB32:
        return RGB32(int(self.r * 255), int(self.g * 255), int(self.b * 255))

    def to_rgba32(self) -> RGBA32:
        return RGBA32(
            int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255)
        )

    def to_rgb(self) -> RGB:
        return RGB(self.r, self.g, self.b)

    def to_rgba(self) -> RGBA:
        return RGBA(self.r, self.g, self.b, self.a)

    def to_hsv(self) -> HSV:
        hsv: tuple[float, float, float] = colorsys.rgb_to_hsv(self.r, self.g, self.b)
        return HSV(hsv[0], hsv[1], hsv[2])

    def to_hsva(self) -> HSVA:
        hsv: tuple[float, float, float] = colorsys.rgb_to_hsv(self.r, self.g, self.b)
        return HSVA(hsv.r, hsv.g, hsv.b, self.a)


def getrgb(color):
    """
     Convert a color string to an RGB or RGBA tuple. If the string cannot be
     parsed, this function raises a :py:exc:`ValueError` exception.

    .. versionadded:: 1.1.4

    :param color: A color string
    :return: ``(red, green, blue[, alpha])``
    """
    if len(color) > 100:
        raise ValueError("color specifier is too long")
    color = color.lower()

    rgb = colormap.get(color, None)
    if rgb:
        if isinstance(rgb, tuple):
            return rgb
        colormap[color] = rgb = getrgb(rgb)
        return rgb

    # check for known string formats
    if re.match("#[a-f0-9]{3}$", color):
        return int(color[1] * 2, 16), int(color[2] * 2, 16), int(color[3] * 2, 16)

    if re.match("#[a-f0-9]{4}$", color):
        return (
            int(color[1] * 2, 16),
            int(color[2] * 2, 16),
            int(color[3] * 2, 16),
            int(color[4] * 2, 16),
        )

    if re.match("#[a-f0-9]{6}$", color):
        return int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

    if re.match("#[a-f0-9]{8}$", color):
        return (
            int(color[1:3], 16),
            int(color[3:5], 16),
            int(color[5:7], 16),
            int(color[7:9], 16),
        )

    m = re.match(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$", color)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3))

    m = re.match(r"rgb\(\s*(\d+)%\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)$", color)
    if m:
        return (
            int((int(m.group(1)) * 255) / 100.0 + 0.5),
            int((int(m.group(2)) * 255) / 100.0 + 0.5),
            int((int(m.group(3)) * 255) / 100.0 + 0.5),
        )

    m = re.match(
        r"hsl\(\s*(\d+\.?\d*)\s*,\s*(\d+\.?\d*)%\s*,\s*(\d+\.?\d*)%\s*\)$", color
    )
    if m:
        from colorsys import hls_to_rgb

        rgb = hls_to_rgb(
            float(m.group(1)) / 360.0,
            float(m.group(3)) / 100.0,
            float(m.group(2)) / 100.0,
        )
        return (
            int(rgb[0] * 255 + 0.5),
            int(rgb[1] * 255 + 0.5),
            int(rgb[2] * 255 + 0.5),
        )

    m = re.match(
        r"hs[bv]\(\s*(\d+\.?\d*)\s*,\s*(\d+\.?\d*)%\s*,\s*(\d+\.?\d*)%\s*\)$", color
    )
    if m:
        from colorsys import hsv_to_rgb

        rgb = hsv_to_rgb(
            float(m.group(1)) / 360.0,
            float(m.group(2)) / 100.0,
            float(m.group(3)) / 100.0,
        )
        return (
            int(rgb[0] * 255 + 0.5),
            int(rgb[1] * 255 + 0.5),
            int(rgb[2] * 255 + 0.5),
        )

    m = re.match(r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$", color)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    raise ValueError(f"unknown color specifier: {repr(color)}")


# http://web.simmons.edu/~grovesd/comm244/notes/week3/css-colors
# https://www.webucator.com/article/python-color-constants-module/
# https://www.cssportal.com/css3-color-names/
# https://www.w3.org/wiki/CSS/Properties/color/keywords
# https://www.w3.org/TR/css-color-4/#named-colors

colormap: dict[str, str] = {
    # X11 colour table from https://drafts.csswg.org/css-color-4/, with
    # gray/grey spelling issues fixed.  This is a superset of HTML 4.0
    # colour names used in CSS 1.
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50",
    "cornflowerblue": "#6495ed",
    "cornsilk": "#fff8dc",
    "crimson": "#dc143c",
    "cyan": "#00ffff",
    "darkblue": "#00008b",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgrey": "#a9a9a9",
    "darkgreen": "#006400",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslateblue": "#483d8b",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "deepskyblue": "#00bfff",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1e90ff",
    "firebrick": "#b22222",
    "floralwhite": "#fffaf0",
    "forestgreen": "#228b22",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "gold": "#ffd700",
    "goldenrod": "#daa520",
    "gray": "#808080",
    "grey": "#808080",
    "green": "#008000",
    "greenyellow": "#adff2f",
    "honeydew": "#f0fff0",
    "hotpink": "#ff69b4",
    "indianred": "#cd5c5c",
    "indigo": "#4b0082",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgreen": "#90ee90",
    "lightgray": "#d3d3d3",
    "lightgrey": "#d3d3d3",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "lime": "#00ff00",
    "limegreen": "#32cd32",
    "linen": "#faf0e6",
    "magenta": "#ff00ff",
    "maroon": "#800000",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "oldlace": "#fdf5e6",
    "olive": "#808000",
    "olivedrab": "#6b8e23",
    "orange": "#ffa500",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "pink": "#ffc0cb",
    "plum": "#dda0dd",
    "powderblue": "#b0e0e6",
    "purple": "#800080",
    "rebeccapurple": "#663399",
    "red": "#ff0000",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "saddlebrown": "#8b4513",
    "salmon": "#fa8072",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "silver": "#c0c0c0",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "snow": "#fffafa",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "tan": "#d2b48c",
    "teal": "#008080",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "violet": "#ee82ee",
    "wheat": "#f5deb3",
    "white": "#ffffff",
    "whitesmoke": "#f5f5f5",
    "yellow": "#ffff00",
    "yellowgreen": "#9acd32",
}
