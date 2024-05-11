from dataclasses import dataclass, field

import division2calc.weapon.attrs as attrs
import division2calc.weapon.mods as mods
import division2calc.weapon.talents as talents
from division2calc.weapon import Weapon, WeaponType


@dataclass(kw_only=True)
class ShieldSplinterer(Weapon):
    expertise_level: int
    # presets
    name: str = "Shield Splinterer"
    type: WeaponType = 'AR'
    base_damage: int = 45132
    core1: attrs.CoreAttribute = field(default_factory=attrs.AssultRifleDamage)
    core2: attrs.CoreAttribute = field(default_factory=attrs.HealthDamage)
    minor: attrs.MinorAttribute = field(default_factory=lambda: attrs.DamageToTargetOutOfCover(0.09))
    optics: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(0.05))
    magazine: mods.Mod = field(default_factory=mods.NoMod)
    muzzle: mods.Mod = field(default_factory=mods.NoMod)
    underbarrel: mods.Mod = field(default_factory=mods.NoMod)
    talent: talents.Talent = field(default_factory=talents.ActumEst)
