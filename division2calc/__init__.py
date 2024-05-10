from pathlib import Path
from pprint import pprint

import click
import pandas as pd

import division2calc.gear.attrs as gearattrs
import division2calc.gear.brandsets.Lengmo as Lengmo
import division2calc.gear.brandsets.OverlordArmaments as Overlord
import division2calc.gear.gearsets.StrikersBattlegear as Striker
import division2calc.gear.mods as gearmods
from division2calc.build import Build
from division2calc.build.specialization import Gunner
from division2calc.utils import load_build_file
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


@division2calc.command()
@click.argument('file', required=True, type=click.Path())
def summary(file: Path) -> None:
    build = load_build_file(file)
    pprint(build)


@division2calc.command()
@click.argument('file1', required=True, type=click.Path())
@click.argument('file2', required=True, type=click.Path())
@click.option('--x', is_flag=True, default=False, help='Enable x comparison')
@click.option('--damage', is_flag=True, default=False, help='Enable damage comparison')
@click.option('--dydx', is_flag=True, default=False, help='Enable dydx comparison')
def compare(file1: Path,
            file2: Path,
            damage: bool,
            x: bool,
            dydx: bool) -> None:
    build1 = load_build_file(file1)
    build2 = load_build_file(file2)
    all = not any((x, damage, dydx))
    if all or damage:
        click.secho(f'\ndiff(damage): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diff: pd.DataFrame = build2.summary.damage() - build1.summary.damage()
        print(diff.round(2))
        click.secho(f'\ndiff%(damage): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diffpct: pd.DataFrame = (build2.summary.damage() / build1.summary.damage() - 1)*100
        print(diffpct.round(4))
    if all or x:
        click.secho(f'\ndiff(x): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diff: pd.DataFrame = build2.summary.x - build1.summary.x
        print(diff.round(4))
    if all or dydx:
        click.secho(f'\ndiff(dydx): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diff: pd.DataFrame = build2.summary.dydx - build1.summary.dydx
        print(diff.round(4))
