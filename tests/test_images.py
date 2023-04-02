import gonzago.images

from pathlib import Path

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_icons(capsys):
    with capsys.disabled():
        src_dir: Path = SCRIPT_PATH.joinpath("data/icons")
        out_dir: Path = SCRIPT_PATH.joinpath("output/icons")
        gonzago.images.optimize_icons(src_dir, out_dir)


def test_svg_to_png(capsys):
    with capsys.disabled():
        src_dir: Path = SCRIPT_PATH.joinpath("data/icons/icon.svg")
        out_dir: Path = SCRIPT_PATH.joinpath("output/png/icon.png")
        gonzago.images.svg_to_png(src_dir, out_dir)

        src_dir: Path = SCRIPT_PATH.joinpath("data/splash.svg")
        out_dir: Path = SCRIPT_PATH.joinpath("output/png/splash.png")
        gonzago.images.inkscape_to_png(src_dir, out_dir)


def test_os_icons(capsys):
    with capsys.disabled():
        src_dir: Path = SCRIPT_PATH.joinpath("data/application")
        out_dir: Path = SCRIPT_PATH.joinpath("output/application")
        gonzago.images.build_os_icons(src_dir.glob("*.svg"), out_dir)
