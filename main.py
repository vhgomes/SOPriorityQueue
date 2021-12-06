import random
from RRobin import RoundRobin

class SO:
    def __init__(self):
        self.filas = []
        for i in range(1):
            self.filas.append(RoundRobin(i + 1, 2))
        self.filaatual = 0
        self.filassorted = sorted(self.filas, key=lambda a: a.priority, reverse=True)

    def inicio(self):
        while True:
            if self.filassorted[self.filaatual].finished:
                self.filaatual = (self.filaatual + 1) % len(self.filassorted)
            else:
                self.filassorted[self.filaatual].printfila()
                self.filassorted[self.filaatual].filaprocess()

SO().inicio()