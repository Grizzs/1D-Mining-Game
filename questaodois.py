# NOME: CRISTIAN CAMILLO | # DOMINIO: JOGO/SIMULAÇÃO | EXECUTE O CÓDIGO PARA VER AS REGRAS
import random

class FilaDeEntrega:
    
    def __init__(self, FilaPassageiros=[10,20,30]):
        self.fila = []
        self.filaPassageiros = FilaPassageiros

        
    def criaTamanhoFila(self):
        self.rangeFila = random.choice(self.filaPassageiros)
        return self.rangeFila
    
    def CriaFila(self):
        self.tamanhoFila = self.criaTamanhoFila()
        self.fila = ["𖨆" for _ in range(self.tamanhoFila)]
        return print(self.fila)
    
    def mostraFila(self):
        return ' '.join(self.fila)


comecar = FilaDeEntrega()
comecar.CriaFila()

class Ojogo:
    
    def __init__(self):
        pass