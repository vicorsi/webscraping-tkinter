from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import selenium



class Mundial:
    def __init__(self):
        self.SITE_LINK = "https://www.mundialcalcados.com.br/tenis?&O=OrderByReleaseDateDESC"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()

    def abrir_site(self):
        time.sleep(1)
        self.driver.get(self.SITE_LINK)
        self.driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/button").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.adidas()

    def adidas(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[1]/a").click()
        self.lista_adidas = []
        for i in range(10):
            adidas_nome = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a').text
            adidas_valor = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]').text
            self.lista_adidas.append(adidas_nome)
            self.lista_adidas.append(adidas_valor)

        for i in range(20):
            print(self.lista_adidas[i])
        self.asics()

    def asics(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[2]/a").click()
        self.lista_asics = []
        for i in range(10):
            asics_nome = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a").text
            asics_valor = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]").text
            self.lista_asics.append(asics_nome)
            self.lista_asics.append(asics_valor)

        for i in range(20):
            print(self.lista_asics[i])
        self.cocacola()

    def cocacola(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[5]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[5]/a").click()
        self.lista_cocacola = []
        for i in range(10):
            coca_nome = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a").text
            coca_valor = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]").text
            self.lista_cocacola.append(coca_nome)
            self.lista_cocacola.append(coca_valor)

        for i in range(20):
            print(self.lista_cocacola[i])
        self.cavalera()

    def cavalera(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[4]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[4]/a").click()
        self.lista_cavalera = []
        for i in range(10):
            cavalera_nome = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a").text
            cavalera_valor = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]").text
            self.lista_cavalera.append(cavalera_nome)
            self.lista_cavalera.append(cavalera_valor)

        for i in range(20):
            print(self.lista_cavalera[i])
        self.tommy_hilfiger()

    def tommy_hilfiger(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[24]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[22]/a").click()
        self.lista_tommy = []
        for i in range(10):
            tommy_nome = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a').text
            tommy_valor = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]').text
            self.lista_tommy.append(tommy_nome)
            self.lista_tommy.append(tommy_valor)

        for i in range(20):
            print(self.lista_tommy[i])
        quit(print("FIM DO BOT"))

mun = Mundial()


