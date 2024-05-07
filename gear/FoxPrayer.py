from dataclasses import dataclass, field

from gear import Gear
from gear.attribute import (CoreAttribute, CriticalHitDamage, MinorAttribute,
                            RedCore)


@dataclass(kw_only=True)
class FoxPrayer(Gear):
    name: str = 'Fox Prayer'
    core: CoreAttribute = field(default_factory=RedCore)
    minor: MinorAttribute = field(default_factory=CriticalHitDamage)
