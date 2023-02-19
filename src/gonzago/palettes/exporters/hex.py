from pathlib import Path
from gonzago.palettes.exporters import Exporter


class HexExporter(Exporter):
    def export(self, template_data: dict):
        print("Hex")

    def export_hex(output_path: Path, template_data: dict):
        output_path = output_path.with_suffix(f".hex")
        with output_path.open("w") as file:
            for color_data in template_data["colors"]:
                color = color_data["color"].lstrip("#").lower()
                file.write(f"{color}\n")
