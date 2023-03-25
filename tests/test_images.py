import gonzago.images

from pathlib import Path

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_icons(capsys):
    with capsys.disabled():
        src_dir: Path = SCRIPT_PATH.joinpath("data")
        out_dir: Path = SCRIPT_PATH.joinpath("output")
        gonzago.images.optimize_icons(src_dir, out_dir)
