from dataclasses import dataclass
from typing import Literal

from weapon.attribute import AssultRifleDamage, CoreAttribute, MinorAttribute
from weapon.mods import (CriticalHitChance, CriticalHitDamage, HeadshotDamage,
                         Mod)

WeaponType = Literal['AR', 'SMG', 'LMG', 'Rifle', 'MMR', 'Shotgun']


@dataclass(kw_only=True)
class Weapon:
    name: str
    type: WeaponType
    base_damage: int
    expertise_level: int
    # attribute
    core1: CoreAttribute
    core2: CoreAttribute
    minor: MinorAttribute
    # mods
    optics: Mod
    magazine: Mod
    muzzle: Mod
    underbarrel: Mod

    def __post_init__(self) -> None:
        self.cores = (self.core1, self.core2)
        self.mods = (self.optics, self.magazine, self.muzzle, self.underbarrel)

    @property
    def weapon_damage_pct(self) -> float:
        return self.expertise_level * 0.01

    @property
    def weapon_type_damage_pct(self) -> float:
        pct = 0
        # cores
        for core in self.cores:
            if self.type == 'AR' and isinstance(core, AssultRifleDamage):
                pct += core.weapon_type_damage_pct

        # result
        return pct

    @property
    def critical_hit_chance_pct(self) -> float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, CriticalHitChance):
                pct += mod.pct

        # result
        return pct

    @property
    def critical_hit_damage_pct(self) -> float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, CriticalHitDamage):
                pct += mod.pct

        # result
        return pct

    @property
    def headshot_damage_pct(self) -> float:
        pct = 0
        # mods
        for mod in self.mods:
            if isinstance(mod, HeadshotDamage):
                pct += mod.pct

        # result
        return pct
