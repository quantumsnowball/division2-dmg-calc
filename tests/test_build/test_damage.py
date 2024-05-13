import pytest

from division2calc.agent import Build
from division2calc.agent.common import PROFILES, Profile
from division2calc.agent.damage.Dydx import X_Derivatives
from division2calc.agent.damage.X import X_Value


@pytest.mark.parametrize('profile', PROFILES)
def test_build_damage(build: Build, profile: Profile):
    assert isinstance(build.damage.__getattribute__(profile), float)


@pytest.mark.parametrize('profile', PROFILES)
def test_build_damage_x(build: Build, profile: Profile):
    x_value: X_Value = build.damage.x.__getattribute__(profile)
    for k, v in x_value.items():
        assert isinstance(k, str)
        assert isinstance(v, float)


@pytest.mark.parametrize('profile', PROFILES)
def test_build_damage_dydx(build: Build, profile: Profile):
    x_der: X_Derivatives = build.damage.dydx.__getattribute__(profile)
    for k, v in x_der.items():
        assert isinstance(k, str)
        assert isinstance(v, float)
