class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        if fuel_quantity <= 0:
            raise ValueError("Количество топлива должно быть положительным")
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise ValueError("Вы пытаетесь залить слишком много бензина!")
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        if distance_km <= 0:
            raise ValueError("Дистанция должна быть положительной")
        # Расход 8 литров на 100 км
        fuel_burned = 8 * (distance_km / 100)
        if self._fuel_in_tank < fuel_burned:
            raise ValueError("Не доедем жеж...")
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
