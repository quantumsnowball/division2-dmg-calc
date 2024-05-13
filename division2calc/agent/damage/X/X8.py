from dataclasses import dataclass
from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats


@dataclass
class X8(Profile[float]):
    _stats: Stats

    @property
    def basic(self) -> float:
        return 1.0

    @property
    def min(self) -> float:
        x = 1.0
        x += self._stats.damage_to_target_out_of_cover
        # result
        return x

    @property
    def average(self) -> float:
        return self.min

    @property
    def max(self) -> float:
        return self.min
