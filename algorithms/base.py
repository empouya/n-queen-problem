from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self, n):
        self.n = n
        self.steps = 0

    @abstractmethod
    def run(self):
        """Generator that yields board states"""
        pass
