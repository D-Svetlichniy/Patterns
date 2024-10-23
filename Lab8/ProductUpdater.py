from Lab8.EntityUpdater import EntityUpdater


class ProductUpdater(EntityUpdater):
    def get_entity(self):
        return "Product"

    def validate(self, entity):
        # Наприклад, валідація провалена
        return False

    def save(self, entity):
        print("Saving product")

    def format_response(self, entity):
        return {"status": "success", "code": 200}

    def handle_validation_failure(self):
        # Адміністратор отримує сповіщення
        print("Admin notified via messenger")
