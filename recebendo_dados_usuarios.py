"""
Recebendo dados do usuario
"""
# Entrada de dados
print("Qual seu nome? ")
nome = input()  # input > entrada

# Exemplo de print antigo 2.x
#print('Seja Bem-vindo(a) %s' % nome)

#Print moderno 3.x
#print('Seja bem vindo(a) {0}'.format(nome))

print(f'Seja bem vindo {nome}')

print("Qual sua idade? ")
idade = input()

# Processamento

# Saída
# Exemplo de print antigo 2.x
#print('A %s tem %s anos' % (nome, idade))

#print moderno 3.x
#print('A {0} tem {1} anos'.format(nome, idade))

print(f'A {nome} tem {idade} anos')
