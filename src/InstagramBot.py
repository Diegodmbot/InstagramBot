from time import sleep
from selenium.webdriver.common.by import By
import os

class InstagramBot:
  def __init__(self, username, password, browser):
    self.username = username
    self.password = password
    self.browser = browser
  def run_browser(self):
    self.browser.implicitly_wait(10)
    self.browser.get('https://www.instagram.com/')
  # Iniciar sesión
  def login(self):
    username_input = self.browser.find_element(By.XPATH, '//input[@name="username"]')
    password_input = self.browser.find_element(By.XPATH,'//input[@name="password"]')
    username_input.send_keys(self.username)
    password_input.send_keys(self.password)
    sleep(1.5)
    self.browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
    # El tiempo de este sleep es importante, si es muy corto no se loguea
    sleep(2)
    while self.is_not_logged():
      sleep(1)
    print("You are logged in")
    self.save_login()
    self.not_aceppt_notifications()
    return True
  def is_not_logged(self):
    try:
      self.browser.find_element(By.XPATH, '//input[@name="username"]')
      return True
    except:
      return False
  # Aceptar cookies (Solo las necesarias)
  def accept_cookies(self):
    self.browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
    print("Cookies accepted")
  # Guarda información de la sesión para que no se tenga que loguear cada vez
  def save_login(self):
    self.browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/section/div/button').click()
  def not_aceppt_notifications(self):
    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
  # Cerrar el navegador
  def close_browser(self):
    sleep(3)
    self.browser.close()
    print("Browser closed")
  # Tomar captura de pantalla
  def take_screenshot(self, screenshot_name):
    sleep(2)
    self.browser.save_screenshot(screenshot_name + '.png')
    print("Screenshot taken")
    return True
  # Devuelve el número de followers
  def get_followers_number(self):
    self.browser.get('https://www.instagram.com/' + self.username + '/followers')
    sleep(2)
    followers_list = self.browser.find_elements(By.XPATH, '//a[@href="/' + self.username + '/followers/"]')
    return int(followers_list[0].text.split(' ')[0])
  # Seguir a un usuario introduciendo su nombre
  def follow_user(self, user):
    self.browser.get('https://www.instagram.com/' + user)
    try:
      self.browser.find_element(By.XPATH, '//div[text()="Seguir"]').click()
      print("You are following " + user)
      return True
    except:
      return False
  # Seguir a un usuario que ya te sigue
  def follow_user_following(self, follower):
    self.browser.get('https://www.instagram.com/' + follower)
    try:
      self.browser.find_element(By.XPATH, '//div[text()="Seguir también"]').click()
      try:
        self.browser.find_element(By.XPATH, '//div[text()="Restringimos determinada actividad para proteger a nuestra comunidad."]')
        return False
      except:
        print("You are following " + follower)
    except:
        return False
    sleep(2)
    return True
  # seguir a los seguidores de un usuario
  def follow_all_followers(self):
    number_of_followers = self.get_followers_number()
    self.browser.get('https://www.instagram.com/' + self.username + '/followers')
    sleep(2)
    self.scroll_down()
    # Guarda a los followers en un array
    followers = []
    j = 1
    while j < number_of_followers:
      followers_list = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[' + str(j) +']/div[2]/div[1]/div/div/span/a/span/div')
      followers.append(followers_list.text)
      j += 1
    # Seguir a los followers
    for follower in followers:
      if self.follow_user_following(follower) == False: 
        break
    return True
  def unfollow_user(self, user):
    self.browser.get('https://www.instagram.com/' + user)
    try:
      self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button').click()
      sleep(1)
      self.browser.find_element(By.XPATH, '//button[text()="Dejar de seguir"]').click()
      print("You are not following " + user)
      return True
    except:
      return False
  # https://medium.com/jacklee26/selenium-instagram-followers-and-following-list-52c335a4ec03
  def scroll_down(self):
    scroll_box = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
    last_ht, ht = 0, 1
    print("Scrolling...")
    while last_ht != ht:
      last_ht = ht
      sleep(2)
      # script en js para hacer scroll
      ht = self.browser.execute_script(""" 
      arguments[0].scrollTo(0, arguments[0].scrollHeight);
      return arguments[0].scrollHeight; """, scroll_box)
    sleep(1)
    return True
  # Subir fotos con el formato 1:1 de una carpeta
  def upload_photo(self, photo_name, caption):
    sleep(2)
    self.browser.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
    # Seleccionar la imagen
    add_file_button = self.browser.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input')
    add_file_button.send_keys(os.getcwd() + '\\img\\' + photo_name)
    self.browser.find_element(By.XPATH, '//button[text()="Siguiente"]').click()
    # Editar la imagen
    sleep(2)
    self.browser.find_element(By.XPATH, '//button[text()="Siguiente"]').click()
    # Pie de pagina
    bottom_pic_input = self.browser.find_element(By.XPATH, '//textarea[@placeholder="Escribe un pie de foto..."]')
    bottom_pic_input.send_keys(caption)
    # Publicar
    self.browser.find_element(By.XPATH, '//button[text()="Compartir"]').click()
    try:
      self.browser.find_element(By.XPATH, '//div[text()="Se ha compartido tu publicación."]')
      return True
    except:
      return False
