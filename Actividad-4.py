"""
a) Defina una función que reciba como argumento una cadena de texto y retorne un valor entero indicando la cantidad de vocales que contiene la cadena Ejemplo: “agua” -> 3, “pepe” ->2
b) Defina una función que genere una lista de palabras hasta que se ingrese la palabra “fin” la cual NO debe ser almacenada en la lista, por cada palabra, también se guardara la cantidad de 
vocales que contiene la misma, para esto deberá utilizar la función definida en el punto 1) a, al finalizar la función deberá retornar la lista generada. a) La lista resultado deberá tener una estructura similar a: 1) [[“uno”,2],[ “pepe”,2],[”agua!”,3],…etc]
c) defina una función que reciba como argumento la lista generada en el punto 1.b) e imprimir las palabras que tienen mas de 3 vocales.
d) escriba el código del programa que integra las 3 funciones antes definidas.
"""
def cantidad_vocales(p):
  vocal = 0
  for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      vocal = vocal + 1
  return vocal

palabra = input("Ingrese una palabra")
cantidad = cantidad_vocales(palabra)

print("La cantidad de vocales que tiene la palabra " + palabra + " es: " + str(cantidad))

t1 = input("Ingrese un texto: ")
t2 = input("Ingrese otro texto: ")
if len(t1) >= 2 and len(t2) >= 2:
  if t1[0] == t2[0] and t1[-1] == t2[-1]:
    print("Son iguales")
  else:
    print("Son diferentes")
else:
  print("El texto debe tener al menos dos caracteres. ")

cadena = []
cont = 1
while cont <= 2:
  texto = input("Ingrese una palabra: ")
  if len(texto) >= 2:
    cadena.append(texto)
    contador = contador + 1
  else:
    print("La palabra debe tener al menos dos caracteres. ")
t1 = cadena[0]
t2 = cadena[1]
if t1[0] == t2[0] and t1[-1] == t2[-1]:
  print("Son iguales")
else:
  print("No diferentes")

texto = input("Ingrese una palabra: ")
num = int(input("Ingrese un número: "))
if len(texto) > 0 and num > 0:
  print(texto * num)
else:
  print("Los datos no cumplen los requisitos mínimos.")

verificar = True
while verificar:
  texto = input("Ingrese una palabra: ")
  num = int(input("Ingrese un número: "))
  if len(texto) > 0 and num > 0:
    print(texto * num)
    verificar = False
  else:
    print("Los datos no cumplen los requisitos mínimos.")