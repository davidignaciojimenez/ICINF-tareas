print("Ingrese alguna de las siguientes acciones a realizar: ")
print("Opción 1: Ingresar un elemento nuevo a la lista.")
print("Opción 2: Modificar un elemento de la lista según el índice (inicia en 0).")
print("Opción 3: Eliminar un elemento de la lista según el índice (inicia en 0).")
print("Opción 4: Eliminar el último elemento de la lista.")
print("Opción 5: Entregar el índice de un dato de la lista.")
print("Opción 6: Mostrar todo los datos de la lista.")
print("Opción 7: Salir.")
lista=[]
accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))
while accion!="":
      match accion:
            case 1:
                  intro=input("Introdusca una palabra: ")
                  lista.append(intro)
                  accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))
            case 2:
                  aindice=int(input("Ingrese un índice a modificar de la lista: "))
                  lista.pop(aindice)
                  reemplazo=input("Introdusca el reemplazo de la palabra removida: ")
                  lista.insert(aindice, reemplazo)
                  accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))
            case 3:
                  aindice=int(input("Ingrese un índice a remover de la lista: "))
                  lista.pop(aindice)
                  accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))
            case 4:
                  lista.pop()
                  accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))
            case 6:
                  print(lista)
                  accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))
            case 7:
                  break
            case other:
                  print("Acción inválida.")
                  accion=int(input("Ingrese un número correspondiente a una de las acciones disponibles: "))