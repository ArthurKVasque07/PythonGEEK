from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    lista = ['dog', 'gato', 'elefante']
    print(contador_letras(lista))

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    televisao = Televisao()
    print(televisao.ligada)