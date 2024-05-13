from dataclasses import dataclass
from division2calc.build.damage.common import Profile


@dataclass
class X5(Profile[float]):
    @property
    def basic(self) -> float:
        return 1.0

    @property
    def min(self) -> float:
        return self.basic

    @property
    def average(self) -> float:
        return self.basic

    @property
    def max(self) -> float:
        return self.basic
