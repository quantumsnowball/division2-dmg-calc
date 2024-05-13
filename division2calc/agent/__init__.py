from dataclasses import dataclass, field

import division2calc.gear.utils as utils
from division2calc.agent.damage import Damage
from division2calc.agent.specialization import Specialization
from division2calc.agent.stats import Stats
from division2calc.agent.summary import Summary
from division2calc.agent.watch import Watch
from division2calc.agent.weapon import Weapon
from division2calc.gear import (Backpack, Chest, Gears, Gloves, Holster,
                                Kneepads, Mask)


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
        self.summary = Summary(self.stats, self.damage)
