from dataclasses import dataclass, field

import division2calc.agent.gear as gear
import division2calc.agent.gear.attrs as attrs
import division2calc.agent.gear.brandsets.bonus as bonus
from division2calc.agent.gear.brandsets import BonusPool, Brandsets


@dataclass(kw_only=True)
class OverlordArmaments(Brandsets):
    brandset: str = 'Overlord Armaments'
    bonus_pool: BonusPool = field(default=(bonus.RifleDamage(0.1),
                                           bonus.Accuracy(0.3),
                                           bonus.WeaponHandling(0.3)), repr=False)


@ dataclass(kw_only=True)
class FoxsPrayer(gear.Kneepads, OverlordArmaments):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.DamageToTargetOutOfCover(.08))
    attr2: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))
