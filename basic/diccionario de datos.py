dic_datos = {
    "id": "6513",
    "Nombre": "Eury Zorrilla",
    "Edad": "25",
    "Telefono": "8298776471",
    "Email": "zorrillaaraujo01@gmail.com",
}

datos = int(input("""Programa que identefica y modifica datos personales.

Porfavor digite el id de la persona a editar: """))

if "id" in dic_datos:
    print("Nombre", dic_datos["Nombre"])
    print("edad", dic_datos["Edad"])
    print("Telefono", dic_datos["Telefono"])
    print("Email", dic_datos["Email"])
    que = input("Le gustaria hacer algun tipo de cambio? ").lower()
    if que == "si":
        print(dic_datos)
        b = input("que le gustaria modificar? ")

        if b == "Nombre":
            b = str(input("agrega el nombre a sustituir "))
            dic_datos["Nombre"] = b
            print("Actualizado sastifactoriamente")
            print("Nombre", dic_datos["Nombre"])
            print("edad", dic_datos["Edad"])
            print("Telefono", dic_datos["Telefono"])
            print("Email", dic_datos["Email"])
else:
    print("No se encuentra ninguna informacion")
