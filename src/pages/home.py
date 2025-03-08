import time
import flet as ft
from utils.colormanager import color_manager
from utils.stylemanager import style_manager
from assets.data.texts import TEXTS


class HomePage(ft.Container):
    def __init__(self, page: ft.Page, language="es"):
        super().__init__()
        self.page = page
        self.language = language

        # Inicializar el gestor de colores y estilos
        self.color_manager = color_manager
        self.style_manager = style_manager
        self.colors = self.color_manager.get_colors(self.theme_mode)

        self.page.on_resize = self.update_layout  # Detectar cambios de tamaño

        # Cargar los textos según el idioma
        self.texts = TEXTS[self.language]["dynamic_texts"]
        self.name = TEXTS[self.language]["name"]
        self.profile = TEXTS[self.language]["profile"]
        self.skills_title = TEXTS[self.language]["skills_title"]
        self.skills_list = TEXTS[self.language]["skills"]

        # Configuración inicial responsive
        self.breakpoint = 800  # Punto de quiebre para mobile/desktop
        self.is_mobile = self.page.width < self.breakpoint

        # Inicializar componentes
        self.build_components()
        self.build_layout()

        # Registrar este componente como observador del monitor de la ventana
        self.page.window_monitor.add_observer(self.handle_resize)

    def handle_resize(self, new_width):
        """
        Maneja cambios en el tamaño de la pantalla.
        """

        print("ENTRE A CONSTRUIR LOS COMPONENTES")

        # Reconstruir la barra de navegación cuando cambia el tamaño de la pantalla
        self.build_components()
        self.update_layout()
        # self.build_layout()
        self.page.update()

    def build_components(self):

        print(self.style_manager.get_text_size("megatitle", self.page.width))

        self.greeting_text = ft.Text(
            TEXTS[self.language]["greeting"],
            size=self.style_manager.get_text_size("subtitle", self.page.width),
            text_align=ft.TextAlign.LEFT,
        )

        self.name_text = ft.Text(
            self.name,
            size=self.style_manager.get_text_size("megatitle", self.page.width),
            weight="bold",
            text_align=ft.TextAlign.LEFT,
        )

        # Contenedor de imagen responsive
        self.profile_image = ft.Container(
            content=ft.Image(
                src="images/WillyNegro.png",
                fit=ft.ImageFit.COVER,
                width=self.get_image_size()[0],
                height=self.get_image_size()[1],
            ),
            border_radius=ft.border_radius.all(10),
        )

        # Contenido principal responsive
        self.content_text = ft.Text(
            "Contenido principal",
            size=self.get_scaled_font(3),
            text_align=ft.TextAlign.JUSTIFY,
        )

    def build_layout(self):
        # Crear layout responsive
        if self.is_mobile:
            print("ENTRE A MOVIL")
            self.build_mobile_layout()
        else:
            print("ENTRE A DESKTOP")
            self.build_desktop_layout()

        self.alignment = ft.alignment.center
        self.margin = ft.margin.all(self.get_scaled_font(1))

    def build_mobile_layout(self):
        self.content = ft.Column(
            [
                self.profile_image,
                ft.Divider(height=10),
                self.greeting_text,
                self.name_text,
                
                
                ft.Container(height=20),
                self.content_text,
            ],
            spacing=5,
        )

    def build_desktop_layout(self):
        self.content = ft.ResponsiveRow(
            [
                ft.Column([self.profile_image], col=3),
                ft.Column(
                    [
                        ft.Container(height=20, bgcolor="red"),
                        self.greeting_text,
                        self.name_text,
                    ],
                    col=9,
                ),
            ],
            spacing=10,
        )

    def get_scaled_font(self, percentage: float) -> float:
        """Calcula tamaño de fuente basado en ancho de pantalla"""
        return max(12, min(self.page.width * percentage / 100, 24))

    def get_image_size(self) -> tuple:
        """Calcula tamaño de imagen responsive"""
        if self.is_mobile:
            return (self.page.width * 0.8, 300)
        return (400, 500)

    def update_layout(self, e=None):
        """Actualiza el layout cuando cambia el tamaño"""
        print(self.page.width)
        print(self.breakpoint)
        new_is_mobile = self.page.width < self.breakpoint
        print(new_is_mobile)
        if new_is_mobile != self.is_mobile:
            self.is_mobile = new_is_mobile
            self.build_layout()
            self.update()


#         # Inicializar componentes
#         self.init_components()
#         self.build_layout()


#         self.current_text_index = 0  # Índice del texto actual

#         # Indice del boton seleccionado
#         self.selected_index = 0


#         # Generación de componentes gráficos
#         self.build_components()


#     def start_text_animation(self):
#         """
#         Inicia un hilo para cambiar el texto dinámico.
#         """

#         def change_text():
#             while True:
#                 # Actualizar el índice del texto
#                 self.current_text_index = (self.current_text_index + 1) % len(
#                     self.texts
#                 )
#                 self.dynamic_text.value = self.texts[self.current_text_index]

#                 # Animación de desvanecimiento
#                 self.dynamic_text.opacity = 0
#                 self.page.update()

#                 self.dynamic_text.opacity = 1
#                 self.page.update()

#                 # Esperar 5 segundos antes de cambiar el texto nuevamente
#                 time.sleep(5)

#         # Ejecutar el cambio de texto en un hilo separado
#         import threading

#         threading.Thread(target=change_text, daemon=True).start()

#     # ? CONSTRUCCION DE LOS COMPONENTES

#     def create_skill_chip(self, skill_name):
#         """
#         Crea un chip de habilidad con diseño personalizado.
#         """
#         return ft.Container(
#             content=ft.Text(
#                 skill_name,
#                 size=self.style_manager.get_text_size("body", self.page.width),
#                 color="white",
#             ),
#             padding=ft.padding.symmetric(horizontal=15, vertical=5),
#             bgcolor=self.colors["accent_primary"],
#         )

#     def build_components(self):
#         """
#         Construye todos los componentes gráficos necesarios.
#         """

#         # Texto dinámico que cambiará con el tiempo
#         self.dynamic_text = ft.Text(
#             value=self.texts[self.current_text_index],
#             size=self.style_manager.get_text_size("title", self.page.width),
#             text_align=ft.TextAlign.LEFT,
#             animate_opacity=300,  # Animación de opacidad
#         )

#         # Iniciar el temporizador para cambiar el texto
#         self.start_text_animation()

#         # Cuadro de habilidades
#         self.skills_box = ft.Container(
#             content=ft.Column(
#                 controls=[
#                     ft.Text(
#                         self.skills_title,
#                         size=self.style_manager.get_text_size(
#                             "subtitle", self.page.width
#                         ),
#                     ),
#                     ft.Divider(height=5, color="transparent"),
#                     ft.Row(
#                         wrap=True,  # Permite que los elementos se ajusten al ancho
#                         spacing=10,
#                         controls=[
#                             self.create_skill_chip(skill) for skill in self.skills_list
#                         ],
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.START,
#                 horizontal_alignment=ft.CrossAxisAlignment.START,
#             ),
#             border_radius=10,
#             expand=True,
#         )

#         # Contenido principal
#         self.content = ft.Row(
#             alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
#             expand=True,  # Expandir para ocupar todo el espacio disponible
#             controls=[
#                 # Columna para la imagen
#                 ft.Column(
#                     controls=[
#                         ft.Image(
#                             src="/images/WillyNegro.png",  # URL de la imagen (puedes cambiarla)
#                             width=500,  # Ancho de la imagen
#                             height=750,  # Alto de la imagen
#                             fit=ft.ImageFit.COVER,  # Ajuste de la imagen
#                         )
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
#                     expand=3,  # Ocupa el 30% del espacio disponible
#                 ),
#                 # Columna para el texto
#                 ft.Column(
#                     controls=[

#
#                         self.dynamic_text,  # Texto dinámico
#                         ft.Container(
#                             padding=ft.padding.only(right=50),  # Padding a la derecha
#                             content=ft.Text(
#                                 self.profile,
#                                 size=self.style_manager.get_text_size(
#                                     "body", self.page.width
#                                 ),
#                                 text_align=ft.TextAlign.JUSTIFY,
#                             ),
#                         ),
#                         ft.Divider(height=10, color="transparent"),  # Espaciado
#                         self.skills_box,  # Cuadro de habilidades
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
#                     horizontal_alignment=ft.CrossAxisAlignment.START,  # Alinear a la izquierda
#                     expand=7,  # Ocupa el 70% del espacio disponible
#                 ),
#             ],
#         )

#         # Menú desplegable para pantallas pequeñas
#         self.menu = ft.Column(
#             visible=False,  # Inicialmente oculto
#             controls=[
#                 ft.TextButton(
#                     text=dato,
#                     style=ft.ButtonStyle(
#                         color=self.colors["accent_primary"],
#                         padding=10,
#                         text_style=ft.TextStyle(
#                             size=self.style_manager.get_text_size(
#                                 "body", self.page.width
#                             ),
#                             color=self.colors["text"],
#                         ),
#                     ),
#                     on_click=lambda e, index=index: self.handle_button_click(index),
#                 )
#                 for index, dato in enumerate(self.lista_botones)
#             ],
#         )

#         # Construir la barra de navegación
#         self.build()

#     def build(self):
#         """
#         Construye la barra de navegación según el tamaño de la pantalla.
#         """
#         if self.page.width > 800:
#             # Para pantallas grandes, mostrar todos los botones horizontalmente
#             self.content = ft.Row(
#                 controls=[
#                     self.content,
#                     ft.VerticalDivider(
#                         width=5, thickness=10, color=self.colors["divider"]
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
#                 expand=True,
#             )
#         else:
#             # Para pantallas pequeñas, mostrar solo el logo y un ícono de menú
#             self.content = ft.Row(
#                 controls=[
#                     ft.IconButton(
#                         icon=ft.Icons.MENU,
#                         bgcolor=self.colors["accent_primary"],
#                         icon_color=self.colors["text"],
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
#                 expand=True,
#             )
#             # Agregar el menú desplegable (inicialmente oculto)
#             self.content.controls.append(self.menu)
