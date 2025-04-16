# Este script contiene errores comunes que violan las normas PEP 8

"""Incluye las clases FiguraGeometrica (abstracta), Rectangulo, Triangulo y Circulo.
Cada clase implementa un método para calcular el área de la figura correspondiente."""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas.

    Esta clase define la interfaz para calcular el área de una figura geométrica.
    Todas las figuras geométricas concretas (como rectángulos, triángulos, círculos, etc.)
    deben implementar el método 'calcular_area' para calcular el área de la figura."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""

    def descripcion(self):
        """Método que devuelve una breve descripción de la figura."""
        return "Figura geométrica abstracta"


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo.

        Esta clase hereda de FiguraGeometrica y permite calcular el área de un rectángulo,
        dados su base y altura."""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        area = self.base * self.altura
        return area


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo.

        Esta clase hereda de FiguraGeometrica y permite calcular el área de un triángulo,
        dados su base y altura."""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        area = (self.base * self.altura) / 2
        return area


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo.

        Esta clase hereda de FiguraGeometrica y permite calcular el área de un círculo,
        dado su radio."""
    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        area = self.pi * (self.radio ** 2)
        return area


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
