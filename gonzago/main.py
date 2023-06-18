import typer

import palettes
import images
import videos

app = typer.Typer()
app.add_typer(palettes.app, name="palettes")
app.add_typer(images.app, name="images")
app.add_typer(videos.app, name="videos")

if __name__ == "__main__":
    app()
