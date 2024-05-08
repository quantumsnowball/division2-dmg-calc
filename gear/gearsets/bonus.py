from dataclasses import dataclass


class Bonus:
    pass


@dataclass
class WeaponHandling(Bonus):
    pct: float = 0.15


@dataclass
class RateOfFire(Bonus):
    pct: float = 0.15


class Talent:
    pass


class BonusTalent(Bonus, Talent):
    pass


@dataclass
class StrikersGamble(BonusTalent):
    unit: float = 0.65
    max_stack: int = 100


#
# Empty
#


class NoBonus(Bonus):
    def __repr__(self) -> str:
        return 'N/A'
