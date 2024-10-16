from Lab7.DeliveryStrategy import DeliveryStrategy


# Стратегія власної служби доставки
class InternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, distance: float) -> float:
        return 5.0 + distance * 1.5  # Фіксована сума + залежить від відстані
