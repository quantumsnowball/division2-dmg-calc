from dataclasses import dataclass, field

from weapon import Weapon, WeaponType
from weapon.attribute import (AssultRifleDamage, CoreAttribute, HealthDamage,
                              MinorAttribute, RateOfFire)


@dataclass(kw_only=True)
class StElmosEngine(Weapon):
    expertise_level: int
    # presets
    name: str = "St Elmo's Engine"
    type: WeaponType = 'AR'
    base_damage: int = 44191
    core1: CoreAttribute = field(default_factory=AssultRifleDamage)
    core2: CoreAttribute = field(default_factory=HealthDamage)
    minor: MinorAttribute = field(default_factory=RateOfFire)
