# https://inkscape.gitlab.io/inkscape/doxygen-extensions/colors_8py_source.html
# https://github.com/meodai/color-names
# https://en.wikipedia.org/wiki/Web_colors#Extended_colors
# https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
# https://developer.mozilla.org/en-US/docs/Web/CSS/named-color
# https://github.com/ubernostrum/webcolors

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
