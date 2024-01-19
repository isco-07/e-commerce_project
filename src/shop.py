from abc import ABC, abstractmethod


class Shop(ABC):
    @abstractmethod
    def __add__(self, other):
        pass
