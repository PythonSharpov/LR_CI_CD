class FuelQuantityError(ValueError):
    """Количество топлива должно быть положительным"""
    def __init__(self):
        super().__init__("Количество топлива должно быть положительным")

class OverfillError(ValueError):
    """Вы пытаетесь залить слишком много бензина!"""
    def __init__(self):
        super().__init__("Вы пытаетесь залить слишком много бензина!")

class DistanceError(ValueError):
    """Дистанция должна быть положительной"""
    def __init__(self):
        super().__init__("Дистанция должна быть положительной")

class InsufficientFuelError(ValueError):
    """Не доедем жеж..."""
    def __init__(self):
        super().__init__("Не доедем жеж...")

class Car:
    DEFAULT_CONSUMPTION = 8.0

    def __init__(self, model: str, fuel_capacity: float, consumption: float = DEFAULT_CONSUMPTION) -> None:
        if fuel_capacity <= 0:
            raise ValueError("Ёмкость бака должна быть положительной")
        if consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным")
        self._model = model
        self._max_fuel_capacity = fuel_capacity
        self._consumption = consumption
        self._fuel_in_tank = 0.0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        if fuel_quantity <= 0:
            raise FuelQuantityError()
        if self._fuel_in_tank + fuel_quantity > self._max_fuel_capacity + 1e-9:
            raise OverfillError()
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        if distance_km <= 0:
            raise DistanceError()
        fuel_needed = self._consumption * (distance_km / 100)
        if self._fuel_in_tank < fuel_needed - 1e-9:
            raise InsufficientFuelError()
        self._fuel_in_tank -= fuel_needed
        return self._fuel_in_tank
