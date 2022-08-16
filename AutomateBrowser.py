from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#abrir navegador
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com')
# aceptar cookies
cookies_link = browser.find_element(By.XPATH, '//button[text()="Permitir solo cookies necesarias"]')
cookies_link.click()
# ingresar usuario y contraseña
username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")
username_input.send_keys("diegodm35")
password_input.send_keys("Chocolate13")
sleep(1)
login_link = browser.find_element(By.CSS_SELECTOR,'.L3NKy > div:nth-child(1)')
login_link.click()
#Entrar al perfil
icon_link = browser.find_element(By.CSS_SELECTOR, '._2dbep')
icon_link.click()
profile_link = browser.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div')
profile_link.click()