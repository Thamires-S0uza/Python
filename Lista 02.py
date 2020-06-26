# Python
Exerc. aulas que tive c/ Professor Fernando Masanori
# Faça um Programa que peça os três lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
print('Questão 01')
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro seguimento:'))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os seguimentos talvez formem um triângulo')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os seguimentos não podem formar um triangulo')

# Determine se um ano é bissexto.
print('Questão 02')
ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('0 ano {} é bissexto'. format(ano))
else:
    print('0 ano {} não é bissexto'. format(ano))

# João Papo-de-Pescador, comprou um microcomputador para controlar seu rendimento diário.
# Sempre que o peso do peixe for =< 50Kg, ele não paga multa.
# Se o Kg do peixe for superior a 50Kg, ele pagará multa de R$ 4,00 por quilo a mais.
#print('Questão 03')
peso = int(input('Peso do Peixe:'))
multa = (peso - 50) * 4
if peso > 50:
    print('Vai pagar multa!','Sua multa é de',multa,'reais')
if peso <= 50:
    print('Se livrou dessa vez, safado')

# Faça um Programa que leia três números e mostre o maior deles
print('Questão 04')
a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('Terceiro número:'))
if a > b and a > c:
    print('O primeiro número é maior')
elif b > a and b > c:
    print('O segundo número é maior')
elif c > a and c > b:
    print('O terceiro número é maior')

# Faça um Programa que leia três números e mostre o maior e o menor deles.
print('Questão 05')
a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('Terceiro número:'))
if a > b and a > c:
    print('Primeiro é maior')
elif a < b and a < c:
    print('Primeiro é menor')
if b > a and b > c:
    print('Segundo é maior')
elif b < a and b < c:
    print('Segundo é menor')
if c > a and c > b:
    print('Terceiro é maior')
elif c < a and c < b:
    print('Terceiro é menor')

# Faça um programa que calcule o sálario líquido.
# Tem que perguntar: quanto que ganha por hora, e quantas horas trabalho no mês.
# Será descontado: Imposto de Renda(IR): 11%; INSS: 8%; Sindicato: 5%
# O programa precisa mostrar o sálario bruto, quanto pagou de cada item da acima, e o sálario líquido
print('Questão 06')
qh = int(input('Quanto você ganha por hora: '))
ht = int(input('Quantas horas você trabalhou: '))
sb = qh * ht
ir = (11/100.0 * sb)
inss = (8/100.0 * sb)
sindicato = (5/100.0 * sb)
vt = ir + inss + sindicato
sl = sb - vt
print ('Seu salário bruto é',sb)
print ('Valor dos impostos:',vt)
print ('IR: ',ir)
print ('INSS: ',inss)
print ('Sindicato: ',sindicato)
print ('Seu salário liquido é: ',sl)

# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados.
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas.
print('Questão 07')
metros = int(input('Tamanho em metros quadrados: '))
litros = metros / 3
if metros % 3 == 0:
	latas = metros / 3
else: 
	latas = int(metros / 3) + 1
preço = latas * 80
print ('Serão necessárias', latas, 'latas e será pago R$', preço)
