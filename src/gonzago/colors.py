from gonzago.math import clamp01


class Color:
    def __init__(
        self, r: float = 0.0, g: float = 0.0, b: float = 0.0, a: float = 1.0
    ) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, value: float) -> None:
        self._r = clamp01(value)
