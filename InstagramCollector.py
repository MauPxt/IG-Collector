import time
from datetime import datetime, timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import logging
from getpass import getpass


class InstagramBot:
    def __init__(self):
        # Log
        logging.basicConfig(filename="log.log", level=logging.WARNING,
                            format='%(asctime)s :: %(name)s :: %(levelname)s :: %(lineno)d :: %(message)s')
        self.log = logging.getLogger(__name__)

        # Selenium
        self.log.info("Configurando o robô...")
        options = Options()
        options.add_argument('--disable-notifications')
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-crash-reporter')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-in-process-stack-traces')
        options.add_argument('--disable-logging')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--log-level=3')
        options.add_argument('--output=/dev/null')
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

        # Controle
        self.login_switch = 0

    def login(self, username, password):
        if self.login_switch != 1:
            self.log.info("Iniciando função de login")
            print('Entrando no instagram')
            self.driver.get('https://www.instagram.com/')
            time.sleep(5)
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         '//*[@id="loginForm"]/div/div[1]/div/label/input')))
                print('Iniciando processo de login...')
                self.log.info("Procurando campo de login")
                self.driver.find_element(
                    By.XPATH,
                    '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(
                    username)
                self.log.info("Procurando campo de senha...")
                self.driver.find_element(
                    By.XPATH,
                    '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
                    password)
                self.log.info("Clicando no botão de entrar...")
                self.driver.find_element(
                    By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH,
                             '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img')))
                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img').click()
                    self.login_switch = 1

                except Exception:
                    print('Falha no processo de login!')
                    try:
                        a = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[2]/p').text
                        print(f'Motivo: {a}')
                    except Exception:
                        pass
                    self.login_switch = 0

            except Exception as e:
                self.log.critical(
                    f'O robô não conseguiu fazer login! Motivo: {e}')
                print('Falha no login!')
                desejo = input('Deseja tentar novamente? y/n')
                if desejo == 'y' or 'Y':
                    self.start(self.username, self.password)
                else:
                    self.driver.quit()
        else:
            print('O login já foi realizado!')

    def start(self, username, password):
        time.sleep(1)
        self.log.info("Iniciando a rotina do robô...")
        now = datetime.now()
        self.login(username, password)
        if self.login_switch == 1:
            self.log.info("Login realizado com sucesso!")
            print('Coletando usuários no documento "perfis.txt"')

            self.log.info("Abrindo arquivo perfis.txt")
            with open('perfis.txt', 'r') as t:
                x = t.read().split()
            self.log.info("Leitura realizada com sucesso!")

            print('Iniciando rotina...')
            self.log.info("Iniciando coleta dos dados...")
            resultado = []
            for i in x:
                print('')
                print(f'Coletando dados da página: {i}')
                try:
                    # Entrando no Instagram da página
                    self.log.info(f"Acessando a página {i}")
                    self.driver.get(f'https://www.instagram.com/{i}/')

                    # Clicando no último post
                    self.log.info("Procurando o último post")
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH,
                             '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')))
                    self.driver.find_element(
                        By.XPATH,
                        '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()

                    # Coletando a data
                    self.log.info("Coletando o elemento de data")
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH,
                             '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/div/div/a/div/time')))
                    post_date = self.driver.find_element(
                        By.XPATH,
                        '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/div/div/a/div/time')

                    # Manipulando a data
                    self.log.info("Transformando o elemento data")
                    tempo = post_date.get_attribute('datetime')
                    data = tempo[:10] + ' ' + tempo[11:16]
                    tempo = datetime.strptime(data, '%Y-%m-%d %H:%M')

                    # Realizando a comparação. Se a última postagem tiver mais de 3 dias, mandar notificação
                    self.log.info("Realizando comparação")
                    if now > (tempo + timedelta(days=3)):
                        print(
                            f'A página "{i}" passou do prazo! Enviar mensagem.')
                        resultado.append([i, now.strftime('%d/%m/%Y'),
                                          tempo.strftime('%d/%m/%Y'),
                                          'NOTIFICAR'])
                    else:
                        print(f'A página "{i}" está dentro do prazo!')
                        resultado.append([i, now.strftime('%d/%m/%Y'),
                                          tempo.strftime('%d/%m/%Y'),
                                          'NO PRAZO'])
                except Exception as e:
                    self.log.warning(
                        f"O robô não conseguiu coletar dados da página {i}, motivo: {e}")
                    print(f'Falha ao coletar dados da página: {i}')
                    resultado.append([i, now.strftime('%d/%m/%Y'),
                                      'ERRO',
                                      'ERRO'])
                    continue

            # Passando os resultados para uma planilha csv
            print()
            self.log.info(
                "Salvando dados na planilha csv 'resultados.csv'")
            print(
                'Salvando os resultados na planilha csv "resultados.csv"')
            dados = pd.DataFrame(resultado, columns=[
                'página', 'data da consulta', 'data do ultimo post',
                'resultado'])
            dados.to_csv('resultados.csv')
        else:
            print(
                'O programa será encerrado em 5 segundos! Tente novamente...')
            time.sleep(5)

    def initialize(self):
        print('*---*---*')
        self.username = input('Digite o usuário: ')
        self.password = getpass(
            'Digite a senha (é normal não aparecer os caracteres): ')
        print('*---*---*')
        self.start(self.username, self.password)
        self.driver.quit()


if __name__ == '__main__':
    IB = InstagramBot()
    IB.initialize()
