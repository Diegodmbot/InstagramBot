from multiprocessing.connection import wait
from sys import excepthook
from time import sleep
from selenium.webdriver.common.by import By

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
    login_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
    login_button.click()
    # El tiempo de este sleep es importante, si es muy corto no se loguea
    sleep(2)
    print("You are logged in")
    return True
  # Aceptar cookies (Solo las necesarias)
  def accept_cookies(self):
    cookies_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
    cookies_button.click()
    print("Cookies accepted")
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
      follow_button = self.browser.find_element(By.XPATH, '//div[text()="Seguir"]')
      follow_button.click()
      print("You are following " + user)
      return True
    except:
      return False
  # Seguir a un usuario que ya te sigue
  def follow_user_following(self, follower):
    self.browser.get('https://www.instagram.com/' + follower)
    try:
        follow_button = self.browser.find_element(By.XPATH, '//div[text()="Seguir también"]')
        follow_button.click()
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
      follow_button = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
      follow_button.click()
      sleep(1)
      unfollow_button = self.browser.find_element(By.XPATH, '//button[text()="Dejar de seguir"]')
      unfollow_button.click()
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
  def upload_pictures(self):
    self.browser.get('https://www.instagram.com/')
    sleep(2)
    upload_photo_button = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
    upload_photo_button.click()
    # Seleccionar la imagen
    #
    next_button = self.browser.find_element(By.XPATH, '//button[text()="Siguiente"]')
    next_button.click()
    # Editar la imagen
    next_button.click()
    # Pie de pagina
    bottom_pic_input = self.browser.find_element(By.XPATH, '//textarea[@placeholder="Escribe un comentario..."]')
    bottom_pic = input("Escribe un comentario para la foto: ")
    bottom_pic_input.send_keys(bottom_pic)
    # Publicar
    share_button = self.browser.find_element(By.XPATH, '//button[text()="Compartir"]')
    share_button.click()
