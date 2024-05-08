from dataclasses import dataclass, field

import gear.attrs as attrs
import gear.mods as mods
from gear.brandsets import Brandsets


@dataclass(kw_only=True)
class Gear:
    core: attrs.CoreAttribute
    attr1: attrs.MinorAttribute

    def __post_init__(self) -> None:
        self.attrs = [self.core, self.attr1]
        if isinstance(self, Brandsets):
            self.attrs.append(self.attr2)

    @property
    def weapon_damage_pct(self) -> float:
        if isinstance(self.core, attrs.RedCore):
            return self.core.weapon_damage_pct
        return 0.0

    @property
    def critical_hit_chance_pct(self) -> float:
        pct = 0
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.CriticalHitChance):
                pct += attr.pct
        # mods
        if isinstance(self, (Mask, Backpack, Chest)):
            if isinstance(self.mod, mods.CriticalHitChance):
                pct += self.mod.pct

        # result
        return pct

    @property
    def critical_hit_damage_pct(self) -> float:
        pct = 0
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.CriticalHitDamage):
                pct += attr.pct
        # mods
        if isinstance(self, (Mask, Backpack, Chest)):
            if isinstance(self.mod, mods.CriticalHitDamage):
                pct += self.mod.pct

        # result
        return pct

    @property
    def headshot_damage_pct(self) -> float:
        pct = 0
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.HeadshotDamage):
                pct += attr.pct
        # mods
        if isinstance(self, (Mask, Backpack, Chest)):
            if isinstance(self.mod, mods.HeadshotDamage):
                pct += self.mod.pct

        # result
        return pct

    @property
    def damage_to_health_pct(self) -> float:
        pct = 0
        # attribute
        for attr in self.attrs:
            if isinstance(attr, attrs.DamageToHealth):
                pct += attr.pct

        # result
        return pct

    @property
    def damage_to_target_out_of_cover_pct(self) -> float:
        pct = 0
        # attrs
        for attr in self.attrs:
            if isinstance(attr, attrs.DamageToTargetOutOfCover):
                pct += attr.pct

        # result
        return pct


@dataclass(kw_only=True)
class Mask(Gear):
    mod: mods.Mod = field(default_factory=mods.NoMod)


@dataclass(kw_only=True)
class Backpack(Gear):
    mod: mods.Mod = field(default_factory=mods.NoMod)


@dataclass(kw_only=True)
class Chest(Gear):
    mod: mods.Mod = field(default_factory=mods.NoMod)


@dataclass(kw_only=True)
class Gloves(Gear):
    pass


@dataclass(kw_only=True)
class Holster(Gear):
    pass


@dataclass(kw_only=True)
class Kneepads(Gear):
    pass


Gears = tuple[Mask, Backpack, Chest, Gloves, Holster, Kneepads]
