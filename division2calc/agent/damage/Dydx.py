import math
from dataclasses import dataclass

from division2calc.agent.damage.common import Profile
from division2calc.agent.damage.X import Name, X, X_Value

X_Derivatives = dict[Name, float]


@dataclass
class Dydx(Profile[X_Derivatives]):
    _x: X

    def dydx(self, x: X_Value) -> X_Derivatives:
        prod_x = math.prod(x.values())
        dydx: X_Derivatives = {k: prod_x/v for k, v in x.items()}
        return dydx

    #
    # use cases
    #
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
