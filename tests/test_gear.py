from division2calc.agent import Build
from division2calc.agent.gear import Gear


def test_build_gears(build: Build):
    for gear in build.gears:
        assert isinstance(gear, Gear)
