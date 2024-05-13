from dataclasses import dataclass


@dataclass
class Talent:
    pass


@dataclass
class ActumEst(Talent):
    pass


@dataclass
class PerfectOptimist(Talent):
    # TODO
    pass


#
# Empty
#
@dataclass
class NoTalent(Talent):
    def __repr__(self) -> str:
        return 'N/A'
