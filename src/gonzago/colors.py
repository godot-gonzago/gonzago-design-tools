from abc import ABC
from dataclasses import dataclass
from gonzago.math import RangedValue

# https://stackoverflow.com/a/70700159
# https://docs.python.org/3/howto/descriptor.html#validator-class
# https://docs.python.org/3/howto/descriptor.html#properties

@dataclass
class Color:
    r: float = RangedValue(0.0, 1.0, 0.0)
    g: float = RangedValue(0.0, 1.0, 0.0)
    b: float = RangedValue(0.0, 1.0, 0.0)
    a: float = RangedValue(0.0, 1.0, 1.0)


# https://stackoverflow.com/questions/55973284/how-to-create-self-registering-factory-in-python
# https://realpython.com/primer-on-python-decorators/#registering-plugins
# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration
# https://docs.python.org/3/library/functools.html#functools.singledispatch ???


class ColorFactory:
    pass
