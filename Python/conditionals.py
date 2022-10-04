#de dos numeros, saber cual es el mayor
#crear una variable numerica y si esta entre 0 y 10 mostrar un mensaje
#entre 11 y 20 otro
#entre 21 y 30 otro

import re
from unittest import result


print("Bienvenido")
var1 = int(input("Ingresa un numero: "))
var2 = int(input("Ingresa otro numero: "))
if var1>var2:
    print(str(var1)+" Es el numero mas grande")
elif var1<var2:
    print(str(var2)+" Es el numero mas grande")
elif var1==var2:
    print("Son iguales!")
resultado=int(input("Ingresa un numero entre 0 y 30: "))
if (resultado>= 0 and resultado<=10):
    print("Esta entre 0 y 10")
elif (resultado >=11 and resultado<=20):
    print("Esta entre 11 y 20")
elif (resultado>=21 and resultado<=30):
    print("Esta entre 21 y 30")