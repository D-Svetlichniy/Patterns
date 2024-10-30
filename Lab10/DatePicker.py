from Lab10.Component import Component


class DatePicker(Component):
    def select_date(self, date):
        print(f"Дата обрана: {date}")
        self.mediator.notify(self, "date_selected")
