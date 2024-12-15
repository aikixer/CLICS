import flet as ft

def front_page(page: ft.Page):
    # Route handler
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            show_front_page()
        elif page.route == "/login":
            show_login_panel()
        page.update()

    def show_front_page():
        title = ft.Text(
            "Welcome to CLICS Portal",
            size=50,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )

        subtitle = ft.Text(
            "Campus League of Ingenious Computer Science Students.",
            size=16,
            color=ft.Colors.GREY_200,
            text_align=ft.TextAlign.JUSTIFY,
        )

        logo_image = ft.Image(
            src="assets/clics.png",  # Replace with your logo's actual path
            width=300,
            height=300,
        )

        def on_get_started(e):
            page.go("/login")  # Navigate to login panel

        get_started_button = ft.ElevatedButton(
            text="Get Started",
            on_click=on_get_started,
            style=ft.ButtonStyle(
                padding=ft.Padding(15, 15, 15, 15),
                bgcolor="#B0E0E6",
            ),
        )

        page.views.append(
            ft.View(
                route="/",
                bgcolor="#2D5DA1",  # Explicitly set the background color
                controls=[
                    ft.Column(
                        controls=[
                            logo_image,
                            title,
                            subtitle,
                            ft.Row(
                                controls=[get_started_button],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    )
                ]
            )
        )

    def show_login_panel():
        login_title = ft.Text(
            "LOGIN",
            size=80,
            weight=ft.FontWeight.BOLD,
            color="#002244",
            text_align=ft.TextAlign.CENTER,
        )

        username_field = ft.TextField(
            label="Username",
            width=500,
            height=40,
            border_color=ft.Colors.BLUE,
            color=ft.Colors.GREY_200,
            label_style=ft.TextStyle(color=ft.Colors.GREY_200),
        )

        password_field = ft.TextField(
            label="Password",
            password=True,
            width=500,
            height=40,
            border_color=ft.Colors.BLUE,
            color=ft.Colors.GREY_200,
            label_style=ft.TextStyle(color=ft.Colors.GREY_200),
        )

        def on_login(e):
            page.go("/")  # Navigate back to front page after login (replace with actual logic)

        login_button = ft.ElevatedButton(
            text="Login",
            on_click=on_login,
            style=ft.ButtonStyle(
                padding=ft.Padding(15, 15, 15, 15),
                bgcolor="#B0E0E6",
            ),
        )

        page.views.append(
            ft.View(
                route="/login",
                bgcolor="#2D5DA1",  # Explicitly set the background color
                controls=[
                    ft.Column(
                        controls=[
                            login_title,
                            username_field,
                            password_field,
                            ft.Row(
                                controls=[login_button],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    )
                ]
            )
        )

    # Assign route change handler
    page.on_route_change = route_change
    # Initialize to front page
    page.go("/")

# Start the Flet app
ft.app(target=front_page)
