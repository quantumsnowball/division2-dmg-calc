from pathlib import Path

import click

from division2calc.parser import parse_build_yaml
from division2calc.parser.utils import BuildYAMLPathParamType


@click.group()
def division2calc() -> None:
    pass


@division2calc.command()
@click.argument('file', required=True, type=BuildYAMLPathParamType())
def summary(file: Path) -> None:
    parse_build_yaml(file)
