from Lab10.DatePicker import DatePicker
from Lab10.Mediator import OrderPageMediator
from Lab10.ReceiverCheckbox import ReceiverCheckbox
from Lab10.SelfPickupCheckbox import SelfPickupCheckbox
from Lab10.TextField import TextField
from Lab10.TimePicker import TimePicker

date_picker = DatePicker()
time_picker = TimePicker()
receiver_checkbox = ReceiverCheckbox()
name_field = TextField()
phone_field = TextField()
self_pickup_checkbox = SelfPickupCheckbox()

# Створення посередника та передача йому компонентів
mediator = OrderPageMediator(date_picker, time_picker, receiver_checkbox, name_field, phone_field, self_pickup_checkbox)

# Взаємодії
date_picker.select_date("2024-11-15")
receiver_checkbox.toggle()
self_pickup_checkbox.toggle()
