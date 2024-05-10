from dataclasses import dataclass


@dataclass
class Talent:
    pass


@dataclass
class ActumEst(Talent):
    pass


#
# Empty
#
@dataclass
class NoTalent(Talent):
    def __repr__(self) -> str:
        return 'N/A'
