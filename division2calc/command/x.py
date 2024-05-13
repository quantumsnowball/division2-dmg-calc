from pathlib import Path

import click

from division2calc.agent.common import PROFILES
from division2calc.command.utils import load_builds_metric


@click.command()
@click.argument('file', required=True, type=click.Path())
def x(file: Path) -> None:
    for profile in PROFILES:
        # load
        df = load_builds_metric(file, 'x', profile)
        # format
        df = df.map(lambda v: f'{v:.3f}')
        # result
        click.secho(f'\nx - profile `{profile}`:', fg='yellow')
        print(df)
