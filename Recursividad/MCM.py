#Codigo que calcula
def Mcd(a, b):
    if b == 0:
        return a
    else:
        return Mcd(b, a % b)

def mcm(a, b):
    return (a * b) // Mcd(a, b)