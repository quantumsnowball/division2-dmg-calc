from dataclasses import dataclass, field

from gear import Gear
from gear.attribute import (BlueCore, CoreAttribute, CriticalHitChance,
                            MinorAttribute)


@dataclass(kw_only=True)
class Lengmo(Gear):
    name: str = 'Lengmo'
    core: CoreAttribute = field(default_factory=BlueCore)
    attr1: MinorAttribute = field(default_factory=CriticalHitChance)
