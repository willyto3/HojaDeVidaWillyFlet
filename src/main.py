import flet as ft
from principal import Principal


# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(
        target=lambda page: Principal(page), view=ft.WEB_BROWSER, assets_dir="assets"
    )
