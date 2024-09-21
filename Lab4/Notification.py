from abc import ABC, abstractmethod

class Notification(ABC):  # Інтерфейс Notification
    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass
