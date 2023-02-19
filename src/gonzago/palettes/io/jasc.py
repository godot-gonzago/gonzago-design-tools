from pathlib import Path


class JascExporter:
    def export(self, template_data: dict):
        print("Jasc")

    def export_jasc_palette(output_path: Path, template_data: dict):
        # https://liero.nl/lierohack/docformats/other-jasc.html
        # JASC-PAL      <- constant string
        # 0100          <- constant version of palette file format
        # 16            <- color count
        # 255 0 0       <- [0-255] rgb separated by space
        # 0 255 0
        # 0 0 255
        # 255 255 0
        pass
