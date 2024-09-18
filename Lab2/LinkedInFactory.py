from Lab2.LinkedIn import LinkedIn
from Lab2.SocialNetworkFactory import SocialNetworkFactory
from Lab2.SocialNetwork import SocialNetwork

class LinkedInFactory(SocialNetworkFactory): # Фабрика для LinkedIn

    def create_network(self) -> SocialNetwork:
        return LinkedIn()
