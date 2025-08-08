import flet as ft

class NavigationRail(ft.NavigationDrawer):
    def __init__(self, page: ft.Page, on_destination_change=None):
        super().__init__()
        self.page = page
        self.selected_index = 0
        self.bgcolor = ft.Colors.GREEN_50
        self.on_destination_change = on_destination_change

        # Define largura máxima baseada no tamanho da tela
        self.width = 100
        
        self.controls = [
            ft.NavigationDrawerDestination(
                icon=ft.Icons.DASHBOARD,
                label="Dashboard"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.CHAT,
                label="Chat"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.SETTINGS,
                label="Configurações"
            ),
            ft.Divider(),
            ft.Container(
                content=ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    tooltip="Logout",
                    on_click=self.logout,
                    icon_color=ft.Colors.RED_400
                ),
                alignment=ft.alignment.center
            )
        ]
        
        if on_destination_change:
            self.on_change = on_destination_change
    
    def toggle_visibility(self):
        self.open = not self.open
        self.update()
    
    def logout(self, e):
        # Remove tokens salvos
        self.page.client_storage.remove("token")
        self.page.client_storage.remove("expiry")
        self.page.go('/login')
