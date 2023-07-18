import os
os.system("clear")

def suma(a,b):
    c = a + b
    print ("La suma de a + b es: ",c)
def resta(a,b):
    c = a - b
    print ("La resta de a + b es: ",c)
def multiplicacion(a,b):
    c = a * b
    print ("La multiplicación de a + b es: ",c)
def division(a,b):
    if b == 0:
        print ("La division no se puede hacer")
    else:
        c = a / b
        print ("La división de a + b es: ",c)

# calculadora

suma (2, 4)
resta (2, 4)
multiplicacion (2, 4)
division (2, 6)