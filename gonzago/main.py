from typing import Annotated, Optional

import typer
from rich.console import Console

from . import (CONFIG_FILE_PATH, __app_name__, __version__, images, palettes,
               videos)

console: Console = Console()
app = typer.Typer(name=__app_name__)
app.add_typer(palettes.app, name="palettes")
app.add_typer(images.app, name="images")
app.add_typer(videos.app, name="videos")


@app.command("init")
def init() -> None:
    """
    Initialize Gonzago Design Tools.
    """
    console.print(CONFIG_FILE_PATH)


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback(no_args_is_help=True)
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = None
) -> None:
    """
    Gonzago Design Tools.

    Command line interface providing tools to automate Gonzago design asset production.
    """
    return


if __name__ == "__main__":
    app()
