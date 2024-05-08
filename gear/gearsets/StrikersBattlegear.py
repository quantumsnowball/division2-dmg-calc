from dataclasses import dataclass, field

import gear
import gear.attrs as attrs
from gear.gearsets import Gearsets


@dataclass(kw_only=True)
class StrikersBattlegear(Gearsets):
    gearset: str = "Striker's Battlegear"


@dataclass(kw_only=True)
class Mask(gear.Mask, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Backpack(gear.Backpack, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Chest(gear.Chest, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Gloves(gear.Gloves, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Holster(gear.Holster, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Kneepads(gear.Kneepads, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
