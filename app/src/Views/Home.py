import flet as ft

class Home(ft.View):
    def __init__(
            self,
            page: ft.Page
    ):
        super().__init__()
        self.route = '/'
        self.padding = ft.padding.all(0)
        self.controls = [
            ft.Stack(
                controls=[
                    ChatBackground(page=page, color1= ft.Colors.GREEN_ACCENT_200, color2= ft.Colors.GREEN_300)
                ]
            )
        ]

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
