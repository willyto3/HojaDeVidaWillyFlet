import flet as ft


class ProjectsPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text("Proyectos", size=24, weight="bold"),
                ft.Text("Optimización de Procesos Industriales"),
                ft.Text("Desarrollo de Sistemas de Control Automático"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )