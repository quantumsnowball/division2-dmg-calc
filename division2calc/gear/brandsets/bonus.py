from dataclasses import dataclass


class Bonus:
    pass


@dataclass
class RifleDamage(Bonus):
    pct: float = 0.1


@dataclass
class Accuracy(Bonus):
    pct: float = 0.3


@dataclass
class WeaponHandling(Bonus):
    pct: float = 0.3


@dataclass
class ExploosiveResistance(Bonus):
    pct: float = 0.2


@dataclass
class SkillHealth(Bonus):
    pct: float = 0.25


@dataclass
class LMGDamage(Bonus):
    pct: float = 0.3


#
# Empty
#
class NoBonus(Bonus):
    def __repr__(self) -> str:
        return 'N/A'
