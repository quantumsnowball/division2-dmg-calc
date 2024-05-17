from dataclasses import dataclass
from typing import Literal

import division2calc.agent.weapon.attrs as attrs
import division2calc.agent.weapon.mods as mods
import division2calc.agent.weapon.talents as talents
from division2calc.utils import Float

WeaponType = Literal['AR', 'SMG', 'LMG', 'Rifle', 'MMR', 'Shotgun']


@dataclass(kw_only=True)
class Weapon:
    name: str
    type: WeaponType
    base_damage: int
    rpm: int
    reload_time: float
    magazine_size: int
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
    def clsn(self) -> str:
        return self.__class__.__name__

    @property
    def weapon_damage(self) -> Float:
        unit = 0.01
        pct = self.expertise_level * unit
        src = [f'{self.clsn}.exp{self.expertise_level}({pct})', ]
        return Float(pct, src)

    @property
    def weapon_type_damage(self) -> Float:
        pct = 0
        src = []
        # cores
        for core in self.cores:
            if self.type == 'AR' and isinstance(core, attrs.AssultRifleDamage):
                pct += core.pct
                src += [f'{self.clsn}.AR({core.pct})']
        for core in self.cores:
            if self.type == 'LMG' and isinstance(core, attrs.LMGDamage):
                pct += core.pct
                src += [f'{self.clsn}.LMG({core.pct})']
        # result
        return Float(pct, src)

    @property
    def critical_hit_chance(self) -> Float:
        pct = 0
        src = []
        # attrs
        for attr in self.attrs:
            if isinstance(attr, attrs.CriticalHitChance):
                pct += attr.pct
                src += [f'{self.clsn}.attr.CHC({attr.pct})']
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.CriticalHitChance):
                pct += mod.pct
                src += [f'{self.clsn}.mod.CHC({mod.pct})']
        # result
        return Float(pct, src)

    @property
    def critical_hit_damage(self) -> Float:
        pct = 0
        src = []
        # attrs
        for attr in self.attrs:
            if isinstance(attr, attrs.CriticalHitDamage):
                pct += attr.pct
                src += [f'{self.clsn}.attr.CHD({attr.pct})']
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.CriticalHitDamage):
                pct += mod.pct
                src += [f'{self.clsn}.mod.CHD({mod.pct})']
        # result
        return Float(pct, src)

    @ property
    def headshot_damage(self) -> Float:
        pct = 0
        src = []
        # mods
        for mod in self.mods:
            if isinstance(mod, mods.HeadshotDamage):
                pct += mod.pct
                src += [f'{self.clsn}.mod.HS({mod.pct})']
        # result
        return Float(pct, src)

    @ property
    def damage_to_health(self) -> Float:
        pct = 0
        src = []
        # attr
        for attr in self.attrs:
            if isinstance(attr, attrs.HealthDamage):
                pct += attr.pct
                src += [f'{self.clsn}.attr.DtH({attr.pct})']
        # result
        return Float(pct, src)

    @ property
    def damage_to_target_out_of_cover(self) -> Float:
        pct = 0
        src = []
        # attr
        for attr in self.attrs:
            if isinstance(attr, attrs.DamageToTargetOutOfCover):
                pct += attr.pct
                src += [f'{self.clsn}.attr.DtooC({attr.pct})']
        # result
        return Float(pct, src)

    @ property
    def rate_of_fire(self) -> Float:
        pct = 0
        src = []
        # attr
        for attr in self.attrs:
            if isinstance(attr, attrs.RateOfFire):
                pct += attr.pct
                src += [f'{self.clsn}.attr.RateOfFire({attr.pct})']
        # mod
        for mod in self.mods:
            if isinstance(mod, mods.RateOfFire):
                pct += mod.pct
                src += [f'{self.clsn}.attr.RateOfFire({mod.pct})']
        # result
        return Float(pct, src)
