from Lab5.Page import Page
from Lab5.Renderer import Renderer


class SimplePage(Page):  # Проста сторінка
    def __init__(self, title: str, content: str, renderer: Renderer):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        return f"Title: {self.title}\nContent: {self.content}\nRendered: {self.renderer.render()}"
