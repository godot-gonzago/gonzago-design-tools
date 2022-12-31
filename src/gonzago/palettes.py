from dataclasses import dataclass
from pathlib import Path
from typing import Generator, NamedTuple


class Color(NamedTuple):
    r: float
    g: float
    b: float
    a: float = 1.0


class ColorInfo(NamedTuple):
    name: str
    description: str | None = None


class PaletteInfo(NamedTuple):
    file_name: str
    name: str
    description: str | None = None


@dataclass
class PaletteTemplate:
    pass


@dataclass
class Palette:
    pass


# Find template files in folder (relative paths)
def find_templates(template_folder: Path) -> list[Path]:
    # templates: list[Path] = []
    # for path in template_folder.rglob('*.py'):
    #    templates.append(path.relative_to(input))
    # return templates
    return list(template_folder.rglob("*.py"))


# Read template from file
def read_template(template_path: Path) -> PaletteTemplate:
    pass


# Generate palettes (exportable data structures from template) list from template
def generate_palettes(template: PaletteTemplate):# -> Generator[Palette]:
    pass


# Export palette from all known exporter
def export_palette(palette: Palette, output_folder: Path):
    pass


def build(input_folder: Path, output_folder: Path) -> None:
    # find templates in input folder
    # for each template
    #   load template
    #   generate palettes from template
    #   for each palette
    #       for each exporter
    #           generate output path from template path and palette info? this might be made easier
    #           export template to output path
    pass


if __name__ == "__main__":
    pass
