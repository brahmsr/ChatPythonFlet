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
    
    # Verifica se há token válido para decidir rota inicial
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
