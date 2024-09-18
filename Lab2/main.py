from Lab2.FacebookFactory import FacebookFactory
from Lab2.LinkedInFactory import LinkedInFactory
from Lab2.post_message_to_network import post_message_to_network

# Публікація на Facebook
facebook_factory = FacebookFactory()
facebook_credentials = {'login': 'user_facebook', 'password': 'facebook_pass'}
post_message_to_network(facebook_factory, facebook_credentials, "Hello, Facebook!")

# Публікація на LinkedIn
linkedin_factory = LinkedInFactory()
linkedin_credentials = {'email': 'user_linkedin@example.com', 'password': 'linkedin_pass'}
post_message_to_network(linkedin_factory, linkedin_credentials, "Hello, LinkedIn!")
