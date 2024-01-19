from abc import ABC, abstractmethod


class Option(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
