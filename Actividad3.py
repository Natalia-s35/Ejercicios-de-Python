#Ejercicio 4: Diseñar un programa que dado un número de 1 a 7 determine el día de la
#semana que representa: 1- Domingo a 7 – Sábado. ¿Qué pasa si ingreso un número mayor que 7?

def dia_semana(num):
    dias_de_la_semana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
    if num >= 1 and num <= 7:
        return(dias_de_la_semana[num-1])
    else:
        return "El número no se encuentra en el rango indicado"


a = int(input("Ingrese un número del 1 al 7: "))

print(dia_semana(a))


"""
#Ejercicio 10: Dadas 3 longitudes, decir mediante un mensaje si se forma o no un triángulo (cada lado tiene que ser menor que la suma de los otros dos)
def triangulo(lado1,lado2,lado3):
    if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
        return("Es un tríangulo")
    else:
        return("No es un tríangulo")

a = int(input("Ingrese la primer longitud: "))
b = int(input("Ingrese la segunda longitud: "))
c = int(input("Ingrese la tercer longitud: "))

print(triangulo(a,b,c))


#Ejercicio 14: Calcular el número de pulsaciones que una persona debe tener por cada 10
#segundos de ejercicio aeróbico; la fórmula que se aplica cuando la persona no está entrenada: (220-edad)/10; si la persona está entrenada: (210-edad)/10

def calculo_pulsaciones(edad, entrenamiento):
    if entrenamiento == "si":
        return("El número de pulsaciones es: " + str((220 - edad)/10))
    elif entrenamiento == "no":
        return("El número de pulsaciones es: " + str((210 - edad)/10))
    else:
        return("No es posible calcular el número de pulsaciones.")

a = int(input("Ingrese su edad: "))
b = input("Si entrena ingrese: si. Si no entrena ingrese no: ")

print(calculo_pulsaciones(a,b.lower))
"""