from pathlib import Path

from scour import scour

_SCOUR_OPTIONS = scour.parse_args(
    [
        "--set-precision=5",
        "--create-groups",
        "--strip-xml-prolog",
        "--remove-descriptive-elements",
        "--enable-comment-stripping",
        "--enable-viewboxing",
        "--no-line-breaks",
        "--strip-xml-space",
        "--enable-id-stripping",
        "--shorten-ids",
        "--quiet",
    ]
)


def _minimize_svg(src_file: Path, out_file: Path, scour_options=_SCOUR_OPTIONS) -> None:
    # Sanitize paths
    src_file: Path = src_file.resolve(True)
    out_file: Path = out_file.with_suffix(".svg").resolve()

    # Ensure folders
    out_file.parent.mkdir(parents=True, exist_ok=True)

    # Optimize
    scour_options.infilename = src_file
    scour_options.outfilename = out_file
    (input, output) = scour.getInOut(scour_options)
    scour.start(scour_options, input, output)


def optimize_icons(src_dir: Path, out_dir: Path, scour_options=_SCOUR_OPTIONS) -> None:
    for src_file in src_dir.rglob("*.svg"):
        rel_path: Path = src_file.relative_to(src_dir)
        out_file: Path = out_dir.joinpath(rel_path)
        print("Exporting {}...".format(rel_path.as_posix()))
        _minimize_svg(src_file, out_file, scour_options)


# https://wiki.inkscape.org/wiki/Using_the_Command_Line
# https://inkscape.org/doc/inkscape-man.html
def inkscape_to_png(src_file: Path, out_file: Path) -> None:
    import subprocess

    # shutil.which
    # https://docs.python.org/3/library/subprocess.html#subprocess.Popen
    # https://docs.python.org/3/library/subprocess.html#subprocess.run

    inkscape: Path = Path("C:/Program Files/Inkscape/bin/inkscape.exe").resolve()
    blender: Path = Path("C:/Program Files/Blender Foundation/Blender 3.4/blender.exe").resolve()

    # Sanitize paths
    src_file: Path = src_file.resolve(True)
    out_file: Path = out_file.with_suffix(".png").resolve()

    # Ensure folders
    out_file.parent.mkdir(parents=True, exist_ok=True)

    # Convert
    # inkscape --export-filename=out_file.png src_file.svg
    subprocess.run([inkscape, "--export-filename", out_file, src_file])
    pass


def svg_to_png(src_file: Path, out_file: Path) -> None:
    # Sanitize paths
    src_file: Path = src_file.resolve(True)
    out_file: Path = out_file.with_suffix(".png").resolve()

    # Ensure folders
    out_file.parent.mkdir(parents=True, exist_ok=True)

    # Convert (https://cairosvg.org/documentation/)
    from cairosvg import svg2png
    svg2png(url=str(src_file), write_to=str(out_file))


def build_os_icons() -> None:
    # ICO https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#ico
    # ICNS https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#icns
    # MOBILE?
    pass


def build_splash_image() -> None:
    pass
