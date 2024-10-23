# Створюємо оновлювач для товару
from Lab8.OrderUpdater import OrderUpdater
from Lab8.ProductUpdater import ProductUpdater
from Lab8.UserUpdater import UserUpdater

product_updater = ProductUpdater()
response = product_updater.update()
print(response)

# Створюємо оновлювач для користувача
user_updater = UserUpdater()
response = user_updater.update()
print(response)

# Створюємо оновлювач для замовлення
order_updater = OrderUpdater()
response = order_updater.update()
print(response)
