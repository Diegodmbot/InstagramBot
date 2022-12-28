
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class BrowserManager:
    def __init__(self):
        self.browser_options = Options()
        self.set_headles_mode()
        self.browser = webdriver.Firefox(options=self.browser_options)
        self.browser.implicitly_wait(10)

    def access_url(self, url):
        self.browser.get(url)

    def get_browser(self):
        return self.browser

    # set options to browser
    def set_headles_mode(self):
        self.browser_options.add_argument("--headless")

    # find element by xpath and interact with it
    def find_element_by_xpath(self, element):
        return self.browser.find_element(By.XPATH, element)

    def click_element(self, element):
        self.browser.find_element(By.XPATH, element).click()

    def send_key_to_element(self, element, key):
        self.browser.find_element(By.XPATH, element).send_keys(key)

    # run a script in the browser
    def run_script(self, script, element):
        self.browser.execute_script(script, element)

    def close_browser(self):
        self.browser.close()
