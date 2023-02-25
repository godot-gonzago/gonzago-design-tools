from pathlib import Path

from gonzago.palettes.palette import Palette

#from gonzago.palettes.io import PaletteWriterReader


class PaintNetExporter: #(PaletteWriterReader):
    def export(self, template_data: dict):
        print("Paint.Net")

    def export_paint_net_palette(output_path: Path, template_data: dict):
        # https://www.getpaint.net/doc/latest/WorkingWithPalettes.html
        # ;paint.net Palette File
        # ;Downloaded from Lospec.com/palette-list
        # ;Palette Name: Lospec500
        # ;Description: A collaboration from the Lospec Discord server to create a palette celebrating 500 palettes hosted on Lospec.
        # ;Colors: 42
        # FF10121c
        # FF2c1e31
        # FF6b2643
        pass

    def read(self, file_path: Path) -> Palette:
        raise NotImplementedError

    def write(self, file_path: Path, palette: Palette):
        raise NotImplementedError

#        with open(file_path, 'w') as file:
#            file.write(';paint.net Palette File\n')
#
#            for color in palette.colors:
#                file.write()
