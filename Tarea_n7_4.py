deudores={}
a=0
while a<5:
    RUT=input("Ingrese un RUT de un deudor: ")
    deuda=int(input("Ingrese la deuda asociada al RUT ingresado: "))
    deudores[RUT]=deuda
    print(deudores)
    a+=1
while True:
    print(deudores)
    cuenta=input("Ingrese un RUT a abonar: ")
    if cuenta=="":
        break
    elif cuenta in deudores:
        abono=int(input("Ingrese un abono: "))
        deudores[cuenta]-=abono
        print("La cantidad de deuda asociada a éste RUT es de:", deudores[cuenta])
        if deudores[cuenta]<1:
            del deudores[cuenta]
    else:
        print("El RUT ingresado no se encuentra en la lista de deudores.")
print("Los RUTs con deudas asociadas son:", deudores)