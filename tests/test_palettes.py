import gonzago.palettes
import tomlkit


def test_download(capsys):
    for palette in gonzago.palettes.download_color_pairs():
        with capsys.disabled():
            print(gonzago.palettes.convert_to_toml(palette).as_string())

