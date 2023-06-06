from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import database
import time

class Mundial:
    def __init__(self):
        self.SITE_LINK = "https://www.mundialcalcados.com.br/tenis?&O=OrderByReleaseDateDESC"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()
        self.database_inserir()
        self.database_delete()

    def abrir_site(self):
        time.sleep(1)
        self.driver.get(self.SITE_LINK)
        self.driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/button").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.adidas()

    def adidas(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[1]/a").click()
        self.lista_adidas_nome = []
        self.lista_adidas_valor = []
        for i in range(10):
            adidas_nome = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a').text
            adidas_valor = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]').text
            self.lista_adidas_nome.append(adidas_nome)
            self.lista_adidas_valor.append(adidas_valor)

        for i in range(10):
            print(self.lista_adidas_nome[i])
            print(self.lista_adidas_valor[i])
        self.asics()

    def asics(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[2]/a").click()
        self.lista_asics_nome = []
        self.lista_asics_valor = []
        for i in range(10):
            asics_nome = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a").text
            asics_valor = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]").text
            self.lista_asics_nome.append(asics_nome)
            self.lista_asics_valor.append(asics_valor)

        for i in range(10):
            print(self.lista_asics_nome[i])
            print(self.lista_asics_valor[i])
        self.cocacola()

    def cocacola(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[5]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[5]/a").click()
        self.lista_cocacola_nome = []
        self.lista_cocacola_valor = []
        for i in range(10):
            coca_nome = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a").text
            coca_valor = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]").text
            self.lista_cocacola_nome.append(coca_nome)
            self.lista_cocacola_valor.append(coca_valor)

        for i in range(10):
            print(self.lista_cocacola_nome[i])
            print(self.lista_cocacola_valor[i])
        self.cavalera()

    def cavalera(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[4]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/h5[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/section[3]/div/div[1]/div[1]/aside/div[2]/div[1]/div/div/div[3]/ul[7]/li[4]/a").click()
        self.lista_cavalera_nome = []
        self.lista_cavalera_valor = []
        for i in range(10):
            cavalera_nome = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a").text
            cavalera_valor = self.driver.find_element(By.XPATH, f"/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]").text
            self.lista_cavalera_nome.append(cavalera_nome)
            self.lista_cavalera_valor.append(cavalera_valor)

        for i in range(10):
            print(self.lista_cavalera_nome[i])
            print(self.lista_cavalera_valor[i])
        self.tommy_hilfiger()

    def tommy_hilfiger(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/header[1]/div[1]/div[3]/div[1]/div/div[3]/div/ul/li[4]/i").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/header[1]/div[1]/div[3]/div[1]/div/div[3]/div/div/fieldset/input[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/header[1]/div[1]/div[3]/div[1]/div/div[3]/div/div/fieldset/input[2]").send_keys("tommy")
        self.driver.find_element(By.XPATH, "/html/body/header[1]/div[1]/div[3]/div[1]/div/div[3]/div/div/fieldset/input[2]").send_keys(Keys.ENTER)


        self.lista_tommy_nome = []
        self.lista_tommy_valor = []
        for i in range(10):
            tommy_nome = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[4]/div/div/div/h3/a').text
            tommy_valor = self.driver.find_element(By.XPATH, f'/html/body/main/div/section[3]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul[{i+1}]/li[1]/div/div[5]/div/div/div/div/p[2]').text
            self.lista_tommy_nome.append(tommy_nome)
            self.lista_tommy_valor.append(tommy_valor)

        for i in range(10):
            print(self.lista_tommy_nome[i])
            print(self.lista_tommy_valor[i])

    def database_inserir(self):
        for i in range(10):
            database.cur.execute(f"INSERT INTO tenis VALUES ('adidas', '{self.lista_adidas_nome[i]}', '{self.lista_adidas_valor[i]}')")
            database.cur.execute(f"INSERT INTO tenis VALUES ('asics', '{self.lista_asics_nome[i]}','{self.lista_asics_valor[i]}')")
            database.cur.execute(f"INSERT INTO tenis VALUES ('coca cola','{self.lista_cocacola_nome[i]}','{self.lista_cocacola_valor[i]}')")
            database.cur.execute(f"INSERT INTO tenis VALUES ('cavalera', '{self.lista_cavalera_nome[i]}', '{self.lista_cavalera_valor[i]}')")
            database.cur.execute(f"INSERT INTO tenis VALUES ('tommy hilfinger', '{self.lista_tommy_nome[i]}', '{self.lista_tommy_valor[i]}')")
            database.var.commit()

    def database_delete(self):
        database.cur.execute(f"DELETE FROM tenis")
        database.var.commit()








