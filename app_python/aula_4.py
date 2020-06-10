# a = int(input('Entre com um numero: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('numero {} é primo'.format(a))
# else:
#     print('numero {} é primo'.format(a))

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1
#
# nota = int(input('Digite a nota: '))
# while nota > 10:
#     nota = int(input('Nota incorreta. Digite a nota: '))

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado, refaça. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado, refaça. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
media = (a + b + c + d) / 4
print('Media: {}'.format(media))
