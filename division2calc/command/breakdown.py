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
        st = build.stats
        vals = dict(
            CHC=st.critical_hit_chance,
            CHD=st.critical_hit_damage,
        )
        srcs = {k: '\n'.join(v.src) for k, v in vals.items()}
        data = {'total': vals, '>>>': srcs}
        df = pd.DataFrame.from_dict(data, orient='index')
        # result
        click.secho(f'\nbreakdown - Build({build.name}):', fg='yellow')
        print(df)
