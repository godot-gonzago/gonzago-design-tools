# TODO Reader/Writer name and description?
# TODO Config initialize with and get default values?


from abc import ABC, abstractmethod
from pathlib import Path

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
