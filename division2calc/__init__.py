from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from pprint import pprint

import click

import division2calc.gear.attrs as gearattrs
import division2calc.gear.brandsets.Lengmo as Lengmo
import division2calc.gear.brandsets.OverlordArmaments as Overlord
import division2calc.gear.gearsets.StrikersBattlegear as Striker
import division2calc.gear.mods as gearmods
from division2calc.build import Build
from division2calc.build.specialization import Gunner
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
@click.argument('file', required=True, type=str)
def summary(file: str) -> None:
    spec = spec_from_file_location('build', Path(file))
    if not spec or not spec.loader:
        return
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    build: Build = module.build
    pprint(build.summary.dydx)
