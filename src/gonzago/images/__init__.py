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


def optimize_icons(src_dir: Path, out_dir: Path, scour_options=_SCOUR_OPTIONS) -> None:
    for src_file in src_dir.rglob("*.svg"):
        rel_path: Path = src_file.relative_to(src_dir)

        print("Exporting {}...".format(rel_path.as_posix()))

        out_file: Path = out_dir.joinpath(rel_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        scour_options.infilename = src_file.resolve()
        scour_options.outfilename = out_file.resolve()
        (input, output) = scour.getInOut(scour_options)
        scour.start(scour_options, input, output)


def svg_to_png() -> None:
    # https://cairosvg.org/documentation/
    # cairosvg.svg2png(url="/path/to/input.svg", write_to="/tmp/output.png")
    pass


def build_os_icons() -> None:
    # ICO https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#ico
    # ICNS https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#icns
    # MOBILE?
    pass


def build_splash_image() -> None:
    pass
