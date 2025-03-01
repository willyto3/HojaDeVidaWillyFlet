import flet as ft


class HomePage(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text("Bienvenido a mi Hoja de Vida", size=30, weight="bold"),
                ft.Text("Soy un ingeniero químico con experiencia en procesos industriales."),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )