from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

#abrir navegador
browser_options = Options()
#browser_options.add_argument("--headless")
browser = webdriver.Firefox(options=browser_options)
browser.implicitly_wait(5)
browser.get('https://www.instagram.com')
# aceptar cookies
cookies_button = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]')
cookies_button.click()
print("Cookies accepted")
# ingresar usuario y contraseña
username_input = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
password_input = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
#region usuario y contraseña
username_input.send_keys("diegodm35")
password_input.send_keys("Chocolate13")
#endregion 
sleep(2)
login_button = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
login_button.click()
print("You are logged in")
#Entrar al perfil
icon_profile = browser.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span')
icon_profile.click()
profile = browser.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div')
profile.click()
print("I am in your profile")
browser.save_full_page_screenshot("profile.png")
#cerrar pestaña
sleep(10)
print("Closing browser")
browser.quit()