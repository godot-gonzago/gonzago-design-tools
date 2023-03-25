# TODO Reader/Writer name and description?
# TODO Config initialize with and get default values?


from abc import ABC, abstractmethod
from pathlib import Path
from jsonschema import ValidationError, validate

import yaml

from gonzago.palettes.palette import Palette


class PaletteIOBase(ABC):
    @abstractmethod
    def get_recognized_extensions(self) -> list[str]:
        raise NotImplementedError


class PaletteReader(PaletteIOBase):
    @abstractmethod
    def read(self, file_path: Path) -> Palette:
        raise NotImplementedError


class PaletteWriter(PaletteIOBase):
    @abstractmethod
    def write(self, file_path: Path, palette: Palette):
        raise NotImplementedError


class PaletteWriterReader(PaletteWriter, PaletteReader):
    pass


def find_palette_file_handlers():
    for path in Path(__file__).parent.joinpath("formats").glob("[!__]*.py"):
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        print(path)


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
