import gonzago.palettes


def test_download(capsys):
    count: int = 0
    for pair in gonzago.palettes.download_color_pairs():
        with capsys.disabled():
            print(pair)
        count += 1
    assert count > 0
