from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from Iniciarwhatsapp import IniciarWhatsApp

def VerificarPerfilWhatsApp():
    perfil_dir = os.path.abspath("whatsapp_sessao")
    # Configura o Chrome para usar a pasta como perfil
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={perfil_dir}")
    chrome_options.add_argument("--profile-directory=Default")
    
    driver = webdriver.Chrome(options=chrome_options)
    # Verifica se o WhatsApp está aberto
    try:
        driver.get("https://web.whatsapp.com/")
        if os.path.exists(perfil_dir):
            print("WhatsApp está aberto.")
        else:
            IniciarWhatsApp(driver)
        input("Pressione ENTER para sair...")
        driver.quit()
        return True
    except Exception as e:
        print("Erro ao iniciar o navegador:", e)
        return False