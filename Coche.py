"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Alejandro Priego Izquierdo.
"""


class Vehiculo:
    """
    Esta clase nos permite simular el comportamiento de un vehículo.
    """
    color = 'rojo'
    fabricante = 'seat'
    num_serie = 1

    def __init__(self, num_serie, color, fabricante):
        """
        Constructor de la clase Vehículo.
        :param num_serie: Número de serie del vehículo.
        :param color: Color del vehículo.
        :param fabricante: Fabricante del Vehículo.
        """
        self.__num_serie = num_serie
        self.__color = color
        self.__fabricante = fabricante

    @property
    def num_serie(self):
        """
        Getter del número de serie del vehículo.
        :return: Devuelve el número de serie del vehículo.
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Permite modificar el número de serie del vehículo.
        :param value: Nuevo número de serie.
        :return: No devuelve nada.
        """
        self.__num_serie = value


class Coche:
    """
    Esta clase nos permite simular el comportamiento de un Coche.
    """
    cilindrada = 1000

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Constructor de la clase Coche.
        :param num_serie: Número de serie del Coche.
        :param cilindrada: Cilindrada del Coche.
        :param fabricante: Fabricante del Coche.
        :param color: Color del Coche.
        """
        self.num_serie = num_serie
        self.cilindrada = cilindrada
        self.fabricante = fabricante
        self.color = color

    @property
    def color(self):
        """
        Getter del color del Coche.
        :return: Devuelve el color.
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Setter del color del Coche.
        :param value: Nuevo Color.
        :return: No devuelve nada.
        """
        self.__color = value

    @property
    def cilindrada(self):
        """
        Getter de la cilindrada del Coche.
        :return: Devuelve la cilindrada.
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Setter de la cilindrada del Coche.
        :param value: Nueva Cilindrada.
        :return: No devuelve nada.
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Getter del fabricante del Coche.
        :return: Devuelve el fabricante.
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Setter del fabricante del Coche.
        :param value: Nuevo Fabricante.
        :return: No devuelve nada.
        """
        self.__fabricante = value
