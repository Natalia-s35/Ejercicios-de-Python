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
    denominador = y[0] * x[1]
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