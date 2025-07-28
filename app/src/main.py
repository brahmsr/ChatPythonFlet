import flet as ft


def main(page: ft.Page):
    page.title = 'IAm Chat'

    def router(route):
        page.views.clear()
        
        if page.route == '/':
            page.views.append(

            )

        page.update()

    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
