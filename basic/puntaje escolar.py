calif = int(input("dijite la calificacion del estudiante..:"))
if calif <= 0 or calif > 100:

    print("Desconocemos de esa calificacion!")
if calif <= 100 and calif >= 95:
    print("promovido con excelencia")

elif calif <= 94 and calif >= 85:
    print("promovido con honores")

elif calif <= 84 and calif >= 70:
    print("promovido")

else:
    print("reprovado")
