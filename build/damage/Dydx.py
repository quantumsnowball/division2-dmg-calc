from dataclasses import dataclass

import math
from build.damage.X import X, Name, X_Value

X_Derivatives = dict[Name, float]


@dataclass
class Dydx:
    _x: X

    def dydx(self, x: X_Value) -> X_Derivatives:
        prod_x = math.prod(x.values())
        dydx: X_Derivatives = {k: prod_x/v for k, v in x.items()}
        return dydx

    @property
    def basic(self) -> X_Derivatives:
        return self.dydx(self._x.basic)

    @property
    def min(self) -> X_Derivatives:
        return self.dydx(self._x.min)

    @property
    def average(self) -> X_Derivatives:
        return self.dydx(self._x.average)

    @property
    def max(self) -> X_Derivatives:
        return self.dydx(self._x.max)
