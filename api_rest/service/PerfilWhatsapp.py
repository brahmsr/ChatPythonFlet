from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Iniciarwhatsapp import IniciarWhatsApp

def VerificarPerfilWhatsApp(userSession = None):
    if userSession == None:
        return False
    perfil_dir = os.path.abspath("api_root/whatsapp_sessao_" . userSession.id)
    
    # Configura o Chrome para usar a pasta como perfil
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={perfil_dir}")
    chrome_options.add_argument("--profile-directory=Default")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://web.whatsapp.com/")
        try: 
                qr_elements = driver.find_elements(By.CSS_SELECTOR, '[data-ref]')
                if qr_elements:
                    IniciarWhatsApp(driver)
                else:
                    print("WhatsApp já está logado.")
        except:
                print("WhatsApp está logado.")
        input("Pressione ENTER para sair...")
        return driver
    except Exception as e:
        print("Erro ao iniciar o navegador:", e)
        return False
    finally:
        if 'driver' in locals():
            driver.quit()
