from .Engine import Engine
from .bases import Vehicle
from .exceptions import EngineTypeError, MustBeIntError, NegValueError
from inspect import currentframe


class Boat(Vehicle):

    def __init__(self, weight, capacity, speed):
        super().__init__(weight, capacity, speed)
        self.weight = weight
        self.capacity = capacity
        self.speed = speed

    def __str__(self):
        return (super().__str__() +
                f'max speed: {self.speed} knots \n')

    def honk(self):
        print(f'{currentframe().f_code.co_name}()')
        print('Boats don\'t honk')

    def start(self):
        print(f'{currentframe().f_code.co_name}()')
        print('Go ahead and steer your paddles!')


class Ship(Boat):

    def __init__(self, weight, capacity, speed, crew, engine):
        super().__init__(weight, capacity, speed)
        if isinstance(crew, int) and crew < 0:
            raise NegValueError(crew)
        elif not isinstance(crew, int):
            raise MustBeIntError(crew)
        else:
            self.crew = crew

        if engine.e_type in Engine.engine_types:
            self.engine = engine.e_type
        else:
            raise EngineTypeError(self.engine)

    def __str__(self):
        return (super().__str__() +
                f'crew: {self.crew} members \n'
                f'engine type: {self.engine} \n')

    def start(self):
        print(f'{currentframe().f_code.co_name}()')
        print(f'Firing that huge badass {self.engine} engine!')

    def honk(self):
        print(f'{currentframe().f_code.co_name}()')
        print('Ships say hooooooorn')