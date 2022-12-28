from BrowserManager import BrowserManager
from time import sleep
import os


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = BrowserManager()
        self.PHOTOPATH = os.getcwd() + '\\img\\'
    ############################################################################
    #                              INICIAR SESION                              #
    ############################################################################
    # Iniciar sesión

    def login(self):
        self.browser.send_key_to_element(
            '//input[@name="username"]', self.username)
        self.browser.send_key_to_element(
            '//input[@name="password"]', self.password)
        sleep(2)
        # Hacer click en el botón de iniciar sesión
        try:
            self.browser.click_element(
                '//button[@type="submit"]')
        except:
            self.browser.click_element(
                '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        # El tiempo de este sleep es importante, si es muy corto no se loguea
        sleep(2)
        print("You are logged in")
        self.save_login()
        self.not_aceppt_notifications()
        return True

    def run_browser(self):
        self.browser.access_url('https://www.instagram.com/')

    # Aceptar cookies (Solo las necesarias)
    def accept_cookies(self):
        try:
            self.browser.click_element('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/' +
                                       'div/div/div/div[2]/div/button[1]')
        except:
            print("Can't accept cookies")
            return False
        print("Cookies accepted")
        return True

    # Guarda información de la sesión para que no se tenga que loguear cada vez
    def save_login(self):
        # Diferentes referencias para acceder al boton de guardar información
        try:
            self.browser.click_element(
                '//button[text()="Guardar información"]')
        except:
            print("Can't save login")
            return False
        return True

    def not_aceppt_notifications(self):
        try:
            self.browser.click_element('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/' +
                                       'div/div/div/div[2]/div/div/div[3]/button[2]')
        except:
            print("Can't not accept notifications")
            return False
        return True
    ############################################################################
    #                             FUNCIONALIDADES                              #
    ############################################################################

    # Cerrar el navegador
    def close_browser(self):
        sleep(3)
        self.browser.close_browser()
        print("Browser closed")

    # Tomar captura de pantalla
    def take_screenshot(self, screenshot_name):
        sleep(2)
        self.browser.save_screenshot(screenshot_name + '.png')
        print("Screenshot taken")
        return True

    # Bajar hasta el final de la página
    # https://medium.com/jacklee26/selenium-instagram-followers-and-following-list-52c335a4ec03
    def scroll_down(self, scroll_box):
        try:
            last_ht, ht = 0, 1
            while last_ht != ht:
                last_ht = ht
                sleep(2)
                # script en js para hacer scroll
                ht = self.browser.run_script(""" 
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight; """, scroll_box)
            sleep(1)
            del scroll_box
            del last_ht, ht
            return True
        except:
            return False

    ############################################################################
    #                                 GETTERS                                  #
    ############################################################################

    # Devuelve el número de seguidores
    def get_followers_number(self):
        self.browser.access_url('https://www.instagram.com/' +
                                self.username + '/followers')
        sleep(2)
        followers_number = self.browser.find_element_by_xpath(
            '//a[@href="/' + self.username + '/followers/"]')
        return int(followers_number[0].text.split(' ')[0])

    # Devuelve el número de seguidos
    def get_following_number(self):
        self.browser.access_url('https://www.instagram.com/' +
                                self.username + '/following')
        sleep(2)
        following_number = self.browser.find_element_by_xpath(
            '//a[@href="/' + self.username + '/following/"]')
        return int(following_number[0].text.split(' ')[0])

    # Devuelve una lista con los seguidores
    def get_followers(self):
        number_of_followers = self.get_followers_number()
        self.browser.get('https://www.instagram.com/' +
                         self.username + '/followers')
        sleep(2)
        scroll_box = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/' +
                                                        'div[2]/div/div/div/div/div[2]/div/div/div[2]')
        self.scroll_down(scroll_box)
        followers = []
        j = 1
        while j <= number_of_followers:
            followers_list = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/' +
                                                                'div/div[2]/div/div/div/div/div[2]/div/div/div[2]/' +
                                                                'div[1]/div/div[' + str(j) + ']/div[2]/div[1]/div/' +
                                                                'div/span/a/span/div')
            followers.append(followers_list.text)
            j += 1
        return followers

    # Devuelve una lista con los seguidos
    def get_following(self):
        number_of_following = self.get_following_number()
        self.browser.access_url(
            'https://www.instagram.com/' + self.username + '/following')
        sleep(2)
        scroll_box = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/' +
                                                        'div[2]/div/div/div/div/div[2]/div/div/div[3]')
        self.scroll_down(scroll_box)
        following = []
        j = 1
        while j <= number_of_following:
            try:
                following_list = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/' +
                                                                    'div[1]/div/div[2]/div/div/div/div/div[2]/div/' +
                                                                    'div/div[3]/div[1]/div/div[' + str(j) + ']/div[2]' +
                                                                    '/div[1]/div/div/span/a/span/div')
                following.append(following_list.text)
            except:
                pass
            j += 1
        return following

    ############################################################################
    #                           METODOS PARA SEGUIR                            #
    ############################################################################
    # sigue a un usuario

    def follow_user(self, user):
        self.browser.access_url('https://www.instagram.com/' + user)
        try:
            self.browser.click_element('//div[text()="Seguir"]')
            print("You are following " + user)
            return True
        except:
            return self.follow_follower(user)

    # Seguir a un usuario que ya te sigue
    def follow_follower(self, follower):
        self.browser.access_url('https://www.instagram.com/' + follower)
        try:
            self.browser.click_element('//div[text()="Seguir también"]')
            try:
                self.browser.find_element_by_xpath(
                    '//div[text()="Restringimos determinada actividad para proteger a nuestra comunidad."]')
                return False
            except:
                print("You are following " + follower)
                return True
        except:
            return False

    def unfollow_user(self, user):
        self.browser.get('https://www.instagram.com/' + user)
        try:
            self.browser.click_element('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/' +
                                       'div[1]/div[1]/div/div[2]/button')
            sleep(1)
            self.browser.click_element('//button[text()="Dejar de seguir"]')
            print("You are not following " + user)
            return True
        except:
            return False

    # seguir a todos los seguidores del usuario
    def follow_all_followers(self):
        try:
            followers = self.get_followers()
            print("You are following " + str(len(followers)) + " users")
            following = self.get_following()
            print("You are following " + str(len(following)) + " users")
            # Seguir a los followers
            for follower in followers:
                if follower not in following:
                    self.follow_user(follower)
            # dejar de seguir a los que no te siguen
            for user in following:
                if user not in followers:
                    self.unfollow_user(user)
            return True
        except Exception as e:
            print(e)
            return False

    ############################################################################
    #                         METODOS  PARA SUBIR FOTOS                        #
    ############################################################################
    def upload_photo(self, photo_list, caption):
        # Abrir la página de subir fotos
        self.open_upload_page()
        # Seleccionar la primera imagen
        try:
            add_file_input = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/' +
                                                                'div/div[3]/div/div/div/div/div[2]/div/div/div/' +
                                                                'div[2]/div[1]/form/input')
        except:
            print("Can't find the image selector button")
            return False
        try:
            add_file_input.send_keys(self.PHOTOPATH + photo_list[0])
        except:
            print("Can't find the image")
            return False
        print("Photo: " + photo_list[0] + " uploaded")
        # Abrir menu para seleccionar mas fotos
        self.browser.click_element('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/' +
                                   'div[2]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/button')
        for photo in photo_list[1:]:
            sleep(1)
            self.browser.send_key_to_element('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/' +
                                             'div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[1]/' +
                                             'div/div/div/div[2]/form/input', self.PHOTOPATH + photo)
            print("Photo: " + photo + " uploaded")
            # Se cierra y se abre el menu de seleccionar fotos para resetaear la opcion de seleccionar mas fotos
            # Esto soluciona el problema de que se suben varias fotos en cada iteración
            self.browser.click_element('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/' +
                                       'div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/button')
            self.browser.click_element('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/ ' +
                                       'div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/button')
        self.browser.click_element('//button[text()="Siguiente"]')
        # Editar la imagen
        sleep(2)
        self.browser.click_element('//button[text()="Siguiente"]')
        # Pie de pagina
        try:
            caption_input = self.browser.send_key_to_element(
                '//textarea[@placeholder="Escribe un pie de foto..."]', caption)
        except:
            print("Can't find the caption input")
            return False
        # Publicar
        self.browser.click_element('//button[text()="Compartir"]')
        sleep(2)
        # Esperar a que se publique la foto
        while self.photo_uploaded() == False:
            sleep(1)
        return True

    def open_upload_page(self):
        try:
            self.browser.click_element('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/' +
                                       'div/div/div/div[2]/div[6]/div/div/a/div')
        except:
            print("Can't find the upload button")
            return False
        return True

    def photo_uploaded(self):
        try:
            self.browser.find_element_by_xpath(
                '//textarea[@placeholder="Se ha compartido tu publicación."]')
            return True
        except:
            return False
