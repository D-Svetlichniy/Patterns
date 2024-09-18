from abc import ABC, abstractmethod
from Lab2 import SocialNetwork


class SocialNetworkFactory(ABC): # Фабрика соціальних мереж

    @abstractmethod
    def create_network(self) -> SocialNetwork:  # Абстрактний метод, який повертає об'єкт, що реалізує інтерфейс SocialNetwork
        pass