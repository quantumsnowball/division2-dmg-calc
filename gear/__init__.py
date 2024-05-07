from dataclasses import dataclass
from typing import Literal

Core = Literal['red', 'blue', 'yellow']


@dataclass
class Gear:
    name: str
    core: Core

    @property
    def weapon_damage_pct(self) -> float:
        if self.core == 'red':
            return 0.15
        return 0
