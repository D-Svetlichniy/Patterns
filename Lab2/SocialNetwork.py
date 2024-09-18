from abc import ABC, abstractmethod


class SocialNetwork(ABC):  #Інтерфейс для соціальних мереж

    @abstractmethod
    def authenticate(self, **credentials):
        pass

    @abstractmethod
    def post_message(self, message: str):
        pass
