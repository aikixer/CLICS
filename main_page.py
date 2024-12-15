import flet as ft

def main_page(page: ft.Page):
    def on_logout(e):
        page.go("/")  # Navigate back to the front page

    # Announcements tab content
    def announcements_tab():
        return ft.Column(
            controls=[
                ft.Text(
                    "Announcements",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF",
                ),
                ft.Text(
                    "No announcements at the moment.",
                    size=16,
                    color=ft.Colors.GREY_200,
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )

    # Free Wall tab content
    def free_wall_tab():
        def post_message(e):
            # Add logic to handle the message (e.g., save or display it)
            print("Message posted:", message_input.value)
            message_input.value = ""  # Clear the input field
            page.update()

        message_input = ft.TextField(
            label="Post a message",
            multiline=True,
            width=500,
            height=60,
            border_color=ft.Colors.BLUE,
            color=ft.Colors.GREY_200,
        )

        return ft.Column(
            controls=[
                ft.Text(
                    "Free Wall",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF",
                ),
                message_input,
                ft.ElevatedButton(
                    text="Post",
                    on_click=post_message,
                    style=ft.ButtonStyle(
                        padding=ft.Padding(10, 10, 10, 10),
                        bgcolor="#B0E0E6",
                    ),
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )

    # Tabs widget for Announcements and Free Wall
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Announcements",
                content=announcements_tab(),
            ),
            ft.Tab(
                text="Free Wall",
                content=free_wall_tab(),
            ),
        ],
        expand=True,
    )

    return ft.View(
        route="/main",
        bgcolor="#2D5DA1",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "CLICS Portal - Main Page",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF",
                    ),
                    tabs,
                    ft.ElevatedButton(
                        text="Logout",
                        on_click=on_logout,
                        style=ft.ButtonStyle(
                            padding=ft.Padding(15, 15, 15, 15),
                            bgcolor="#FF6347",
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
            )
        ],
    )
