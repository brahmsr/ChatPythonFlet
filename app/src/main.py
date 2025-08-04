import flet as ft
from Views.Home import (ft, Home)
from Views.Login import Login
from Components.NavigationRail import NavigationRail
from Views.MainView import MainView

def main(page: ft.Page):
    page.title = 'IAm Chat'
    page.window.width = 320
    page.window.height = 568
    page.window.resizable = False
    page.window.frameless = True
    page.window.icon = ft.Image('logosemfundo.png')

    # Componentes de navegação
    nav_rail = NavigationRail(page=page)

    # Views
    login = Login(page=page)
    main_view = None

    def router(route):
        nonlocal main_view
        page.views.clear()
        
        if page.route == '/':
            if main_view is None:
                main_view = MainView(page=page)  # Cria apenas após login
            page.views.append(main_view)
        elif page.route == '/login':
            page.views.append(login)

        page.update()

    page.on_route_change = router
    
    def check_initial_route():
        from datetime import datetime, timezone
        token = page.client_storage.get("token")
        expiry = page.client_storage.get("expiry")
        
        if token and expiry:
            try:
                if datetime.now(timezone.utc) < datetime.fromisoformat(expiry.replace("Z", "+00:00")):
                    page.go('/')
                    return
            except Exception:
                pass
        
        page.go('/login')
    
    check_initial_route()

if __name__ == '__main__':
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir='assets',
        web_renderer=ft.WebRenderer.CANVAS_KIT
        )
