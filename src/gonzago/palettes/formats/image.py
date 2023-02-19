from pathlib import Path

from PIL import Image, ImageDraw


class PNGExporter:
    def export(self, template_data: dict):
        print("PNG")

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
