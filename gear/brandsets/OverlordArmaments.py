from dataclasses import dataclass, field

import gear
import gear.attrs as attrs
from gear.brandsets import Brandsets


@dataclass(kw_only=True)
class OverlordArmaments(Brandsets):
    brandset: str = 'Overlord Armaments'


@dataclass(kw_only=True)
class FoxsPrayer(gear.Kneepads, OverlordArmaments):
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.DamageToTargetOutOfCover)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
