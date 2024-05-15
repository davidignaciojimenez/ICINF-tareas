num1=int(input("Ingrese la cantidad de preguntas: "))
num2=int(input("Ingrese la cantidad de preguntas respondidas correctamente: "))
porcentaje=float((num2*100)/num1)
print(porcentaje, "%") 
calificación=(print(
    "Nivel Máximo" if porcentaje>94 else
    "Nivel Medio" if porcentaje>69 and porcentaje<95 else
    "Nivel regular" if porcentaje>39 and porcentaje<70 else
    "Fuera de nivel"
))