import os
import platform
from functools import cache
from pathlib import Path

# @cache
# def get_temp_dir() -> Path:
#    import tempfile
#
#    return Path(tempfile.gettempdir()).absolute()


@cache
def get_data_dir() -> Path:
    # Linux: $XDG_DATA_HOME/gonzago or ~/.local/share/gonzago
    # Windows: %APPDATA%\gonzago
    # MacOS: ~/Library/Application Support/gonzago

    match platform.system():
        case "Linux":
            if "XDG_DATA_HOME" in os.environ:
                path = Path(os.environ["XDG_DATA_HOME"])
            else:
                path = Path.home().joinpath(".local/share")
        case "Windows":
            path = Path(os.environ["APPDATA"])
        case "Darwin":  # MacOS
            path = Path.home().joinpath("Library/Application Support")
        case _:
            path = Path.cwd().joinpath(".data")

    return path.joinpath("gonzago").resolve()


@cache
def get_config_dir() -> Path:
    # Linux: $XDG_CONFIG_HOME/gonzago or ~/.config/gonzago
    # Windows: %APPDATA%\gonzago
    # MacOS: ~/Library/Preferences/gonzago

    match platform.system():
        case "Linux":
            if "XDG_CONFIG_HOME" in os.environ:
                path = Path(os.environ["XDG_CONFIG_HOME"])
            else:
                path = Path.home().joinpath(".config")
        case "Windows":
            path = Path(os.environ["APPDATA"])
        case "Darwin":  # MacOS
            path = Path.home().joinpath("Library/Preferences")
        case _:
            path = Path.cwd().joinpath(".config")

    return path.joinpath("gonzago").resolve()


@cache
def get_cache_dir() -> Path:
    # Linux: $XDG_CACHE_HOME/gonzago or ~/.cache/gonzago
    # Windows: %LOCALAPPDATA%\gonzago
    # MacOS: ~/Library/Caches/gonzago

    match platform.system():
        case "Linux":
            if "XDG_CACHE_HOME" in os.environ:
                path = Path(os.environ["XDG_CACHE_HOME"])
            else:
                path = Path.home().joinpath(".cache").absolute()
        case "Windows":
            path = Path(os.environ["LOCALAPPDATA"]).absolute()
        case "Darwin":  # MacOs
            path = Path.home().joinpath("Library/Caches").absolute()
        case _:
            path = Path.cwd().joinpath(".cache").absolute()

    return path.joinpath("gonzago").resolve()
