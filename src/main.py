from InstagramBot import InstagramBot
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def create_webdriver():
  browser_options = Options()
  #browser_options.add_argument("--headless")
  browser = webdriver.Firefox(options=browser_options)
  return browser

def main():
  username = input("User: ")
  password = ""
  while len(password) < 6:
    password = input("Password: ")
  browser = create_webdriver()
  bot = InstagramBot(username, password, browser)
  bot.run_browser()
  bot.accept_cookies()
  while not bot.login():
    pass
  #bot.get_followers_number()
  bot.follow_followers()
  #bot.follow_user()
  #bot.take_screenshot()
  bot.close_browser()

main()

# TODO:
  # Mirar si ya se está siguiendo al usuario
  # Comprobar que el input es correcto para seguir al usuario
  # Seguir a todos los usuarios que siguen a un usuario
  # Subir una foto