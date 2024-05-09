from dataclasses import dataclass, replace

from gear.gearsets import Gearsets
from gear.gearsets.bonus import StrikersGamble


class Talent:
    pass


@dataclass
class BackpackTalent(Talent):
    pass


@dataclass
class RiskManagement(BackpackTalent):
    unit: float = 0.01

    def update(self, target: Gearsets) -> None:
        if isinstance(target.gearset_bonus, StrikersGamble):
            target.gearset_bonus = replace(target.gearset_bonus,
                                           unit=self.unit)


@dataclass
class ChestTalent(Talent):
    pass


@dataclass
class Obliterate(ChestTalent):
    unit: float = 0.01
    max_stack: int = 25
    prob: float = 0.5

    @property
    def buff(self) -> float:
        return self.unit*self.max_stack

    @property
    def min(self) -> float:
        return 0

    @property
    def average(self) -> float:
        return self.prob*self.buff

    @property
    def max(self) -> float:
        return self.buff

#
# Empty
#


class NoTalent(BackpackTalent, ChestTalent):
    def __repr__(self) -> str:
        return 'N/A'
