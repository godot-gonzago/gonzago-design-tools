# <https://www.cyotek.com/cyotek-palette-editor/supported-palette-formats>
# <https://lospec.com/palette-list/fuzzyfour>
# <http://www.selapa.net/swatches/colors/fileformats.php>
# <https://docs.krita.org/en/untranslatable_pages/kpl_defintion.html>

# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/logging.html

from pathlib import Path
from typing import Callable, Generator, Iterator, NamedTuple, Optional

import typer
import yaml
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

app = typer.Typer()
console: Console = Console()


class ExporterInfo(NamedTuple):
    name: str
    description: str
    suffix: str
    fn: Callable[[Path, dict], None]


EXPORTERS = dict[str, ExporterInfo]()


def exporter(id: str, name: str, description: str, suffix: str) -> Callable:
    def inner(fn) -> Callable[[Path, dict], None]:
        EXPORTERS[id] = ExporterInfo(
            name=name, description=description, suffix=suffix, fn=fn
        )
        return fn

    return inner


@exporter("png", "PNG", "PNG palette image with size 1px.", ".png")
def export_png(out_file: Path, template: dict, size: int = 1) -> None:
    from PIL import Image, ImageDraw

    color_count: int = len(template["colors"])
    image: Image = Image.new("RGB", (color_count * size, size))

    draw = ImageDraw.Draw(image, "RGB")
    for i in range(color_count):
        color = template["colors"][i]["color"]
        draw.rectangle((i * size, 0, i * size + size, size), color)

    image.save(out_file, "PNG")


@exporter("png-8", "PNG", "PNG palette image with size 8px.", ".x8.png")
def export_png_8(out_file: Path, template: dict) -> None:
    export_png(out_file, template, 8)


@exporter("png-32", "PNG", "PNG palette image with size 32px.", ".x32.png")
def export_png_8(out_file: Path, template: dict):
    export_png(out_file, template, 32)


@exporter("gpl", "Gimp", "Gimp/Inkscape color palette.", ".gpl")
def export_gimp(out_file: Path, template: dict):
    with out_file.open("w") as file:
        file.write("GIMP Palette\n")
        file.write(f"Name: {template['name']}\n")
        file.write(f"Columns: 0\n")

        if template.get("description", None):
            file.write(f"# Description: {template['description']}\n")
        if template.get("version", None):
            file.write(f"# Version: {template['version']}\n")
        if template.get("author", None):
            file.write(f"# Author: {template['author']}\n")
        if template.get("source", None):
            file.write(f"# Source: {template['source']}\n")

        file.write(f"#")

        for color_data in template["colors"]:
            file.write("\n")
            for i in [1, 3, 5]:
                file.write(f"{str(int(color_data['color'][i:i+2], 16))}\t")
            file.write(color_data["name"])
            if color_data.get("description", None):
                file.write(f" - {color_data['description']}")


@exporter("hex", "HEX", "Simple HEX color palette.", ".hex")
def export_hex(out_file: Path, template: dict):
    colors = [c["color"].lstrip("#").lower() for c in template["colors"]]
    with out_file.open("w") as file:
        file.writelines("\n".join(colors))


# @exporter("ase", "Adobe Swatch Exchange", "Color palette for Adobe products.", ".ase")
# def export_adobe_swatch_exchange(out_file: Path, template: dict):
#    # https://medium.com/swlh/mastering-adobe-color-file-formats-d29e43fde8eb
#    # http://www.selapa.net/swatches/colors/fileformats.php#adobe_ase
#    with out_file.open("wb") as file:
#        # Write header
#        file.write(b"\x41\x53\x45\x46")  # Signature (Constant: ASEF)
#        file.write(b"\x00\x01\x00\x00")  # Version (Constant: 1.0)
#        file.write(b"\x00\x00\x00\x03")  # Number of blocks
#
#        # Group start
#        file.write(b"\xC0\x01")  # Block type (Group start)
#        file.write(b"\x00\x00\x00\x00")  # Block length
#        file.write(b"\x00\x00")  # Name length
#        file.write(b"\x00")  # 0-terminated group name encoded in UTF-16
#
#        # Color entry
#        file.write(b"\x00\x01")  # Block type (Color entry)
#        file.write(b"\x00\x00\x00\x00")  # Block length
#        file.write(b"\x00\x00")  # Name length
#        file.write(b"\x00")  # 0-terminated color name encoded in UTF-16
#        file.write(b"\x52\x47\x42\x20")  # Color space (Constant: RGB)
#        file.write(b"\x00\x00\x00\x00")  # Red
#        file.write(b"\x00\x00\x00\x00")  # Green
#        file.write(b"\x00\x00\x00\x00")  # Blue
#        file.write(b"\x00\x02")  # Color mode (Constant: Normal)
#
#        # Group end
#        file.write(b"\xC0\x02")  # Block type (Group end)
#        file.write(b"\x00\x00\x00\x00")  # Block length (Constant for Group end)


# @exporter("paint", "Paint.NET", "Paint.NET color palette.", ".txt")
# def export_paint_net(out_file: Path, template: dict):
#    https://www.getpaint.net/doc/latest/WorkingWithPalettes.html
#    ;paint.net Palette File
#    ;Downloaded from Lospec.com/palette-list
#    ;Palette Name: Lospec500
#    ;Description: A collaboration from the Lospec Discord server to create a palette celebrating 500 palettes hosted on Lospec.
#    ;Colors: 42
#    FF10121c
#    FF2c1e31
#    FF6b2643
#    pass


# @exporter("paintshop", "Paintshop Pro", "Paintshop Pro color palette.", ".pal")
# def export_jasc(out_file: Path, template: dict):
#    # https://liero.nl/lierohack/docformats/other-jasc.html
#    # JASC-PAL      <- constant string
#    # 0100          <- constant version of palette file format
#    # 16            <- color count
#    # 255 0 0       <- [0-255] rgb separated by space
#    # 0 255 0
#    # 0 0 255
#    # 255 255 0
#    pass


# @exporter("krita", "Krita", "Krita color palette.", ".kpl")
# def export_krita(out_file: Path, template: dict):
#    # https://docs.krita.org/en/untranslatable_pages/kpl_defintion.html
#    pass


# @exporter("office", "StartOffice", "Color palette for StarOffice/OpenOffice/LibreOffice.", ".soc")
# def export_star_office(out_file: Path, template: dict):
#    # http://www.selapa.net/swatches/colors/fileformats.php#ooo_soc
#    pass


# @exporter("scribus", "Scribus", "Color palette for Scribus.", ".xml")
# def export_scribus(out_file: Path, template: dict):
#    # https://github.com/1j01/anypalette.js
#    pass


def _get_template_schema() -> dict:
    from importlib.resources import files

    schema: dict = yaml.safe_load(
        files("gonzago").joinpath("palettes.schema.yaml").read_text()
    )
    return schema


def _discover_templates(
    dir: Path, recursive: bool = True
) -> Iterator[tuple[Path, dict]]:
    from jsonschema import validate

    schema: dict = _get_template_schema()
    files: Generator[Path, None, None] = (
        dir.rglob("*.y[a]ml") if recursive else dir.glob("*.y[a]ml")
    )
    for file in files:
        with file.open() as template_file:
            template: dict = yaml.safe_load(template_file)
            try:
                validate(template, schema)
            except:
                continue
            yield file, template


@app.command("templates")
def list_templates(
    dir: Annotated[
        Optional[Path],
        typer.Argument(
            help="The name of the user to greet",
            exists=True,
            dir_okay=True,
            readable=True,
            resolve_path=True,
        ),
    ] = None,
    recursive: Annotated[
        Optional[bool], typer.Option(help="The name of the user to greet")
    ] = True,
):
    """
    List the valid templates at the directory.
    """
    # TODO: Make dir optional and fallback to config dir if ommited! Integrate config creation procedure?
    if dir is None:
        console.print("Try to get dir from config")
        return

    table: Table = Table("Path", "Name", "Description")
    for file, template in _discover_templates(dir, recursive):
        table.add_row(
            str(file.relative_to(dir)),
            template["name"],
            template.get("description", ""),
        )
    if table.row_count > 0:
        console.print("Found valid palette templates: {}".format(table.row_count))
        console.print(table)
    else:
        console.print("No valid palette templates found!", style="yellow")


@app.command("exporters")
def list_exporters():
    table: Table = Table("id", "Name", "Description", "Suffix")
    for id in EXPORTERS:
        exporter: ExporterInfo = EXPORTERS[id]
        table.add_row(id, exporter.name, exporter.description, exporter.suffix)
    if table.row_count > 0:
        console.print("Available exporters: {}".format(table.row_count))
        console.print(table)
    else:
        console.print("No exporters available!", style="yellow")


@app.command()
def build_palettes(
    src_dir: Annotated[
        Path, typer.Option(exists=True, dir_okay=True, readable=True, resolve_path=True)
    ],
    out_dir: Annotated[
        Path,
        typer.Option(
            dir_okay=True,
            writable=True,
            resolve_path=True,
        ),
    ],
):
    """
    Build palettes in all formats.
    """

    from importlib.resources import files

    import yaml
    from jsonschema import validate

    # Load palette schema
    schema: dict = yaml.safe_load(
        files("gonzago").joinpath("palettes.schema.yaml").read_text()
    )

    # Find valid templates in input folder
    print(f"Looking for valid palette templates at {src_dir}...")

    templates: dict = dict()
    for src_file in src_dir.rglob("*.y[a]ml"):
        with src_file.open() as template_file:
            template: dict = yaml.safe_load(template_file)
            try:
                validate(template, schema)
            except:
                continue
            rel_path: Path = src_file.relative_to(src_dir)
            templates[rel_path] = template
            print(rel_path)

    templates_count: int = len(templates)
    if templates_count == 0:
        print("No valid palette templates found.")
        return

    # Call exporters
    for rel_path in templates:
        template = templates[rel_path]
        for id in EXPORTERS:
            exporter: ExporterInfo = EXPORTERS[id]
            out_file: Path = (
                out_dir.joinpath(rel_path).with_suffix(exporter.suffix).resolve()
            )
            out_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folders
            print(out_file)
            exporter.fn(out_file, template)


@app.callback()
def main():
    """
    Manage users CLI app.

    Use it with the create command.

    A new user with the given NAME will be created.
    """


if __name__ == "__main__":
    app()
