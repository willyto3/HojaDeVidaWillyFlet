import flet as ft
from navigation_bar import NavigationBar
from pages.home import HomePage
from pages.experience import ExperiencePage
from pages.education import EducationPage
from pages.projects import ProjectsPage
from pages.contact import ContactPage
from utils.colormanager import color_manager
from utils.stylemanager import style_manager
from window_monitor import WindowMonitor


class Principal(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        # Configuración inicial de la página
        self.padding = 0
        self.expand = True
        self.page.scroll = ft.ScrollMode.AUTO

        # Cargar fuente personalizada desde Google Fonts
        self.page.fonts = {
            "Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap",
            "Roboto": "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap",
            "Sigmar": "https://fonts.googleapis.com/css2?family=Sigmar&display=swap",
        }
        self.page.theme = ft.Theme(
            font_family=style_manager.get_font("primary")
        )  # Establecer fuente predeterminada

        # Configuración inicial del tema
        self.color_manager = color_manager

        self.theme_mode = "dark"  # Inicia en modo oscuro
        self.current_index = 0  # Agregar índice de página actual

        self.colors = self.color_manager.get_colors(self.theme_mode)

        # Configuración inicial de la página
        self.page.title = "Ing. Willy Corzo"
        self.page.bgcolor = self.colors["background"]

        # Inicializar el monitor de la ventana
        self.page.window_monitor = WindowMonitor(page)

        # Construir la interfaz
        self.build()

    def toggle_theme(self):
        """Alterna el tema y actualiza toda la interfaz"""
        self.theme_mode = "light" if self.theme_mode == "dark" else "dark"
        self.colors = self.color_manager.get_colors(self.theme_mode)
        self.page.bgcolor = self.colors["background"]

        # Forzar reconstrucción de la página actual
        self.nav_pages(self.current_index)
        self.navbar.update_theme(self.theme_mode)  # Actualizar navbar

        self.page.update()

    def nav_pages(self, index):
        """
        Cambia entre páginas según el índice seleccionado.
        """
        if index == 0:
            new_page = HomePage(self.page, theme_mode=self.theme_mode)
            self.current_index = 0
        elif index == 1:
            new_page = ExperiencePage(self.page, theme_mode=self.theme_mode)
            self.current_index = 1
        elif index == 2:
            new_page = EducationPage(self.page, theme_mode=self.theme_mode)
            self.current_index = 2
        elif index == 3:
            new_page = ProjectsPage(self.page, theme_mode=self.theme_mode)
            self.current_index = 3
        elif index == 4:
            new_page = ContactPage(self.page, theme_mode=self.theme_mode)
            self.current_index = 4

        self.current_page.content = new_page
        self.page.update()

    def build(self):
        """
        Construye la interfaz principal.
        """
        # Instancia de la barra de navegación
        self.navbar = NavigationBar(
            page=self.page,
            on_nav_click=self.nav_pages,
            on_theme_toggle=self.toggle_theme,
            theme_mode=self.theme_mode,  # Nombre correcto del parámetro
        )

        # Corregir inicialización de HomePage
        self.current_page = ft.Container(
            content=HomePage(self.page, theme_mode=self.theme_mode),
            expand=True,
            alignment=ft.alignment.center,
        )

        # Diseño principal de la página
        self.content = ft.Column(
            spacing=25,
            alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra horizontalmente
            expand=True,
            controls=[
                self.navbar,  # Barra de navegación
                self.current_page,  # Contenido dinámico
            ],
        )

        # Limpiar la página antes de agregar el contenido
        self.page.clean()
        self.page.add(self.content)

        # Actualizar la página
        self.page.update()
