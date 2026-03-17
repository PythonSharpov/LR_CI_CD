import unittest
from .car import Car

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def test_drive(self):
        # Сначала заправим машину, чтобы было чем ехать
        self.car.refuel_car(60)  # допустим, 60 литров
        # Проверим, что после поездки на 20 км уровень уменьшился
        self.car.drive(20)
        # Проверим, что слишком длинная поездка вызывает исключение
        with self.assertRaises(ValueError):
            self.car.drive(80000)

    def test_refuel(self):
        self.car.refuel_car(20)
        self.assertEqual(self.car.get_current_fuel_level(), 20)
        # Проверка перелива
        with self.assertRaises(ValueError):
            self.car.refuel_car(80)
