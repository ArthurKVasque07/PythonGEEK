"""
Operadores unarios:
    - not, is

Operadores binários:
    -and, or
Para 'and' , ambos valores precisam ser True
Para 'or' , um dos valores precisam ser True
Para o 'not', o valor do booleano é invertido, ou seja se for True vira False
"""

ativo = True
logado = False

if ativo and logado:
    print('Bem vindo')
else:
    print('Voce precisa ativar conta!')

##############

if ativo or logado:
    print('Bem vindo')
else:
    print('Voce precisa ativar conta!')

    ##############
# Se não estiver ativo
if not ativo:
        print('Voce precisa ativar sua conta')
else:
        print('Bem vindo')

#############

if ativo is logado:
    print('Bem vindo')
else:
    print('Você precisa ativar sua conta')


