from Lab2.SocialNetwork import SocialNetwork


class Facebook(SocialNetwork):  #Клас для Facebook, реалізує методи для аутентифікації та публікації

    def authenticate(self, login: str, password: str):
        # Аутентифікація через логін та пароль
        print(f"Authenticating on Facebook as {login}")

    def post_message(self, message: str):
        # Публікація
        print(f"Posting message on Facebook: {message}")
