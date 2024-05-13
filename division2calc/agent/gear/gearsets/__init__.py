from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import division2calc.agent.gear.gearsets.bonus as bonus

BonusPool = tuple[bonus.NoBonus,
                  bonus.Bonus,
                  bonus.Bonus,
                  bonus.BonusTalent]


@dataclass(kw_only=True)
class Gearsets(ABC):
    gearset: str
    bonus_pool: BonusPool
    gearset_bonus: bonus.Bonus = field(default_factory=bonus.NoBonus)

    @abstractmethod
    def upgrade_bonus_talent(self) -> None:
        pass
