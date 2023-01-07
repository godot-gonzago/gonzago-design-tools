from pathlib import Path

from gonzago import __version__

__all__ = ["templates", "exporters"]


def build_palettes_from_templates(template_folder: Path, output_folder: Path) -> None:
    from gonzago.palettes.templates import get_valid_templates

    for template_path, template in get_valid_templates(template_folder):
        rel_path = template_path.relative_to(template_folder)
        print(rel_path)

    # find templates in input folder
    # for each template
    #   load template
    #   generate palettes from template
    #   for each palette
    #       for each exporter
    #           generate output path from template path and palette info? this might be made easier
    #           export template to output path
    pass
