from dataclasses import dataclass


@dataclass
class Bonus:
    pass


@dataclass
class WeaponHandling(Bonus):
    pct: float = 0.15


@dataclass
class RateOfFire(Bonus):
    pct: float = 0.15


@dataclass
class Talent:
    pass


@dataclass
class BonusTalent(Bonus, Talent):
    pass


@dataclass
class StrikersGamble(BonusTalent):
    unit: float = 0.0065
    max_stack: int = 100
    prob: float = 0.40

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


@dataclass
class NoBonus(Bonus):
    def __repr__(self) -> str:
        return 'N/A'
