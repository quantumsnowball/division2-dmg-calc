from dataclasses import dataclass


@dataclass
class Talent:
    pass


@dataclass
class ActumEst(Talent):
    pass


@dataclass
class PerfectOptimist(Talent):
    '''
    Perfect Optimist 
    Weapon damage is increased by 4% for every 10% ammo missing from the magazine.	
    '''
    prob: float = 0.5
    max_buff: float = 0.4


#
# Empty
#
@dataclass
class NoTalent(Talent):
    def __repr__(self) -> str:
        return 'N/A'
