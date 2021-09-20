from selenium import webdriver
import pandas as pd
import time

class WhatsappBot:
    def __init__(self):
        # Lê o arquivo CSV onde contem os nomes exatos dos contatos
        contatos = pd.read_csv('contatos.csv')
        # Cria uma variável contendo apenas a coluna dos nomes dos contatos
        self.grupos_ou_pessoas = contatos['Contato']
        options = webdriver.ChromeOptions()
        # Informa para o Chrome qual Perfil será usado (para não precisar logar no whatsapp toda vez)
        options.add_argument(r"--user-data-dir=C:\Users\Master\AppData\Local\Google\Chrome\User Data\Default")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        # Abre o site do Whatsapp Web
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)

        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            # Cria uma variável com a mensagem a ser enviada, contendo o nome completo do contato
            mensagem = (f"""Olá {grupo_ou_pessoa}, é um prazer ter você aqui. Acesse nosso site e descubra mais!
            https://yuri.prawucki.com.br""")
            # Clica no botão de nova conversa
            novo_chat = self.driver.find_element_by_xpath("//span[@data-icon='chat']")
            novo_chat.click()
            time.sleep(3)
            # Clica na caixa de texto para digitar o contato
            busca_contato = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]')
            busca_contato.click()
            #time.sleep(3)
            # Escreve o contato
            busca_contato.send_keys(grupo_ou_pessoa)
            time.sleep(3)
            # Clica no contato
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            # Clica na caixa de texto para digitar a mensagem
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            #time.sleep(3)
            chat_box.click()
            # Escreve a mensagem
            chat_box.send_keys(mensagem)
            time.sleep(3)
            # Clica no botão enviar
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            #time.sleep(3)
            botao_enviar.click()
            time.sleep(3)


bot = WhatsappBot()
bot.EnviarMensagens()