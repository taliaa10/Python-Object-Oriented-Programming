# Public => memberName
# Protected => _memberName
# Private => __Private


class Car:
    numberOfWheels = 4
    _color = 'Black'
    __yearOfManufacture = 2017  # _Car__yearOfManufacture


class BMW(Car):
    def __init__(self):
        print('Protected attribute color:', self._color)


car = Car()
print('Public attribute numberOfWheels', car.numberOfWheels)
bmw = BMW()
print('Private attribute yearOfManufacture:', car._Car__yearOfManufacture)
