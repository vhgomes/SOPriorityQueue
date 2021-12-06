from pcb import PCB
import random

class RoundRobin:
    def __init__(self, fila, processos):
        self.fila = fila
        self.process = processos
        self.quantum = random.randint(1,5) 
        self.priority = random.randint(1,10)
        self.finished = False
        self.currentprocess = 0
        self.process = [PCB(random.randint(1,10000), random.randint(1,5)) for _ in range(processos)]

    def __str__(self) -> str:
        return f"Prioridade: {self.priority}"

    def printfila(self):
        if not self.process:
            print(f"FILA:{self.fila} está vazia\n\n")
        else:
            print(f"FILA:{self.fila}")

    def filaprocess(self):
        if len(self.process) == 0:
            self.finished = True
            return

        self.process[self.currentprocess].process(self.quantum)
        if self.process[self.currentprocess].finished:
            self.process.pop(self.currentprocess)
            if self.currentprocess == len(self.process) and len(self.process) != 0:
                self.currentprocess = 0
            return
            
        if self.currentprocess == len(self.process) and len != 0:
            self.currentprocess = (self.currentprocess + 1) % len(self.process)
            return

        self.currentprocess = (self.currentprocess + 1) % len(self.process)
