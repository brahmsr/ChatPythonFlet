import flet as ft

class AppBar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.logo = ft.Image(src="logosemfundo.png", width=50, height=50)
        self.title = ft.Text("IAm", size=30, text_align=ft.TextAlign.CENTER, width=100)
        self.actions = [
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ]