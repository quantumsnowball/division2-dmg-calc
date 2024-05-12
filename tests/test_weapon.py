from division2calc.build import Build
from division2calc.weapon import Weapon


def test_build_weapon(build: Build):
    assert isinstance(build.weapon, Weapon)
