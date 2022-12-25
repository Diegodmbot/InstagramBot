from InstagramBot import InstagramBot
from FileManager import FileManager
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from getpass import getpass
from time import sleep
from datetime import date, datetime
import os

EMOJI_BOT = "🤖"


def clear_console():
    # Use cls when running on Windows
    os.system("clear" if os.name == "posix" else "cls")


def create_webdriver(headless):
    browser_options = Options()
    if headless:
        browser_options.add_argument("--headless")
    browser = webdriver.Firefox(options=browser_options)
    return browser


def get_week_of_the_year():
    return date.today().isocalendar()[1]


def menu(bot):
    filemanager = FileManager()
    while True:
        print("MENU " + bot.username.upper())
        print("1. Take screenshot")
        print("2. Get followers number")
        print("3. Get following number")
        print("4. Follow user")
        print("5. Unfollow user")
        print("6. Follow only my followers")
        print("7. Upload photo")
        print("8. Exit")
        option = input("Option: ")
        clear_console()
        if option == "1":
            screenshot_name = input("Screenshot name: ")
            bot.take_screenshot(screenshot_name)
        elif option == "2":
            print("Número de seguidores: " + str(bot.get_followers_number()))
        elif option == "3":
            print("Número de seguidos: " + str(bot.get_following_number()))
        elif option == "4":
            user = input("User: ")
            if bot.follow_user(user) == True:
                print("User: @" + user + " followed")
            else:
                print("Cannot follow user")
        elif option == "5":
            user = input("User: ")
            if bot.unfollow_user(user) == True:
                print("User: @" + user + " unfollowed")
            else:
                print("Cannot unfollow user")
        elif option == "6":
            if bot.follow_all_followers() == True:
                print("You are following only your followers")
            else:
                print("Error ocurred")
        elif option == "7":
            photos_name = filemanager.get_photos_name()
            caption = EMOJI_BOT + "Semana " + \
                str(get_week_of_the_year()) + " de " + \
                str(datetime.now().year) + EMOJI_BOT
            if bot.upload_photo(photos_name, caption) == True:
                print("Photo uploaded")
                filemanager.remove_photos(photos_name)
            else:
                print("Cannot upload photo")
        elif option == "8":
            bot.close_browser()
            break
        else:
            print("Invalid option")
        input("Press enter to continue...")
        clear_console()


def main():
    clear_console()
    username = input("User: ")
    password = getpass("Password: ")
    headless_flag = input("Headless mode? (y/n): ")
    browser = create_webdriver(headless_flag == "y")
    bot = InstagramBot(username, password, browser)
    bot.run_browser()
    bot.accept_cookies()
    while not bot.login():
        pass
    clear_console()
    menu(bot)


main()
