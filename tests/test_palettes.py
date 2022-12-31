from pathlib import Path
import gonzago.palettes
import tomlkit


def test_download(capsys):
    with capsys.disabled():
        print(gonzago.palettes.find_templates(Path('D:/Users/Dave/Documents/Godot/GonzagoFramework/GonzagoDesignTools/src/gonzago')))

