import sys

numero_inicial = 0

print("Vamos a hacer un triángulo con estrellas, te parece?")
numero_del_usuario = int(input("Ingresa el número:\t"))

if numero_del_usuario == 0:
    print("Debes ingresa un valor válido")
    sys.exit()

while numero_inicial != numero_del_usuario:
    print('* ' * (numero_inicial+1) + '\n')
    numero_inicial += 1


