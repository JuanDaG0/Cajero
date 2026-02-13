saldo = 1000


print ("1. Consultar saldo") 
print ("2. Depositar")
print ("3. Retirar")

opcion = input ("SELECCIONE UNA OPCION(1-3)") 
if opcion == "1":
    print ("Su saldo actual es: ", saldo)
elif opcion == "2":
    if deposito > 0:
    saldo = saldo + deposito
    print ("Deposito exitoso")
    print ("Nuevo saldo: ", saldo)
else:
    print ("El monto debe ser mayor a ")