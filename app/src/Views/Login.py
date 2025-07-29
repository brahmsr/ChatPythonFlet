import flet as ft
import requests

class Login(ft.View):
    def __init__(
            self,
            page: ft.Page):
        super().__init__()
        self.page = page
        self.route = '/login'
        self.padding = ft.padding.all(0)

        self.check_token()

        # Campos de login
        self.imageLogo = ft.Image(
            src="logosemfundo.png",
            width=100,
            height=100)

        self.titleLogin = ft.Text("Bem-vindo!",
                                  size=32,
                                  weight=ft.FontWeight.BOLD,
                                  color=ft.Colors.GREEN_900)

        self.username = ft.TextField(
            label="Username",
            prefix_icon=ft.Icons.PERSON,
            autofocus=True,
            hint_text="Digite seu nome de usuário",
            width=300,
            text_align=ft.TextAlign.LEFT,
            border_radius=10
        )
        
        # Password field
        self.password = ft.TextField(
            label="Password",
            prefix_icon=ft.Icons.LOCK,
            hint_text="Digite sua senha",
            width=300,
            password=True,
            can_reveal_password=True,
            border_radius=10
        )
        
        # Botão de login
        self.login_button = ft.ElevatedButton(
            text="Login",
            width=300,
            on_click=self.login_click,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREEN_500,
                color=ft.Colors.WHITE,
                padding=ft.padding.all(10),
                shape=ft.RoundedRectangleBorder(radius=10)
            )
        )

        # Lembrar-se de mim
        self.radio_remember = ft.Checkbox(
            label="Lembrar-se de mim",
            value=False
            )

        self.controls = [
            ft.Stack(
                controls=[
                    ChatBackground(
                        page=page,
                        color1=ft.Colors.GREEN_ACCENT_200,
                        color2=ft.Colors.GREEN_300
                    ),
                    ft.Container(
                        content=ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        self.imageLogo,
                                        self.titleLogin,
                                        self.username,
                                        self.password,
                                        self.radio_remember,
                                        self.login_button,
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20
                                ),
                                padding=40,
                                bgcolor=ft.Colors.WHITE,
                                border_radius=20,
                                width=380, height=470
                            ),
                            elevation=8,
                        ),
                        alignment=ft.alignment.center,
                        expand=True
                    )
                ],
                expand=True,
                alignment=ft.alignment.center
            )
        ]

    def login_click(self, e):
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
                self.page.go('/')
            else:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Usuário ou senha inválidos!"),
                    bgcolor=ft.Colors.RED_400
                )
                self.page.snack_bar.open = True
                self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro de conexão: {ex}"),
                bgcolor=ft.Colors.RED_400
            )
            self.page.snack_bar.open = True
            self.page.update()
    
    def check_token(self):
        token = self.page.client_storage.get("token")
        expiry = self.page.client_storage.get("expiry")
        from datetime import datetime
        if token and expiry:
            # Verifica se o token não expirou
            if datetime.now(datetime.timezone.utc) < datetime.fromisoformat(expiry.replace("Z", "+00:00")):
                self.page.go('/')

class ChatBackground(ft.Container):
    def __init__(
            self,
            page: ft.Page,
            color1: str,
            color2: str      
    ):
        super().__init__()
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[color1, color2]
        )
        self.width = page.width
        self.height = page.height