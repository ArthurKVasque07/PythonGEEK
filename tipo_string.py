"""
Em python, um dado é considerado um string sempre que:

- Estiver entre aspas simples > 'uma string' '123' 'a'
- Estiver em aspas duplas > "uma string" "123" "a"
- Estiver entre aspas triplas > '''uma string''' '''123''' '''a'''
"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome[0:4])

print(nome.split()[0])
print(nome.split()[1])

#inverter o nome keeg geek

print(nome[::-1])

print(nome.replace('e', 'i'))