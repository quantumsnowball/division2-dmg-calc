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


@dataclass
class Measured(Talent):
    '''
    The top half of the magazine has 20% rate of fire and -30% (27%) weapon damage.
    The bottom half of the magazine has -20% rate of fire and +30% (33%) total weapon damage.
    '''
    top_wd_dec: float = .3
    top_rof_inc: float = .2
    bottom_twd_inc: float = .3
    bottom_rof_dec: float = .2
    prob: float = 0.7

    @property
    def average_rof(self) -> float:
        return self.prob*self.top_rof_inc + (1-self.prob)*(-self.bottom_rof_dec)

    def adjust_dmg_min(self, dmg: float, x1: float, x2: float) -> float:
        x1_ = x1 + self.top_wd_dec
        x2_ = x2 + self.bottom_twd_inc
        return dmg / x1 / x2 * x1_ * x2_

    def adjust_dmg_max(self, dmg: float, x1: float, x2: float) -> float:
        x1_ = x1 - self.top_wd_dec
        x2_ = x2 - self.bottom_twd_inc
        return dmg / x1 / x2 * x1_ * x2_


#
# Empty
#
@dataclass
class NoTalent(Talent):
    def __repr__(self) -> str:
        return 'N/A'
