from abc import ABCMeta, abstractmethod
from .exceptions import NegValueError, MustBeIntError


class Vehicle(metaclass=ABCMeta):
    weight = None
    capacity = None
    tank = None
    fuel = 0

    def __init__(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                raise MustBeIntError(arg)
            if arg < 0:
                raise NegValueError(arg)

    def __str__(self):
        return (f'---{self.__class__.__name__}--- \n'
                f'weight: {self.weight} tons \n'
                f'capacity: {self.capacity} passengers \n'
                f'tank: {self.tank} litres \n'
                f'fuel: {self.fuel} litres \n')

    @abstractmethod
    def honk(self):
        pass

    @abstractmethod
    def start(self):
        pass

