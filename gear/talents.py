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
    pass

#
# Empty
#


class NoTalent(BackpackTalent, ChestTalent):
    def __repr__(self) -> str:
        return 'N/A'
