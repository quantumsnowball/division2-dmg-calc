from dataclasses import dataclass
from typing import Literal


@dataclass
class Gear:
    name: str
    core: Literal['red', 'blue', 'yellow']

    @property
    def weapon_damage_pct(self) -> float:
        if self.core == 'red':
            return 0.15
        return 0
