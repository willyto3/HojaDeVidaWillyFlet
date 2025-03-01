import flet as ft


class ContactPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text("Contacto", size=24, weight="bold"),
                ft.Text("Correo Electrónico: willy.corzo@example.com"),
                ft.Text("Teléfono: +123 456 7890"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )