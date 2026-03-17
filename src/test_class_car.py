import unittest
from .car import Car

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def tearDown(self):
        pass

    def test_drive(self):
        self.car.drive(20)
        self.assertRaises(Exception, lambda: self.car.drive(80000))

    def test_refuel(self):
        # Заправим 20 литров
        self.car.refuel_car(20)
        assert self.car.get_current_fuel_level() == 20
        # Проверим, что будет исключение, если перельем
        self.assertRaises(Exception, lambda: self.car.refuel_car(80))0
