con = input("A que le gustaria convertir: (C) Celcius o (F) Fahrenheit?")
con = con.lower()

if con == "c" or con == "celcius":
    c = float(input("digitar el numero que decea convertir a Celcius..:"))
    resultado = (c - 32) * 5/9
    print("El resultado a celcius es..:", resultado)

if con == "f" or con == "fahrenheit":
    f = float(input("Digitar el numero que decea convertir a Fahrenheit..:"))
    resultado = f * 9/5 + 32
    print("El resultado a Fahrenheit es..:", resultado)

else:
    print("Escala incorrecta")
