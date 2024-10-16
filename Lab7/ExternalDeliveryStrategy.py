from Lab7.DeliveryStrategy import DeliveryStrategy


# Стратегія зовнішньої служби доставки
class ExternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, distance: float) -> float:
        return 10.0 + distance * 2  # Фіксована сума + залежить від відстані
