class StyleManager:
    """
    Clase para manejar los estilos globales de la aplicación.
    """

    def __init__(self):
        # Definir tamaños de texto para diferentes anchos de pantalla
        self.text_sizes = {
            "megatitle": {
                "xs": 50,  # Pantallas pequeñas (móviles)
                "sm": 60,  # Pantallas medianas (tablets)
                "md": 70,  # Pantallas grandes (escritorio estándar)
                "lg": 80,  # Pantallas muy grandes (monitores grandes)
                "xl": 90,  # Pantallas extra grandes
            },
            "title": {
                "xs": 20,  # Pantallas pequeñas (móviles)
                "sm": 24,  # Pantallas medianas (tablets)
                "md": 30,  # Pantallas grandes (escritorio estándar)
                "lg": 36,  # Pantallas muy grandes (monitores grandes)
                "xl": 40,  # Pantallas extra grandes
            },
            "subtitle": {
                "xs": 16,
                "sm": 18,
                "md": 20,
                "lg": 24,
                "xl": 28,
            },
            "body": {
                "xs": 10,
                "sm": 12,
                "md": 14,
                "lg": 16,
                "xl": 18,
            },
        }

        # Definir fuentes para diferentes tipos de texto
        self.fonts = {
            "primary": "Poppins",  # Fuente principal
            "secondary": "Roboto",  # Fuente secundaria (opcional)
            "terciary": "Sigmar",  # Fuente secundaria (opcional)
        }

    def get_text_size(self, text_type, width):
        """
        Retorna el tamaño de texto correspondiente al tipo y ancho de pantalla.
        :param text_type: "title", "subtitle" o "body"
        :param width: Ancho de la pantalla
        :return: Tamaño de texto
        """
        if width > 1400:  # Pantallas extra grandes
            return self.text_sizes[text_type]["xl"]
        elif width > 1200:  # Pantallas muy grandes
            return self.text_sizes[text_type]["lg"]
        elif width > 900:  # Pantallas grandes
            return self.text_sizes[text_type]["md"]
        elif width > 600:  # Pantallas medianas
            return self.text_sizes[text_type]["sm"]
        else:  # Pantallas pequeñas
            return self.text_sizes[text_type]["xs"]

    def get_font(self, font_type="primary"):
        """
        Retorna la fuente correspondiente al tipo especificado.
        :param font_type: "primary" o "secondary"
        :return: Nombre de la fuente
        """
        return self.fonts.get(font_type, "Poppins")  # Por defecto, usa "Poppins"


# Instancia global de StyleManager
style_manager = StyleManager()
