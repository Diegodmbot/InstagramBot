from InstagramBot import InstagramBot
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def create_webdriver():
  browser_options = Options()
  browser_options.add_argument("--headless")
  browser = webdriver.Firefox(options=browser_options)
  return browser

def main():
  username = input("User: ")
  password = input("Password: ")
  browser = create_webdriver()
  bot = InstagramBot(username, password, browser)
  bot.run_browser()
  bot.accept_cookies()
  bot.login()
  bot.follow_user()
  bot.take_screenshot()
  bot.close_browser()

main()

# TODO:
  # Comprobar que se inicia sesión
  # Mirar si ya se está siguiendo al usuario
  # Comprobar que el input es correcto para seguir al usuario