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
        return f"ID: {self.idprocess}\n Exectime: {self.exectime}\n Priority: {self.priority}\n Finished: {self.finished}\n"

    def process(self, quantumtime):
        while True:
            print(self)
            if quantumtime != 0 and self.exectime != 0:
                sleep(1)
                quantumtime -= 1
                self.exectime -= 1

                # Verificação se ja acabou o tempo do processo.
                if self.exectime == 0:
                    self.finished = True
                    break
                # Verificação se o quantum acabou.
                if quantumtime == 0:
                    break