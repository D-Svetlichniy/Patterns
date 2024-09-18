from Lab2.Facebook import Facebook
from Lab2.SocialNetworkFactory import SocialNetworkFactory
from Lab2.SocialNetwork import SocialNetwork


class FacebookFactory(SocialNetworkFactory):  # Фабрика для Facebook

    def create_network(self) -> SocialNetwork:
        return Facebook()
