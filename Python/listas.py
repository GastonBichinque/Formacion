from sre_constants import JUMP


lista = ["perro", "gato", "raton"]
print("Tu lista actual " + str(lista))
respuesta = input("Ingresa un nuevo item ")
if respuesta in lista:
    print("Este item ya existe")
else: 
    print(str(respuesta) + " Item agreagado: ")
    lista.append(respuesta)
    print(lista)
