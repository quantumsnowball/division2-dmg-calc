from dataclasses import dataclass, field

from gear import Gear
from gear.attribute import (CoreAttribute, CriticalHitDamage, MinorAttribute,
                            RedCore)


@dataclass(kw_only=True)
class Striker(Gear):
    name: str = 'Striker'
    core: CoreAttribute = field(default_factory=RedCore)
    attr1: MinorAttribute = field(default_factory=CriticalHitDamage)
