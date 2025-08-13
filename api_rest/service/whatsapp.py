from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

print("Escaneie o QR Code e pressione ENTER no terminal...")
input()

# Função para enviar mensagem
def enviar_mensagem(contato, mensagem):
    try:
        # Localiza o campo de busca e digita o nome/telefone do contato
        campo_busca = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        campo_busca.clear()
        campo_busca.send_keys(contato)
        campo_busca.send_keys(Keys.ENTER)
        time.sleep(1)

        # Campo de mensagem
        campo_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        campo_mensagem.send_keys(mensagem)
        campo_mensagem.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para {contato}")

    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato}: {e}")

# Exemplo de envio
enviar_mensagem("Fulano", "Olá! Este é um bot de teste 🤖")

# Mantém o navegador aberto
time.sleep(10)
driver.quit()
