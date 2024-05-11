import pprint
from pathlib import Path
from typing import get_args

import click
import pandas as pd

import division2calc.gear.attrs as gearattrs
import division2calc.gear.brandsets.Lengmo as Lengmo
import division2calc.gear.brandsets.OverlordArmaments as Overlord
import division2calc.gear.gearsets.StrikersBattlegear as Striker
import division2calc.gear.mods as gearmods
from division2calc.build import Build
from division2calc.build.common import Metric, Profile, SortBy, SortOrder
from division2calc.build.specialization import Gunner
from division2calc.command.compare import compare
from division2calc.command.rank import rank
from division2calc.command.stats import stats
from division2calc.utils import load_builds_file, pformat_dataclass
from division2calc.weapon.StElmosEngine import StElmosEngine

__all__ = [
    'Build',
    'Gunner',
    'StElmosEngine',
    'Striker',
    'Lengmo',
    'Overlord',
    'gearattrs',
    'gearmods',
]


@click.group()
def division2calc() -> None:
    pass


division2calc.add_command(stats)


@division2calc.command()
@click.argument('file', required=True, type=click.Path())
@click.option('-i', '--index', type=int, default=0, help='which build in the list to display')
@click.option('--stats', is_flag=True, default=False, help='Enable stats summary')
@click.option('--x', is_flag=True, default=False, help='Enable x summary')
@click.option('--damage', is_flag=True, default=False, help='Enable damage summary')
@click.option('--dydx', is_flag=True, default=False, help='Enable dydx summary')
def summary(file: Path,
            index: int,
            stats: bool,
            damage: bool,
            x: bool,
            dydx: bool) -> None:
    build = load_builds_file(file)[index]
    all = not any((stats, x, damage, dydx))
    if all or stats:
        click.secho(f'\nstats: Build({build.name})', fg='yellow')
        print(build.summary.stats)

    if all or damage:
        click.secho(f'\ndamage: Build({build.name})', fg='yellow')
        print(build.summary.damage.round(2))
    if all or x:
        click.secho(f'\nx: Build({build.name})', fg='yellow')
        print(build.summary.x.round(4))
    if all or dydx:
        click.secho(f'\ndydx: Build({build.name})', fg='yellow')
        print(build.summary.dydx.round(4))
    # pprint.pp(dataclass_asdict(build))
    # print(build_as_yaml(build))
    # pprint.pp(build)
    # print(pformat_dataclass(build))


division2calc.add_command(compare)
division2calc.add_command(rank)
