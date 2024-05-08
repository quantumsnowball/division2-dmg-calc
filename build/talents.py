from dataclasses import dataclass

from gear.gearsets.talent import GearsetTalent
from gear.talent import BackpackTalent, ChestTalent
from weapon.talent import WeaponTalent


@dataclass
class Talents:
    weapon: WeaponTalent
    backpack: BackpackTalent
    chest: ChestTalent
    geatset: GearsetTalent
