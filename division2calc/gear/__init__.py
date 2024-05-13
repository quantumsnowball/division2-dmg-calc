from __future__ import annotations

from dataclasses import dataclass, field
from typing import NamedTuple

import division2calc.gear.attrs as attrs
import division2calc.gear.mods as mods
import division2calc.gear.talents as talents
from division2calc.gear.brandsets import Brandsets
from division2calc.utils import Float


@dataclass(kw_only=True)
class Gear:
    core: attrs.CoreAttribute
    attr1: attrs.MinorAttribute
    # refer to other gears, warning: circular reference!
    _gears: Gears = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.attrs = [self.core, self.attr1]
        if isinstance(self, Brandsets):
            self.attrs.append(self.attr2)

    @property
    def clsn(self) -> str:
        return self.__class__.__name__

    @property
    def weapon_damage(self) -> Float:
        if isinstance(self.core, attrs.RedCore):
            return Float(self.core.damage, [f'RedCore({self.core.damage})', ])
        return Float(0.0)

    @property
    def critical_hit_chance(self) -> Float:
        pct = 0
        src = []
        # bonus
        # TODO
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.CriticalHitChance):
                pct += attr.pct
                src += [f'{self.clsn}.attr.CHC({attr.pct})']
        # mods
        if isinstance(self, (Mask, Backpack, Chest)):
            if isinstance(self.mod, mods.CriticalHitChance):
                pct += self.mod.pct
                src += [f'{self.clsn}.mod.CHC({self.mod.pct})']
        # result
        return Float(pct, src)

    @property
    def critical_hit_damage(self) -> Float:
        pct = 0
        src = []
        # bonus
        # TODO
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.CriticalHitDamage):
                pct += attr.pct
                src += [f'{self.clsn}.attr.CHD({attr.pct})']
        # mods
        if isinstance(self, (Mask, Backpack, Chest)):
            if isinstance(self.mod, mods.CriticalHitDamage):
                pct += self.mod.pct
                src += [f'{self.clsn}.mod.CHD({self.mod.pct})']
        # result
        return Float(pct, src)

    @property
    def headshot_damage(self) -> Float:
        pct = 0
        src = []
        # bonus
        # TODO
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.HeadshotDamage):
                pct += attr.pct
                src += [f'{self.clsn}.attr.HS({attr.pct})']
        # mods
        if isinstance(self, (Mask, Backpack, Chest)):
            if isinstance(self.mod, mods.HeadshotDamage):
                pct += self.mod.pct
                src += [f'{self.clsn}.mod.HS({self.mod.pct})']
        # result
        return Float(pct, src)

    @property
    def damage_to_health(self) -> Float:
        pct = 0
        src = []
        # bonus
        # TODO
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.DamageToHealth):
                pct += attr.pct
                src += [f'{self.clsn}.attr.DtH({attr.pct})']
        # result
        return Float(pct, src)

    @property
    def damage_to_target_out_of_cover(self) -> Float:
        pct = 0
        src = []
        # attrs
        for attr in self.attrs:
            if isinstance(attr, attrs.DamageToTargetOutOfCover):
                pct += attr.pct
                src += [f'{self.clsn}.attr.DtooC({attr.pct})']
        # result
        return Float(pct, src)


@dataclass(kw_only=True)
class Mask(Gear):
    mod: mods.Mod = field(default_factory=mods.NoMod)


@dataclass(kw_only=True)
class Backpack(Gear):
    mod: mods.Mod = field(default_factory=mods.NoMod)
    talent: talents.BackpackTalent = field(default_factory=talents.NoTalent)


@dataclass(kw_only=True)
class Chest(Gear):
    mod: mods.Mod = field(default_factory=mods.NoMod)
    talent: talents.ChestTalent = field(default_factory=talents.NoTalent)


@dataclass(kw_only=True)
class Gloves(Gear):
    pass


@dataclass(kw_only=True)
class Holster(Gear):
    pass


@dataclass(kw_only=True)
class Kneepads(Gear):
    pass


class Gears(NamedTuple):
    mask: Mask
    backpack: Backpack
    chest: Chest
    gloves: Gloves
    holster: Holster
    kneepads: Kneepads
