class ColorManager:
    """
    Clase para manejar los colores de la aplicación en modo claro y oscuro.
    """

    def __init__(self):
        self.light_theme = {
            "background": "#FAFAFA",  # Blanco suave
            "text": "#212121",  # Negro profundo
            "accent_primary": "#0D47A1",  # Azul profundo (seguridad y confianza)
            "accent_secondary": "#FFA726",  # Naranja brillante (logros y energía)
            "divider": "#EEEEEE",  # Gris claro
            "sun_color": "yellow",  # Amarillo
        }

        # Definir colores para el tema oscuro
        self.dark_theme = {
            "background": "#1E1E2F",  # Azul profundo oscuro
            "text": "#E0E0E0",  # Gris claro
            "accent_primary": "#1976D2",  # Azul profundo (consistente con el tema claro)
            "accent_secondary": "#FFA726",  # Naranja brillante (consistente con el tema claro)
            "divider": "#33334F",  # Azul grisáceo oscuro
            "sun_color": "#212121",  # Negro profundo
        }

        # Tema actual (por defecto, claro)
        self.current_theme = "light"

    def get_colors(self, theme_mode):
        """
        Retorna los colores correspondientes al tema seleccionado.
        :param theme_mode: "dark" o "light"
        :return: Diccionario de colores
        """
        if theme_mode == "dark":
            return self.dark_theme
        return self.light_theme


# Instancia global de ColorManager
color_manager = ColorManager()
