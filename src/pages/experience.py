import flet as ft


class ExperiencePage(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text("Experiencia Profesional", size=24, weight="bold"),
                ft.Text("Gerente de Procesos - Empresa XYZ (2018 - Presente)"),
                ft.Text("Responsable de la optimización de procesos químicos."),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )