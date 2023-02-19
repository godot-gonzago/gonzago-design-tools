import gonzago.colors

from pathlib import Path

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_color(capsys):
    with capsys.disabled():
        pass
