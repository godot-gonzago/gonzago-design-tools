from pathlib import Path

from jsonschema import ValidationError, validate
import yaml

from gonzago import palettes


def test_templates(capsys):
    with capsys.disabled():
        for template in palettes.get_valid_templates(
            Path(__file__, "../../src/gonzago")
        ):
            print(template)
