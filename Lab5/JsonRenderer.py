from Lab5.Renderer import Renderer


class JsonRenderer(Renderer):  # JSON рендерер
    def render(self) -> str:
        # Рендеринг в JSON
        return '{"message": "Rendered in JSON"}'