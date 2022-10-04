print("hola mundo")
jugar= input(print("Quieres sumar dos numeros? S/N"))
if jugar == "s":
    var1 = int(input("Ingresa un numero: "))
    var2 = int(input("Ingresa otro numero: "))
    print("Ingresaste " + str(var1), str(var2))
    print("La suma es: ", str(var1+var2))
else:
    IVA = 0.21
    precioproducto = 100
    previoiva = precioproducto*IVA
    preciofinal =  precioproducto+previoiva
    print("El precio con IVA es: " + str(preciofinal))
