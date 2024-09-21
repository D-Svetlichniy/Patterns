from Lab4.Notification import Notification


class SMSNotificationAdapter(Notification):  # Адаптер для SMS
    def __init__(self, sms_service):
        self.sms_service = sms_service

    def send(self, title: str, message: str) -> None:
        # Адаптуємо методи під SMS
        self.sms_service.send_sms(title, message)


# SMS сервіс
class SMSService:
    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender

    def send_sms(self, title: str, message: str) -> None:
        # Імітація відправки SMS
        print(f"Sent SMS to {self.phone} from {self.sender} with title '{title}' that says '{message}'")
