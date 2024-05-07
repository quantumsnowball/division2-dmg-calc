from dataclasses import dataclass

from gear import Core, Gear


@dataclass(kw_only=True)
class Striker(Gear):
    name: str = 'Striker'
    core: Core = 'red'
