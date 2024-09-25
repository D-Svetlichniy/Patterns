from abc import ABC, abstractmethod

class Renderer(ABC):  # Інтерфейс рендерера
    @abstractmethod
    def render(self) -> str:
        pass
