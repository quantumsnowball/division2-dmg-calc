from dataclasses import dataclass


class Bonus:
    pass


@dataclass
class WeaponHandling(Bonus):
    pct: float = 0.15


@dataclass
class RateOfFire(Bonus):
    pct: float = 0.15


#
# Empty
#
class NoBonus(Bonus):
    def __repr__(self) -> str:
        return 'N/A'
