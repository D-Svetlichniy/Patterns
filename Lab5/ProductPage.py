from Lab5.Page import Page
from Lab5.Product import Product
from Lab5.Renderer import Renderer


class ProductPage(Page):   # Сторінка товару
    def __init__(self, product: Product, renderer: Renderer):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        return (f"Product ID: {self.product.product_id}\n"
                f"Name: {self.product.name}\n"
                f"Description: {self.product.description}\n"
                f"Image: {self.product.image}\n"
                f"Rendered: {self.renderer.render()}")