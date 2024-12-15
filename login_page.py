import flet as ft

def login_page(page: ft.Page):
    # Title and other UI elements for the login page
    title = ft.Text(
        "LOGIN",
        size=50,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="#002244",
    )

    username_input = ft.TextField(
        label="Username",
        width=500,
        color=ft.Colors.GREY_200,
    )

    password_input = ft.TextField(
        label="Password",
        password=True,
        width=500,
        color=ft.Colors.GREY_200,
    )

    def on_login(e):
        # Check if fields are filled out
        if username_input.value and password_input.value:
            page.go("/main")  # Navigate to the main page
        else:
            # Display error message if username or password is empty
            page.add(ft.Text("Please fill in both fields", color=ft.Colors.RED))
            page.update()

    login_button = ft.ElevatedButton(
        text="Login",
        on_click=on_login,
        style=ft.ButtonStyle(
            padding=ft.Padding(15, 15, 15, 15),
            bgcolor="#B0E0E6",
        ),
    )

    return ft.View(
        route="/login",
        bgcolor="#2D5DA1",
        controls=[
            ft.Column(
                controls=[
                    title,
                    username_input,
                    password_input,
                    login_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ]
    )
