from abc import ABC, abstractmethod


class EntityUpdater(ABC):
    def update(self):
        entity = self.get_entity()
        if self.validate(entity):
            self.save(entity)
            return self.format_response(entity)
        else:
            self.handle_validation_failure()
            return {"status": "error", "code": 400}

    @abstractmethod
    def get_entity(self):
        """Отримати сутність, яку потрібно оновити"""
        pass

    @abstractmethod
    def validate(self, entity):
        """Валідація сутності"""
        pass

    @abstractmethod
    def save(self, entity):
        """Зберегти оновлену сутність"""
        pass

    @abstractmethod
    def format_response(self, entity):
        """Формування відповіді"""
        pass

    def handle_validation_failure(self):
        """Обробка невдалої валідації"""
        pass
