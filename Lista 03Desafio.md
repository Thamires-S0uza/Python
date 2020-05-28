# Python
Exerc. aulas que tive c/ Professor Fernando Masanori
# Dizemos que um número natural é triangular se 
# Ele é produto de três números naturais consecutivos.
# Exemplo: 120 é triangular, pois 4.5.6 = 120.
# Dado um inteiro não-negativo n, verificar se n é triangular.
print('Questão 01')
n = int(input('N:'))
k = 0
while k * (k + 1) * (k + 2) < n:
        k = k + 1
print(k * (k + 1) * (k + 2) == n)

# Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
# Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado
# Desprezando os centavos.
# Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais
# E que nenhuma delas esteja em falta no caixa.
print('Questão 02')
divida = int(input('Quanto a ser pago?:'))
pagamento = int(input('Quanto pagou:'))
troco = pagamento - divida
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
        while troco >= nota:
                print('Uma nota de %d' %nota)
                troco -= nota

# Verifique se um inteiro positivo n é primo.
print('Questão 03')
n = int(input('Número a ser julgado:'))
k = 1
divisor = 0
while k<= n:
        if n % k == 0:
                divisor = divisor + 1
        k = k + 1
print(divisor == 2)

# Dado um número inteiro positivo,
# Determine a sua decomposição em fatores primos,
# Calculando também a multiplicidade de cada fator.
print('Questão 04')
n = int(input('Número:'))
for k in range(2, n):
        while n % k == 0:
            n = n / k
            print(k)

# Faça um programa que peça um inteiro positivo e o mostre invertido.
# Ex.: 1234 gera 4321
print('Questão 05')
n = int(input('Manda um número:'))
inv = 0
while n >0:
    inv *= 10
    inv += n % 10
    n //= 10
print(inv)
