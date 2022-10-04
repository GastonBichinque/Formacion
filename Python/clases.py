class Perro:
    def __init__(self, id, raza, edad):
        self.raza = raza
        self.edad = edad
        self.id = id

rottweiler = Perro(1,"Rottweiler", 9)
yorkshire = Perro(2,"Yorkshire", 3)
print("Elige uno: ")
print("1 ",rottweiler.raza, rottweiler.edad)
print("2 ",yorkshire.raza, yorkshire.edad)
eleccion = int(input("Elige una opción: 1-2"))
if eleccion==rottweiler.id:
    print("Elegiste a ", rottweiler.raza)
elif eleccion==yorkshire.id:
    print("Elegiste a ", yorkshire.raza)
