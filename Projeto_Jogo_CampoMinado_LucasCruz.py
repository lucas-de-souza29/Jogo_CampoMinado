# Projeto: Jogo (Campo minado)
# Regras do jogo : Tabuleiro 9x9 onde serão distribuídas 10 minas em áreas aleatórias
#                  O jogador deverá ir abrindo espaços no campo colocando bandeiras nos locais que são as
#                  minas. Após marcar as 10 minas corretamente o jogo termina(computar o tempo de jogo)

from random import randint
from sys import argv

class InputDados:

    #Coordenadas
    @staticmethod
    def buscaCoordenadas():
        print("Informe número válido entre 0 e 8")
        linhas = int(input("Informe a linha da coordenada"))
        if(linhas < 0 or linhas > 8):
           print("Linha inválida, informe novamente!")
        colunas = int(input("Informa a coluna da coordenada"))
        if(colunas < 0 or colunas > 8):
           print("Coluna inválida, informe novamente!")
        return (linhas,colunas)

class Tabuleiro:

      qtdeBombas = 0  #Inicializando a quantidade de bombas com zero(0)
      tabuleiro = []  # Tabuleiro
      mapaBombas = []  # Mapa com bombas que vão ser geradas aleatoriamente
      vazio = '[]'  # Espaço vazio (empty)
      marcaDeBomba ='[B]' #Marcar a bomba quando for pisada
      mapInicial = '[!]' #Mapa inicial

      def __init__(self,qtdeBombas):
          self.qtdeBombas = qtdeBombas
          self.iniciaTabuleiro()
          self.iniciaMapaBombas()

      def iniciaTabuleiro(self):
          for i in range(9):
              self.tabuleiro.append([])
              self.mapaBombas.append([])
              for j in range(9):
                  self.tabuleiro[i].append(self.mapInicial)
                  self.mapaBombas[i].append(self.mapInicial)

      def iniciaMapaBombas(self):
          for i in range(self.qtdeBombas):
              linhas = randint(0,8)
              colunas = randint(0,8)
              self.mapaBombas[linhas][colunas] = self.marcaDeBomba

      #GETS

      def getMapaBombas(self):
          return self.mapaBombas

      def getQtdeBombas(self):
          return self.qtdeBombas

      def getTabuleiro(self):
          return self.tabuleiro

      def getVazio(self):
          return  self.vazio

      def getMarcaDeBomba(self):
          return self.marcaDeBomba

      #SETS
      def setQtdeBombas(self,qtdeBombas):
          self.qtdeBombas = qtdeBombas


      #Método para subtrair as minas
      def subtraiQtdeBombas(self):
          self.qtdeBombas = self.qtdeBombas - 1

      #Método para verificar coordenadas nulas
      def verificaNulo(self,coord):
          if(self.tabuleiro[coord[0]] [coord[1]] == self.vazio):
              return True
          return  False

      #Método para verificar posição marcada
      def verificaMarcado(self,coord):
          if(self.tabuleiro[coord[0]][coord[1]] == '[M]'):
             return True
          return False

      #Encontrou bomba
      def acertouBomba(self,coord):
          if(self.mapaBombas[coord[0]][coord[1]] == self.marcaDeBomba):
             return True
          return False

      #Mudar ou setar posição diferente do tabuleiro para a mina
      def setLocalTabMina(self,coord):
          self.tabuleiro[coord[0]][coord[1]] = self.marcaDeBomba

      def setLocalTabNulo(self,coord):
          self.tabuleiro[coord[0]][coord[1]] = self.vazio

      def setLocalTabMarcado(self,coord):
          self.tabuleiro[coord[0]][coord[1]] = '[M]'

#Play Game! (Start com 10 minas)
tabuleiro = Tabuleiro(10)

def imprimeTabuleiro(tabuleiro):
    print("     ")
    for i in range(len(tabuleiro)):
        print(i,"      ",end="")
        print("\n")
        for j in range(len(tabuleiro)):
            for x in range(len(tabuleiro)):
                print(tabuleiro[j][x],end= " ")
            print("\n")

def menuInterface():
    print("---CAMPO MINADO---")
    opcao = input("Informe a opcao que deseja escolher : 1-Pisa ou 2- Marca ")

    #Opção pisar
    if(opcao == 1):
       coord = InputDados.buscaCoordenadas()
       if(tabuleiro.verificaNulo(coord)):
           print("Local já foi verificado! Escolha outro local!")
           return True
       if (tabuleiro.acertouBomba(coord)):
           print("Você pisou em uma mina :( Game Over!")
           return False
       else:
            print("Você pisou em lugar seguro! Continue...")
            tabuleiro.setLocalTabNulo(coord)
            return True

    else:
         #Marcar
          coord = InputDados.buscaCoordenadas()
          if(tabuleiro.verificaNulo(coord)):
              print("Local já foi verificado! Escolha outro local!")
              return True
          if(tabuleiro.verificaMarcado(coord)):
             print("Local já foi marcado! Escolha outro local!")
             return False

          if(tabuleiro.acertouBomba(coord)):
             tabuleiro.setLocalTabMina(coord)
             print("Mina encontrada! Parabéns ")
             tabuleiro.subtraiQtdeBombas()
             return True

          else:
               print("\n")
               tabuleiro.setLocalTabMarcado(coord)
               return True
#MAIN
def main(args):
    flag = True
    while(flag):
          print("Mapa - Minas")
          imprimeTabuleiro(tabuleiro.getMapaBombas())
          if(tabuleiro.getQtdeBombas == 0):
             print("Você venceu! Nenhuma mina atingida!")
          else:
               print("Tabuleiro")
               imprimeTabuleiro(tabuleiro.getTabuleiro())
               print("===================================")
               print('\t \t Numero de bombas afetadas: {}'.format(tabuleiro.getQtdeBombas()),'\n')
               flag = menuInterface()


#Chamada da função MAIN
if __name__ == "__main__":
    print(main(argv))
