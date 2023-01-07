from gonzago import ROOT_PATH
from gonzago.palettes import templates, exporters


def test_templates(capsys):
    with capsys.disabled():
        for template in templates.get_valid_templates(ROOT_PATH):
            print(template)

        for func in exporters._exporter_registry:
            print(func)
