from gonzago import SCRIPTS_PATH
from gonzago.palettes import templates, exporters

from pathlib import Path

SCRIPT_PATH: Path = Path(__file__).parent.resolve()


def test_templates(capsys):
    with capsys.disabled():
        for template_path, template in templates.get_valid_templates(SCRIPTS_PATH):
            print(template_path)
            print(template)
            if template.get("source", None):
                print(template["source"])

            # exporters.export_png_palette(template_path, template)
            # exporters.export_hex(template_path, template)

        print(list(exporters.Exporter.get_subclasses()))
