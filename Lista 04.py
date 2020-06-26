# Python
Exerc. aulas que tive c/ Professor Fernando Masanori
# Sorteie 10 inteiros entre 1 e 100 para uma lista e
# Descubra o maior e o menor valor, sem usar as funções max e min.
print('Questão 01')
import random
print (random.sample(range(1, 100),10))

# Sorteie 20 inteiros entre 1 e 100 numa lista.
# Armazene os números pares na lista PAR e os números ímpares na lista IMPAR.
# Imprima as três listas.
print('Questão 02')
import random
lista = []
par = []
impar = []
for i in range(20):
	n = random.randint(1,100)
	lista.append(n)

	if n % 2 == 0: 
		par.append(n)
	else:
		impar.append(n)
lista.sort()
par.sort()
impar.sort()
print ('\nLISTA = ', lista)
print ('PAR   = ', par)
print ('IMPAR = "', impar, "\n")

# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
# Gere um terceiro vetor de 20 elementos,
# Cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
# Imprima os três vetores.
print('Questão 03')
import random
lista1 = []
lista2 = []
lista3 = []
for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))
	lista3.append(lista1[i])
	lista3.append(lista2[i])
print (lista1)
print (lista2)
print (lista3)

# Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone. Our community is based on
# mutual respect, tolerance, and encouragement, and we are working to help each other live up
# to these principles. We want our community to be more diverse: whoever you are, and
# whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
# e cuidado com maiúsculas e minúsculas.
print('Questão 04')
from re import sub
text1 = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.'''
text2 = text1.replace('.', ' ')
text3 = text2.replace(',', ' ')
text4 = text3.replace(':', ' ')
text5 = text4.lower()
print(text5)
text6 = text5.split()
print(text6)

def verifica(p):
    for l in 'python':
        if l in p and len(p) > 4:
            return True
        return False   
lista = []
paragrafo = text6
total = 0
for palavra in paragrafo:
    if verifica(palavra):
        lista.append(palavra)
        total += 1
print("\n\nNúmero de palavras que tem uma letra de python: ", total)
print("\n\nPalavras que tem uma das letras de python: ", lista)

# Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
# minúsculas e de remover antes os caracteres especiais.
print('Questão 05')
from re import sub
text1 = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.'''
text2 = text1.replace('.', ' ')
text3 = text2.replace(',', ' ')
text4 = text3.replace(':', ' ')
text5 = text4.lower()
print(text5)
text6 = text5.split()
print(text6)      
lista= []
for y in range(0,(len(text6))):
	if len(text6[y]) >= 4:
		lista.append(text6[y])		
print ('\nLista: %d palavras com 4 caracteres ou mais: ' % (len(lista)) ,"\n",lista)
