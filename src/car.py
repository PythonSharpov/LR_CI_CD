class Car:
    # Константы с сообщениями об ошибках
    ERR_FUEL_QUANTITY_POSITIVE = "Количество топлива должно быть положительным"
    ERR_OVERFILL = "Вы пытаетесь залить слишком много бензина!"
    ERR_DISTANCE_POSITIVE = "Дистанция должна быть положительной"
    ERR_INSUFFICIENT_FUEL = "Не доедем жеж..."

    DEFAULT_CONSUMPTION = 8.0

    def __init__(self, model: str, fuel_capacity: float, consumption: float = DEFAULT_CONSUMPTION) -> None:
        if fuel_capacity <= 0:
            raise ValueError("Ёмкость бака должна быть положительной")  # Это сообщение тоже можно вынести, но линтер пока не ругается
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
            raise ValueError(self.ERR_FUEL_QUANTITY_POSITIVE)
        if self._fuel_in_tank + fuel_quantity > self._max_fuel_capacity + 1e-9:
            raise ValueError(self.ERR_OVERFILL)
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        if distance_km <= 0:
            raise ValueError(self.ERR_DISTANCE_POSITIVE)
        fuel_needed = self._consumption * (distance_km / 100)
        if self._fuel_in_tank < fuel_needed - 1e-9:
            raise ValueError(self.ERR_INSUFFICIENT_FUEL)
        self._fuel_in_tank -= fuel_needed
        return self._fuel_in_tank
