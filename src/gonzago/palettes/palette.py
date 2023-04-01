# Build based on schema (ignore groups as they are only available in ase)

from dataclasses import dataclass, field
from typing import NamedTuple


class ColorValue(NamedTuple):
    r: int = 0
    g: int = 0
    b: int = 0


@dataclass
class Color:
    name: str
    description: str = ""
    value: ColorValue = ColorValue()
    variants: dict[str, ColorValue] = field(default_factory=dict)

    def get_variant_value(self, variant: str) -> ColorValue:
        self.variants.get(variant, self.value)


@dataclass
class Palette:
    name: str
    description: str = ""
    version: str = ""
    author: str = ""
    source: str = ""
    colors: list[Color] = field(default_factory=list)
