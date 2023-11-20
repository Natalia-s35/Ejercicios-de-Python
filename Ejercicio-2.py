"""
Realice un programa para manejar equipos de fútbol, Armar una lista que tenga información sobre los equipos de fútbol. 
Para cada equipo deberán tener: el nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor. 
b) Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los equipos que están en la primera y última posición de la lista. 
c) Imprimir el nombre del equipo Campeón de la lista generada en el punto a), el equipo campeón es aquel que sumo más puntos
"""
def cargar_datos():
    equipos = []
    nombre = input("Ingrese el nombre del equipo. La carga finaliza cuando ingresa 'zzz': ")

    while nombre != "zzz":
        puntos = int(input("Ingrese los puntos: "))
        goles = int(input("Ingrese los goles: "))
        posicion = int(input("Ingrese la posición: "))
        equipos.append([nombre, puntos, goles, posicion])
    nombre = input("Ingrese el nombre del equipo (la carga finaliza cuando ingreza 'zzz': ")

    return equipos

funcion = cargar_datos()
print(funcion)

def equipo_ultima_posicion(equipos):
  pos = -1
  equi = []
  for e in equipos:
    if e[3] > pos:
      pos = e[3]
      equi = e
  return equi[2]

goles_a_favor = equipo_ultima_posicion(funcion)
print("Los goles a favor del último equipo son: " + str(goles_a_favor))

def equipo_goles_del_primero(equipos):
  pos = -1
  equi = []
  for e in equipos:
    if e[3] > pos:
      pos = e[1]
      equi = e
  return equi[2]

goles_a_favor_del_pri = equipo_goles_del_primero(funcion)
print("Los goles a favor del primero son: " + str(goles_a_favor_del_pri))

def equipo_primera_posicion(equipos):
  pos = -1
  equi = []
  for e in equipos:
    if e[3] > pos:
      pos = e[1]
      equi = e
  return equi[0]

equipo_campeon = equipo_primera_posicion(funcion)
print("El equipo campeón es: " + equipo_campeon)