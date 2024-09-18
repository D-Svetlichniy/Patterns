from Lab2.SocialNetwork import SocialNetwork


class LinkedIn(SocialNetwork):  #Клас для LinkedIn, реалізує методи для аутентифікації та публікації

    def authenticate(self, email: str, password: str):
        # Аутентифікація через email та пароль
        print(f"Authenticating on LinkedIn with email {email}")

    def post_message(self, message: str):
        # Публікація
        print(f"Posting message on LinkedIn: {message}")
