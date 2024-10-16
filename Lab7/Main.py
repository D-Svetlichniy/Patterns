from Lab7.DeliveryApp import DeliveryApp
from Lab7.ExternalDeliveryStrategy import ExternalDeliveryStrategy
from Lab7.InternalDeliveryStrategy import InternalDeliveryStrategy
from Lab7.PickupStrategy import PickupStrategy

if __name__ == "__main__":

    distance = 15  # Відстань у кілометрах

    # Використання стратегії самовивозу
    app = DeliveryApp(PickupStrategy())
    print(f"Вартість самовивозу: {app.calculate_delivery_cost(distance)}")

    # Використання стратегії зовнішньої служби доставки
    app.set_strategy(ExternalDeliveryStrategy())
    print(f"Вартість доставки зовнішньою службою: {app.calculate_delivery_cost(distance)}")

    # Використання стратегії власної служби доставки
    app.set_strategy(InternalDeliveryStrategy())
    print(f"Вартість доставки власною службою: {app.calculate_delivery_cost(distance)}")