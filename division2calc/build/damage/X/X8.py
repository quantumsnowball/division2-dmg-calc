from dataclasses import dataclass

from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats
from division2calc.utils import Float


@dataclass
class X8(Profile[Float]):
    _stats: Stats

    @property
    def basic(self) -> Float:
        return Float(1.0)

    @property
    def min(self) -> Float:
        x = Float(1.0)
        x += self._stats.damage_to_target_out_of_cover
        # result
        return x

    @property
    def average(self) -> Float:
        return self.min

    @property
    def max(self) -> Float:
        return self.min
