from pathlib import Path

import click

from division2calc.parser.utils import BuildYAMLPathParamType


@click.group()
def division2calc() -> None:
    pass


@division2calc.command()
@click.argument('build-yaml', required=True, type=BuildYAMLPathParamType())
def summary(build_yaml: Path) -> None:
    print(type(build_yaml))
