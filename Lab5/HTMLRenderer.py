from Lab5.Renderer import Renderer


class HTMLRenderer(Renderer):    # HTML рендерер
    def render(self) -> str:
        # Рендеринг в HTML
        return "<html><body>Rendered in HTML</body></html>"
