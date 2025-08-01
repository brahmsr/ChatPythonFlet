import flet as ft
from ..Components.NavigationRail import NavigationRail

class Kanban(ft.View):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.route = '/kanban'
        self.padding = ft.padding.all(0)

        # Navigation Rail
        self.nav_rail = NavigationRail(
            page=page,
            on_destination_change=self.on_nav_change
        )