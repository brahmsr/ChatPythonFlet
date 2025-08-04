import flet as ft

class NavigationRail(ft.NavigationRail):
    def __init__(self, page: ft.Page, on_destination_change=None):
        super().__init__()
        self.page = page
        self.selected_index = 0
        self.label_type = ft.NavigationRailLabelType.ALL
        self.min_width = 100
        self.min_extended_width = 160
        self.bgcolor = ft.Colors.GREEN_50
        self.visible = True
        
        self.destinations = [
            ft.NavigationRailDestination(
                icon=ft.Icons.DASHBOARD,
                selected_icon=ft.Icons.DASHBOARD,
                label="Dashboard"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.CHAT,
                selected_icon=ft.Icons.CHAT,
                label="Chat"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS,
                selected_icon=ft.Icons.SETTINGS,
                label="Configurações"
            ),
        ]
        
        self.trailing = ft.IconButton(
            icon=ft.Icons.LOGOUT,
            tooltip="Logout",
            on_click=self.logout,
            icon_color=ft.Colors.RED_400
        )
        
        if on_destination_change:
            self.on_change = on_destination_change
    
    def toggle_visibility(self):
        self.visible = not self.visible
        self.update()
    
    def logout(self, e):
        # Remove tokens salvos
        self.page.client_storage.remove("token")
        self.page.client_storage.remove("expiry")
        self.page.go('/login')