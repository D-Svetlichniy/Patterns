from Lab7.DeliveryStrategy import DeliveryStrategy


# Стратегія самовивозу
class PickupStrategy(DeliveryStrategy):
    def calculate_cost(self, distance: float) -> float:
        return 0.0  # Самовивіз безкоштовний
