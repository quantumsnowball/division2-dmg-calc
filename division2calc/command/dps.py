from pathlib import Path

import click

from division2calc.agent.common import PROFILES
from division2calc.command.utils import load_builds_metric


@click.command()
@click.argument('file', required=True, type=click.Path())
def dps(file: Path) -> None:
    for profile in PROFILES:
        # load
        df = load_builds_metric(file, 'dps', profile)
        # format
        df = df.map(lambda v: f'{v:,.0f}')
        # result
        click.secho(f'\ndps - profile `{profile}`:', fg='yellow')
        print(df)
