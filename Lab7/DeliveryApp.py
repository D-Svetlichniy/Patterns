from Lab7.DeliveryStrategy import DeliveryStrategy


# Контекст — додаток для доставки
class DeliveryApp:
    def __init__(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def calculate_delivery_cost(self, distance: float) -> float:
        return self._strategy.calculate_cost(distance)