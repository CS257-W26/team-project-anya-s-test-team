from abc import ABC, abstractmethod

class VendingState(ABC):
    @abstractmethod
    def insert_quarter(self, machine):
        pass

    @abstractmethod
    def eject_quarter(self, machine):
        pass

    @abstractmethod
    def turn_crank(self, machine):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass