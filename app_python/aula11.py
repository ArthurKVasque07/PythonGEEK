
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print('Fechando arquivo')

except ZeroDivisionError:
    print('Não é possivel divisão por zero!')
except ArithmeticError:
    print('Houve um erro de aritimetica!')
except IndexError:
    print('Erro ao acessar um indice invalido da lista!')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre nenhuma exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()

