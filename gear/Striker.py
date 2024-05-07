from dataclasses import dataclass, field

import gear.attrs as attrs
from gear import Gear


@dataclass(kw_only=True)
class Striker(Gear):
    name: str = 'Striker'
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
