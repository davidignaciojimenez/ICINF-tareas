lista=[]
listarev=[]
num=0
while num<10:
    add=int(input("Ingrese un número en la lista: "))
    lista.append(add)
    num+=1
listarev=lista[::-1]
print(listarev)