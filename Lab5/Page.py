from abc import ABC, abstractmethod
from Lab5.Renderer import Renderer
class Page(ABC):  # Інтерфейс сторінки
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self) -> str:
        pass
