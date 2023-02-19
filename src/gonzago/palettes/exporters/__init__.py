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
from abc import ABC, abstractmethod

__all__ = ["Exporter", "ase", "gimp", "hex", "jasc", "paint_net", "png"]

# https://milovantomasevic.com/courses/python-design-patterns-registry/
# https://github.com/faif/python-patterns/blob/master/patterns/behavioral/registry.py
# https://github.com/BrianPugh/autoregistry
class Exporter(ABC):
    _exporters = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._exporters.append(cls)

    @classmethod
    def get_subclasses(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.get_subclasses()
            yield subclass

    @staticmethod
    def export_all():
        #for exporter in Exporter._exporters:
        print(Exporter._exporters)


    @abstractmethod
    def export(self, template_data: dict):
        pass
