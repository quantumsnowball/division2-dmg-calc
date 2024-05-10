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
    pprint(build.summary.dydx)


@division2calc.command()
@click.argument('file1', required=True, type=click.Path())
@click.argument('file2', required=True, type=click.Path())
@click.option('--x', is_flag=True, default=False, help='Enable x comparison')
@click.option('--dydx', is_flag=True, default=False, help='Enable dydx comparison')
def compare(file1: Path, file2: Path, x: bool, dydx: bool) -> None:
    build1 = load_build_file(file1)
    build2 = load_build_file(file2)
    if x:
        click.echo(f'\nx: Build({build2.name}) net Build({build1.name})\n')
        diff: pd.DataFrame = build2.summary.x - build1.summary.x
        print(diff.round(4))
    if dydx:
        click.echo(f'\nDydx: Build({build2.name}) net Build({build1.name})\n')
        diff: pd.DataFrame = build2.summary.dydx - build1.summary.dydx
        print(diff.round(4))
