operacion = input("Digita la operación que deseas efectuar, ej: +, -, /, *\t")
numero_uno = int(input("Cuál es el primer número?\t"))
numero_dos = int(input("Cuál es el segundo número?\t"))

if operacion == "+":
    print("El resultado es", numero_uno + numero_dos)
elif operacion == "-":
    print("El resultado es", numero_uno - numero_dos)
elif operacion == "*":
    print("El resultado es", numero_uno * numero_dos)
elif operacion == "/":
    print("El resultado es", numero_uno / numero_dos)
else:
    print("La operación no se puede efectuar")    
