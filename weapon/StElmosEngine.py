from dataclasses import dataclass, field

from weapon import Weapon, WeaponType
from weapon.attribute import (AssultRifleDamage, CoreAttribute, HealthDamage,
                              MinorAttribute, RateOfFire)
from weapon.mods import CriticalHitChance, CriticalHitDamage, Mod, NoMod


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
    optics: Mod = field(default_factory=lambda: CriticalHitDamage(0.20))
    magazine: Mod = field(default_factory=NoMod)
    muzzle: Mod = field(default_factory=lambda: CriticalHitChance(0.20))
    underbarrel: Mod = field(default_factory=NoMod)
