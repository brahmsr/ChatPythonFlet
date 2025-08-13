from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def IniciarWhatsApp(driver):
    try:
        # Aguarda o QR Code ser carregado
        elemento_qr = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ref]'))
        )
        
        # Captura o atributo data-ref do QR Code
        try:
            data_ref = elemento_qr.get_attribute('data-ref')
            print("Data Ref:", data_ref)
            time.sleep(180)  # Espera 180 segundos para o usuário escanear o QR Code
            qr_ainda_existe = len(driver.find_elements(By.CSS_SELECTOR, '[data-ref]')) > 0
            
            if qr_ainda_existe:
                print("QR Code ainda existe. Aguarde mais 180 segundos...")
                time.sleep(180)  # Espera mais 180 segundos caso o QR Code ainda exista

        except Exception as e:
            print("Erro ao capturar o atributo data-ref:", e)
        
    except Exception as e:
        print("Erro ao localizar o QR Code:", e)
        driver.quit()
        exit()

    # manter o navegador aberto
    input("Pressione ENTER para continuar após escanear o QR Code...")

