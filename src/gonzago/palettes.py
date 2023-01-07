from dataclasses import dataclass
from pathlib import Path
from typing import Generator


@dataclass
class PaletteTemplate:
    source_path: Path
    relative_path: Path
    data: dict


def get_valid_templates(
    template_folder: Path,
) -> Generator[PaletteTemplate, None, None]:
    import yaml
    from jsonschema import ValidationError, validate

    # Load palette schema
    schema_path: Path = Path(__file__).parent.joinpath("palettes.schema.yaml")
    with schema_path.open() as schema_file:
        schema: dict = yaml.safe_load(schema_file)

    # Find valid templates in input folder
    for template_path in template_folder.rglob("*.pal.yaml"):
        with template_path.open() as template_file:
            template_data: dict = yaml.safe_load(template_file)
            try:
                validate(template_data, schema)
                template: PaletteTemplate = PaletteTemplate(
                    template_path.resolve(),
                    template_path.relative_to(template_folder),
                    template_data,
                )
                yield template
            except ValidationError:
                pass
            except:
                pass


def build_palettes(template_folder: Path, output_folder: Path) -> None:
    # find templates in input folder
    # for each template
    #   load template
    #   generate palettes from template
    #   for each palette
    #       for each exporter
    #           generate output path from template path and palette info? this might be made easier
    #           export template to output path
    pass


if __name__ == "__main__":
    pass
