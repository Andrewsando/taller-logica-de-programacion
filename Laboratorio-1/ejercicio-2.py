import random
import sys
numero_aleatorio = random.randint(1,10)

print("Tengo un número del 1 al 10, puedes adivinar cuál es?")
print("Tienes tres intentos")

#Primer intento
primer_intento = int(input("Ingresa el primer intento\t"))
if primer_intento > numero_aleatorio:
    print("Tu número es mayor al que tengo pensado")
elif primer_intento < numero_aleatorio:
    print("Tu número es menor al que tengo pensado")
else:
    print("Adivinaste!, el número es", numero_aleatorio)
    sys.exit()

#Segundo intento
segundo_intento = int(input("Ingresa el segundo intento\t"))
if segundo_intento > numero_aleatorio:
    print("Tu número es mayor al que tengo pensado")
elif segundo_intento < numero_aleatorio:
    print("Tu número es menor al que tengo pensado")
else:
    print("Adivinaste!, el número es", numero_aleatorio)
    sys.exit()
    
#Tercer intento
tercer_intento = int(input("Ingresa el tercer intento\t"))
if tercer_intento > numero_aleatorio or tercer_intento < numero_aleatorio:
    print("Perdiste!, el número que pensaba es", numero_aleatorio)
else:
    print("Adivinaste!, el número es", numero_aleatorio)
   