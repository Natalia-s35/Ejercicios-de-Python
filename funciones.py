"""
Definir una función que calcule el área de un círculo, otra que calcule el área de
un rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían
recibir dichas funciones

def calculo_area_circulo(a,b ):
    calculo = a * b**2
    return calculo

def calculo_area_rectangulo(a,b):
    calculo = a * b
    return calculo

def calculo_area_cuadrado(a):
    calculo = a*a
    return calculo

pi = float(3.141592)
radio = int(input("Ingrese el radio del circulo: "))

print(calculo_area_circulo(pi,radio))

base = int(input("Ingrese la base del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
print(calculo_area_rectangulo(base,altura))

lado = int(input("Ingrese el lado del cuadrado: "))
print(calculo_area_cuadrado(lado))


Definir una función llamada calculo_nuevo_precio que reciba dos números,
uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el
precio aumentado.

def calculo_nuevo_producto(num1,num2):
    calculo = (num1 *num2) + num1
    return calculo

a = float(input("Ingrese el precio anterior del producto: "))
b = float(input("Ingrese el porcentaje a aumentar: "))
print(calculo_nuevo_producto(a,b))


Definir una función llamada calculo_transporte que reciba cuatro números: la
cantidad de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de
asientos del transporte escolar. La función debe retornar cuántos micros necesito contratar
para una excursión sabiendo que cada salita es acompañada por tres adultos.

def calculo_transporte(num1,num2,num3,num4):
    cantidad = ((num1)*3 + (num2)*3 + (num3)*3)
    return cantidad

a = int(input("Ingrese la cantidad de alumnos: "))
b = int(input("Ingrese la cantidad de alumnos: "))
c = int(input("Ingrese la cantidad de alumnos: "))
d = int(input("Ingrese la cantidad de asientos del transporte escolar: "))

def cargarFraccion():
    num = int(input("Ingresar el numerador: "))
    den = int(input("Ingresar el denominador: "))
    lista1 = [num,den]
    return lista1

def numerador_fraccion(x):
    return x[0]

def denominador_fraccion(x):
    return x[1]

def sumaFracciones(x,y):
    denominador = x[1] * y[1]
    sumaNum = (x[0] * y[1]) + (y[0] * x[1])
    lista = [sumaNum, denominador]
    return lista

def restaFracciones(x,y):
    denominador = x[1] * y[1]
    restaNumerador = (x[0] * y[1]) - (y[0] * x[1])
    lista = [restaNumerador, denominador]
    return lista

def divisionFracciones(x,y):
    numerador = x[0] * y[1]
    denominador = y[1] * x[0]
    lista = [numerador, denominador]
    return lista

def multiplicacion_fracciones(x,y):
    numerador = x[0] * y[0]
    denominador = x[1] * y[1]
    lista = [numerador, denominador]
    return lista

print("Bienvenidos/as a cuentas con fracciones")
a = cargarFraccion()
b = cargarFraccion()

print("El denominador de la primera fracción es: ", denominador_fraccion(a))
print ("El numerador de la segunda fraccion es:", numerador_fraccion(b))
print ("La suma de dichas fracciones es:", sumaFracciones(a,b))
print ("La resta de dichas fracciones es:", restaFracciones(a,b))
print ("La multiplicacion de dichas fracciones es:", multiplicacion_fracciones(a,b))
print ("La division es:", divisionFracciones(a,b))


def armo_cartel(nombre, precioA,precioB):
    print("Atención! Gran rebaja para el producto nombre: " + (nombre))
    print("Antes: precio anterior " + (precioA) + "$")
    print("Ahora: precio rebajado " + (precioB) + "$")

armo_cartel("productoX", "20", "15")

tupla1 = ("Guerra de Peloponeso", "431 a.C")
tupla2 = ("Revolución de Mayo", "1810 d.C")
tupla3 = ("Llegada de españoles a América", "1492 d.C")
tupla4 = ("Comienza de la construcción de la Gran Muralla China", "214 a.C")

lista1 = [tupla1, tupla2, tupla3, tupla4]
print(lista1)

lista = [1, True,["a", "b", "c"],"hola"]
print(lista[2])
lista.append(False)
print(lista)

tupla = (1, True,["a", "b", "c"],"hola")
tupla[2][0]="b"
print(tupla)

def sumPrimUlt(lista):
    suma = lista[0] + lista[-1]
    return suma

def promedioPrimUlt(lista):
    prom = (lista[0] + lista[-1])/2
    return prom

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el primer número: "))
num3 = int(input("Ingrese el primer número: "))

l = [num1, num2, num3]

print(sumPrimUlt(l))
print(promedioPrimUlt(l))

Pedir nombre, apellido de una persona y el día, mes, año en que nació.
Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión
bajo y de su año de nacimiento) y mostrarla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dia = input("Ingrese el día en que nació: ")
mes = input("Ingrese el mes en el que nació: ")
anio = input("Ingrese el año en que nació: ")

print("Su clave es: " + (nombre[0]) + (apellido[0]) + "_"+(anio))

def cuantos_dias(nro_mes):
  meses = [["enero,31"], ["febrero", 28], ["marzo",31], ["abril", 30], ["mayo", 31], ["junio", 30], ["julio", 31],["agosto", 31], ["septiembre",30],["octubre", 31], ["noviembre", 30], ["diciembre", 31]]
  mes = meses[nro_mes-1]
  cant = mes[1]
  return cant

print(cuantos_dias(3))

def triangulo(lado1,lado2,lado3):
    if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
        print("Se forma un triangulo")
    else:
        print("No se forma un triángulo")


a = int(input("Ingrese la primer longitud: "))
b = int(input("Ingrese la segunda longitud: "))
c = int(input("Ingrese la tercer longitud: "))

print(triangulo(a,b,c))
"""

def calculo_pulsaciones(edad, entrenamiento):
    if entrenamiento == "si":
        return (220 - edad)/10
    elif entrenamiento == "no":
        return (210 - edad)/10
    else:
        return "No es posible calcular el número de pulsaciones."


a = int(input("Ingrese su edad: "))
b = input("Si entrena ingrese: si. Si no entrena ingrese no: ")

print(calculo_pulsaciones(a,b.lower))
