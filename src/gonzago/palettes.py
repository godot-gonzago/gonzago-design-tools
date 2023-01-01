from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, NamedTuple
import re


class Color(NamedTuple):
    r: float
    g: float
    b: float
    a: float = 1.0


@dataclass
class PaletteTemplate:
    themes: list[str] = field(default_factory=dict)
    comment: str | None = None
    version: str | None = None


@dataclass
class PaletteEntry:
    name: str
    color: Color
    description: str | None = None
    comment: str | None = None


@dataclass
class Palette(list[PaletteEntry]):
    name: str
    description: str | None = None
    comment: str | None = None
    # entries: list[PaletteEntry] = field(default_factory=list)


# Find template files in folder (relative paths)
def find_templates(template_folder: Path) -> list[Path]:
    # templates: list[Path] = []
    # for path in template_folder.rglob('*.txt'):
    #    templates.append(path.relative_to(input))
    # return templates
    return list(template_folder.rglob("*.txt"))


# Read template from file
def read_template(template_path: Path) -> PaletteTemplate:
    # https://pythex.org/
    # https://docs.python.org/3/howto/regex.html

    with template_path.open('r') as f:
        # File header
        m = re.match(r'^[ |\t]*[\/]{2,}[ |\t]*GonzagoDesignToolsPalette', f.readline())
        if not m:
            raise TypeError(f'File {template_path.absolute()} is not a valid palette template file!')

        # comment = r'[\/]{2,}\s*(?P<comment>\S.*)?'
        # attribute = r'(?:^[ |\t]*[\/]{2,}[ |\t]*@(?P<attr>\w+(?:\.\w+)*)[ |\t]*:[ |\t]*(?P<attr_value>.*))' /gm
        # themes = r'//\s*@themes:\s*(?P<themes>\w+(?:\s*,\s*\w+)?)'
        # name = r'^//\s*@name:\s*(?P<name>[^//|\n]*)(?:$|\s*//\s*(?P<comment>.*)$)' -> not working yet
        # colors = (?P<colors>#[a-fA-F0-9]{6}(?:[ ]+#[a-fA-F0-9]{6})?)[ ]+(?P<name>[^//|\n]+)(?:[ ]*//[ ]*(?P<comment>.*))?
        # color match (for use in colors) = r'(?P<color>#[a-fA-F0-9]{6})'


# Generate palettes (exportable data structures from template) list from template
def generate_palettes(template: PaletteTemplate):  # -> Generator[Palette]:
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
