import flet as ft
from front_page import front_page
from login_page import login_page
from main_page import main_page

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(front_page(page))
        elif page.route == "/login":
            page.views.append(login_page(page))
        elif page.route == "/main":
            page.views.append(main_page(page))
        else:
            page.views.append(
        ft.View(
        route=page.route,
        controls=[
            ft.Text("404: Page Not Found", size=30, color="red"),
            ft.ElevatedButton(
                text="Go to Front Page",
                on_click=lambda e: page.go("/"),
                style=ft.ButtonStyle(bgcolor="#FF6347"),
            ),
        ],
    )
)

        page.update()

    page.on_route_change = route_change
    page.go("/")  # Start with the front page
    

ft.app(target=main)
