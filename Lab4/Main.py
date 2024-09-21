# Клієнтський код
from Lab4.EmailNotification import EmailNotification
from Lab4.SMSNotificationAdapter import SMSService, SMSNotificationAdapter
from Lab4.SlackNotificationAdapter import SlackService, SlackNotificationAdapter

# Відправка email-повідомлення
email_notification = EmailNotification("admin@example.com")
email_notification.send("System Alert", "This is an email notification.")

# Відправка повідомлення у Slack через адаптер
slack_service = SlackService("userLogin", "apiKey123", "chat123")
slack_notification = SlackNotificationAdapter(slack_service)
slack_notification.send("System Alert", "This is a Slack notification.")

# Відправка SMS через адаптер
sms_service = SMSService("+123456789", "MyCompany")
sms_notification = SMSNotificationAdapter(sms_service)
sms_notification.send("System Alert", "This is an SMS notification.")
