from Lab5.HTMLRenderer import HTMLRenderer
from Lab5.JsonRenderer import JsonRenderer
from Lab5.Product import Product
from Lab5.ProductPage import ProductPage
from Lab5.SimplePage import SimplePage
from Lab5.XmlRenderer import XmlRenderer


def client_code():
    # Створення продукту
    product = Product(1, "Example Product", "This is an example product.", "image_url.png")

    # Створення простої сторінки з HTML рендером
    simple_page = SimplePage("Simple Page Title", "This is some simple content.", HTMLRenderer())
    print(simple_page.render())

    # Створення сторінки продукту з JSON рендером
    product_page_json = ProductPage(product, JsonRenderer())
    print(product_page_json.render())

    # Створення сторінки продукту з XML рендером
    product_page_xml = ProductPage(product, XmlRenderer())
    print(product_page_xml.render())

client_code()
