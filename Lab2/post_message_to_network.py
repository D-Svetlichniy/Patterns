from Lab2 import SocialNetworkFactory


def post_message_to_network(factory: SocialNetworkFactory, credentials: dict, message: str):
    network = factory.create_network()
    # Аутентифікація в мережі
    network.authenticate(**credentials)
    # Публікація повідомлення
    network.post_message(message)
