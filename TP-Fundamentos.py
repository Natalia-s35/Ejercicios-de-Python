#Nombre: Natalia Hernandez
#DNI: 40305779
"""
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3)/3
print("El promedio de las notas es: " + str(promedio))

#Ingresar 2 textos por teclado y agregar la primer y última letra de cada texto en una lista y en una tupla
texto1 = input("Ingrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")

lista1 = [texto1[0], texto1[-1],texto2[0],texto2[-1]]
tupla1 = (texto1[0],texto1[-1],texto2[0],texto2[-1])

print(lista1, tupla1)

tuplaPalabras = ("casa", "arbol", "camino", "lluvia")
print("camino" in tuplaPalabras)

#Listas
listaNueva = [1, "Hola", "Argentina", 193, "fundamentos"]
listaNueva[1] = "Adios"
print(listaNueva)

listaNueva.append(5)


mensaje = "Hola que tal"
print(mensaje[len(mensaje)-1])
print(mensaje[1:3])

palabra = "manzana"
nuevaPalabra = palabra.upper()
print(nuevaPalabra)

#Calcular el sueldo con el 20% de aumento de un empleado:
antiguedad = input("Ingrese su antiguedad en el trabajo: ")
sueldo = input("Ingrese su sueldo: ")
sueldo2 = (int(sueldo) + int(antiguedad)) * 0.20
print(sueldo2)
"""
