import flet as ft


class Principal(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 0
        self.expand = True
        self.page.title = "Ing. Willy Corzo"

        self.primary_color = ft.Colors.BLACK

        self.build()

    def build(self):

        self.change_theme = ft.IconButton(
            icon=ft.Icons.DARK_MODE,
            bgcolor=self.primary_color,
            on_click=self.toggle_dark_mode,
        )

        self.logo = ft.Container(
            margin=ft.Margin(20, 0, 0, 0),
            content=ft.Text("Willy Corzo", size=30),
        )

        self.theme_logo = ft.Container(
            width=50,
            margin=ft.Margin(0, 0, 20, 0),
            content=self.change_theme,
        )

        self.buttons = ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.END,
            spacing=0,
            expand=True,
            controls=[
                ft.TextButton(
                    text="Inicio",
                    style=ft.ButtonStyle(color=self.primary_color),
                    col={"xs": 12, "sm": 6, "lg": 2},
                    on_click=lambda e: self.nav_pages(0),
                ),
                ft.TextButton(
                    "Experiencia",
                    style=ft.ButtonStyle(color=self.primary_color),
                    col={"xs": 12, "sm": 6, "lg": 2},
                    on_click=lambda e: self.nav_pages(1),
                ),
                ft.TextButton(
                    "Estudios",
                    style=ft.ButtonStyle(color=self.primary_color),
                    col={"xs": 12, "sm": 6, "lg": 2},
                    on_click=lambda e: self.nav_pages(2),
                ),
                ft.TextButton(
                    "Proyectos",
                    style=ft.ButtonStyle(color=self.primary_color),
                    col={"xs": 12, "sm": 6, "lg": 2},
                    on_click=lambda e: self.nav_pages(3),
                ),
                ft.TextButton(
                    "Contacto",
                    style=ft.ButtonStyle(color=self.primary_color),
                    col={"xs": 12, "sm": 6, "lg": 2},
                    on_click=lambda e: self.nav_pages(4),
                ),
            ],
        )

        self.content = ft.Column(
            spacing=2,
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Row(
                        controls=[
                            self.logo,
                            self.buttons,
                            ft.VerticalDivider(width=5, thickness=10),
                            self.theme_logo,
                        ],
                    ),
                ),
                ft.Container(),
                ft.Container(),
            ],
        )

        self.page.add(self.content)

    def nav_pages(self, e):
        print("e", e)

    def toggle_dark_mode(self, e):

        if e.control.icon == ft.Icons.DARK_MODE:
            print("LIGHT_MODE")
            self.change_theme.icon = ft.Icons.LIGHT_MODE
            self.page.theme_mode = ft.ThemeMode.LIGHT
        else:
            print("DARK_MODE")
            self.change_theme.icon = ft.Icons.DARK_MODE
            self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()


ft.app(target=lambda page: Principal(page), view=ft.WEB_BROWSER, assets_dir="assets")
