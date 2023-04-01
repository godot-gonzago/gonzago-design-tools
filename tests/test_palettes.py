from pathlib import Path
from gonzago.palettes import build_templates

from gonzago.palettes.io import find_palette_file_handlers, get_valid_templates

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_io(capsys):
    with capsys.disabled():
        #for template in get_valid_templates(SCRIPT_PATH):
        #    print(template)

        #find_palette_file_handlers()

        build_templates(SCRIPT_PATH.joinpath("data"), SCRIPT_PATH.joinpath("output"))
        pass
