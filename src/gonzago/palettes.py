import csv
import re
from dataclasses import dataclass
from io import TextIOWrapper
from pathlib import PurePath
from tokenize import String
from typing import Iterator, NamedTuple

import requests
import yaml
from PIL import ImageColor
from tomlkit import comment, document, nl, table, array
from tomlkit.items import Item

ColorPair = NamedTuple("ColorPair", dark=str, light=str, comment=str, line=int)
NamedColor = NamedTuple("NamedColor", name=str, color=str)
NamedColorPair = NamedTuple("NamedColor", name=str, dark=str, light=str)


@dataclass
class ColorValue:
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0

    @classmethod
    def from_string(cls, color):
        rgb = ImageColor.getrgb(color)
        return cls(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) > 3 else 1.0)

    def to_hex_rgb(self, upper: bool = False) -> str:
        hex_rgb: str = (
            f"#{int(self.r * 255):02x}{int(self.g * 255):02x}{int(self.b * 255):02x}"
        )
        return hex_rgb.upper() if upper else hex_rgb


# TODO: Make name, description mixin https://www.pythontutorial.net/python-oop/python-mixin/
# TODO: Color groups/categories as well?
@dataclass
class ColorDescriptor:
    name: str
    description: str | None = None


@dataclass
class ThemeDescriptor:
    name: str
    description: str | None = None


@dataclass
class ThemeColorMap:
    # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    # https://www.tutorialspoint.com/python_data_structure/python_2darray.htm
    # https://appdividend.com/2022/06/02/how-to-convert-python-tuple-to-dataframe/
    # https://docs.python.org/3/library/collections.abc.html
    # https://www.geeksforgeeks.org/__getitem__-in-python/

    _themes: list[  # columns
        ThemeDescriptor
    ]  # unique names? never empty at least has 'default', first is name of default, copy values from default if new theme is added
    _colors: list[ColorDescriptor]  # not unique names? rows descriptors
    _values: list[ColorValue]  # list of all values (2d index, width * row + col)

    # [(theme: int | str | None, color: int | str | None)] for indexing (str = lookup int index?)
    # [0, 0] get value for theme and color
    # [0, ] or [0] get list of values for theme
    # [ , 0] get list of values for color
    # [] get full ordered list?
    # TODO: filter for color groups/categories?


@dataclass
class PaletteDescriptor:
    name: str
    description: str
    categories: list[str]
    entries: ThemeColorMap

    @classmethod
    def from_godot_source(cls):
        # rgb = ImageColor.getrgb(color)
        # return cls(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) > 3 else 1.0)
        pass

    @classmethod
    def from_toml(cls, item: Item):
        pass

    # https://realpython.com/python-toml/
    # https://pypi.org/project/tomlkit/
    # https://github.com/sdispater/tomlkit/blob/master/docs/quickstart.rst

    # https://github.com/sdispater/tomlkit/blob/master/tomlkit/items.py Item is base class
    # TODO: Return such item so it can be called on children

    def to_toml(self) -> Item:
        item = table()
        item.add("name", self.name)
        item.add("description", self.description)
        item.add("categories", array().extend(self.categories))
        return item

    def to_toml_str(self) -> str:
        # File data
        doc = document()
        doc.add(comment("This is a TOML document."))
        doc.add(nl())
        doc.append("title", "TOML Example")

        # Palette data
        doc.append("palette", self.to_toml())

        # Color data
        # TODO: array of color description with array of values

        return doc.as_string()


def download_color_pairs() -> Iterator[ColorPair]:
    respone = requests.get(
        "https://github.com/godotengine/godot/raw/master/editor/editor_themes.cpp"
    )

    # https://pythex.org/
    pattern = re.compile(
        r'"(#[a-fA-F0-9]{6})".*"(#[a-fA-F0-9]{6})"(?:.*[\/]{2}?[ \t]*(\w+[ \t\w]*))?'
    )
    line_pattern = re.compile(r"\n")

    last_pos: int = -1
    line_count: int = 1

    for result in pattern.finditer(respone.text):
        pos: int = result.start(0)
        for _ in line_pattern.finditer(respone.text, last_pos, pos):
            line_count += 1
        last_pos = pos

        pair: ColorPair = ColorPair(
            result.group(1),
            result.group(2),
            result.group(3) if result.lastindex > 2 else "",
            line_count,
        )
        yield pair
