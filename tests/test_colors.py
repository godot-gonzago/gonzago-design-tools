from gonzago.colors import Color

def test_color():
    test_color: str = "#123123"
    color: Color = Color.from_string(test_color)
    rgb: str = color.to_hex_rgb()
    assert rgb == test_color
