import typer

from . import palettes, images, videos

app = typer.Typer()
app.add_typer(palettes.app, name="palettes")
app.add_typer(images.app, name="images")
app.add_typer(videos.app, name="videos")


@app.callback()
def main():
    """
    Manage users CLI app.

    Use it with the create command.

    A new user with the given NAME will be created.
    """


if __name__ == "__main__":
    app()
