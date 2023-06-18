# <https://www.cyotek.com/cyotek-palette-editor/supported-palette-formats>
# <https://lospec.com/palette-list/fuzzyfour>
# <http://www.selapa.net/swatches/colors/fileformats.php>
# <https://docs.krita.org/en/untranslatable_pages/kpl_defintion.html>

# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/logging.html

from importlib.resources import files
from pathlib import Path
from typing import Callable, Generator, Iterator, List, NamedTuple, Optional

import typer
import yaml
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated


class TemplateFileInfo(NamedTuple):
    path: Path
    name: str
    description: str
    color_count: int


class ExporterInfo(NamedTuple):
    suffix: str
    description: str
    fn: Callable[[Path, dict], None]


TEMPLATE_SCHEMA: dict = yaml.safe_load(
    files("gonzago").joinpath("palettes.schema.yaml").read_text()
)
EXPORTERS = dict[str, ExporterInfo]()

console: Console = Console()
app = typer.Typer()


def exporter(id: str, suffix: str, description: str = "") -> Callable:
    def inner(fn: Callable[[Path, dict], None]) -> Callable[[Path, dict], None]:
        EXPORTERS[id] = ExporterInfo(suffix=suffix, description=description, fn=fn)
        return fn

    return inner


@exporter("png", ".png", "PNG palette image with size 1px.")
def export_png(out_file: Path, template: dict, size: int = 1) -> None:
    """
    PNG

    PNG palette image with size 1px.
    """
    from PIL import Image, ImageDraw

    color_count: int = len(template["colors"])
    image: Image = Image.new("RGB", (color_count * size, size))

    draw = ImageDraw.Draw(image, "RGB")
    for i in range(color_count):
        color = template["colors"][i]["color"]
        draw.rectangle((i * size, 0, i * size + size, size), color)

    image.save(out_file, "PNG")


@exporter("png-8", ".x8.png", "PNG palette image with size 8px.")
def export_png_8(out_file: Path, template: dict) -> None:
    export_png(out_file, template, 8)


@exporter("png-32", ".x32.png", "PNG palette image with size 32px.")
def export_png_8(out_file: Path, template: dict):
    export_png(out_file, template, 32)


@exporter("gpl", ".gpl", "Gimp/Inkscape color palette.")
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


@exporter("hex", ".hex", "Simple HEX color palette.")
def export_hex(out_file: Path, template: dict):
    colors = [c["color"].lstrip("#").lower() for c in template["colors"]]
    with out_file.open("w") as file:
        file.writelines("\n".join(colors))


# @exporter("ase", ".ase", "Color palette for Adobe products (Adobe Swatch Exchange).")
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


# @exporter("paintnet", ".txt", "Paint.NET color palette.")
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


# @exporter("paintshop", ".pal", "Paintshop Pro color palette.")
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


# @exporter("krita", ".kpl", "Krita color palette.")
# def export_krita(out_file: Path, template: dict):
#    # https://docs.krita.org/en/untranslatable_pages/kpl_defintion.html
#    pass


# @exporter("office", ".soc", "Color palette for StarOffice/OpenOffice/LibreOffice.")
# def export_star_office(out_file: Path, template: dict):
#    # http://www.selapa.net/swatches/colors/fileformats.php#ooo_soc
#    pass


# @exporter("scribus", ".xml", "Color palette for Scribus.")
# def export_scribus(out_file: Path, template: dict):
#    # https://github.com/1j01/anypalette.js
#    pass


# TODO: Check based on id if exporter is desired/available?
def _get_exporter_ids() -> List[str]:
    pass


def _discover_templates(
    dir: Path, recursive: bool = True
) -> Iterator[TemplateFileInfo]:
    from jsonschema import validate

    files: Generator[Path, None, None] = (
        dir.rglob("*.y[a]ml") if recursive else dir.glob("*.y[a]ml")
    )
    for file in files:
        with file.open() as template_file:
            template: dict = yaml.safe_load(template_file)
            try:
                validate(template, TEMPLATE_SCHEMA)
            except:
                del template
                continue
            info: TemplateFileInfo = (
                file,
                template["name"],
                template.get("description", ""),
                len(template["colors"]),
            )
            del template
            yield info


@app.command("templates")
def list_templates(
    dir: Annotated[
        Optional[Path],
        typer.Option(
            "--dir",
            "-d",
            help="Template directory to search.",
            show_default=False,
            exists=True,
            file_okay=False,
            dir_okay=True,
            readable=True,
            resolve_path=True,
        ),
    ] = None,
    recursive: Annotated[
        Optional[bool], typer.Option("--recursive", "-r", help="Search in sub folders.")
    ] = True,
):
    """
    List valid palette templates.
    """
    # TODO: Make dir optional and fallback to config dir if ommited! Integrate config creation procedure?
    if dir is None:
        console.print("Try to get dir from config")
        return

    table: Table = Table("Path", "Name", "Description", "Colors")
    for file, name, description, colors in _discover_templates(dir, recursive):
        table.add_row(str(file.relative_to(dir)), name, description, str(colors))
    if table.row_count > 0:
        console.print(f"Found valid palette templates: {table.row_count}")
        console.print(table)
    else:
        console.print("No valid palette templates found!", style="yellow")


@app.command("exporters")
def list_exporters():
    """
    List available exporters.
    """
    count: int = len(EXPORTERS)
    if count == 0:
        console.print("No exporters available!", style="yellow")
        return
    console.print(f"Available exporters: {count}")
    table: Table = Table("ID", "Suffix", "Description")
    for id, (suffix, description, _) in EXPORTERS.items():
        table.add_row(id, suffix, description)
    console.print(table)


@app.command("build")
def build(
    src_path: Annotated[
        Optional[Path],
        typer.Option(
            "--in",
            "-i",
            help="Input template file or directory.",
            exists=True,
            file_okay=True,
            dir_okay=True,
            readable=True,
            resolve_path=True,
            show_default=False,
        ),
    ] = None,
    out_dir: Annotated[
        Optional[Path],
        typer.Option(
            "--out",
            "-o",
            help="Palettes output direcory.",
            file_okay=False,
            dir_okay=True,
            writable=True,
            resolve_path=True,
            show_default=False,
        ),
    ] = None,
    exporters: Annotated[
        Optional[List[str]],
        typer.Option("--export", "-e", help="List of exporters to use."),
    ] = list[str](EXPORTERS.keys()),
):
    """
    Build palettes in all formats.
    """
    pass


# TODO: Check and validate exporters

#    if src_path is None:
#        src_path = # TODO: Get from config

#    if out_dir is None:
#        out_dir = # TODO: Get from config

#    from importlib.resources import files
#
#    import yaml
#    from jsonschema import validate
#
#    # Load palette schema
#    schema: dict = yaml.safe_load(
#        files("gonzago").joinpath("palettes.schema.yaml").read_text()
#    )
#
#    # Find valid templates in input folder
#    print(f"Looking for valid palette templates at {src_dir}...")
#
#    templates: dict = dict()
#    for src_file in src_dir.rglob("*.y[a]ml"):
#        with src_file.open() as template_file:
#            template: dict = yaml.safe_load(template_file)
#            try:
#                validate(template, schema)
#            except:
#                continue
#            rel_path: Path = src_file.relative_to(src_dir)
#            templates[rel_path] = template
#            print(rel_path)
#
#    templates_count: int = len(templates)
#    if templates_count == 0:
#        print("No valid palette templates found.")
#        return
#
#    # Call exporters
#    for rel_path in templates:
#        template = templates[rel_path]
#        for _, exporter in EXPORTERS.items():
#            out_file: Path = (
#                out_dir.joinpath(rel_path).with_suffix(exporter.suffix).resolve()
#            )
#            out_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folders
#            print(out_file)
#            exporter.fn(out_file, template)


@app.callback(no_args_is_help=True)
def main():
    """
    Color palette tools.
    """
    pass


if __name__ == "__main__":
    app()
