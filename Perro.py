"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""


class Perro:
    def __init__(self):
        Perro.ladrar()

    @classmethod
    def ladrar(cls):
        print('Guau')


p = Perro()
p.ladrar()
