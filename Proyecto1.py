"""
print("Hola fundamentos")
print(2 + 3)

#Al poner los números entre comillas, se lo toma como un String y la suma funciona para concatenar
print("2" + "3") 

print(2 * (3 + 5))
print(2 * 3 + 5)

#Concatenar 3 veces la palabra Hola
print(3 * "Hola")
#Concatenar 3 veces la palabra Hola
print("Hola" * 3)

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese otro valor: "))
suma = num1 + num2
print(suma)

#Pedir que se ingrese un número e imprimir el triple
num = int(input("Ingrese un número: "))
resultado = num * 3
print("El resultado es: " + str(resultado))

#Pedir que se ingrese un número e imprimir la mitad
num1 = int(input("Ingrese un número: "))
division = num1 / 2
print("El resultado es: " + str(division))

#Pedir que se ingrese 3 notas e imprimir el promedio. Recordar que el
#promedio es la suma de los números dividido la cantidad.
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3)/3
print("El promedio de las notas es: " + str(promedio))

#Pedir base y altura de un triángulo y mostrar el área del mismo
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es: " + str(area))

#Pedir el diámetro de un círculo y calcular su área y perímetro. Recordar
# que Perímetro = π * Diámetro , Área = π * radio2. Por último, el diámetro = 2 * radio
pi = 3,14
diametro = float(input("Ingrese el diámetro del círculo: "))
perimetro = pi * diametro

"""



""" Ejercicio 17: Pedir cuatro datos, quién, qué hizo, cuándo y cómo. Mostrar la siguiente
noticia: “Última noticia!, la persona xx, en el dia xx, hizo xx, de la siguiente manera xx”

nombre = input("Ingrese el nombre: ")
hecho = input("Ingrese el hecho que realizó: ")
cuando = input("Ingrese cuando lo hizo: ")
como = input("Ingrese como lo hizo: ")
print("Última noticia!, la persona " + nombre + " en el día " + cuando + " hizo " + hecho + ", de la siguiente manera " + como ".")
"""

"""Ejercicio 16: Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse.
Mostrar el siguiente mensaje “La solicitud de inscripción a la comisión <comision>
solicitada por el alumno <apellido>, <nombre> está siendo procesada”
"""
"""
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
num = input("Ingrese el número del alumno: ")
comision = input("Ingrese la comisión: ")
print("La solicitud de inscripción a la comisión: " + comision + " solicitada por el alumno: " + apellido + ", " + nombre + " está siendo procesada.")
"""
"""Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació.
Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión
bajo y de su año de nacimiento) y mostrarla.
"""
"""
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dia = input("Ingrese el día en que nació: ")
mes = input("Ingrese el mes en que nació: ")
anio = input("Ingrese el año en que nació: ")

#Ejercicio 19: Mostrar 5 veces la cadena “Hola”
#print("hola " * 5)

palabra1 = input("Ingrese la primer palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

longitud1 = len(palabra1)
longitud2 = len(palabra2)

print("La cantidad total de letras son: " +  str(longitud1 + longitud2))
"""

"""Ejercicio 16: Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse.
Mostrar el siguiente mensaje “La solicitud de inscripción a la comisión <comision>
solicitada por el alumno <apellido>, <nombre> está siendo procesada”
"""
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
num = input("Ingrese el número del alumno: ")
comision = input("Ingrese la comisión: ")
print("La solicitud de inscripción a la comisión: " + comision + " solicitada por el alumno: " + apellido + ", " + nombre + " está siendo procesada.")

#Ejercicio 30: Pedir 5 palabras y mostrar la cantidad de letras que tienen en total.
palabra1 = input("Ingrese la primer palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera palabra: ")

longitud1 = len(palabra1)
longitud2 = len(palabra2)
longitud3 = len(palabra3)

print("La cantidad total de letras son: " +  str(longitud1 + longitud2 + longitud3))

#longitud = len(str(palabra1))+len(str(palabra2))+len(str(palabra3))

#print("La cantidad total de letras son: " +  longitud)