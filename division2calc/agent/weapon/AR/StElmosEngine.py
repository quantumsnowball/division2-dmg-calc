from dataclasses import dataclass, field

import division2calc.agent.weapon.attrs as attrs
import division2calc.agent.weapon.mods as mods
import division2calc.agent.weapon.talents as talents
from division2calc.agent.weapon import Weapon, WeaponType


@dataclass(kw_only=True)
class StElmosEngine(Weapon):
    expertise_level: int
    # presets
    name: str = "St Elmo's Engine"
    type: WeaponType = 'AR'
    base_damage: int = 44191
    core1: attrs.CoreAttribute = field(default_factory=lambda: attrs.AssultRifleDamage(.15))
    core2: attrs.CoreAttribute = field(default_factory=lambda: attrs.HealthDamage(.21))
    minor: attrs.MinorAttribute = field(default_factory=lambda: attrs.RateOfFire(.05))
    optics: mods.Mod = field(default_factory=lambda: mods.CriticalHitDamage(.20))
    magazine: mods.Mod = field(default_factory=lambda: mods.Rounds(30))
    muzzle: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.20))
    underbarrel: mods.Mod = field(default_factory=lambda: mods.WeaponHandling(.20))
    talent: talents.Talent = field(default_factory=lambda: talents.ActumEst())
