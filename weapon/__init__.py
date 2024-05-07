from dataclasses import dataclass
from typing import Literal

import weapon.attribute as attrs
import weapon.mods as mods

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

    def __post_init__(self) -> None:
        self.cores = (self.core1, self.core2)
        self.attrs = (*self.cores, self.minor)
        self.mods = (self.optics, self.magazine, self.muzzle, self.underbarrel)

    @property
    def weapon_damage_pct(self) -> float:
        return self.expertise_level * 0.01

    @property
    def weapon_type_damage_pct(self) -> float:
        pct = 0
        # cores
        for core in self.cores:
            if self.type == 'AR' and isinstance(core, attrs.AssultRifleDamage):
                pct += core.weapon_type_damage_pct

        # result
        return pct

    @property
    def critical_hit_chance_pct(self) -> float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.CriticalHitChance):
                pct += mod.pct

        # result
        return pct

    @property
    def critical_hit_damage_pct(self) -> float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.CriticalHitDamage):
                pct += mod.pct

        # result
        return pct

    @property
    def headshot_damage_pct(self) -> float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.HeadshotDamage):
                pct += mod.pct

        # result
        return pct

    @property
    def damage_to_health_pct(self) -> float:
        pct = 0
        # attr
        for attr in self.attrs:
            if isinstance(attr, attrs.HealthDamage):
                pct += attr.pct

        # result
        return pct
