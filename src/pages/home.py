import flet as ft
import time

from utils.colormanager import color_manager
from utils.stylemanager import style_manager
from assets.data.texts import TEXTS


class HomePage(ft.Container):
    def __init__(self, page: ft.Page, language="es"):
        super().__init__()
        self.page = page
        self.language = language  # Idioma seleccionado

        # Inicializar el gestor de colores y estilos
        self.color_manager = color_manager
        self.style_manager = style_manager
        self.theme_mode = "dark"  # Inicia en modo oscuro
        self.colors = self.color_manager.get_colors(self.theme_mode)

        # Cargar los textos según el idioma
        self.texts = TEXTS[self.language]["dynamic_texts"]
        self.profile = TEXTS[self.language]["profile"]
        self.skills_title = TEXTS[self.language]["skills_title"]
        self.skills_list = TEXTS[self.language]["skills"]

        self.current_text_index = 0  # Índice del texto actual

        # Cuadro de habilidades
        self.skills_box = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        self.skills_title,
                        size=self.style_manager.get_text_size(
                            "subtitle", self.page.width
                        ),
                    ),
                    ft.Divider(height=5, color="transparent"),
                    ft.Row(
                        wrap=True,  # Permite que los elementos se ajusten al ancho
                        spacing=10,
                        controls=[
                            self.create_skill_chip(skill) for skill in self.skills_list
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=ft.padding.all(10),
            bgcolor="#1E1E1E",  # Color de fondo oscuro
            border_radius=10,
            expand=True,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "black"),
            ),
        )

        # Texto dinámico que cambiará con el tiempo
        self.dynamic_text = ft.Text(
            value=self.texts[self.current_text_index],
            size=self.style_manager.get_text_size("title", self.page.width),
            text_align=ft.TextAlign.LEFT,
            animate_opacity=300,  # Animación de opacidad
        )

        # Contenido principal
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
            expand=True,  # Expandir para ocupar todo el espacio disponible
            controls=[
                # Columna para la imagen
                ft.Column(
                    controls=[
                        ft.Image(
                            src="/images/WillyNegro.png",  # URL de la imagen (puedes cambiarla)
                            width=500,  # Ancho de la imagen
                            height=750,  # Alto de la imagen
                            fit=ft.ImageFit.COVER,  # Ajuste de la imagen
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
                    expand=3,  # Ocupa el 30% del espacio disponible
                ),
                # Columna para el texto
                ft.Column(
                    controls=[
                        ft.Text(
                            "Hola, Mi Nombre es",
                            size=self.style_manager.get_text_size(
                                "subtitle", self.page.width
                            ),
                            weight="bold",
                            text_align=ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            "Willy Corzo Lubo",
                            size=80,
                            weight="bold",
                            text_align=ft.TextAlign.LEFT,
                        ),
                        self.dynamic_text,  # Texto dinámico
                        ft.Text(
                            self.profile,
                            size=self.style_manager.get_text_size(
                                "body", self.page.width
                            ),
                            text_align=ft.TextAlign.LEFT,
                        ),
                        ft.Divider(height=10, color="transparent"),  # Espaciado
                        self.skills_box,  # Cuadro de habilidades
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
                    horizontal_alignment=ft.CrossAxisAlignment.START,  # Alinear a la izquierda
                    expand=7,  # Ocupa el 70% del espacio disponible
                ),
            ],
        )

        # Iniciar el temporizador para cambiar el texto
        self.start_text_animation()

    def create_skill_chip(self, skill_name):
        """
        Crea un chip de habilidad con diseño personalizado.
        """
        return ft.Container(
            content=ft.Text(
                skill_name,
                size=self.style_manager.get_text_size("body", self.page.width),
                color="white",
            ),
            padding=ft.padding.symmetric(horizontal=15, vertical=5),
            bgcolor="#2E7D32",  # Color verde oscuro
            border_radius=20,
        )

    def start_text_animation(self):
        """
        Inicia un hilo para cambiar el texto dinámico.
        """

        def change_text():
            while True:
                # Actualizar el índice del texto
                self.current_text_index = (self.current_text_index + 1) % len(
                    self.texts
                )
                self.dynamic_text.value = self.texts[self.current_text_index]

                # Animación de desvanecimiento
                self.dynamic_text.opacity = 0
                self.page.update()

                self.dynamic_text.opacity = 1
                self.page.update()

                # Esperar 5 segundos antes de cambiar el texto nuevamente
                time.sleep(5)

        # Ejecutar el cambio de texto en un hilo separado
        import threading

        threading.Thread(target=change_text, daemon=True).start()
