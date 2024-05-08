from dataclasses import dataclass, field

import gear.gearsets.bonus as bonus

BonusPool = tuple[bonus.NoBonus,
                  bonus.Bonus,
                  bonus.Bonus,
                  bonus.BonusTalent]


@dataclass(kw_only=True)
class Gearsets:
    gearset: str
    bonus_pool: BonusPool
    gearset_bonus: bonus.Bonus = field(default_factory=bonus.NoBonus)
