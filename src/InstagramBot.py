from time import sleep
from selenium.webdriver.common.by import By

class InstagramBot:
  def __init__(self, username, password, browser):
    self.username = username
    self.password = password
    self.browser = browser
  def set_password(self):
    while len(self.password) < 6:
      self.password = input("Password: ")
  def run_browser(self):
    self.browser.implicitly_wait(5)
    self.browser.get('https://www.instagram.com/')
  def login(self):
    username_input = self.browser.find_element(By.XPATH, '//input[@name="username"]')
    password_input = self.browser.find_element(By.XPATH,'//input[@name="password"]')
    username_input.send_keys(self.username)
    password_input.send_keys(self.password)
    sleep(1.5)
    login_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
    login_button.click()
    sleep(3)
    # Si el boton de login no está visible es que se ha iniciado sesión y salta la excepción
    # si no el login ha fallado y se vuelve a intentar
    try: 
      self.browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
      username_input.clear()
      password_input.clear()
      print("Wrong username or password")
      self.username = input("User: ")
      self.password = ""
      self.set_password()
      return False
    except:
      print("You are logged in")
      return True
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
    follow_button = self.browser.find_element(By.XPATH, '//div[text()="Seguir"]')
    follow_button.click()
    print("You are following " + user)
    return True
  # Pasos:
  # 1. Ir a la página de seguidores del usuario
  # 2. Scroll hasta el final de la página
  # 3. Obtener los seguidores de la página y guardarlos en un array
  # 4. Seguir a los seguidores
  def follow_followers(self):
    self.browser.get('https://www.instagram.com/' + self.username + '/followers')
    sleep(2)
    followers = []
    while True:
      followers_list = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/span/a/span/div')
      print(followers_list.text)
      # for follower in followers_list:
      #   followers.append(follower.text)
      #   print(follower.text)
      sleep(2)
      self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      sleep(2)
      try:
        self.browser.find_element(By.XPATH, '//a[@href="/' + self.username + '/followers/"]')
        break
      except:
        pass
    #followers_list = self.browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]')
    # Dos XPATH para obtener los usuarios 
    #/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/span/a/span/div
    # el href dentro de la etiqueta a es el nombre de usuario
    #/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/span/a
    #---
    #/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/span/a/span/div

    #followers = followers_list.find_elements(By.TAG_NAME, 'li')
    #print(followers)
  def get_followers_number(self):

    self.browser.get('https://www.instagram.com/' + self.username + '/followers')
    sleep(2)
    followers_list = self.browser.find_elements(By.XPATH, '//a[@href="/' + self.username + '/followers/"]')
    print("Followers: " + followers_list[0].text)