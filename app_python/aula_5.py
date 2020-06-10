lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

tupla = (1, 10, 12, 14)
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_num = list(tupla)
print(type(lista_num))
print(lista_num)

# lista.sort()
# # lista_animal.sort()
# # print(lista_animal)
# # print(lista)

# print(lista_animal[1])
# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe lobo na lista!')
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.pop(1)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado)