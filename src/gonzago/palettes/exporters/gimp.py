from pathlib import Path
from gonzago.palettes.exporters import Exporter


class GimpExporter(Exporter):
    def export(self, template_data: dict):
        print("Gimp")

    def export_gimp_palette(output_path: Path, template_data: dict):
        output_path = output_path.with_suffix(f".hex")
        with output_path.open("w") as file:
            file.write("GIMP Palette\n")
            file.write(f"#Palette Name: {template_data['name']}\n")
            if template_data.get("description", None):
                file.write(f"#Description: {template_data['description']}\n")
            file.write(f"#Colors: {len(template_data['colors'])}\n")

            for color_data in template_data["colors"]:
                # [0-255]\t[0-255]\t[0-255]\tcolor_data["name"]
                color = color_data["color"].lstrip("#").lower()
                file.write(f"{color}\n")
