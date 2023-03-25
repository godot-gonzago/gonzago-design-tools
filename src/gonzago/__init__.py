__version__ = "0.0.1"
__all__ = ["core", "colors", "palettes", "images", "videos"]

from pathlib import Path


SCRIPTS_PATH: Path = Path(__file__).parent.resolve()

# TODO:
# https://davidebove.com/blog/2019/09/29/a-modular-template-for-extensible-python-projects/
# https://dev.to/charlesw001/plugin-architecture-in-python-jla
# https://www.youtube.com/watch?v=iCE1bDoit9Q -> https://github.com/ArjanCodes/2021-plugin-architecture/tree/main/after
