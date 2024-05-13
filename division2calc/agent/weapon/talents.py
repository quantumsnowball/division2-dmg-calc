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


@dataclass
class BulletHell(Talent):
    pass


@dataclass
class Ranger(Talent):
    '''
    Amplifies weapon damage by 2% for every 5m (4m) you are away from your target.
    '''
    # assuming 25m / 5 * 2% = 10%
    avg_buff: float = 0.15
    # assuming 60m / 5 * 2% = 24%
    max_buff: float = 0.24


#
# Empty
#
@dataclass
class NoTalent(Talent):
    def __repr__(self) -> str:
        return 'N/A'
