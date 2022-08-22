from time import sleep
from selenium.webdriver.common.by import By

class InstagramBot:
  def __init__(self, username, password, browser):
    self.username = username
    self.password = password
    self.browser = browser
  def run_browser(self):
    self.browser.implicitly_wait(5)
    self.browser.get('https://www.instagram.com/')
  def login(self):
    username_input = self.browser.find_element(By.XPATH, '//input[@name="username"]')
    password_input = self.browser.find_element(By.XPATH,'//input[@name="password"]')
    username_input.send_keys(self.username)
    password_input.send_keys(self.password)
    sleep(1)
    login_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
    login_button.click()
    print("You are logged in")
  def accept_cookies(self):
    cookies_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
    cookies_button.click()
    print("Cookies accepted")
  def close_browser(self):
    sleep(3)
    self.browser.close()
    print("Browser closed")
  def take_screenshot(self):
    sleep(2)
    self.browser.save_screenshot('screenshot.png')
    print("Screenshot taken")
  def follow_user(self):
    user = input("Enter the user you want to follow: ")
    self.browser.get('https://www.instagram.com/' + user)
    sleep(2)
    follow_button = self.browser.find_element(By.XPATH, '//div[text()="Seguir"]')
    follow_button.click()
    print("You are following " + user)