lista=[]
listacountv=[]
listacountc=[]
vocales=("aeiouAEIOU")
consonantes=("bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNPÑQRSTVWXYZ")
palabra=input("Ingrese una palabra a la lista: ")
while palabra!="":
    lista.append(palabra)
    countv=0
    countc=0
    for thisChar in palabra:
        if thisChar in vocales:
            countv=countv+1
        if thisChar in consonantes:
            countc=countc+1
    listacountv.append(countv)
    listacountc.append(countc)
    palabra=input("Ingrese una palabra a la lista: ")
print(lista)
print("Cantidad de vocales:", listacountv, ", Cantidad de consonantes", listacountc)