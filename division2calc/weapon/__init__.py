from dataclasses import dataclass
from typing import Literal

import division2calc.weapon.attrs as attrs
import division2calc.weapon.mods as mods
import division2calc.weapon.talents as talents
from division2calc.utils import Float

WeaponType = Literal['AR', 'SMG', 'LMG', 'Rifle', 'MMR', 'Shotgun']


@dataclass(kw_only=True)
class Weapon:
    name: str
    type: WeaponType
    base_damage: int
    expertise_level: int
    # attribute
    core1: attrs.CoreAttribute
    core2: attrs.CoreAttribute
    minor: attrs.MinorAttribute
    # mods
    optics: mods.Mod
    magazine: mods.Mod
    muzzle: mods.Mod
    underbarrel: mods.Mod
    # talent
    talent: talents.Talent

    def __post_init__(self) -> None:
        self.cores = (self.core1, self.core2)
        self.attrs = (*self.cores, self.minor)
        self.mods = (self.optics, self.magazine, self.muzzle, self.underbarrel)

    @property
    def weapon_damage(self) -> Float:
        pct = self.expertise_level * 0.01
        src = [f'{self.__class__.__name__}.expertise({pct})', ]
        return Float(pct, src)

    @property
    def weapon_type_damage(self) -> Float:
        pct = 0
        src = []
        # cores
        for core in self.cores:
            if self.type == 'AR' and isinstance(core, attrs.AssultRifleDamage):
                pct += core.pct
                src += [f'{self.__class__.__name__}.{attrs.AssultRifleDamage.__name__}({core.pct})']
        # result
        return Float(pct, src)

    @property
    def critical_hit_chance(self) -> Float:
        pct = 0
        src = []
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.CriticalHitChance):
                pct += mod.pct
                src += [f'{self.__class__.__name__}.{mods.CriticalHitChance.__name__}({mod.pct})']
        # result
        return Float(pct, src)

    @property
    def critical_hit_damage(self) -> Float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.CriticalHitDamage):
                pct += mod.pct
        # result
        return Float(pct)

    @property
    def headshot_damage(self) -> Float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.HeadshotDamage):
                pct += mod.pct
        # result
        return Float(pct)

    @property
    def damage_to_health(self) -> Float:
        pct = 0
        # attr
        for attr in self.attrs:
            if isinstance(attr, attrs.HealthDamage):
                pct += attr.pct
        # result
        return Float(pct)

    @property
    def damage_to_target_out_of_cover(self) -> Float:
        pct = 0
        # attr
        for attr in self.attrs:
            if isinstance(attr, attrs.DamageToTargetOutOfCover):
                pct += attr.pct
        # result
        return Float(pct)
