from dataclasses import dataclass, field

import gear
import gear.attrs as attrs
from gear.gearsets import Gearsets


@dataclass(kw_only=True)
class Mask(gear.Mask, Gearsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Backpack(gear.Backpack, Gearsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Chest(gear.Chest, Gearsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Gloves(gear.Gloves, Gearsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Holster(gear.Holster, Gearsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)


@dataclass(kw_only=True)
class Kneepads(gear.Kneepads, Gearsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
