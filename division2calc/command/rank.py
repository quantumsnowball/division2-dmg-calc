from pathlib import Path
from typing import get_args

import click
import pandas as pd

from division2calc.build.common import Metric, Profile, SortBy, SortOrder
from division2calc.command.utils import load_builds_metric
from division2calc.utils import load_builds_file

ClickMetric = click.Choice(get_args(Metric))
ClickProfile = click.Choice(get_args(Profile))
ClickSortOrder = click.Choice(get_args(SortOrder))
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
    if sort_by:
        by, order = sort_by
        by = tuple(by.split(',')) if df.columns.nlevels > 1 else by
        df.sort_values(by, ascending=order == 'asc', inplace=True)
    # format
    match metric:
        case 'stats':
            df.iloc[:, :1] = df.iloc[:, :1].map(lambda v: f'{v:,.0f}')
            df.iloc[:, 1:] = df.iloc[:, 1:].map(lambda v: f'{v:.1%}')
        case 'damage':
            df = df.map(lambda v: f'{v:,.0f}')
        case 'x' | 'dydx':
            df = df.map(lambda v: f'{v:.3f}')
        case _:
            pass
    # result
    print(df)
