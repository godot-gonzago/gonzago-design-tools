# https://docs.blender.org/manual/en/latest/advanced/command_line/render.html
# https://wiki.blender.org/wiki/Building_Blender/Other/BlenderAsPyModule
# https://docs.blender.org/manual/en/latest/files/media/video_formats.html
# https://github.com/kkroening/ffmpeg-python
# https://github.com/jonghwanhyeon/python-ffmpeg

import typer

app = typer.Typer()


@app.callback()
def main():
    """
    Manage users CLI app.

    Use it with the create command.

    A new user with the given NAME will be created.
    """


if __name__ == "__main__":
    app()
