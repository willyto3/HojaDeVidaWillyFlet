class StyleManager:
    """
    Clase para manejar los estilos globales de la aplicación.
    """

    def __init__(self):
        # Definir tamaños de texto para diferentes anchos de pantalla
        self.text_sizes = {
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
                "xs": 12,
                "sm": 14,
                "md": 16,
                "lg": 18,
                "xl": 20,
            },
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


# Instancia global de StyleManager
style_manager = StyleManager()