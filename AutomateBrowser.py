from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

# aceptar cookies
cookies_link = browser.find_element(By.XPATH, '//button[text()="Permitir solo cookies necesarias"]')
cookies_link.click()

# ingresar usuario
username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")

username_input.send_keys("diegodm35")
password_input.send_keys("Chocolate13")

login_link = browser.find_element(By.XPATH,"//button[@type='Entrar']")
login_link.click()

