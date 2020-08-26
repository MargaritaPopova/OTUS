from lesson6_OOP.Car import Car, Truck
from lesson6_OOP.Boat import Boat, Ship
from lesson6_OOP.exceptions import NegValueError, MustBeIntError, EngineTypeError
import traceback
from lesson6_OOP.Engine import Engine


def showcase_vehicle(v):
    print(v)
    v.start()
    v.honk()


def main():
    try:
        c = Car(3, 10, 40)
        showcase_vehicle(c)
        c.get_gas(30)
        c.get_gas(50)
        print()

        t = Truck(8, 2, 500, 20)
        showcase_vehicle(t)
        t.get_gas(200)
        t.get_cargo(15)
        print()

        b = Boat(2, 2, 3)
        showcase_vehicle(b)
        print()

        e = Engine('diesel', 'diesel', 200, 4)
        s = Ship(50000, 200, 30, '1', e)
        showcase_vehicle(s)

    except MustBeIntError:
        print(traceback.format_exc())
    except NegValueError:
        print(traceback.format_exc())
    except EngineTypeError:
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
