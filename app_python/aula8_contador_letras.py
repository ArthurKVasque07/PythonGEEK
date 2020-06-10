def contador_letras(listas_palavras):
    contador = []
    for x in listas_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
