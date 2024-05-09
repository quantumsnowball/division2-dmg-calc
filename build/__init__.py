from dataclasses import dataclass, field

from build.damage import Damage
from build.stats import Stats
from build.summary import Summary
from build.specialization import Specialization
from build.watch import Watch
from gear import Mask, Backpack, Chest, Gloves, Holster, Kneepads
from gear import Gears
import gear.utils as utils
from weapon import Weapon


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
        # enable brandset bonus
        utils.enable_brandset_bonus(self.gears)
        # enable gearset bonus
        utils.enable_gearset_bonus(self.gears)
        # helpers
        self.stats = Stats(self.weapon, self.gears, self.watch, self.specialization)
        self.damage = Damage(self.weapon, self.gears, self.stats)
        self.summary = Summary(self.stats, self.damage)
