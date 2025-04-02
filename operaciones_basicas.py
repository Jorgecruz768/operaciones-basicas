"""Módulo de operaciones matemáticas básicas.

Este script contiene ejemplos de operaciones básicas como suma, resta y cálculo de promedio,
implementadas en clases Python siguiendo las buenas prácticas de estilo.
"""


class OperacionesBasicas:
    """Clase para realizar operaciones aritméticas básicas.

    Permite realizar sumas y restas, almacenando el resultado
    que puede ser recuperado posteriormente.
    """

    def __init__(self):
        """Inicializa la clase con un resultado predeterminado a cero."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado.

        Args:
            a (int or float): Primer operando.
            b (int or float): Segundo operando.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado.

        Args:
            a (int or float): Minuendo.
            b (int or float): Sustraendo.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado de la última operación realizada.

        Returns:
            int or float: Resultado almacenado.
        """
        return self.resultado


# pylint: disable=too-few-public-methods
class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la calculadora con una lista de valores.

        Args:
            valores (list): Lista de números a promediar.
        """
        self.valores = valores

    def calcular_promedio(self):
        """Calcula el promedio aritmético de los valores almacenados.

        Returns:
            float: Promedio de los valores.
        """
        suma = 0
        for valor in self.valores:
            suma += valor
        promediolocal = suma / len(self.valores)
        return promediolocal

# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
