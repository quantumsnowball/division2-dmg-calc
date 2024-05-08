from dataclasses import dataclass, field

import gear
import gear.attrs as attrs
from gear.brandsets import Brandsets


@dataclass(kw_only=True)
class Chest(gear.Chest, Brandsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.BlueCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.ExplosiveResistence)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitChance)
