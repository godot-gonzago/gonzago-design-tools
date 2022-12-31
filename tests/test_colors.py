from gonzago.colors import Color


def test_color(capsys):
    c: Color = Color(0.0, 0.0, 0.0)
    with capsys.disabled():
        print(c)

    c.r = 0.5
    with capsys.disabled():
        print(c)

    c.r = -2.0
    with capsys.disabled():
        print(c)
