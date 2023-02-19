# https://pypi.org/project/click/
# https://pypi.org/project/typer/
# https://pypi.org/project/rich/
# https://pypi.org/project/textual/

import click


@click.command()
def main():
    click.echo("This is a CLI built with Click")


if __name__ == "__main__":
    main()
