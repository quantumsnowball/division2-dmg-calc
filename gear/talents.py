from dataclasses import dataclass


class Talent:
    pass


@dataclass
class BackpackTalent(Talent):
    pass


@dataclass
class RiskManagement(BackpackTalent):
    pass


@dataclass
class ChestTalent(Talent):
    pass


@dataclass
class Obliterate(ChestTalent):
    unit: float = 0.01
    max_stack: int = 25

#
# Empty
#


class NoTalent(BackpackTalent, ChestTalent):
    def __repr__(self) -> str:
        return 'N/A'
