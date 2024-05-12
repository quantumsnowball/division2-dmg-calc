from dataclasses import dataclass

from division2calc.build.damage.common import Profile
from division2calc.utils import Float


@dataclass
class X4(Profile[Float]):
    @property
    def basic(self) -> Float:
        return Float(1.0)

    @property
    def min(self) -> Float:
        return self.basic

    @property
    def average(self) -> Float:
        return self.basic

    @property
    def max(self) -> Float:
        return self.basic
