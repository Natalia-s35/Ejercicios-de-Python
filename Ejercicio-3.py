"""
Realice un programa que tenga las funciones que se detallan en a), b), c) y d), y luego coordinar su llamado a través del menú que se solicite en el inciso e) de esta consigna.
a)Llamada a carga_datos que permita ingresar los datos de personas encuestadas: nombre de la cancion preferida, 
la cantidad de veces que la escucha al dia y el año de publicacion de la cancion. (30 personas)
b)crear una funcion mostrar_lista_encuestados que reciba como parametro la lista de encuestados y la muestre por pantalla.
c) Crear una funcion veces_al_dia que deberá contar la cantidad de canciones que son escuchadas mas de 4 veces al dia y que muestre el resultado por pantalla.
d)funcion calcular_promedio que calcule el promedio de reproducciones de canciones que se publicaron en 2010
e)Realizar un menú que coordine la invocacion de las funciones anteriores
"""
#Definición de funciones
def cargar_datos():
  lista = []
  for i in range(30):
    nombre = input("Ingrese el nombre de la canción: ")
    reproducciones = int(input("Ingrese el número de reproducciones diarias: "))
    año = int(input("Ingrese el año de publicación: "))
    cancion = [nombre, reproducciones, año]
    lista.append(cancion)
  return lista

def mostrar_lista_canciones(lista):
  for cancion in lista:
    print(cancion)

def veces_al_dia(lista):
  cont = 0
  for cancion in lista:
    if cancion [1] > 4:
      cont = cont + 1
  return cont

def canciones2010(lista_canciones):
  canciones_2010 = []
  for cancion in lista_canciones:
    if cancion[2] == 2010:
      canciones_2010.append(cancion)
  return canciones_2010


def calcular_promedio(lista):
  can_2010 = canciones2010(lista)
  suma = 0 
  cantidad = len(can_2010)
  for cancion in can_2010:
    suma = suma + cancion[1]
  if cantidad!= 0:
    promedio = suma / cantidad
    return promedio
  else:
    return 0

def opcionesMenu():
    print("1.-Mostrar la lista de canciones")
    print("2.-Mostrar la cantidad de canciones que son escuchas mas de cuatro veces al dia")
    print("3.-Mostrar el promedio de reproducciones de las canciones que fueron publicaas en el año 2010")
    print("4.-Salir")

#Programa principal
canciones = cargar_datos()
opcionesMenu()
opcion = int(input("Ingrese una opción: "))

while opcion != 4:
    if opcion == 1:
        mostrar_lista_canciones(canciones)
    elif opcion == 2:
        veces_al_dia(canciones)
    elif opcion == 3:
        prom = calcular_promedio(canciones)
        print("El promedio es: " + str(prom) + ".")
    else:
        print("Opción incorrecta.")

    opcionesMenu()
    opcion = int(input("Ingrese una opción: "))

print("El programa ha finalizado.")
