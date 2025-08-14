import requests
from datetime import datetime, timezone
from Components.MessageError import error_message
import flet as ft

## Ao clicar no login
def login_click(self, e):
        
        # Ativar estado de carregamento
        self.login_button.disabled = True
        self.login_button.text = "Carregando..."
        self.page.update()

        url = "http://127.0.0.1:8000/api/login/"
        payload = {
            "username": self.username.value,
            "password": self.password.value
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                # Login bem-sucedido
                data = response.json()
                token = data.get("token")
                expiry = data.get("expiry")
                
                if self.radio_remember.value:
                    # Salva token e expiry localmente
                    self.page.client_storage.set("token", token)
                    self.page.client_storage.set("expiry", expiry)
                else:
                    # Remove tokens salvos se checkbox não estiver marcado
                    self.page.client_storage.remove("token")
                    self.page.client_storage.remove("expiry")
                    
                self.page.go('/')
            else:
                error_message(self.page, 'Login/Senha incorretos', ft.Icons.INFO)
        except Exception as ex:
            error = 'Erro ao fazer login: ' + ex
            error_message(self.page, error, ft.Icons.ERROR, ft.Colors.RED)
        finally:
            # Restaurar estado do botão
            self.login_button.disabled = False
            self.login_button.text = "Login"
            self.page.update()

### Checar se o token está ativo    
def check_token(self):
    token = self.page.client_storage.get("token")
    expiry = self.page.client_storage.get("expiry")
    
    if token and expiry:
        try:
            # Verifica se o token não expirou
            if datetime.now(timezone.utc) < datetime.fromisoformat(expiry.replace("Z", "+00:00")):
                self.page.go('/')
            else:
                # Token expirado, remove do storage
                self.page.client_storage.remove("token")
                self.page.client_storage.remove("expiry")
        except Exception:
            # Erro ao processar data, remove tokens inválidos
            self.page.client_storage.remove("token")
            self.page.client_storage.remove("expiry")