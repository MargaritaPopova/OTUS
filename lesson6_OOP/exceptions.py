class NegValueError(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Значение \'{self.value}\' отрицательно, должно быть положительным'


class MustBeIntError(TypeError):

    def __init__(self, value):
        self.value = type(value)

    def __str__(self):
        return f'Значение параметра должно быть числовым, передано значение: {self.value}'


class EngineTypeError(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Тип двигателя \'{self.value}\' не соответствует классу'
