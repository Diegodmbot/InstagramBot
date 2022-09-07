from InstagramBot import InstagramBot
from selenium.webdriver.firefox.options import Options
from time import sleep
import os

def create_webdriver(headless):
  browser_options = Options()
  if headless:
    browser_options.add_argument("--headless")
  browser = webdriver.Firefox(options=browser_options)
  return browser

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
  # MENU
  while True:
    print("MENU " + bot.username.upper())
    print("1. Follow user")
    print("2. Take screenshot")
    print("3. Follow my followers")
    print("4. Get followers number")
    print("5. Unfollow user")
    print("6. Upload photo")
    print("7. Exit")
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
      user = input("User: ")
      if bot.unfollow_user(user) == False:
        print("Cannot unfollow user")
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

main()

# TODO:
  # Cuando se hace login se puede guardar la sesión para no tener que loguearse cada vez
  # Métele un NLP para que analice los comentarios y los blauee o les de a like dependiendo de si son buenos o malos