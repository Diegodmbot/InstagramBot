from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class Bot:
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
  def accept_coockies(self):
    cookies_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]')
    cookies_button.click()
    print("Cookies accepted")
  def take_screenshot(self):
    sleep(2)
    self.browser.save_screenshot('screenshot.png')
    print("Screenshot taken")
  def close_browser(self):
    sleep(3)
    self.browser.close()
    print("Browser closed")
  def follow_user(self):
    user = input("Enter the user you want to follow: ")
    self.browser.get('https://www.instagram.com/' + user)
    sleep(2)
    follow_button = self.browser.find_element(By.XPATH, '//div[text()="Seguir"]')
    follow_button.click()
    print("You are following " + user)

def set_browser_options():
  browser_options = Options()
  browser_options.add_argument("--headless")
  browser = webdriver.Firefox(options=browser_options)
  return browser

def main():
  username = input("User: ")
  password = input("Password: ")
  browser = set_browser_options()
  bot = Bot(username, password, browser)
  bot.run_browser()
  bot.accept_coockies()
  bot.login()
  bot.follow_user()
  bot.take_screenshot()
  bot.close_browser()

main()

# TODO:
  # Mirar si ya se está siguiendo al usuario
  # Comprobar que el input es correcto para seguir al usuario