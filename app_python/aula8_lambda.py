# contador_letras = lambda lista: [len(x) for x in lista]
#
# lista_animais = ['cachorro', 'gato', 'elefante']
# print(contador_letras(lista_animais))
#
# soma = lambda a, b: a + b
# sub = lambda a, b: a - b
# print(soma(5, 10))
# print(sub(10, 5))
#
# calculadora = {
#     'soma' : lambda a, b: a + b,
#     'sub' : lambda a, b: a - b,
#     'multiplicação' : lambda a, b: a * b,
#     'divisão' : lambda a, b: a / b
# }
#
# print(type(calculadora))
# soma = calculadora['soma']
# # soma = lambda a, b: a + b
# multiplicacao = calculadora['multiplicação']
# print(soma(10, 2))

valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)
print(resultado)
