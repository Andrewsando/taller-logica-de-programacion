total_cuenta_inicial = int(input("Ingrese el monto total de la cuenta\t"))
propina_inicial = int(input("Ingrese el porcentaje de propina que desea dejar\t")) / 100

propina_final = total_cuenta_inicial * propina_inicial
total_cuenta_final = total_cuenta_inicial - propina_final

print("La propina es:", propina_final)
print("El total a pagar es:", total_cuenta_final)



