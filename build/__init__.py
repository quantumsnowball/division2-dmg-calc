from dataclasses import dataclass

from weapon import Weapon


@dataclass
class Build:
    name: str
    weapon: Weapon
