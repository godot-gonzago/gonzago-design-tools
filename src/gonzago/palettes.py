import csv
import re
from io import TextIOWrapper
from pathlib import PurePath
from tokenize import String
from typing import Iterator, NamedTuple

import requests
import yaml
from PIL import ImageColor

ColorPair = NamedTuple("ColorPair", dark=str, light=str, comment=str, line=int)
NamedColor = NamedTuple("NamedColor", name=str, color=str)
NamedColorPair = NamedTuple("NamedColor", name=str, dark=str, light=str)

# https://pyyaml.org/wiki/PyYAMLDocumentation
# Implicit resolver for color
# Constructors, representers, resolvers
# import re
# pattern = re.compile(r'^\d+d\d+$')
# yaml.add_implicit_resolver(u'!dice', pattern)
# class MyYAMLObject(YAMLObject): ???

# see https://www.programcreek.com/python/?code=facelessuser%2Fpyspelling%2Fpyspelling-master%2Fpyspelling%2Futil%2F__init__.py def yaml_load(source, loader=yaml.Loader):
# https://gist.github.com/danielpops/5a0726f2fb6288da749c4cd604276be8
# https://matthewpburruss.com/post/yaml/
# https://death.andgravity.com/any-yaml
# https://net-square.com/yaml-deserialization-attack-in-python.html
# yaml.add_implicit_resolver in custom loader

# Maybe just make dictionary derived classes with required keys or something of the sort.

class Palette:
    name: str
    description: str
    category: str


class PaletteColorsMixin:
    colors: list[NamedColor]


class PalettePairsMixin:
    pairs: list[NamedColorPair]


class GodotPalette(PalettePairsMixin, Palette):
    pass

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
