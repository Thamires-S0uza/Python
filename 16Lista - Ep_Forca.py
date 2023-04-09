##letras = chute(certas + erradas)
##letras in sorteada
##certas = certas + letras
##for c in sorteada:
##     if c in certas:
##              print(c, end = ' ')
##     else:
##              print ('_', end = ' ')
##print(forca[len(erradas)])
##letras = chute(certas + erradas)
##letras in sorteada
##erradas = erradas + letras
##print(forca[len(erradas)])

import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
p = requests.get(url)
palavras = p.text.lower()
palavras = palavras.split()
from random import choice
choice(palavras)
forca = ['''
+-------------+
l             l
l
l
l
l
l
l
+----------------+''', '''
+-------------+
l             l
l             O
l
l
l
l
l
+----------------+''', '''
+-------------+
l             l
l             O
l             l
l
l
l
l
+----------------+''', '''
+-------------+
l             l
l             O
l           / l
l
l
l
+----------------+''', '''
+-------------+
l             l
l             O
l           / l \
l
l
l
+----------------+''', '''
+-------------+
l             l
l             O
l           / l \
l            /
l
l
+----------------+''', '''
+-------------+
l             l
l             O
l           / l \
l            / \
l
l
+----------------+''']
certas = erradas = ' '
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
import requests
p = requests.get(url)
palavras = p.text.lower().split()
from random import choice
def escolhe():
      return choice(palavras)
def desenha():
      print(forca[len(erradas)])
      for x in sorteadas:
            if x in certas: print(x, end = ' ')
            else: print('_', end = ' ')
      print()
def chute(letras):
      from string import digits, punctuacion
      while True:
            x = input ('Dígite letra:')
            if x in digits + punctuacion: print('Inválido')
            elif x in letras: print('Repetido')
            elif len(x) != 1: print('Somente uma letra')
            else: return x
def jogar_novamente():
      return input('Deseja jogar novamente? (SsNn)') in 'Ss'
def ganhou():
      return set(sorteada) == set(certas)
sorteada = escolhe()
while True:
      desenha()#ta faltando aqui
      x = chute(certas + erradas)
      if x in sorteadas:
            certas = certas + x
      else: erradas = erradas + x
      if len(erradas) == len(forca):
            print('Perdeu! Palavra era:', sorteada)
            acabou = True
      if ganhou():
            print('Parabéns!')
            acabou = True
      if acabou:
            if jogar_novamente():
               #Você irá reiniciar a palavra sorteada
               #E as variáveis de ambiente
               #Como certas e erradas
            else: break
