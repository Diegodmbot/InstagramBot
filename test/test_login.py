import sys
from os.path import join, dirname
import pytest


sys.path.insert(0, join(dirname(dirname(__file__)), "src"))

from InstagramBot import InstagramBot
from Credentials import Credentials

class TestLogin:
    username, password = Credentials().get_credentials()
    instagram_bot = InstagramBot(username, password)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.instagram_bot.run_browser()

    def test_sample(self):
        assert 1 == 1
        
    def test_accept_cookies(self):
        assert self.instagram_bot.accept_cookies() == True
        
    def test_login(self):
        self.instagram_bot.accept_cookies()
        assert self.instagram_bot.login() == True
        

    # Hay que testar save_loggin y not_aceppt_notifications pero creo que hace
    # falta usar mock para ello
