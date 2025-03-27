lista = ["joan", "ramc", "anthony"]
print("hola!, en la lista tenemos varios amigos tuyos, ellos son..:", lista)
agregaroquitar = input("Te gustaria agregar o quitar algunos de ellos?..:")
agregaroquitar = agregaroquitar.lower()

if (agregaroquitar == "quitar"):

    listar = input("a quien te gustaria quitar?..:")
    listar = listar.lower()

    if listar == "anthony":
        b = input("seguro que quieres remover a anthony?")
        b = b.lower()
        if (b == "si"):
            listar = "anthony"
            if listar in lista:
                lista.remove(listar)
            print(lista)
            print("Removido sastifactoriamente")
    elif listar == "ramc":
        b = input("seguro que quieres remover a ramc?")
        b = b.lower()

        if (b == "si"):

            if listar in lista:
                lista.remove(listar)
            print(lista)
            print("Removido sastifactoriamente")
            listar = listar.lower()
    elif listar == "joan":
        b = input("seguro que quieres remover a joan?")
        b = b.lower()
        if (b == "si"):
            if listar in lista:
                lista.remove(listar)
            print(lista)
            print("Removido sastifactoriamente")
        else:
            (
                print("cancelado")
            )

if (agregaroquitar == "agregar"):

    listaadd = input("digite el nombre a agregar?..:")
    h = input("Seguro que quieres agregar dicho nombre?..:")
    if (h == "si"):

        if listaadd not in lista:
            lista.append(listaadd)
            print(lista)
        print("agregado sastifactoriamente")

    elif (h == "no"):

        print("Cancelado")

    if h != "si" and h != "no":
        print("Disculpa no entendí")
if listar != lista:
    print("No se encuentra en la lista")
    listar = listar.lower()

elif (agregaroquitar != "agregar", "quitar",):
    print("ok!")
