from dataclasses import dataclass, field

import division2calc.agent.weapon.attrs as attrs
import division2calc.agent.weapon.mods as mods
import division2calc.agent.weapon.talents as talents
from division2calc.agent.weapon import Weapon, WeaponType


@dataclass(kw_only=True)
class ShieldSplinterer(Weapon):
    expertise_level: int
    # presets
    name: str = "Shield Splinterer"
    type: WeaponType = 'AR'
    base_damage: int = 45132
    rpm: int = 900
    reload_time: float = 2.1
    magazine_size: int = 60
    core1: attrs.CoreAttribute = field(default_factory=lambda: attrs.AssultRifleDamage(.15))
    core2: attrs.CoreAttribute = field(default_factory=lambda: attrs.HealthDamage(.21))
    minor: attrs.MinorAttribute = field(default_factory=lambda: attrs.DamageToTargetOutOfCover(.09))
    optics: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.05))
    magazine: mods.Mod = field(default_factory=mods.NoMod)
    muzzle: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.05))
    underbarrel: mods.Mod = field(default_factory=mods.NoMod)
    talent: talents.Talent = field(default_factory=lambda: talents.PerfectOptimist())
