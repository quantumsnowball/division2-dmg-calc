from dataclasses import dataclass

import math
from build.damage.X import X


@dataclass
class Dydx:
    _x: X

    def dydx(self, x: dict[str, float]) -> dict[str, float]:
        prod_x = math.prod(x.values())
        dydx = {k: prod_x/v for k, v in x.items()}
        return dydx

    @property
    def basic(self) -> dict[str, float]:
        return self.dydx(self._x.basic)

    @property
    def min(self) -> dict[str, float]:
        return self.dydx(self._x.min)

    @property
    def average(self) -> dict[str, float]:
        return self.dydx(self._x.average)

    @property
    def max(self) -> dict[str, float]:
        return self.dydx(self._x.max)
