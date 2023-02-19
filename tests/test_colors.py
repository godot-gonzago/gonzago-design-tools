import gonzago.colors

from pathlib import Path

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_color(capsys):
    with capsys.disabled():
        col1 = gonzago.colors.Color()
        col2 = gonzago.colors.Color(1.0, 1.0, 1.0)
        print(col1)
        print(col2)
        print(gonzago.colors.square_distance(col1, col2))
        pass
