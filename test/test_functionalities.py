import pytest
import sys
from os.path import join, dirname

sys.path.insert(0, join(dirname(dirname(__file__)), "src"))

from InstagramBot import InstagramBot
from Credentials import Credentials

class TestFunctionalities:
    
    instagram_bot = None
    @pytest.fixture(autouse=True)
    def setup(self):
        username, password = Credentials().get_credentials()
        self.instagram_bot = InstagramBot(username, password)
        self.instagram_bot.run_browser()
        self.instagram_bot.accept_cookies()
        self.instagram_bot.login()
    
    def test_sample(self):
        assert 1 == 1
        
    def test_close_browser(self):
        assert self.instagram_bot.close_browser() == True
        
    def test_take_screenshot(self):
        assert self.instagram_bot.take_screenshot("test_screenshot") == True
        
    def test_scroll_(self):
        scroll_box = self.instagram_bot.browser.find_element_by_xpath("/html")
        assert self.instagram_bot.scroll_down(scroll_box) == True
        
    
    