from pathlib import Path
from pprint import pp

import click
import pandas as pd

from division2calc.command.utils import load_builds_file


@click.command()
@click.argument('file', required=True, type=click.Path())
def breakdown(file: Path) -> None:
    # load
    builds = load_builds_file(file)
    for build in builds:
        # select fields
        st = build.stats
        totals = dict(
            CHC=st.critical_hit_chance,
            CHD=st.critical_hit_damage,
        )
        srcs = {k: '\n'.join(v.src) for k, v in totals.items()}
        # package
        df_totals = pd.DataFrame.from_dict({'total': totals}, orient='index')
        df_srcs = pd.DataFrame.from_dict({'>>>': srcs}, orient='index')
        # format
        df_totals = df_totals.map(lambda v: f'{v:.1%}')
        df = pd.concat([df_totals, df_srcs], axis='index')
        # result
        click.secho(f'\nbreakdown - Build({build.name}):', fg='yellow')
        print(df)
