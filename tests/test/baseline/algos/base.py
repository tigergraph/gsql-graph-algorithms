from abc import ABC, abstractmethod


class Baseline(ABC):
    @abstractmethod
    def run(self):
        ...
