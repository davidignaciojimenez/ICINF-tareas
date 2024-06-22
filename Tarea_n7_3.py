supermercado={}
while True:
    clave=input("Ingrese un producto. Ingrese un nombre vacío para salir: ")
    if clave=="":
        break
    else:
        valor=int(input("Ingrese el valor del producto: "))
        supermercado[clave]=valor
        print(supermercado)
X=int(input("Ingrese un número a multiplicar los precios: "))
for x in supermercado:
    supermercado[x]*=X
print(supermercado)