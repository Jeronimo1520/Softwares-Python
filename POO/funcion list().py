def numero_impar(numero):
    if numero % 2 != 0:
        return True

numeros= [2,3,4,5,6,7,8,9,10,11,12,13]

print(list(filter(numero_impar, numeros)))