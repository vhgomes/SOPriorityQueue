import random
from datetime import datetime
from time import sleep

class PCB:
    def __init__(self, idproc, exectime):
        self.idprocess = idproc
        self.exectime = exectime
        self.priority = random.randint(1,6)
        self.end_init = random.randint(500, 1000)
        self.end_final = random.randint(500, 1000)
        self.data = datetime.today().strftime('%B %d, %H:%M:%S')
        self.finished = False

    def __str__(self) -> str:
        return f"ID:{self.idprocess}\n Exectime: {self.exectime}\n Priority: {self.priority}\n Finished: {self.finished}\n Data: {self.data}\n Endereço Inicial: {self.end_init}\n Endereço Final: {self.end_final}\n"

    def process(self, quantumtime):
        while True:
            if quantumtime != 0 and self.exectime != 0:
                print(self)
                sleep(1)
                quantumtime -= 1
                self.exectime -= 1

                # Verificação se ja acabou o tempo do processo.
                if self.exectime == 0:
                    self.finished = True
                    print(self)
                    break
                # Verificação se o quantum acabou.
                if quantumtime == 0:
                    break