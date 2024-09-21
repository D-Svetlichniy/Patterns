from Lab4.Notification import Notification


class EmailNotification(Notification):  # Реалізація EmailNotification
    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        # Імітація відправки email
        print(f"Sent email with title '{title}' to '{self.admin_email}' that says '{message}'")
