from dataclasses import dataclass


class Talent:
    pass


@dataclass
class ActumEst(Talent):
    pass


#
# Empty
#
class NoTalent(Talent):
    def __repr__(self) -> str:
        return 'N/A'
