#Ingreso de los datos de los alumnos
def ingresar_datos():
  l = []
  nombre = input("Ingrese el nombre: ").lower()
  while nombre != "fin":
    apellido = input("Ingrese el apellido: ").lower()
    mail = input("Ingrese el mail: ")
    direccion = input("Ingrese la dirección del alumno: ")
    orquesta = input("Ingrese el nombre de la orquesta a la que pertenece: ").lower()
    instrumento_propio = input("Si cuenta con instrumento propio (s/si) o no (n/no): ").lower()
    edad = int(input("Ingrese la edad: "))
    legajo = int(input("Ingrese el número de legajo: "))
    alumno = [nombre, apellido, mail, direccion, orquesta, instrumento_propio, edad, legajo]
    l.append(alumno)

    nombre = input("Ingrese el nombre: ")
  return l

#Cantidad de alumnos que no cuentan con instrumento propio:
def instrumentos_no_propio(l):
  cont = 0
  for a in l: #uso de la estructura for para recorrer la lista
    if a[5] == "n" or a[5] == "no":
        cont = cont + 1
  return cont

#promedio de las edades de chicos de la inicial
def promedio_edades_inicial(l):
  suma = 0
  cont = 0
  for a in l:
    if a[4] == "inicial":
      suma = suma + a[6]
      cont = cont + 1
  if cont != 0:
      return suma / cont
  else:
      return 0
    
#funcion general para calcular la cantidad de alumnos por la orquesta solicitada por el usuario
def calcular_cantidad(l, orquesta):
   cant = 0
   for a in l:
      if a[4] == orquesta:
         cant = cant + 1
   return cant


#El alumno con mayor edad
def mayor_edad(l):
  mayor = -99999
  for a in l:
    if mayor < a[6]:
      mayor = a[6]
  return mayor


#El alumno con menor edad
def menor_edad(l):
  menor = 99999
  for a in l:
    if menor > a[6]:
      menor = a[6]
  return menor

#Buscar por número de legajo los datos del alumno (apellido y orquesta)
def buscar_dato(l, n):
  for a in l:
    if a[7] == n:
      print("Apellido: ", a[1])
      print("Orquesta: ", a[4])


def exportar_datos_excel():
   
    #Importamos la librería Pandas de Python
    import pandas as pd

    #Creamos el dataframe a partir de la lista de datos de los alumnos y asignamos el nombre de cada columna
    df = pd.DataFrame(datos, columns = ["Nombre", "Apellido", "Mail", "Direccion", "Orquesta", "Instrumento", "Edad", "Legajo"])

    #Uso del  método .to_excel sobre el dataframe e incluimos la ruta donde queremos que se encuentre el archivo excel con el nombre
    df.to_excel("C:/Users/PC/Desktop/practica/ejemplo.xlsx", index = False)

    print("Proceso finalizado.")

print("-"*130)
print("Bienvenido al sistema de Escuela Orquesta")
print("-"*130)
print()

def opciones_menu():
    print("Menú")
    print("1.Calcular la cantidad de alumnos que no cuentan con instrumento propio")
    print("2.Calcular el promedio de los alumnos de la orquesta inicial")
    print("3.Cantidad de alumnos de una de las orquestas ")
    print("4.Alumno de mayor edad")
    print("5.Alumno de menor edad")
    print("6.Buscar apellido y orquesta del alumno con el número de legajo")
    print("7.Exportar los datos de los alumnos a Excel")
    print("8.Salir")
    print()

datos = ingresar_datos()

def menu():
  
  opciones_menu()

  opcion = int(input("Ingrese una opción: "))

  while opcion != 8:

    if opcion == 1:
        p = instrumentos_no_propio(datos)
        print("La cantidad de alumnos que no cuentan con instrumentos son: " + str(p))
        print()
    elif opcion == 2:
        inicial = promedio_edades_inicial(datos)
        print("El promedio de las edades de los alumnos de la orquesta inicial es: ", inicial)
        print()
    elif opcion == 3:
        orq = input("Ingrese el nombre de la orquesta: ").lower()
        if orq == "inicial" or orq == "sinfonica" or orq == "infanto juvenil":
          cantidad= calcular_cantidad(datos, orq)
          print("En la Orquesta " + orq + " hay "  + str(cantidad) + " alumnos.")
        else:
           print("La orquesta solicitada no existe.")
        print()
    elif opcion == 4:
        mayor = mayor_edad(datos)
        print("El alumno de mayor edad tiene: " + str(mayor) + " años.")
        print()
    elif opcion == 5:
        menor = menor_edad(datos)
        print("El alumno de menor edad tiene: " + str(menor) + " años.")
        print()
    elif opcion == 6:
        num = int(input("Ingrese el número del legajo del alumno: "))
        buscar_dato(datos, num)
        print()
    elif opcion == 7:
       exportar_datos_excel()
       print()
    else:
        print("La Opción ingresada es incorrecta.")

    opciones_menu()

    opcion = int(input("Ingrese una opción: "))

print()
menu()
print()

print("-"*130)
print("El programa ha finalizado.")
print("-"*130)