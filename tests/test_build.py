import pytest

from division2calc import *
from division2calc.build.common import PROFILES, Profile

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
    assert isinstance(getattr(build.damage, profile), float)
