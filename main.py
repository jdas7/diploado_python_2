import os
os.system("clear")

# Primero: Importar modulo
import funciones_2

print("Primera forma de importar: ", funciones_2.suma(5,8))

# segunta manera de importar
from funciones_2 import multiplicacion

print("Segunda manera de importar: ", multiplicacion(7,8))

# Tercera manera de importar

from funciones_2 import * # Mala practica

print("Tercera manera de importar: ", resta(5,6))

print(canal)

# manera de importar desde un paquete

from paquete.funciones_3 import exponente, area_del_cuadrado, area_del_cuadrado_2

area_del_cuadrado(8,6)
print("Importar desde un paquete", exponente(4))
print("El area del cuadrado es: ", area_del_cuadrado_2(8,6))

# para importar sub paquete

from paquete.subpaquete.funcionesAvanzadas import function

function(5,5)# Mala