import flet as ft


def error_message(page: ft.Page, message: str, icon=ft.Icons.INFO, background=ft.Colors.ORANGE):
    snackbar = ft.SnackBar(
        content=ft.Row([
            ft.Icon(icon),
            ft.Text(message, color=ft.Colors.WHITE)
        ]),
        bgcolor=background,
        open=True
    )
    page.snack_bar = snackbar
    page.update()
