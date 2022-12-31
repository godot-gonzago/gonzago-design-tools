from abc import ABC
from dataclasses import dataclass
from typing import NamedTuple
from gonzago.math import RangedValue

# https://stackoverflow.com/a/70700159
# https://docs.python.org/3/howto/descriptor.html#validator-class
# https://docs.python.org/3/howto/descriptor.html#properties


class Color(NamedTuple):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0


# https://stackoverflow.com/questions/55973284/how-to-create-self-registering-factory-in-python
# https://realpython.com/primer-on-python-decorators/#registering-plugins
# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration
# https://docs.python.org/3/library/functools.html#functools.singledispatch ???


class ColorFactory:
    pass
