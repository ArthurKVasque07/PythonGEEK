class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com um numero de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Valor maior que 10')
        elif x < 0:
            raise InputError('Valor menor que 0')
        break
    except ValueError:
        print('Valor errado, somente numeros.')
    except InputError as ex:
        print(ex)