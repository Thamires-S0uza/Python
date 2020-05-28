# Python
Exerc. aulas que tive c/ Professor Fernando Masanori
# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido
# E continue pedindo até que o usuário informe um valor válido.
print('Questão 01')
notas = int(input('Dígite uma nota de 0 a 10:'))
if notas > 0:
    print('Okay')
else:
    print('Não aceito esse valor, dígite outro')
    int(input('Dígite uma nota de 0 a 10:'))

# Faça um programa que leia um nome de usuário e a sua senha
# E não aceite a senha igual ao nome do usuário
# Mostrando uma mensagem de erro e voltando a pedir as informações.
print('Questão 02')
Usuário = input('Dígite o nome de Usuário:')
Senha = input('Dígite sua senha:')
if Usuário != Senha:
    print ('É válido, amore')
else:
    print ('Amorzinho, está errado, vai digitar tudo de novo')
    input('Dígite o nome de Usuário:')
    input('Dígite sua senha:')

# Supondo que a população de um país A seja da ordem de 80000 habitantes
# Com uma taxa anual de crescimento de 3%
# E que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos para que a população do país A 
# Ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
print('Questão 03')
paísA, paísB, anos = 80000, 200000, 1
while paísA <= paísB:
    paísA = paísA + (paísA * 0.03)
    paísB = paísB + (paísB * 0.015)
    anos = anos + 1
print ('Populacao A:', round(paísA))
print ('Populacao B:', round(paísB))
print ('Anos pra isso: ', anos)

# Faça um programa para a sequência de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...)
# Sua regra de formação é simples: os dois primeiros elementos são 1.
# A partir de então, cada elemento é a soma dos dois anteriores.
print('Questão 04')
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('~'*30)
print('{} --> {}'. format(t1, t2), end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-->{}'. format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' --> FIM')

# Dados dois números inteiros positivos,
# Determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
print('Questão 05')
a = int(input('Número:'))
b = int(input('Outro número:'))
while a % b != 0:
    a, b = b, a % b
print('mdc = %d' %b)
