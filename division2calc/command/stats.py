from pathlib import Path

import click
import pandas as pd

from division2calc.command.utils import load_builds_metric


@click.command()
@click.argument('file', required=True, type=click.Path())
def stats(file: Path) -> None:
    # load
    df = load_builds_metric(file, 'stats', 'basic')
    # format
    df = pd.concat([
        df.iloc[:, :1].map(lambda v: f'{v:,.0f}'),
        df.iloc[:, 1:].map(lambda v: f'{v:.1%}'),
    ], axis='columns')
    # result
    click.secho('\nstats:', fg='yellow')
    print(df)
