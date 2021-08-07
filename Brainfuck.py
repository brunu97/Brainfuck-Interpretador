import sys
import os


class BF_Interpretador():
    def __init__(self):
        self.pc = 0
        self.fita = [0 for _ in range(30000)]
        self.ptr = 0
        self.n = 0
        self.codigo = ""

        self.cmds = {
            "+": self.incrementa,
            "-": self.decrementa,
            ">": self.incrementaApontador,
            "<": self.decrementaApontador,
            "[": self.inicioLoop,
            "]": self.fimLoop,
            ".": self.saida,
            ",": self.entrada
        }

    def incrementa(self): 
        self.fita[self.ptr] += 1 

    def decrementa(self):
        self.fita[self.ptr] -= 1

    def incrementaApontador(self):
        self.ptr += 1

    def decrementaApontador(self):
        self.ptr -= 1

    def entrada(self):
        self.fita[self.ptr] = ord(input()[0])

    def saida(self):
        print(chr(self.fita[self.ptr]), end="")

    def inicioLoop(self):
         if self.fita[self.ptr] == 0:
            self.pc += 1
            while self.n > 0 or self.codigo[self.pc] != ']':
                if self.codigo[self.pc] == '[': self.n += 1
                elif self.codigo[self.pc] == ']': self.n -= 1
                self.pc += 1

    def fimLoop(self):
         if self.fita[self.ptr] != 0:
            self.pc -= 1
            while self.n > 0 or self.codigo[self.pc] != '[':
                if self.codigo[self.pc] == ']': self.n += 1
                elif self.codigo[self.pc] == '[': self.n -= 1
                self.pc -= 1
            self.pc -= 1

    def executa(self, codigo):
        self.codigo = codigo
        while self.pc < len(self.codigo):
            if codigo[self.pc] in self.cmds.keys():
                self.cmds[self.codigo[self.pc]]()
            self.pc += 1


if __name__ == "__main__":
    # bf = BF_Interpretador().executa(codigo)
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], 'r') as f:
                BF_Interpretador().executa(f.read())
        else: print(f"O ficheiro \"{sys.argv[1]}\" não foi encontrado.")
