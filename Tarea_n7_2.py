lista=[]
while True:
    add=input("Ingrese una palabra.\nPresione ENTER sin escribir una palabra para salir. ")
    if add=="":
        break
    else:
        lista.append(add)
for x in lista:
    contadorAa=0
    for y in x:
        if y in ("A", "a"):
            contadorAa+=1
    print(x, ": cantidad de letras A/a: ",contadorAa)