# Reader and Writer for custom palette format in yaml
# Validation in here!

from pathlib import Path

import yaml

from ..palette import Color, ColorValue, Palette
from ..io import PaletteWriterReader


class YamlPalette(PaletteWriterReader):
    def read(self, file_path: Path) -> Palette:
        def _read_color_value(hex: str) -> ColorValue:
            return ColorValue(
                int(hex[1:3], 16),
                int(hex[3:5], 16),
                int(hex[5:7], 16),
            )

        with file_path.open() as file:
            palette_data: dict = yaml.safe_load(file)

        palette: Palette = Palette(
            palette_data["name"],
            palette_data.get("description", ""),
            palette_data.get("version", ""),
            palette_data.get("author", ""),
            palette_data.get("source", ""),
        )

        for color_data in palette_data["colors"]:
            color: Color = Color(
                color_data["name"],
                color_data.get("description", ""),
                _read_color_value(color_data["color"]),
            )

            for color_data_key in color_data.keys():
                if color_data_key.startswith("color-"):
                    variant_key = color_data_key[5:]
                    color.variants[variant_key] = _read_color_value(
                        color_data[color_data_key]
                    )

            palette.colors.append(color)

        return palette
