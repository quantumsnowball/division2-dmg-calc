from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import gear.gearsets.bonus as bonus

if TYPE_CHECKING:
    from gear import Gears

BonusPool = tuple[bonus.NoBonus,
                  bonus.Bonus,
                  bonus.Bonus,
                  bonus.BonusTalent]


@dataclass(kw_only=True)
class Gearsets:
    gearset: str
    bonus_pool: BonusPool
    gearset_bonus: bonus.Bonus = field(default_factory=bonus.NoBonus)

    def upgrade_from(self, gears: 'Gears') -> None:
        pass
