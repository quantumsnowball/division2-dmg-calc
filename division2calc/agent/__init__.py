from __future__ import annotations

import copy
from dataclasses import dataclass, field, replace
from typing import Any

import division2calc.agent.gear.utils as utils
from division2calc.agent.damage import Damage
from division2calc.agent.dps import DPS
from division2calc.agent.gear import (Backpack, Chest, Gears, Gloves, Holster,
                                      Kneepads, Mask)
from division2calc.agent.specialization import Specialization
from division2calc.agent.stats import Stats
from division2calc.agent.summary import Summary
from division2calc.agent.watch import Watch
from division2calc.agent.weapon import Weapon


@dataclass(kw_only=True)
class Build:
    name: str
    weapon: Weapon
    mask: Mask
    backpack: Backpack
    chest: Chest
    gloves: Gloves
    holster: Holster
    kneepads: Kneepads
    specialization: Specialization
    watch: Watch = field(default_factory=Watch)

    def __post_init__(self) -> None:
        # additional props
        self.gears = Gears(
            self.mask, self.backpack,
            self.chest, self.gloves,
            self.holster, self.kneepads
        )
        for gear in self.gears:
            gear._gears = self.gears
        # enable brandset bonus
        utils.enable_brandset_bonus(self.gears)
        # enable gearset bonus
        utils.enable_gearset_bonus(self.gears)
        # helpers
        self.stats = Stats(self.weapon, self.gears, self.watch, self.specialization)
        self.damage = Damage(self.weapon, self.gears, self.stats)
        self.dps = DPS(self.weapon, self.stats, self.damage)
        self.summary = Summary(self.stats, self.damage, self.dps)

    def replace(self, **changes: Any) -> Build:
        # generate a deep copy of the same build
        copied: Build = copy.deepcopy(self)
        # replace the fiels as supply by user
        replaced = replace(copied, **changes)
        #
        return replaced
