from Lab10.Component import Component


class SelfPickupCheckbox(Component):
    def __init__(self):
        super().__init__()
        self.checked = False

    def toggle(self):
        self.checked = not self.checked
        print(f"Самовивіз: {'так' if self.checked else 'ні'}")
        self.mediator.notify(self, "checkbox_changed")
