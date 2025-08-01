import flet as ft
from Views.Home import (ft, Home)
from Views.Login import Login
from Components.NavigationRail import NavigationRail

def main(page: ft.Page):
    page.title = 'IAm Chat'

    # Componentes de navegação
    nav_rail = NavigationRail(page=page)

    # Views
    home = Home(page=page)
    login = Login(page=page)

    # Handler de componentes
    def handle_navigation_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0: # Dashboard
            page.go('/')
        elif selected_index == 1: # Chat
            page.go('/login')
        elif selected_index == 2: # Configurações
            page.go('/settings')
    
    nav_rail.on_change = handle_navigation_change

    def router(route):
        page.views.clear()
        
        if page.route == '/':
            # Layout com NavigationRail
            main_view = ft.View(
                route='/',
                controls=[
                    ft.Row(
                        controls=[
                            nav_rail,
                            ft.VerticalDivider(width=1),
                            ft.Container(
                                content=home,
                                expand=True
                            )
                        ],
                        spacing=0,
                        expand=True
                    )
                ],
                padding=ft.padding.all(0)
            )
            page.views.append(main_view)
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
