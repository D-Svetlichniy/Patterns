from abc import ABC, abstractmethod

# Інтерфейс Посередника
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Реалізація Посередника для сторінки оформлення замовлення
class OrderPageMediator(Mediator):
    def __init__(self, date_picker, time_picker, receiver_checkbox, name_field, phone_field, self_pickup_checkbox):
        self.date_picker = date_picker
        self.time_picker = time_picker
        self.receiver_checkbox = receiver_checkbox
        self.name_field = name_field
        self.phone_field = phone_field
        self.self_pickup_checkbox = self_pickup_checkbox

        # Встановлення посередника для кожного компонента
        self.date_picker.mediator = self
        self.receiver_checkbox.mediator = self
        self.self_pickup_checkbox.mediator = self

    def notify(self, sender, event):
        if sender == self.date_picker and event == "date_selected":
            self.update_time_slots()
        elif sender == self.receiver_checkbox and event == "checkbox_changed":
            self.toggle_receiver_fields()
        elif sender == self.self_pickup_checkbox and event == "checkbox_changed":
            self.toggle_delivery_fields()

    def update_time_slots(self):
        # Оновлення часових проміжків залежно від дати
        print("Часові проміжки оновлено залежно від дати")

    def toggle_receiver_fields(self):
        # Ввімкнення/вимкнення полів Ім'я та Телефон
        if self.receiver_checkbox.checked:
            self.name_field.active = True
            self.phone_field.active = True
        else:
            self.name_field.active = False
            self.phone_field.active = False
        print("Поля отримувача оновлені")

    def toggle_delivery_fields(self):
        # Ввімкнення/вимкнення полів доставки
        if self.self_pickup_checkbox.checked:
            self.date_picker.active = False
            self.time_picker.active = False
            self.receiver_checkbox.active = False
            self.name_field.active = False
            self.phone_field.active = False
        else:
            self.date_picker.active = True
            self.time_picker.active = True
            self.receiver_checkbox.active = True
            print("Поля доставки активовані")
