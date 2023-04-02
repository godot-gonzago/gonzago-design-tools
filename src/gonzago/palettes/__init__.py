# <https://www.cyotek.com/cyotek-palette-editor/supported-palette-formats>
# - 18-bit RGB VGA Palette, pal
# - 24-bit RGB VGA Palette, pal
# - Adobe Colour Table, act
# - Adobe Photoshop Colour Swatch, aco
# - Adobe Swatch Exchange, ase
# - CoreDRAW4, pal, xml
# - DeluxePaint Image, bbm, lbm
# - Fractint, map
# - GIMP, gpl
# - Gravit, gvswatch
# - Hex, hex
# - JASC, pal, PspPalette
# - Microsoft RIFF, pal
# - Paint.NET, txt
# <https://lospec.com/palette-list/fuzzyfour>
# - PNG 1px
# - PNG 8px
# - PNG 32px
# - PAL File (JASC)
# - Photoshop ASE
# - Paint.Net TXT
# - GIMP GPL
# - HEX File
# <https://sk1project.net/palettes/>
# - sK1
# - Inkscape
# - GIMP
# - Scribus
# - Karbon
# - Calligra
# - LibreOffice
# - CorelDRAW, Corel PhotoPaint
# - Adobe Illustrator, Adobe InDesign
# - Adobe Photoshop
# - Xara Designer, Xara Web Designer
# <http://www.selapa.net/swatches/colors/fileformats.php>
# <https://docs.krita.org/en/untranslatable_pages/kpl_defintion.html>

# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/logging.html

from pathlib import Path

from gonzago import __version__

__all__ = ["build_palettes"]


EXPORTERS = dict()


def exporter(suffix: str):
    def inner(fn):
        EXPORTERS[suffix] = fn
        return fn

    return inner


def build_palettes(src_dir: Path, out_dir: Path):
    import yaml
    from importlib.resources import files
    from jsonschema import validate

    # Load palette schema
    schema: dict = yaml.safe_load(
        files("gonzago.palettes").joinpath("palettes.schema.yaml").read_text()
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
        for suffix in EXPORTERS:
            out_file: Path = out_dir.joinpath(rel_path).with_suffix(suffix).resolve()
            out_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folders
            print(out_file)
            EXPORTERS[suffix](out_file, template)


@exporter(".png")
def export_png(out_file: Path, template: dict, size: int = 1):
    from PIL import Image, ImageDraw

    color_count: int = len(template["colors"])
    image: Image = Image.new("RGB", (color_count * size, size))

    draw = ImageDraw.Draw(image, "RGB")
    for i in range(color_count):
        color = template["colors"][i]["color"]
        draw.rectangle((i * size, 0, i * size + size, size), color)

    image.save(out_file, "PNG")


@exporter(".x8.png")
def export_png_8(out_file: Path, template: dict):
    export_png(out_file, template, 8)


@exporter(".x32.png")
def export_png_8(out_file: Path, template: dict):
    export_png(out_file, template, 32)


@exporter(".gpl")
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


@exporter(".hex")
def export_hex(out_file: Path, template: dict):
    colors = [c["color"].lstrip("#").lower() for c in template["colors"]]
    with out_file.open("w") as file:
        file.writelines("\n".join(colors))


# @exporter(".ase")
# def export_adobe_swatch_exchange(out_file: Path, template: dict):
#    # https://medium.com/swlh/mastering-adobe-color-file-formats-d29e43fde8eb
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


# @exporter(".txt")
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


# @exporter(".pal")
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
