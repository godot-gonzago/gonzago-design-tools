from gonzago.colors import Color


def test_color(capsys):
    c: Color = Color(0.0)
    with capsys.disabled():
        print(c)

    c = Color(0.5).clamped()
    with capsys.disabled():
        print(c)

    c = Color(-2.0).clamped()
    with capsys.disabled():
        print(c)
