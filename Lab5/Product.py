class Product:   # Клас для продукту
    def __init__(self, product_id: int, name: str, description: str, image: str):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.image = image
