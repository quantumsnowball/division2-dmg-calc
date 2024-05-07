from dataclasses import dataclass, field

from gear import Gear
from gear.attribute import CoreAttribute, RedCore


@dataclass(kw_only=True)
class Striker(Gear):
    name: str = 'Striker'
    core: CoreAttribute = field(default_factory=RedCore)
