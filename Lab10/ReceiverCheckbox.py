from Lab10.Component import Component


class ReceiverCheckbox(Component):
    def __init__(self):
        super().__init__()
        self.checked = False

    def toggle(self):
        self.checked = not self.checked
        print(f"Отримувач інша особа: {'так' if self.checked else 'ні'}")
        self.mediator.notify(self, "checkbox_changed")
