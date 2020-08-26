from .bases import Vehicle
from inspect import currentframe


class Car(Vehicle):

    def __init__(self, weight, capacity, tank):
        super().__init__(weight, capacity, tank)
        self.weight = weight
        self.capacity = capacity
        self.tank = tank
        self.fuel = 0

    def get_gas(self, add):
        print(f'{currentframe().f_code.co_name}()')
        if add:
            if self.fuel + add <= self.tank:
                self.fuel += add
                print(f'Got some gas, yup! [fuel: {self.fuel}]')
            else:
                self.fuel = self.tank
                print(f'Tank full, no more gas! [fuel: {self.fuel}]')
        else:
            print('no fuel to add')

    def honk(self):
        print(f'{currentframe().f_code.co_name}()')
        print(f'{self.__class__.__name__} says honk honk!')

    def start(self):
        print(f'{currentframe().f_code.co_name}()')
        print('Turned the key!')


class Truck(Car):

    def __init__(self, weight, capacity, tank, carrying_capacity):
        super().__init__(weight, capacity, tank)
        self.carrying_capacity = carrying_capacity
        self.cargo = 0

    def __str__(self):
        return (super().__str__() +
                f'carrying capacity: {self.carrying_capacity} tons \n')
    
    def get_cargo(self, weight):
        print(f'{currentframe().f_code.co_name}()')
        if self.cargo + weight <= self.carrying_capacity:
            self.cargo += weight
            print(f'Cargo loaded, weight: {self.cargo}')
        else:
            self.cargo = self.carrying_capacity
            print(f'Cargo container full, no free space')
