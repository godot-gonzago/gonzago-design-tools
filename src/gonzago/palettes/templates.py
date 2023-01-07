from pathlib import Path

import yaml
from jsonschema import ValidationError, validate


def get_valid_templates(template_folder: Path):
    # Load palette schema
    schema_path: Path = Path(__file__).parent.joinpath('palettes.schema.yaml')
    with schema_path.open() as schema_file:
        schema: dict = yaml.safe_load(schema_file)

    # Find valid templates in input folder
    for template_path in template_folder.rglob('*.pal.yaml'):
        with template_path.open() as template_file:
            template: dict = yaml.safe_load(template_file)
            try:
                validate(template, schema)
                yield template_path, template
            except ValidationError:
                pass
            except:
                pass
