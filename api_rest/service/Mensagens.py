from PerfilWhatsapp import VerificarPerfilWhatsApp
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ..models import SuperUser

def VerificarMensagensWhatsApp(userSession):
    # userSession = SuperUser.objects.filter(id=userSession.id).first()
    # if userSession is None:
    #     return False
    
    VerificarPerfilWhatsApp(userSession)
    action = webdriver.ActionChains(VerificarPerfilWhatsApp.driver)
    
    obter_notificacoes = VerificarPerfilWhatsApp.driver.find_elements(By.CLASS_NAME, 'x140p0ai')
    if obter_notificacoes:
        for notificacao in obter_notificacoes:
            action.move_to_element(notificacao)
            action.move_by_offset(-5, 0) # Move slightly to the left
            action.click()
            action.perform()
            notificacao.click()
    
    
