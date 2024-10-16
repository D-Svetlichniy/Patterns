from abc import ABC, abstractmethod

# Інтерфейс Стратегії
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, distance: float) -> float:
        pass
