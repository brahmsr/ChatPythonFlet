import flet as ft
from Views.Home import Home
# from Views.Chat import Chat  # Você precisará criar esta
# from Views.Settings import Settings  # Você precisará criar esta
from Components.NavigationRail import NavigationRail
from Components.AppBar import AppBar

class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = '/main'
        self.padding = ft.padding.all(0)
        
        # NavigationRail
        self.nav_rail = NavigationRail(page=page, on_destination_change=self.handle_navigation)
        
        # AppBar
        self.appbar = AppBar(page=page, nav_rail=self.nav_rail)
        
        # Inicializa as views
        self.home_view = Home(page=page)
        # self.chat_view = Chat(page=page)  # Criar depois
        # self.settings_view = Settings(page=page)  # Criar depois
        
        # Container para conteúdo atual
        self.content_container = ft.Container(
            content=ft.Column(controls=self.home_view.controls, expand=True),
            expand=True
        )
        
        self.controls = [
            ft.Row(
                controls=[
                    self.nav_rail,
                    ft.VerticalDivider(width=1),
                    self.content_container
                ],
                spacing=0,
                expand=True
            )
        ]
    
    def handle_navigation(self, e):
        selected_index = e.control.selected_index
        
        if selected_index == 0:  # Dashboard
            self.content_container.content = ft.Column(controls=self.home_view.controls, expand=True)
        elif selected_index == 1:  # Chat
            self.content_container.content = ft.Column(controls=self.chat_view.controls, expand=True)
        elif selected_index == 2:  # Settings
            self.content_container.content = ft.Column(controls=self.settings_view.controls, expand=True)
        
        self.page.update()
