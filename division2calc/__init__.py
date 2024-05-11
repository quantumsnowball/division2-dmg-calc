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
from division2calc.command.summary import summary
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


division2calc.add_command(summary)
division2calc.add_command(compare)
division2calc.add_command(rank)
