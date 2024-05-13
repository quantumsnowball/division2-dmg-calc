from dataclasses import dataclass, field
from typing import override

import division2calc.agent.gear as gear
import division2calc.agent.gear.attrs as attrs
import division2calc.agent.gear.gearsets.bonus as bonus
import division2calc.agent.gear.talents as talents
from division2calc.agent.gear.gearsets import BonusPool, Gearsets


@dataclass(kw_only=True)
class StrikersBattlegear(gear.Gear, Gearsets):
    gearset: str = "Striker's Battlegear"
    bonus_pool: BonusPool = field(default=(bonus.NoBonus(),
                                           bonus.WeaponHandling(0.15),
                                           bonus.RateOfFire(0.15),
                                           bonus.StrikersGamble()), repr=False)

    @override
    def upgrade_bonus_talent(self) -> None:
        # StrikersGamble bonus talent exists
        if not (
            isinstance(self, StrikersBattlegear) and
            isinstance(self.gearset_bonus, bonus.StrikersGamble)
        ):
            return
        # RiskManagement exists in backpack
        if isinstance(self._gears.backpack.talent, talents.RiskManagement):
            self.gearset_bonus.unit = self._gears.backpack.talent.unit
        # Press the Advantage exists in chest
        if isinstance(self._gears.chest.talent, talents.PressTheAdvantage):
            self.gearset_bonus.max_stack = self._gears.chest.talent.max_stack


@dataclass(kw_only=True)
class Mask(gear.Mask, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))


@dataclass(kw_only=True)
class Backpack(gear.Backpack, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))
    talent: talents.BackpackTalent = field(default_factory=talents.RiskManagement)


@dataclass(kw_only=True)
class Chest(gear.Chest, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))
    talent: talents.ChestTalent = field(default_factory=talents.PressTheAdvantage)


@dataclass(kw_only=True)
class Gloves(gear.Gloves, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))


@dataclass(kw_only=True)
class Holster(gear.Holster, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))


@dataclass(kw_only=True)
class Kneepads(gear.Kneepads, StrikersBattlegear):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.RedCore(.15))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitDamage(.12))
