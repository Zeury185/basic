n1 = float (input("digite el numer a calcular..:"))
n = input("que le gustaria hacer sumar, dividir, o restar..:")
if (n == "sumar" ):
    n2 = float(input("digite el numero a sumar..:"))
    r = (n1 + n2)
    print("el resultado es..:",r)

elif (n == "restar"):
    n2 = float(input("digite el numero a restar..:"))
    r =(n1 - n2)
    print ("resultado es..:", r)

elif (n == "dividir"):
    n2 = float(input("digite el numero a dividir..:")) 
    if n2 == 0:
        print("desconozco de esta operacion")
    else:
        r =(n1 / n2)
        print ("resultado es..:", r)

else:
    
    print("desconozco de esa operacion")
    
    