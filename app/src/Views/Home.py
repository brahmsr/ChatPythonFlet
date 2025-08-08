import flet as ft
import requests
from datetime import datetime

class Home(ft.View):
    def __init__(
            self,
            page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.route = '/'
        self.padding = ft.padding.all(0)
        
        # Dashboard data
        self.stats_data = {}
        self.users_data = []
        
        # Dashboard components
        self.title = ft.Text(
            "Dashboard",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_900
        )
        
        self.stats_cards = ft.Row(
            controls=[],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
        
        self.users_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Username")),
                ft.DataColumn(ft.Text("Contato")),
                ft.DataColumn(ft.Text("Data Cadastro"))
            ],
            rows=[]
        )
        
        self.refresh_button = ft.ElevatedButton(
            text="Atualizar",
            icon=ft.Icons.REFRESH,
            on_click=self.refresh_data,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREEN_500,
                color=ft.Colors.WHITE,
                padding=ft.padding.all(10),
                shape=ft.RoundedRectangleBorder(radius=10)
            )
        )
        
        # Main content
        self.main_content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    self.title,
                                    self.refresh_button,
                                    self.stats_cards,
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=20
                            ),
                            padding=30,
                            bgcolor=ft.Colors.WHITE,
                            border_radius=20
                        ),
                        elevation=8
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Usuários", size=20, weight=ft.FontWeight.BOLD),
                                    self.users_table
                                ],
                                spacing=15
                            ),
                            padding=20,
                            bgcolor=ft.Colors.WHITE,
                            border_radius=20
                        ),
                        elevation=8
                    )
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO
            ),
            padding=20,
            expand=True
        )
        
        self.controls = [
            ft.Stack(
                controls=[
                    ChatBackground(
                        page=page,
                        color1=ft.Colors.GREEN_ACCENT_200, 
                        color2=ft.Colors.GREEN_300
                    ),
                    ft.Row(
                        controls=[
                            ft.VerticalDivider(width=1),
                            self.main_content
                        ],
                        spacing=0,
                        expand=True
                    )
                ],
                expand=True
            )
        ]
        
        # Load initial data
        self.load_dashboard_data()
    
    def on_nav_change(self, e):
        selected_index = e.control.selected_index
        
        if selected_index == 0:  # Dashboard
            # Já estamos no dashboard
            pass
        elif selected_index == 1:  # Chat
            # Implementar navegação para chat
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Chat em desenvolvimento"),
                bgcolor=ft.Colors.BLUE_400
            )
            self.page.snack_bar.open = True
            self.page.update()
        elif selected_index == 2:  # Configurações
            # Implementar navegação para configurações
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Configurações em desenvolvimento"),
                bgcolor=ft.Colors.ORANGE_400
            )
            self.page.snack_bar.open = True
            self.page.update()
    
    def load_dashboard_data(self):
        try:
            # Get stats
            stats_response = requests.get("http://127.0.0.1:8000/api/dashboard/stats/")
            if stats_response.status_code == 200:
                self.stats_data = stats_response.json()
                self.update_stats_cards()
            
            # Get users
            users_response = requests.get("http://127.0.0.1:8000/api/dashboard/users/")
            if users_response.status_code == 200:
                self.users_data = users_response.json()
                self.update_users_table()
                
        except Exception as e:
            self.show_error(f"Erro ao carregar dados: {e}")
    
    def update_stats_cards(self):
        self.stats_cards.controls.clear()
        
        for key, value in self.stats_data.items():
            card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(str(value), size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(key.replace('_', ' ').title(), size=14, color=ft.Colors.GREY_700)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=20,
                    bgcolor=ft.Colors.WHITE,
                    width=150,
                    height=100
                ),
                elevation=4
            )
            self.stats_cards.controls.append(card)
    
    def update_users_table(self):
        self.users_table.rows.clear()
        
        for user in self.users_data:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(user.get('id', '')))),
                    ft.DataCell(ft.Text(user.get('username', ''))),
                    ft.DataCell(ft.Text(user.get('email', ''))),
                    ft.DataCell(ft.Text(user.get('date_joined', '')[:10] if user.get('date_joined') else ''))
                ]
            )
            self.users_table.rows.append(row)
    
    def refresh_data(self, e):
        self.load_dashboard_data()
        self.page.update()
        
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("Dados atualizados!"),
            bgcolor=ft.Colors.GREEN_400
        )
        self.page.snack_bar.open = True
        self.page.update()
    
    def show_error(self, message):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor=ft.Colors.RED_400
        )
        self.page.snack_bar.open = True
        self.page.update()

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
