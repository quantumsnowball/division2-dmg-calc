from dataclasses import dataclass, field

import gear
import gear.attrs as attrs


@dataclass(kw_only=True)
class Mask(gear.Mask):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Backpack(gear.Backpack):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Chest(gear.Chest):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Gloves(gear.Gloves):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Holster(gear.Holster):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)


@dataclass(kw_only=True)
class Kneepads(gear.Kneepads):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.NoAttr)
