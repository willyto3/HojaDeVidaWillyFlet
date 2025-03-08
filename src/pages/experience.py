import flet as ft


class ExperiencePage(ft.Container):
    def __init__(self):
        super().__init__()

        # Lista de experiencias (agrega tantas como necesites)
        self.experiences = [
            self.create_experience_card(
                company_logo="images/copco.jpg",  # URL o ruta local
                position="Desarrollador Full-Stack",
                company="Empresa XYZ",
                period="Ene 2020 - Presente",
                responsibilities=[
                    "Desarrollo de aplicaciones web con Python/Django",
                    "Creación de APIs RESTful con Node.js",
                    "Implementación de interfaces con React",
                ],
            ),
            self.create_experience_card(
                company_logo="images/css-3.png",  # Ruta relativa a tu imagen local
                position="Ingeniero de Software",
                company="Tecnología ABC",
                period="Mar 2018 - Dic 2019",
                responsibilities=[
                    "Desarrollo de microservicios",
                    "Integración de sistemas empresariales",
                    "Automatización de procesos",
                ],
            ),
        ]

        # Contenedor principal con diseño responsive
        self.content = ft.Column(
            controls=self.experiences,
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )

    def create_experience_card(
        self,
        company_logo,
        position,
        company,
        period,
        responsibilities,
    ):
        return ft.Card(
            elevation=5,
            margin=ft.margin.symmetric(vertical=15),
            content=ft.Container(
                padding=10,
                content=ft.Row(
                    [
                        # Columna de imagen (izquierda)
                        ft.Column(
                            [
                                ft.Container(
                                    width=220,
                                    height=220,
                                    bgcolor="transparent",
                                    border_radius=8,
                                    content=ft.Image(
                                        src=company_logo,
                                        width=220,
                                        height=220,
                                        fit=ft.ImageFit.CONTAIN,
                                        border_radius=6,
                                        error_content=ft.Text(
                                            "Sin imagen", color=ft.colors.RED_400
                                        ),
                                    ),
                                )
                            ],
                           
                        ),  # Ajuste de columnas
                        # Columna de información (derecha)
                        ft.Column(
                            [
                                ft.Text(position, weight=ft.FontWeight.BOLD, size=18),
                                ft.Text(company, italic=True, color=ft.colors.GREY_700),
                                ft.Text(period, color=ft.colors.GREY_500),
                                ft.Divider(height=15, color=ft.colors.TRANSPARENT),
                                ft.Text(
                                    "Responsabilidades:", weight=ft.FontWeight.W_600
                                ),
                                ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Icon(
                                                    ft.icons.CHECK_CIRCLE_OUTLINE,
                                                    color=ft.colors.GREEN_500,
                                                    size=16,
                                                ),
                                                ft.Text(responsibility),
                                            ]
                                        )
                                        for responsibility in responsibilities
                                    ],
                                    spacing=8,
                                ),
                            ],
                           
                        ),  # Columnas complementarias
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ),
        )
