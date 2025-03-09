import flet as ft
from utils.colormanager import color_manager
from utils.stylemanager import style_manager
from assets.data.texts import TEXTS


class ExperiencePage(ft.Container):
    def __init__(self, page: ft.Page, theme_mode, language="es"):
        super().__init__()
        self.page = page
        # Agregar verificación de página válida
        if not self.page:
            raise ValueError("La página no puede ser None")
        self.language = language
        self._stop_thread = False

        # Inicializar el gestor de colores y estilos
        self.color_manager = color_manager
        self.style_manager = style_manager
        self.theme_mode = theme_mode

        self.colors = self.color_manager.get_colors(self.theme_mode)

        # Registrar este componente como observador del monitor de la ventana
        self.page.window_monitor.add_observer(self.handle_resize)

        self.page.on_resize = self.update_layout  # Detectar cambios de tamaño

        # Configuración inicial responsive
        self.breakpoint = 800  # Punto de quiebre para mobile/desktop
        self.is_mobile = self.page.width < self.breakpoint

        self.current_text_index = 0  # Índice del texto actual

        # Cargar los textos según el idioma
        self.texts = TEXTS[self.language]["dynamic_texts"]
        self.name = TEXTS[self.language]["name"]
        self.profile = TEXTS[self.language]["profile"]
        self.skills_title = TEXTS[self.language]["skills_title"]
        self.skills_list = TEXTS[self.language]["skills"]

        # Inicializar componentes
        self.build_layout()

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

        # # Contenedor principal con diseño responsive
        # self.content = ft.Column(
        #     controls=self.experiences,
        #     spacing=20,
        #     alignment=ft.MainAxisAlignment.START,
        #     horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        # )

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

        # ? CONSTRUCCION DE LOS COMPONENTES

    def build_components(self):

        self.greeting_text = ft.Text(
            TEXTS[self.language]["greeting"],
            size=self.style_manager.get_text_size("subtitle", self.page.width),
            text_align=ft.TextAlign.LEFT,
            color=self.colors["text"],
        )

        self.profile_text = ft.Container(
            margin=ft.margin.only(right=20),  # Márgen solo a la derecha
            content=ft.Text(
                self.profile,
                size=self.style_manager.get_text_size("body", self.page.width),
                text_align=ft.TextAlign.LEFT,
                color=self.colors["text"],
            ),
        )

    def build_layout(self):
        self.build_components()
        # Crear layout responsive
        if self.is_mobile:
            print("ENTRE A MOVIL")
            self.build_mobile_layout()
        else:
            print("ENTRE A DESKTOP")
            self.build_desktop_layout()

        self.alignment = ft.alignment.center

    def build_mobile_layout(self):
        self.content = ft.Column(
            [
                self.profile_image,
                ft.Divider(height=10),
                self.greeting_text,
                self.name_text,
                self.dynamic_text,
                ft.Container(height=10),
                self.profile_text,
                ft.Container(height=10),
                self.skills_box,
                ft.Container(height=10),
            ],
            spacing=10,
        )

    def build_desktop_layout(self):
        self.content = ft.ResponsiveRow(
            [
                ft.Column(
                    [
                        ft.Container(height=5),
                        self.greeting_text,
                        ft.Container(height=5),
                        self.profile_text,
                        ft.Container(height=5),
                        ft.Container(height=5),
                    ],
                    col=9,
                ),
            ],
            spacing=40,
        )

    def update_layout(self, e=None):
        """Actualiza el layout cuando cambia el tamaño"""
        if not self.page:  # Verificar si la página existe
            return

        new_is_mobile = self.page.width < self.breakpoint
        if new_is_mobile != self.is_mobile:
            self.is_mobile = new_is_mobile
        self.build_layout()
        self.update()

    # ? FUNCIONALIDADES

    def handle_resize(self, new_width):
        """
        Maneja cambios en el tamaño de la pantalla.
        """
        if not self.page:  # Verificar si la página existe
            return
        # Reconstruir la barra de navegación cuando cambia el tamaño de la pantalla

        self.update_layout()

        self.page.update()

    def dispose(self):
        """Detiene el hilo y elimina el observador"""
        self._stop_thread = True
        if self.page and hasattr(self.page, "window_monitor"):
            self.page.window_monitor.remove_observer(
                self.handle_resize
            )  # Eliminar observador
        super().dispose()
