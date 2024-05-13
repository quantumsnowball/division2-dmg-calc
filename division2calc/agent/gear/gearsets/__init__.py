from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import division2calc.gear.gearsets.bonus as bonus
from division2calc.gear import Gear

BonusPool = tuple[bonus.NoBonus,
                  bonus.Bonus,
                  bonus.Bonus,
                  bonus.BonusTalent]


@dataclass(kw_only=True)
class Gearsets(Gear, ABC):
    gearset: str
    bonus_pool: BonusPool
    gearset_bonus: bonus.Bonus = field(default_factory=bonus.NoBonus)

    @abstractmethod
    def upgrade_bonus_talent(self) -> None:
        pass
