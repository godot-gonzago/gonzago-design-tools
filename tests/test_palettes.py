from gonzago import SCRIPTS_PATH
from gonzago.palettes import templates, exporters


def test_templates(capsys):
    with capsys.disabled():
        for template_path, template in templates.get_valid_templates(SCRIPTS_PATH):
            print(template_path)
            print(template)
            if template.get("source", None):
                print(template["source"])

            #exporters.export_png_palette(template_path, template)
            #exporters.export_hex(template_path, template)

        for func in exporters._exporter_registry:
            print(func)
