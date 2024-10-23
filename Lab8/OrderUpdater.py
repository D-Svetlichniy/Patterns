from Lab8.EntityUpdater import EntityUpdater


class OrderUpdater(EntityUpdater):
    def get_entity(self):
        return "Order"

    def validate(self, entity):
        return True

    def save(self, entity):
        print("Saving order")

    def format_response(self, entity):
        # Додаємо JSON-подання замовлення у відповідь
        return {
            "status": "success",
            "code": 200,
            "order": {"id": 1, "status": "confirmed"}  # Приклад JSON
        }
