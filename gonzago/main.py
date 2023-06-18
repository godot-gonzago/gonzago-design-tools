import argparse

import click


@click.command()
def main():
    click.echo("Hello!")


if __name__ == "__main__":
    exit(main())
