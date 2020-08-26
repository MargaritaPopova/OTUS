from dataclasses import dataclass


@dataclass
class Engine:
    e_type: str
    fuel: str
    volume: int
    pistons: int
    engine_types = ['diesel', 'steam turbine', 'gas turbine']

    def __post_init__(self):
        if not all(isinstance(i, str) for i in (self.e_type, self.fuel)):
            raise TypeError('Incorrect input data, str required')
        if not all(isinstance(i, int) for i in (self.volume, self.pistons)):
            raise TypeError('Incorrect input data, int required')
