from pathlib import Path
from pprint import pprint

import click

from division2calc.parser import BuildConfig
from division2calc.parser.utils import BuildYAMLPathParamType


@click.group()
def division2calc() -> None:
    pass


@division2calc.command()
@click.argument('file', required=True, type=BuildYAMLPathParamType())
def summary(file: Path) -> None:
    build_config = BuildConfig(file)
    pprint(build_config.dict)
