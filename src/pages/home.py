import time
import flet as ft
from utils.colormanager import color_manager
from utils.stylemanager import style_manager
from assets.data.texts import TEXTS


class HomePage(ft.Container):
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

        self.current_text_index = 0  # Índice del texto actual

        # Cargar los textos según el idioma
        self.texts = TEXTS[self.language]["dynamic_texts"]
        self.name = TEXTS[self.language]["name"]
        self.profile = TEXTS[self.language]["profile"]
        self.skills_title = TEXTS[self.language]["skills_title"]
        self.skills_list = TEXTS[self.language]["skills"]

        # Registrar este componente como observador del monitor de la ventana
        self.page.window_monitor.add_observer(self.handle_resize)

        self.page.on_resize = self.update_layout  # Detectar cambios de tamaño

        # Configuración inicial responsive
        self.breakpoint = 800  # Punto de quiebre para mobile/desktop
        self.is_mobile = self.page.width < self.breakpoint

        # Inicializar componentes
        self.build_layout()

    # ? CONSTRUCCION DE LOS COMPONENTES

    def build_components(self):

        # Contenedor de imagen responsive
        self.profile_image = ft.Container(
            content=ft.Image(
                src="images/WillyNegro.png",
                fit=ft.ImageFit.COVER,
                width=self.get_image_size()[0],
                height=self.get_image_size()[1],
            ),
            border_radius=ft.border_radius.all(10),
            alignment=ft.alignment.center,
        )

        self.greeting_text = ft.Text(
            TEXTS[self.language]["greeting"],
            size=self.style_manager.get_text_size("subtitle", self.page.width),
            text_align=ft.TextAlign.LEFT,
            color=self.colors["text"],
        )

        self.name_text = ft.Text(
            self.name,
            size=self.style_manager.get_text_size("megatitle", self.page.width),
            weight="bold",
            text_align=ft.TextAlign.LEFT,
            color=self.colors["text"],
        )

        # Texto dinámico que cambiará con el tiempo
        self.dynamic_text = ft.Text(
            value=self.texts[self.current_text_index],
            size=self.style_manager.get_text_size("title", self.page.width),
            text_align=ft.TextAlign.LEFT,
            animate_opacity=300,  # Animación de opacidad
            color=self.colors["text"],
        )

        # Iniciar el temporizador para cambiar el texto
        self.start_text_animation()

        self.profile_text = ft.Container(
            margin=ft.margin.only(right=20),  # Márgen solo a la derecha
            content=ft.Text(
                self.profile,
                size=self.style_manager.get_text_size("body", self.page.width),
                text_align=ft.TextAlign.LEFT,
                color=self.colors["text"],
            ),
        )

        # Cuadro de habilidades
        self.skills_box = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        self.skills_title,
                        size=self.style_manager.get_text_size(
                            "subtitle", self.page.width
                        ),
                        color=self.colors["text"],
                    ),
                    ft.Divider(height=5, color="transparent"),
                    ft.Row(
                        wrap=True,
                        spacing=10,
                        controls=[
                            ft.Chip(
                                label=ft.Text(
                                    skill,
                                    color=self.colors["text"],
                                    size=self.style_manager.get_text_size(
                                        "body", self.page.width
                                    ),
                                ),
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=ft.padding.all(10),
                            )
                            for skill in self.skills_list
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            border_radius=10,
            expand=True,
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
                ft.Column([self.profile_image], col=3),
                ft.Column(
                    [
                        ft.Container(height=5),
                        self.greeting_text,
                        self.name_text,
                        self.dynamic_text,
                        ft.Container(height=5),
                        self.profile_text,
                        ft.Container(height=5),
                        self.skills_box,
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

    def start_text_animation(self):
        """
        Inicia un hilo para cambiar el texto dinámico.
        """

        def change_text():
            while not self._stop_thread:
                # Actualizar el índice del texto
                self.current_text_index = (self.current_text_index + 1) % len(
                    self.texts
                )
                self.dynamic_text.value = self.texts[self.current_text_index]

                # Animación de desvanecimiento
                self.dynamic_text.opacity = 0
                if self.page and not self._stop_thread:
                    self.page.update()

                self.dynamic_text.opacity = 1
                if self.page and not self._stop_thread:
                    self.page.update()

                # Esperar 5 segundos antes de cambiar el texto nuevamente
                time.sleep(5)

        # Ejecutar el cambio de texto en un hilo separado
        import threading

        threading.Thread(target=change_text, daemon=True).start()

    def get_image_size(self) -> tuple:

        if self.page.width < self.breakpoint:
            return (self.page.width * 0.8, self.page.width * 0.8 * 0.75)  # Ratio 4:3
        return (self.page.width * 0.3, self.page.width * 0.3 * 1.4)  # Ratio 2:3
