from Lab8.EntityUpdater import EntityUpdater


class UserUpdater(EntityUpdater):
    def get_entity(self):
        return "User"

    def validate(self, entity):
        # Забороняємо змінювати email, незважаючи на валідацію
        return True

    def save(self, entity):
        print("Saving user")

    def format_response(self, entity):
        return {"status": "success", "code": 200}
