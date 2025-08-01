import flet as ft
from Views.Home import (ft, Home)
from Views.Login import Login

def main(page: ft.Page):
    page.title = 'IAm Chat'

    home = Home(page=page)
    login = Login(page=page)

    def router(route):
        page.views.clear()
        
        if page.route == '/':
            page.views.append(home)
        elif page.route == '/login':
            page.views.append(login)

        page.update()

    page.on_route_change = router
    page.go('/login')

if __name__ == '__main__':
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir='assets',
        web_renderer=ft.WebRenderer.CANVAS_KIT
        )
