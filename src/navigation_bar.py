import flet as ft
from utils.colormanager import color_manager
from utils.stylemanager import style_manager


class NavigationBar(ft.Container):
    def __init__(self, page: ft.Page, on_nav_click):
        super().__init__()
        self.page = page
        self.on_nav_click = on_nav_click  # Callback para manejar la navegación

        # Inicializar el gestor de colores y estilos
        self.color_manager = color_manager
        self.style_manager = style_manager
        self.theme_mode = "dark"  # Inicia en modo oscuro
        self.colors = self.color_manager.get_colors(self.theme_mode)

        # Estado del menú desplegable
        self.menu_visible = False

        # Indice del boton seleccionado
        self.selected_index = 0

        # Lista de botones de navegación
        self.lista_botones = [
            "Inicio",
            "Experiencia",
            "Estudios",
            "Proyectos",
            "Contacto",
        ]

        # Generación de componentes gráficos
        self.build_components()

        # Registrar este componente como observador del monitor de la ventana
        self.page.window_monitor.add_observer(self.handle_resize)

    def toggle_menu(self, e):
        """
        Alterna la visibilidad del menú desplegable.
        """
        self.menu_visible = not self.menu_visible
        self.menu.visible = self.menu_visible
        self.page.update()

    def toggle_theme(self, e):
        """
        Cambia entre modo oscuro y claro.
        """
        self.theme_mode = "light" if self.theme_mode == "dark" else "dark"
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        self.colors = self.color_manager.get_colors(
            self.theme_mode
        )  # Actualizar colores

        # Actualizar el fondo de la página
        self.page.bgcolor = self.colors["background"]

        # Actualizar el ícono del botón de cambio de tema
        self.change_theme_button.icon = (
            ft.Icons.LIGHT_MODE if self.theme_mode == "dark" else ft.Icons.DARK_MODE
        )

        # Reconstruir los componentes gráficos con los nuevos colores
        self.build_components()
        self.page.update()

    def handle_resize(self, new_width):
        """
        Maneja cambios en el tamaño de la pantalla.
        """

        # Reconstruir la barra de navegación cuando cambia el tamaño de la pantalla
        self.build_components()
        self.page.update()

    def handle_button_click(self, index):
        """
        Maneja el clic en un botón de navegación.
        """
        self.selected_index = index  # Actualizar el índice seleccionado
        self.on_nav_click(index)  # Notificar al padre
        self.build_components()  # Reconstruir los componentes
        self.page.update()

    # ? CONSTRUCCION DE LOS COMPONENTES

    def build_components(self):
        """
        Construye todos los componentes gráficos necesarios.
        """

        # Botón para cambiar el tema
        self.change_theme_button = ft.IconButton(
            icon=(
                ft.Icons.DARK_MODE if self.theme_mode == "dark" else ft.Icons.LIGHT_MODE
            ),
            bgcolor=self.colors["accent_primary"],
            icon_color=self.colors["sun_color"],
            on_click=self.toggle_theme,
        )

        # Logo
        self.logo = ft.Container(
            margin=ft.Margin(10, 0, 0, 0),
            content=ft.Text(
                "Willy Corzo",
                size=self.style_manager.get_text_size("title", self.page.width),
                color=self.colors["text"],
                font_family=style_manager.get_font("terciary"),
            ),
        )

        # Menú desplegable para pantallas pequeñas
        self.menu = ft.Column(
            visible=False,  # Inicialmente oculto
            controls=[
                ft.TextButton(
                    text=dato,
                    style=ft.ButtonStyle(
                        color=self.colors["accent_primary"],
                        padding=10,
                        text_style=ft.TextStyle(
                            size=self.style_manager.get_text_size(
                                "body", self.page.width
                            ),
                            color=self.colors["text"],
                        ),
                    ),
                    on_click=lambda e, index=index: self.handle_button_click(index),
                )
                for index, dato in enumerate(self.lista_botones)
            ],
        )

        # Construir la barra de navegación
        self.build()

    def build_buttons(self):
        """
        Construye los botones de navegación adaptativos.
        """
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.TextButton(
                    text=dato,
                    height=50 if self.page.width > 600 else 30,
                    style=ft.ButtonStyle(
                        color=self.colors["text"],
                        padding=15,
                        animation_duration=300,
                        text_style=ft.TextStyle(
                            size=self.style_manager.get_text_size(
                                "subtitle", self.page.width
                            ),
                            color=self.colors["text"],
                        ),
                        bgcolor=(
                            self.colors["divider"]
                            if index == self.selected_index
                            else None
                        ),
                    ),
                    on_click=lambda e, index=index: self.handle_button_click(index),
                )
                for index, dato in enumerate(self.lista_botones)
            ],
        )

    def build(self):
        """
        Construye la barra de navegación según el tamaño de la pantalla.
        """
        if self.page.width > 800:
            # Para pantallas grandes, mostrar todos los botones horizontalmente
            self.content = ft.Row(
                controls=[
                    self.logo,  # Logo siempre visible
                    ft.VerticalDivider(
                        width=5, thickness=10, color=self.colors["divider"]
                    ),
                    self.build_buttons(),  # Botones adaptativos
                    self.change_theme_button,  # Botón de cambio de tema
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        else:
            # Para pantallas pequeñas, mostrar solo el logo y un ícono de menú
            self.content = ft.Row(
                controls=[
                    self.logo,  # Solo el logo en pantallas pequeñas
                    ft.IconButton(
                        icon=ft.Icons.MENU,
                        on_click=self.toggle_menu,
                        bgcolor=self.colors["accent_primary"],
                        icon_color=self.colors["text"],
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
            # Agregar el menú desplegable (inicialmente oculto)
            self.content.controls.append(self.menu)
