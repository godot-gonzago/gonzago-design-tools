from gonzago import ROOT_PATH
from gonzago.palettes import templates, exporters


def test_templates(capsys):
    with capsys.disabled():
        for template_path, template in templates.get_valid_templates(ROOT_PATH):
            print(template_path)
            print(template)
            if template.get("source", None):
                print(template["source"])

            #exporters.export_png_1_palette(template_path.with_suffix(".1x.png"), template)
            #exporters.export_png_8_palette(template_path.with_suffix(".8x.png"), template)
            #exporters.export_png_32_palette(template_path.with_suffix(".32x.png"), template)

        for func in exporters._exporter_registry:
            print(func)
