#Dado dois números inteiros positivos n e k, monte uma lista dos números
#binários de 0 até 2**n - 1, depois coloque em ordem decrescente do número
#de 1's que fazem parte do número binário, finalmente retorne o k-ésimo elemento
#DICAS: bin(x) e sorted (lista, key = função, reverse = True)
##n = 5
##k = 3
##b = [bin(x) for x in range (2**n)]
##sorted (b,key=len, reverse=True)
##bin (13), count('1')
##bin(13)

##n = 5
##k = 3
##b = [bin(x) for x in range (2**n)]
##def conta_uns(x): return x, count('1')
##lista = sorted(b, key=conta_uns, reverse=True)
##lista = [k-1]
#Lambida é função sem nome, serve pra valor de um codigo só da linha
##def hack (n,k):
##    b = [bin(x) for x in range (2**n)]
##    def conta_uns(x): x,count('1')
##    lista = sorted(b, key=conta_uns, reverse=True)
##    return lista[k-1]

##def hack(n,k):
##    return sorted([bin(x) for x in range(2**n)],
##            key=lambda s: s.count('1'),
##            reverse=True) [k - 1]
##print(hack(5,3))

##print('_-' * 10)
##print('Viadagem 1')
##print('_-' * 10)
##a = int(input('Dígite um número:'))
##b = int(input('Dígite um número:'))
##c = int(input('Dígite um número:'))
##if a <= b + c and b <= a + c and c <= a + b:
##    print('É triângulo')
##    if a == b == c: print('É equilátero')
##    elif a != b  and b == c or b != c and a == c or c != a and a == b: print('É isósceles')
##    else: print('É escaleno')
##else: print('Não é triangulo')

##print('_-' * 10)
##print('Viadagem 2')
##print('_-' * 10)
##a = int(input('Dígite um número:'))
##b = int(input('Dígite um número:'))
##c = int(input('Dígite um número:'))
##if a > b and a > c:
##    print('É maior:', a)
##elif b > a and b > c:
##    print('Esse é maior:', b)
##else:
##    print('Acho!!', c)

##print('_-' * 10)
##print('Viadagem 3')
##print('_-' * 10)
##A = 80000 
##B = 200000
##cont = 0
##while A <= B:
##    A = A + (A * 0.03)
##    B = B + (B * 0.015)
##    cont = cont + 1
##print(f'São {cont} anos até lá')
##print('_-' * 10)
##print('Viadagem 4')
##print('_-' * 10)
##import random
##lista = []
##for k in range(10):
##    lista.append(random.randint(1, 100))
##maior = 0
##for i in lista:
##    if i > maior:
##        maior = i
##print(lista)
##print(maior)

##print('x', end = ' ')
##print('x', end = ' ')
##print('0', end = ' ')
##print(62)
##

##for k in range(1000000000000):
##	if k == 42: break
##	print(k)

##def f():
##    yield 42
##    yield 'abacate'
##    yield [1, 2, 3]
##    yield 'acabou'

##guarda = 'Antonio'
##def Fatec():
##    guarda = 'Zé'
##    print (guarda)
##
##print(guarda)
##Fatec()
##print(guarda)

##guarda = 'Antonio'
##def Fatec():
##    global guarda
##    guarda = 'Zé'
##    print (guarda)
##
##print(guarda)
##Fatec()
##print(guarda)
