from Lab4.Notification import Notification


class SlackNotificationAdapter(Notification):  # Адаптер для Slack
    def __init__(self, slack_service):
        self.slack_service = slack_service

    def send(self, title: str, message: str) -> None:
        # Адаптуємо методи під Slack
        self.slack_service.login()
        self.slack_service.send_message(title, message)


# Slack сервіс
class SlackService:
    def __init__(self, user_login: str, api_key: str, chat_id: str):
        self.user_login = user_login  # Змінив назву змінної на user_login
        self.api_key = api_key
        self.chat_id = chat_id

    def login(self) -> None:
        # Імітація авторизації в Slack
        print(f"Logged into Slack with login '{self.user_login}' and apiKey '{self.api_key}'")

    def send_message(self, title: str, message: str) -> None:
        # Імітація відправки повідомлення в Slack
        print(f"Sent Slack message to chat '{self.chat_id}' with title '{title}' that says '{message}'")

