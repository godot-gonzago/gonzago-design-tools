from gonzago import math


def test_clamp():
    assert math.clamp(50, 0, 100) == 50
    assert math.clamp(-100, 0, 100) == 0
    assert math.clamp(200, 0, 100) == 100

    assert math.clamp01(0.5) == 0.5
    assert math.clamp01(-1.0) == 0.0
    assert math.clamp01(2.0) == 1.0

    assert math.clamp8bit(128) == 128
    assert math.clamp8bit(-255) == 0
    assert math.clamp8bit(512) == 255
