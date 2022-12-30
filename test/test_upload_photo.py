import sys
from os.path import join, dirname
import pytest


sys.path.insert(0, join(dirname(dirname(__file__)), "src"))

from InstagramBot import InstagramBot
from Credentials import Credentials

class TestUploadPhoto:
    instagram_bot = None
    @pytest.fixture(autouse=True)
    def setup(self):
        username, password = Credentials().get_credentials()
        self.instagram_bot = InstagramBot(username, password)
        self.instagram_bot.run_browser()
        self.instagram_bot.accept_cookies()
        self.instagram_bot.login()
        
    def test_open_upload_photo_page(self):
        assert self.instagram_bot.open_upload_page() == True