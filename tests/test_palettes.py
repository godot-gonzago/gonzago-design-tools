from pathlib import Path
from gonzago.palettes import build_palettes

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_io(capsys):
    with capsys.disabled():
        build_palettes(SCRIPT_PATH.joinpath("data"), SCRIPT_PATH.joinpath("output"))
        print(Path.home())
        pass
