import shutil
from pathlib import Path

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
            WD=st.weapon_damage,
            WTD=st.weapon_type_damage,
            CHC=st.critical_hit_chance,
            CHD=st.critical_hit_damage,
            HS=st.headshot_damage,
            DtA=st.damage_to_armor,
            DtH=st.damage_to_health,
            DtooC=st.damage_to_target_out_of_cover,
            RoF=st.rate_of_fire,
        )
        srcs = {k: v.src for k, v in totals.items()}
        # package
        df_totals = pd.DataFrame.from_dict({'total': totals}, orient='index')
        df_srcs = pd.DataFrame.from_dict(srcs, orient='index').T
        # format
        df_totals = df_totals.map(lambda v: f'{v:.1%}')
        df_srcs = df_srcs.fillna('-')
        df_srcs.index = ['>>>']+['']*(len(df_srcs)-1)
        df = pd.concat([df_totals, df_srcs], axis='index')
        # result
        click.secho(f'\nbreakdown - Build({build.name}):', fg='yellow')
        with pd.option_context(
            'display.max_columns', None,
            'display.width', shutil.get_terminal_size().columns,
        ):
            print(df)
