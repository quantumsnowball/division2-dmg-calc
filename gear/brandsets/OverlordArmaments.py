from dataclasses import dataclass, field

import gear
import gear.attrs as attrs
from gear.brandsets import Brandsets


@dataclass(kw_only=True)
class FoxsPrayer(gear.Kneepads, Brandsets):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.DamageToTargetOutOfCover)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
