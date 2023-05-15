#codigo que determina el numero de componentes que tiene una lista 

def NumeroLista(lst):
    if lst == []:
        return 0
    else:
        return 1 + NumeroLista(lst[1:])