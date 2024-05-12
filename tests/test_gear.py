from division2calc.build import Build
from division2calc.gear import Gear


def test_build_gears(build: Build):
    for gear in build.gears:
        assert isinstance(gear, Gear)