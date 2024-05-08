from dataclasses import dataclass, field

from build.damage import Damage
from build.stats import Stats
from build.summary import Summary
import gear
from build.specialization import Specialization
from build.watch import Watch
import gear.utils as utils
from weapon import Weapon


@dataclass
class Build:
    name: str
    weapon: Weapon
    mask: gear.Mask
    backpack: gear.Backpack
    chest: gear.Chest
    gloves: gear.Gloves
    holster: gear.Holster
    kneepads: gear.Kneepads
    specialization: Specialization
    watch: Watch = field(default_factory=Watch)

    def __post_init__(self) -> None:
        self.gears = (
            self.mask, self.backpack,
            self.chest, self.gloves,
            self.holster, self.kneepads
        )
        self.stats = Stats(self.weapon, self.gears, self.watch, self.specialization)
        self.damage = Damage(self.weapon, self.gears, self.stats)
        self.summary = Summary(self.stats, self.damage)
        # enable brandset bonus
        utils.enable_brandset_bonus(self.gears)
        # enable gearset bonus
        utils.enable_gearset_bonus(self.gears)
