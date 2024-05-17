from dataclasses import dataclass, field

import division2calc.agent.weapon.attrs as attrs
import division2calc.agent.weapon.mods as mods
import division2calc.agent.weapon.talents as talents
from division2calc.agent.weapon import Weapon, WeaponType


@dataclass(kw_only=True)
class GR9(Weapon):
    expertise_level: int
    # presets
    name: str = 'GR9'
    type: WeaponType = 'LMG'
    base_damage: int = 47905
    rpm: int = 750
    reload_time: float = 4.67
    core1: attrs.CoreAttribute = field(default_factory=lambda: attrs.LMGDamage(.15))
    core2: attrs.CoreAttribute = field(default_factory=lambda: attrs.DamageToTargetOutOfCover(.12))
    minor: attrs.MinorAttribute = field(default_factory=lambda: attrs.DamageToArmor(.06))
    optics: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.05))
    magazine: mods.Mod = field(default_factory=lambda: mods.RateOfFire(.05))
    muzzle: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.05))
    underbarrel: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.05))
    talent: talents.Talent = field(default_factory=lambda: talents.Measured())
