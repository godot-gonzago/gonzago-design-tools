from pathlib import Path
from jsonschema import Draft202012Validator, validate
from gonzago import ROOT_PATH

import yaml
import gonzago.palettes
import tomlkit


def test_download(capsys):
    with capsys.disabled():
        print(gonzago.palettes.find_templates(Path(__file__, '../../src/gonzago')))

    palette_path = Path(__file__, ROOT_PATH.joinpath('test.pal.yaml'))
    with palette_path.open() as f:
        palette = yaml.safe_load(f)

    schema_path = Path(__file__, ROOT_PATH.joinpath('schema.pal.yaml'))
    with schema_path.open() as f:
        schema = yaml.safe_load(f)

    validate(palette, schema)
