from InstagramBot import InstagramBot
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import os

def create_webdriver(headless):
  browser_options = Options()
  if headless:
    browser_options.add_argument("--headless")
  browser = webdriver.Firefox(options=browser_options)
  return browser

def menu(bot):
  while True:
    print("MENU " + bot.username.upper())
    print("1. Take screenshot")
    print("2. Get followers number")
    print("3. Follow user")
    print("4. Unfollow user")
    print("5. Follow my followers")
    print("6. Upload photo")
    print("7. Exit")
    option = input("Option: ")
    if option == "1":
      screenshot_name = input("Screenshot name: ")
      bot.take_screenshot(screenshot_name)
    elif option == "2":
      print("Número de seguidores: " + str(bot.get_followers_number()))
    elif option == "3":
      user = input("User: ")
      if bot.follow_user(user) == True:
        print("User: @" + user + " followed")
      else:
        print("Cannot follow user")
    elif option == "4":
      user = input("User: ")
      if bot.unfollow_user(user) == True:
        print("User: @" + user + " unfollowed")
      else:
        print("Cannot unfollow user")
    elif option == "5":
      if bot.follow_followers() == True:
        print("Followed all your followers")
      else:
        print("Error ocurred")
    elif option == "6":
      photo_name = input("Photo name: ")
      caption = input("Caption: ")
      if bot.upload_photo(photo_name, caption) == True:
        print("Photo uploaded")
      else:
        print("Cannot upload photo")
    elif option == "7":
      bot.close_browser()
      break
    else:
      print("Invalid option")
    sleep(3)
    os.system("cls")

def main():
  os.system("cls")
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
  menu(bot)
  

main()

# TODO:
  # Cuando se hace login se puede guardar la sesión para no tener que loguearse cada vez
  # Script para eliminar las fotos de un directorio local
  # darle forma a todo el código