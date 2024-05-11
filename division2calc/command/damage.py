from pathlib import Path

import click

from division2calc.build.common import PROFILES
from division2calc.command.utils import load_builds_metric


@click.command()
@click.argument('file', required=True, type=click.Path())
def damage(file: Path) -> None:
    for profile in PROFILES:
        # load
        df = load_builds_metric(file, 'damage', profile)
        # format
        df = df.map(lambda v: f'{v:,.0f}')
        # result
        click.secho(f'\ndamage - profile `{profile}`:', fg='yellow')
        print(df)
