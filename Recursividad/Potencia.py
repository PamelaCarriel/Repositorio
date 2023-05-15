#codigo que saca el maximo comun divisor de dos numeros

def potencia(base, exponent): #
    if exponent == 0:
        return 1
    else:
        return base * potencia(base, exponent - 1)