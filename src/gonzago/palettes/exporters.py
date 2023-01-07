from pathlib import Path


_exporter_registry = []


def exporter(func):
    global _exporter_registry
    _exporter_registry.append(func.__name__)
    return func


@exporter
def export_hex(output_path: Path, template_data: str):
    pass


@exporter
def export_gimp_palette(output_path: Path, template_data: str):
    pass


@exporter
def export_paint_net_palette(output_path: Path, template_data: str):
    pass
