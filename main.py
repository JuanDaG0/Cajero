
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
    
elif opcion =="3":
    retiro=float(input("ingrese la cantidad a retirar:$"))
    if retiro>0:
        if retiro<=saldo:
            saldo=saldo-retiro
            print("Retiro exitoso.")
        else:
            print("No tiene suficiente saldo.")
        else:
            print("El monto debe ser mayor a 0.")
            
    elif opcion =="4":
        print("Gracias por usar el cajero automatico.")
        continuar ="n" 
    else:
        print("Opcion invalida.")
        if continuar =="s":
        continuar = input("\n¿Desea realizar otra operacion?(s/n):")
        print("Programa finalizado.")
