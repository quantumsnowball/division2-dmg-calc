from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Profile(ABC, Generic[T]):
    @property
    @abstractmethod
    def basic(self) -> T:
        pass

    @property
    @abstractmethod
    def min(self) -> T:
        pass

    @property
    @abstractmethod
    def average(self) -> T:
        pass

    @property
    @abstractmethod
    def max(self) -> T:
        pass
