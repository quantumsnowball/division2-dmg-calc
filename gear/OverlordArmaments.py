from dataclasses import dataclass, field

import gear
import gear.attrs as attrs


@dataclass(kw_only=True)
class FoxsPrayer(gear.Kneepads):
    name: str = "Fox's Prayer"
    core: attrs.CoreAttribute = field(default_factory=attrs.RedCore)
    attr1: attrs.MinorAttribute = field(default_factory=attrs.DamageToTargetOutOfCover)
    attr2: attrs.MinorAttribute = field(default_factory=attrs.CriticalHitDamage)
