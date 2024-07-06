lista_numeros=[1,2,3,4,5,6,7,8,9,10]
def separar(lista):
    global lista_inpares, lista_pares
    lista_inpares=[]
    lista_pares=[]
    for x in lista_numeros:
        if x%2==0:
            lista_pares.append(x)
        elif x%2!=0:
            lista_inpares.append(x)
    print("Lista de números pares:", lista_pares,"\nLista de números inpares: ",lista_inpares)
separar(lista_numeros)