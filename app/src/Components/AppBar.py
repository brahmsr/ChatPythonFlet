import flet as ft
import Components.NavigationRail as NavigationRail

class AppBar(ft.AppBar):
    def __init__(self, page: ft.Page, nav_rail=None):
        super().__init__()
        self.page = page
        self.nav_rail = nav_rail
        self.logo = ft.Image(src="logosemfundo.png", width=50, height=50)
        self.title = ft.Text("IAm", size=30, text_align=ft.TextAlign.LEFT, width=100)

        self.actions = [
            ft.IconButton(ft.Icons.PERSON, on_click=lambda e: self.page.go("/profile")),
            # ft.PopupMenuButton(
            #     items=[
            #         ft.PopupMenuItem(text="Perfil"),
            #         ft.PopupMenuItem(),  # divider
            #         ft.PopupMenuItem(
            #             text="Checked item", 
            #             checked=False, 
            #             on_click=self.check_item_clicked
            #         ),
            #     ]
            # ),
        ]
    
    def check_item_clicked(self, e):
        # Implementar ação do menu
        pass
