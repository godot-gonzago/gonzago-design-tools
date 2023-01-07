from gonzago import ROOT_PATH
from gonzago.palettes import templates


def test_templates(capsys):
    with capsys.disabled():
        for template in templates.get_valid_templates(ROOT_PATH):
            print(template)
