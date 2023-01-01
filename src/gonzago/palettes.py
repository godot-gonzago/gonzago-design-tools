from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, NamedTuple
import re


# Find template files in folder (relative paths)
def find_templates(template_folder: Path) -> list[Path]:
    # templates: list[Path] = []
    # for path in template_folder.rglob('*.txt'):
    #    templates.append(path.relative_to(input))
    # return templates
    return list(p.relative_to(template_folder) for p in template_folder.rglob("*.txt"))


# Read template from file
def read_template(template_path: Path):
    pass


# Generate palettes (exportable data structures from template) list from template
def generate_palettes(template):  # -> Generator[Palette]:
    pass


# Export palette from all known exporter
def export_palette(palette, output_folder: Path):
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
