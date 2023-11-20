
#Ingreso de los datos de los alumnos y los agregamos a la lista vacia "l"
def ingresar_datos():
  l = []
  nombre = input("Ingrese el nombre: ")
  while nombre != "fin":
    apellido = input("Ingrese el apellido: ")
    mail = input("Ingrese el mail: ")
    direccion = input("Ingrese la dirección del alumno: ")
    orquesta = input("Ingrese el nombre de la orquesta a la que pertenece: ")
    instrumento_propio = input("Si cuenta con instrumento propio (s/si) o no (n/no): ")
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
    if a[5] == "n":
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
    

#cantidad de alumnos en la orquesta sinfonica
def cantidad_sinfonica(l):
  cant = 0
  for a in l:
    if a[4] == "sinfonica":
      cant = cant + 1
  return cant
  
#Cantidad de alumnos en la orquesta infanto juvenil
def cantidad_infanto(l):
  cant = 0
  for a in l:
    if a[4] == "infanto juvenil":
      cant = cant + 1
  return cant
  
#Cantidad de alumnos en la orquesta inicial
def cantidad_inicial(l):
  cant = 0
  for a in l:
    if a[4] == "inicial":
      cant = cant + 1
  return cant

#El alumno con menor edad
def menor_edad(l):
  menor = 99999
  for a in l:
    if menor > a[6]:
      menor = a[6]
  return menor

#El alumno con mayor edad
def mayor_edad(l):
  mayor = -99999
  for a in l:
    if mayor < a[6]:
      mayor = a[6]
  return mayor

#Buscar por número de legajo los datos del alumno (apellido y orquesta)
def buscar_dato(l, n):
  for a in l:
    if a[7] == n:
      print("Apellido: ", a[1])
      print("Orquesta: ", a[4])


print("------Bienvenidos al sistema de Escuela Orquesta 501------")
print("Menú")
print("1.Calcular la cantidad de alumnos que no cuentan con instrumento propio")
print("2.Calcular el promedio de los alumnos de la orquesta inicial")
print("3.Cantidad de alumnos de la orquesta sinfónica")
print("4.Cantidad de alumnos de la orquesta infanto juvenil")
print("5.Cantidad de alumnos de la orquesta inicial")
print("6.Alumno de mayor edad")
print("7.Alumno de menor edad")
print("8.Buscar apellido y orquesta del alumno con el número de legajo")
print("9.Salir")

datos = ingresar_datos()
print(datos)

opcion = int(input("Ingrese una opción: "))

while opcion != 9:
  if opcion == 1:
    p = instrumentos_no_propio(datos)
    print("La cantidad de alumnos que no cuentan con instrumentos son: " + str(p))
  elif opcion == 2:
    inicial = promedio_edades_inicial(datos)
    print("El promedio de las edades de los alumnos de la orquesta inicial es: ", inicial)
  elif opcion == 3:
    cant_s= cantidad_sinfonica(datos)
    print("En la Orquesta sinfónica hay: " + str(cant_s) + " cantidad de alumnos.")
  elif opcion == 4:
    cant_infanto = cantidad_infanto(datos)
    print("En la Orquesta infanto juvenil hay: " + str(cant_infanto) + " cantidad de alumnos.")
  elif opcion == 5:
    cant_inicial = cantidad_inicial(datos)
    print("En la Orquesta inicial " + str(cant_inicial) + " cantidad de alumnos.")
  elif opcion == 6:
    mayor = mayor_edad(datos)
    print("El alumno de mayor edad tiene: " + str(mayor) + " años.")
  elif opcion == 7:
    menor = menor_edad(datos)
    print("El alumno de mayor edad tiene: " + str(menor) + " años.")
  elif opcion == 8:
    num = int(input("Ingrese el número del legajo del alumno: "))
    buscar_dato(datos, num)
  else:
    print("Opción incorrecta.")

  opcion = int(input("Ingrese una opción: "))

print("El programa ha finalizado.")

 

#Importamos la librería Pandas de Python
import pandas as pd

#Creamos el dataframe a partir de la lista de datos de los alumnos y asignamos el nombre de cada columna
df = pd.DataFrame(datos, columns = ["Nombre", "Apellido", "Mail", "Direccion", "Orquesta", "Instrumento", "Edad", "Legajo"])

#Uso del  método .to_excel sobre el dataframe e incluimos la ruta donde queremos que se encuentre el archivo excel con el nombre
df.to_excel("C:/Users/PC/Desktop/practica/ejemplo.xlsx", index = False)

print(df)
