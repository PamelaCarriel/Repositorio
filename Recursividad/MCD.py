#codigo que saca el maximo comun divisor de dos numeros

def mcd(a, b):#Funcion que envia dos parametros 
    if b == 0:
        return a
    else:
        return mcd(b, a % b)