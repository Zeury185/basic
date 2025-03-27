buscar = int(input("""programa que encuentra un numero especifico
      
      por favor digitar un numero..:"""))
for numero in range(10):
    if buscar == numero:
        print("numero encontrado", buscar)
        break
else:
    print("no encontrado")
