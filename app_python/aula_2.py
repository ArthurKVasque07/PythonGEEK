# a = 10
# b = 5
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
soma = a + b
sub = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('soma: {soma} \nSubtração: {sub}'
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                sub=sub,
                                resto=resto,
                                multiplicacao=multiplicacao,
                                divisao=divisao))
print(resultado)

# print('soma: ' + str(soma))
# print(sub)
# print(multiplicacao)
# print(int(divisao))
# print(resto)
# x = '1'
# # soma2 = int(x) + 1
# # print(soma2)

from datetime import datetime, time
data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
hora = time(hour=13, minute=14, second=00)
print('{} às {}'.format(data, hora))