from dataclasses import dataclass, field

import gear
import gear.attrs as attrs
from gear.gearsets import Gearsets


@dataclass(kw_only=True)
class Mask(gear.Mask, Gearsets):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Backpack(gear.Backpack, Gearsets):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Chest(gear.Chest, Gearsets):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Gloves(gear.Gloves, Gearsets):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Holster(gear.Holster, Gearsets):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Kneepads(gear.Kneepads, Gearsets):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)
