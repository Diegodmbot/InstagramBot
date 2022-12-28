from InstagramBot import InstagramBot
from Credentials import get_credentials


class TestBot:
    username, password = get_credentials()
    browser = None
    instagram_bot = InstagramBot(username, password, browser)

    def test_login(self):
        assert self.instagram_bot.login() == True
