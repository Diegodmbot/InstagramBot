from InstagramBot import InstagramBot
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

def create_webdriver(headless):
  browser_options = Options()
  if headless:
    browser_options.add_argument("--headless")
  browser = webdriver.Firefox(options=browser_options)
  return browser

def main():
  username = input("User: ")
  password = ""
  while len(password) < 6:
    password = input("Password: ")
  headless_flag = input("Headless mode? (y/n): ")
  browser = create_webdriver(headless_flag == "y")
  bot = InstagramBot(username, password, browser)
  bot.run_browser()
  bot.accept_cookies()
  while not bot.login():
    pass
  os.system("cls")
  # MENU
  while True:
    print("MENU " + bot.username.upper())
    print("1. Follow user")
    print("2. Take screenshot")
    print("3. Follow my followers")
    print("4. Get followers number")
    print("5. Exit")
    option = input("Option: ")
    if option == "1":
      user = input("User: ")
      if bot.follow_user(user) == False:
        print("Cannot follow user")
    elif option == "2":
      screenshot_name = input("Name of the screenshot: ")
      bot.take_screenshot(screenshot_name)
    elif option == "3":
      if bot.follow_followers() == False:
        print("Cannot follow followers")
    elif option == "4":
      print("Número de seguidores: " + str(bot.get_followers_number()))
    elif option == "5":
      bot.close_browser()
      break
    else:
      print("Invalid option")

main()

# TODO:
  # Subir una foto