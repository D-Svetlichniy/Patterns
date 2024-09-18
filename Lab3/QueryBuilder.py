from abc import ABC, abstractmethod


class QueryBuilder(ABC):  # Інтерфейс будівельника запитів

    @abstractmethod
    def select(self, table: str, columns: list):
        pass

    @abstractmethod
    def where(self, condition: str):
        pass

    @abstractmethod
    def limit(self, limit: int):
        pass

    @abstractmethod
    def getSQL(self) -> str:
        pass
