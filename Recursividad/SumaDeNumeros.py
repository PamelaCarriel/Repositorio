#codigo que suma una lista de numeros 

def sum_list(lst):#la funcion obtiene como parametro una lista que se define entre entre corchetes
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])