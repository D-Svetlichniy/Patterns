from Lab5.Renderer import Renderer


class XmlRenderer(Renderer):  # XML рендерер
    def render(self) -> str:
        # Рендеринг в XML
        return "<message>Rendered in XML</message>"