from gonzago import ROOT_PATH, palettes


def test_templates(capsys):
    with capsys.disabled():
        for template in palettes.get_palette_templates(ROOT_PATH):
            print(template)
