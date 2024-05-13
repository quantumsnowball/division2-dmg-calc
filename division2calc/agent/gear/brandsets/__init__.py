from dataclasses import dataclass, field

import division2calc.agent.gear.attrs as attrs
import division2calc.agent.gear.brandsets.bonus as bonus

BonusPool = tuple[bonus.Bonus,
                  bonus.Bonus,
                  bonus.Bonus]


@dataclass(kw_only=True)
class Brandsets:
    brandset: str
    attr2: attrs.MinorAttribute
    bonus_pool: BonusPool
    brandset_bonus: bonus.Bonus = field(default_factory=bonus.NoBonus)
