# https://inkscape.gitlab.io/inkscape/doxygen-extensions/colors_8py_source.html
# https://github.com/meodai/color-names
# https://en.wikipedia.org/wiki/Web_colors#Extended_colors
# https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
# https://developer.mozilla.org/en-US/docs/Web/CSS/named-color
# https://github.com/ubernostrum/webcolors
# https://pillow.readthedocs.io/en/stable/reference/ImageColor.html

__all__ = "Color"

HEX_COLOR_REGEX_STRING = r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$"

# _NAME_COLOR
# _NAME_PRETTY_NAME
# _COLOR_NAME
# _COLOR_PRETTY_NAME


class Color:
    def __init__(
        self,
        name: str,
        description: str | None = None,
        r: int = 0,
        g: int = 0,
        b: int = 0,
    ) -> None:
        self.name = name
        self.description = description
        self.r = r
        self.g = g
        self.b = b
