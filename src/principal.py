import flet as ft
from navigation_bar import NavigationBar
from pages.home import HomePage
from pages.experience import ExperiencePage
from pages.education import EducationPage
from pages.projects import ProjectsPage
from pages.contact import ContactPage
from utils.colormanager import color_manager
from window_monitor import WindowMonitor


class Principal(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 0
        self.expand = True

        # Configuración inicial del tema
        self.color_manager = color_manager
        self.theme_mode = "dark"  # Inicia en modo oscuro
        self.page.theme_mode = ft.ThemeMode.DARK
        self.colors = self.color_manager.get_colors(self.theme_mode)

        # Configuración inicial de la página
        self.page.title = "Ing. Willy Corzo"
        self.page.bgcolor = self.colors["background"]

        # Inicializar el monitor de la ventana
        self.page.window_monitor = WindowMonitor(page)

        # Construir la interfaz
        self.build()

    def nav_pages(self, index):
        """
        Cambia entre páginas según el índice seleccionado.
        """
        if index == 0:
            self.current_page.content = HomePage()
        elif index == 1:
            self.current_page.content = ExperiencePage()
        elif index == 2:
            self.current_page.content = EducationPage()
        elif index == 3:
            self.current_page.content = ProjectsPage()
        elif index == 4:
            self.current_page.content = ContactPage()
        self.page.update()

    def build(self):
        """
        Construye la interfaz principal.
        """
        # Instancia de la barra de navegación
        self.navbar = NavigationBar(page=self.page, on_nav_click=self.nav_pages)

        # Contenido inicial (página de inicio)
        self.current_page = ft.Container(content=HomePage(), expand=True)

        # Diseño principal de la página
        self.content = ft.Column(
            spacing=2,
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
