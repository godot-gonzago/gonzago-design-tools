from gonzago.palettes.io import find_palette_file_handlers

from pathlib import Path

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_io(capsys):
    with capsys.disabled():
        find_palette_file_handlers()
        pass
