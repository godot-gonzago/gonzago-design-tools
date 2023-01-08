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
from pathlib import Path

from PIL import Image, ImageDraw

_exporter_registry = []


def exporter(func):
    global _exporter_registry
    _exporter_registry.append(func.__name__)
    return func


@exporter
def export_hex(output_path: Path, template_data: dict):
    output_path = output_path.with_suffix(f".hex")
    with output_path.open("w") as file:
        for color_data in template_data["colors"]:
            color = color_data["color"].lstrip("#").lower()
            file.write(f"{color}\n")


@exporter
def export_gimp_palette(output_path: Path, template_data: dict):
    pass


@exporter
def export_paint_net_palette(output_path: Path, template_data: dict):
    # https://www.getpaint.net/doc/latest/WorkingWithPalettes.html
    pass


@exporter
def export_jasc_palette(output_path: Path, template_data: dict):
    pass


@exporter
def export_adobe_swatch_exchange_palette(output_path: Path, template_data: dict):
    # https://medium.com/swlh/mastering-adobe-color-file-formats-d29e43fde8eb
    with output_path.open("wb") as file:
        # Write header
        file.write(b"\x41\x53\x45\x46")  # Signature (Constant: ASEF)
        file.write(b"\x00\x01\x00\x00")  # Version (Constant: 1.0)
        file.write(b"\x00\x00\x00\x03")  # Number of blocks

        # Group start
        file.write(b"\xC0\x01")  # Block type (Group start)
        file.write(b"\x00\x00\x00\x00")  # Block length
        file.write(b"\x00\x00")  # Name length
        file.write(b"\x00")  # 0-terminated group name encoded in UTF-16

        # Color entry
        file.write(b"\x00\x01")  # Block type (Color entry)
        file.write(b"\x00\x00\x00\x00")  # Block length
        file.write(b"\x00\x00")  # Name length
        file.write(b"\x00")  # 0-terminated color name encoded in UTF-16
        file.write(b"\x52\x47\x42\x20")  # Color space (Constant: RGB)
        file.write(b"\x00\x00\x00\x00")  # Red
        file.write(b"\x00\x00\x00\x00")  # Green
        file.write(b"\x00\x00\x00\x00")  # Blue
        file.write(b"\x00\x02")  # Color mode (Constant: Normal)

        # Group end
        file.write(b"\xC0\x02")  # Block type (Group end)
        file.write(b"\x00\x00\x00\x00")  # Block length (Constant for Group end)


@exporter
def export_png_palette(
    output_path: Path, template_data: dict, sizes: set[int] = [1, 8, 32]
):
    color_count: int = len(template_data["colors"])

    for size in sizes:
        image: Image = Image.new("RGB", (color_count * size, size))

        draw = ImageDraw.Draw(image, "RGB")
        for i in range(color_count):
            color_data = template_data["colors"][i]
            color = color_data["color"]
            draw.rectangle((i * size, 0, i * size + size, size), color)

        image_path: Path = output_path.with_suffix(f".x{size}.png")
        image.save(image_path, "PNG")
