numero_ante_suc = int(input('Digite um número: '))

print('Analisando o valor de {} o seu antecessor é {} e o seu sucessor é {}.'
      .format(numero_ante_suc, numero_ante_suc-1, numero_ante_suc+1))

numero_multiplicacao = int(input('Digite outro número: '))

print('Analisando o número {0}, seu dobro é: {1}, seu triplo é: {2}, e sua raiz quadrada é: {3}'.format(
    numero_multiplicacao, numero_multiplicacao*2, numero_multiplicacao*3, numero_multiplicacao**(1/2)))

nota_aluno = float(input('Digite a nota do aluno: '))
nota_aluno2 = float(input('Digite a nota de outro aluno: '))
media = float((nota_aluno + nota_aluno2)) / 2

print('A media entre {:.1f} e {} é de {:.1f}'.format(
    nota_aluno, nota_aluno2, media))

metros_conv = float(input('Digite em metros para converter: '))
cent_conv = float(metros_conv * 100)
milim_conv = float(metros_conv * 1000)


print('O número {}m em centimetros: {}cm em milimetros: {}mm'.format(
    metros_conv, cent_conv, milim_conv))

tabuada = int(input('Digite um número para saber sua tabuada: '))

print('-' * 15)
print(' {0:3} x  1 = {0:2}\n {0:3} x  2 = {1:3}\n {0:3} x  3 = {2:3}\n {0:3} x  4 = {3:3}\n {0:3} x  5 = {4:3}\n {0:3} x  6 = {5:3}\n {0:3} x  7 = {6:3}\n {0:3} x  8 = {7:3}\n {0:3} x  9 = {8:3}\n {0:3} x 10 = {9:3} '.format(
    tabuada, tabuada*2, tabuada*3, tabuada*4, tabuada*5, tabuada*6, tabuada*7, tabuada*8, tabuada*9, tabuada*10))
print('-' * 15)

cache_reais = float(input('Quanto de dinheiro você tem em reais? '))


# Valor fictício de dolar.
print('Você pode comprar {:.2f}$ dolares'.format(cache_reais / 3.27))
