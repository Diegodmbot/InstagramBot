import pytest
import sys
from os.path import join, dirname

sys.path.insert(0, join(dirname(dirname(__file__)), "src"))

from InstagramBot import InstagramBot
from Credentials import Credentials

class TestGetters:
    instagram_bot = None
    @pytest.fixture(autouse=True)
    def setup(self):
        username, password = Credentials().get_credentials()
        self.instagram_bot = InstagramBot(username, password)
        self.instagram_bot.run_browser()
        self.instagram_bot.accept_cookies()
        self.instagram_bot.login()
    
    def test_get_followers_number(self):
        assert self.instagram_bot.get_followers_number() > 0
        
    def test_get_following_number(self):
        assert self.instagram_bot.get_following_number() > 0 
        
    def test_get_followers(self):
        assert self.instagram_bot.get_followers() != []
        
    def test_get_following(self):
        assert self.instagram_bot.get_following() != []