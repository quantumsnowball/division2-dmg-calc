import pytest

from division2calc import *
from division2calc.build.common import PROFILES, Profile
from division2calc.build.damage.Dydx import X_Derivatives
from division2calc.build.damage.X import X_Value

build = Build(
    name='base',
    # specialization
    specialization=Gunner(),
    # weapons
    weapon=AR.StElmosEngine(expertise_level=15),
    # gears
    mask=Striker.Mask(attr1=gearattrs.CHC(0.06),
                      mod=gearmods.CHD(0.12)),
    backpack=Striker.Backpack(mod=gearmods.CHD(0.12)),
    chest=Lengmo.Chest(mod=gearmods.CHD(0.119)),
    gloves=Striker.Gloves(),
    holster=Striker.Holster(),
    kneepads=Overlord.FoxsPrayer(attr2=gearattrs.CHC(0.06)),
)


@pytest.mark.parametrize('profile', PROFILES)
def test_build_damage(profile: Profile):
    assert isinstance(build.damage.__getattribute__(profile), float)


@pytest.mark.parametrize('profile', PROFILES)
def test_build_damage_x(profile: Profile):
    x_value: X_Value = build.damage.x.__getattribute__(profile)
    for k, v in x_value.items():
        assert isinstance(k, str)
        assert isinstance(v, float)


@pytest.mark.parametrize('profile', PROFILES)
def test_build_damage_dydx(profile: Profile):
    x_der: X_Derivatives = build.damage.dydx.__getattribute__(profile)
    for k, v in x_der.items():
        assert isinstance(k, str)
        assert isinstance(v, float)
