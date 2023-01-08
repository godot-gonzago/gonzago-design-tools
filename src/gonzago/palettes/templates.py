from pathlib import Path

import yaml
from jsonschema import ValidationError, validate


# https://inkscape.gitlab.io/inkscape/doxygen-extensions/colors_8py_source.html
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


class Palette:
    def __init__(
        self,
        name: str,
        description: str | None = None,
        version: str | None = None,
        source: str | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self.version = version
        self.source = source
        self.colors = list[Color]


class PaletteTemplate:
    pass


def get_valid_templates(template_folder: Path):
    # Load palette schema
    schema_path: Path = Path(__file__).parent.joinpath("palettes.schema.yaml")
    with schema_path.open() as schema_file:
        schema: dict = yaml.safe_load(schema_file)

    # Find valid templates in input folder
    for template_path in template_folder.rglob("*.pal.yaml"):
        with template_path.open() as template_file:
            template: dict = yaml.safe_load(template_file)
            try:
                validate(template, schema)
                yield template_path, template
            except ValidationError:
                pass
            except:
                pass
