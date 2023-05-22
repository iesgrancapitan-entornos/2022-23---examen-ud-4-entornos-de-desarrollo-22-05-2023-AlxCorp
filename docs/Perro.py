"""
Clase Perro.

Autor: Alejandro Priego Izquierdo.

"""


class Perro:
    """
    Clase que simula el comportamiento de un Perro.
    """
    def __init__(self):
        """
        Constructor de instancias de la clase Perro.
        """
        Perro.ladrar()

    @classmethod
    def ladrar(cls):
        """
        Función que simula el comportamiento de un perro ladrando.
        :return: No devuelve nada, imprime por pantalla un ladrido.
        """
        print('Guau')


p = Perro()
p.ladrar()
