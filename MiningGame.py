# NOME: CRISTIAN CAMILLO | # DOMINIO: JOGO | INSPIRAÇÃO: https://imgur.com/a/iu6MDg4 <- imagem | EXECUTE O CÓDIGO PARA VER AS REGRAS

print("------------------------------------------------------------------------------- \n")
print("                              Bem vindo ao jogo                                   ")
print("")
print("Como jogar: \n")
print("Você está prestes a escavar uma caverna em busca de diamantes")
print("Cuidado, a caverna pode ser grande ou talvez pequena e pode estar cheia de bombas")
print("Se você sentir que está proximo de uma bomba, coloque um bloco para desativa-la")
print("Você é sortudo o suficiente para conseguir alcançar o diamante?")
print("")
print("------------------------------------------------------------------------------- \n")


import random

class Caverna:
    
    def __init__(self, gambaChoice=[10,20,30,40]):
        self.gamba = []
        self.gambaChoice = gambaChoice

    def criaTamanhoCaverna(self):
        self.rangeDaGamba = random.choice(self.gambaChoice)
        return self.rangeDaGamba

    def geraCaverna(self):
        self.tamanhoCaverna = self.criaTamanhoCaverna()
        self.gamba = ["🪨" for _ in range(self.tamanhoCaverna)] 
        return self.tamanhoCaverna

    def geraDiamante(self):
        rangeDiamante = self.geraCaverna() 
        diamantePos = random.randint(0,rangeDiamante)
        self.gamba[diamantePos - 1] = "💎"
        return rangeDiamante
            
    def bombasNaCaverna(self, numeroBomba = 3): 
        rangeBombas = self.geraDiamante() 
        for i in range(numeroBomba):
            bombaPos = random.randint(0,rangeBombas)
            if(self.gamba[bombaPos - 1] != "💎"):
                self.gamba[bombaPos - 1] = "💣"

    def mostraPilha(self):
        return ' '.join(self.gamba)

class Ojogo:

    def __init__(self, blocos=6):
        self.blocos = blocos
        self.caverna = Caverna()
        self.caverna.bombasNaCaverna()

    def startaGame(self):
        while True:
            print("\nEstado da caverna:")
            print(self.caverna.mostraPilha())
        
            jogada = input("Digite 'minerar' para minerar ou 'bloco' para colocar um bloco: ").lower()
            print("")
            if jogada == "minerar":
                self.mineirarDiamante()
            elif jogada == "bloco":
                self.colocaBloco()
            else:
                print("Tenta denovo...")


    def mineirarDiamante(self):
        self.caverna.gamba.pop()
        if(self.caverna.gamba[-1] == "💎"):
            print("\n                                UM DIAMANTE!!!                           \n"
                  "---------------------------------------------------------------------------\n"
                  "--------------------------------FIM DE JOGO--------------------------------\n"
                  "---------------------------------------------------------------------------")
            
            exit()
        elif(self.caverna.gamba[-1] == "💣"):
            print("\n                       DEU RUIM CAISTES NUMA BOMBA!!!                    \n"
                  "---------------------------------------------------------------------------\n"
                  "--------------------------------FIM DE JOGO--------------------------------\n"
                  "---------------------------------------------------------------------------")
            print("")
            exit()
        else:
            print("Mais uma rocha...")

    def colocaBloco(self):   
        if(self.blocos > 0):
            if(len(self.caverna.gamba) + 1 <= self.caverna.tamanhoCaverna):
                self.caverna.gamba.append("🪨")
                self.blocos -= 1
            else:
                print("NÃO PODE PASSAR DO LIMITE DA CAVERNA! ")
            print(f'VOCÊ TEM {self.blocos} BLOCOS NO INVENTARIO')
            if(self.caverna.gamba[-3] == "💣"):
                print("Você escapou por pouco de uma bomba! Ela foi desativada") ###### A IDEIA DO BLOCO SUBSTITUIR A BOMBA É MAIS UMA CARACTERISTICA DO QUE LIGADA DIRETAMENTE COM A PILHA
                self.caverna.gamba[-3] = "🪨"
                
               
        else:
            print("Não tens mais blocos para poder te salvar, agora é só na fé de Deus...")
       
jogo = Ojogo()
jogo.startaGame()


