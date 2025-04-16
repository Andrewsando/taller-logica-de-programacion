print("Vamos a validar cuál es el mayor número, te parece?");
numero_uno = int(input("Ingresa el primer número \t"))
numero_dos = int(input("Ingresa el segundo número \t"))
numero_tres = int(input("Ingresa el tercer número \t"))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El número mayor es", numero_uno)
elif numero_uno < numero_dos and numero_dos > numero_tres:
    print("El número mayor es", numero_dos)
elif numero_uno < numero_tres and numero_tres > numero_dos:
    print("El número mayor es", numero_tres)
else:
     print("Todos los números son iguales")
