from pathlib import Path

import click
import pandas as pd

from division2calc.agent.common import (METRICS, PROFILES, SORT_ORDERS, Metric,
                                        Profile, SortBy)
from division2calc.command.utils import load_builds_metric

ClickMetric = click.Choice(METRICS)
ClickProfile = click.Choice(PROFILES)
ClickSortOrder = click.Choice(SORT_ORDERS)
ClickSortBy = click.Tuple([str, ClickSortOrder])


@click.command()
@click.argument('file', required=True, type=click.Path())
@click.option('-m', '--metric', default='damage', type=ClickMetric)
@click.option('-p', '--profile', default='basic', type=ClickProfile)
@click.option('-by', '--sort-by', default=None, type=ClickSortBy,
              help='sort dataframe by field with order, e.g. -by x6 desc')
def rank(file: Path,
         metric: Metric,
         profile: Profile,
         sort_by: SortBy) -> None:
    df = load_builds_metric(file, metric, profile)
    # sorting
    title = f'\n{metric} - profile `{profile}`'
    if sort_by:
        by, order = sort_by
        title += f' sorted by `{by}` `{order}`'
        by = tuple(by.split(',')) if df.columns.nlevels > 1 else by
        df.sort_values(by, ascending=order == 'asc', inplace=True)
    # format
    match metric:
        case 'stats':
            df = pd.concat([
                df.iloc[:, :1].map(lambda v: f'{v:,.0f}'),
                df.iloc[:, 1:].map(lambda v: f'{v:.1%}'),
            ], axis='columns')
        case 'damage':
            df = df.map(lambda v: f'{v:,.0f}')
        case 'x' | 'dydx':
            df = df.map(lambda v: f'{v:.3f}')
        case _:
            pass
    # result
    click.secho(f'{title}:', fg='yellow')
    print(df)
