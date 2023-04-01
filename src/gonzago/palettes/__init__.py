from pathlib import Path

import yaml
from jsonschema import ValidationError, validate

from gonzago import __version__

from .palette import Palette, Color
from .io import PaletteReader, PaletteWriter, PaletteWriterReader

__all__ = ["Palette", "Color", "PaletteReader", "PaletteWriter", "PaletteWriterReader"]


# https://inkscape.gitlab.io/inkscape/doxygen-extensions/colors_8py_source.html
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
#
#
# class Palette:
#    def __init__(
#        self,
#        name: str,
#        description: str | None = None,
#        version: str | None = None,
#        source: str | None = None,
#    ) -> None:
#        self.name = name
#        self.description = description
#        self.version = version
#        self.source = source
#        self.colors = list[Color]
#
#
# class PaletteTemplate:
#    pass
#
#
# def get_valid_templates(template_folder: Path):
#    # Load palette schema
#    schema_path: Path = Path(__file__).parent.joinpath("palettes.schema.yaml")
#    with schema_path.open() as schema_file:
#        schema: dict = yaml.safe_load(schema_file)
#
#    # Find valid templates in input folder
#    for template_path in template_folder.rglob("*.pal.yaml"):
#        with template_path.open() as template_file:
#            template: dict = yaml.safe_load(template_file)
#            try:
#                validate(template, schema)
#                yield template_path, template
#            except ValidationError:
#                pass
#            except:
#                pass


def build_palettes_from_templates(template_folder: Path, output_folder: Path) -> None:
    #    from gonzago.palettes.templates import get_valid_templates
    #
    #    for template_path, template in get_valid_templates(template_folder):
    #        rel_path = template_path.relative_to(template_folder)
    #        print(rel_path)

    # find templates in input folder
    # for each template
    #   load template
    #   generate palettes from template
    #   for each palette
    #       for each exporter
    #           generate output path from template path and palette info? this might be made easier
    #           export template to output path
    pass


def build_templates(src_dir: Path, out_dir: Path):
    import yaml
    from jsonschema import validate

    # Load palette schema
    schema_path: Path = Path(__file__).parent.joinpath("palettes.schema.yaml")
    with schema_path.open() as schema_file:
        schema: dict = yaml.safe_load(schema_file)

    # Find valid templates in input folder
    templates: dict = dict()
    for src_file in src_dir.rglob("*.pal.y[a]ml"):
        with src_file.open() as template_file:
            template: dict = yaml.safe_load(template_file)
            try:
                validate(template, schema)
            except:
                continue
            rel_path: Path = src_file.with_suffix("").relative_to(src_dir)
            templates[rel_path] = template

    print(templates)

    # Write palette
    for rel_path in templates:
        out_file: Path = out_dir.joinpath(rel_path).with_suffix(".gpl").resolve()
        out_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folders
        print(out_file)

        template = templates[rel_path]

        with out_file.open("w") as file:
            file.write("GIMP Palette\n")
            file.write(f"Name: {template['name']}\n")
            file.write(f"Columns: 0\n")

            if template.get("description", None):
                file.write(f"# Description: {template['description']}\n")
            if template.get("version", None):
                file.write(f"# Version: {template['version']}\n")
            if template.get("author", None):
                file.write(f"# Author: {template['author']}\n")
            if template.get("source", None):
                file.write(f"# Source: {template['source']}\n")

            file.write(f"#")

            for color_data in template["colors"]:
                file.write("\n")
                for i in [1,2,5]:
                    file.write(f"{str(int(color_data['color'][i:i+2], 16))}\t")
                file.write(color_data["name"])
                if color_data.get("description", None):
                    file.write(f" - {color_data['description']}")
