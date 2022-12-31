from abc import ABC
from dataclasses import dataclass
from gonzago.math import clamp01

# https://stackoverflow.com/a/70700159
# https://docs.python.org/3/howto/descriptor.html#validator-class
# https://docs.python.org/3/howto/descriptor.html#properties


class Color:
    class _ColorChannel:
        def __set_name__(self, _, name: str) -> None:
            self.private_name = "_" + name

        def __get__(self, obj: object, _=None) -> float:
            return getattr(obj, self.private_name)

        def __set__(self, obj: object, value: float) -> None:
            if not isinstance(value, float):
                raise TypeError(f"Expected {value!r} to be a float")
            setattr(obj, self.private_name, clamp01(value))

    r: float = _ColorChannel()
    g: float = _ColorChannel()
    b: float = _ColorChannel()
    a: float = _ColorChannel()

    def __init__(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self) -> str:
        return f"rgba({self.r},{self.g},{self.b},{self.a})"

    def __repr__(self) -> str:
        return f"Color({self.r},{self.g},{self.b},{self.a})"


# https://stackoverflow.com/questions/55973284/how-to-create-self-registering-factory-in-python
# https://realpython.com/primer-on-python-decorators/#registering-plugins
# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration
# https://docs.python.org/3/library/functools.html#functools.singledispatch ???


class ColorFactory:
    pass
