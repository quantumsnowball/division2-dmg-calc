from division2calc.agent import Build
from division2calc.agent.weapon import Weapon


def test_build_weapon(build: Build):
    assert isinstance(build.weapon, Weapon)
