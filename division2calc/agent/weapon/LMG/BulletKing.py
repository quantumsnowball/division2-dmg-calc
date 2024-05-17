from dataclasses import dataclass, field

import division2calc.agent.weapon.attrs as attrs
import division2calc.agent.weapon.mods as mods
import division2calc.agent.weapon.talents as talents
from division2calc.agent.weapon import Weapon, WeaponType


@dataclass(kw_only=True)
class BulletKing(Weapon):
    expertise_level: int
    # presets
    name: str = "Bullet King"
    type: WeaponType = 'LMG'
    base_damage: int = 45084
    rpm: int = 850
    core1: attrs.CoreAttribute = field(default_factory=lambda: attrs.LMGDamage(.15))
    core2: attrs.CoreAttribute = field(default_factory=lambda: attrs.DamageToTargetOutOfCover(.12))
    minor: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.1))
    optics: mods.Mod = field(default_factory=mods.NoMod)
    magazine: mods.Mod = field(default_factory=mods.NoMod)
    muzzle: mods.Mod = field(default_factory=lambda: mods.CriticalHitChance(.05))
    underbarrel: mods.Mod = field(default_factory=lambda: mods.Stability(.1))
    talent: talents.Talent = field(default_factory=talents.BulletHell)
