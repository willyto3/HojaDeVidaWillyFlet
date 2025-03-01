import flet as ft


class EducationPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text("Educación", size=24, weight="bold"),
                ft.Text("Ingeniería Química - Universidad ABC (2014 - 2018)"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )