import random

valor_minimo = 1
valor_maximo = 6

volver_a_jugar = input("quieres tirar los dados?: ")

while volver_a_jugar == "si" or volver_a_jugar == "s":
    print("Tirando los dados...")

    dado_1 = random.randint(valor_minimo, valor_maximo)

    dado_2 = random.randint(valor_minimo, valor_maximo)

    print("El primer dado da..." )
    print(dado_1)

    print("El segundo dado da..." )
    print(dado_2)

    print("La suma del valor de los dados es:")
    print(dado_1 + dado_2)

    volver_a_jugar = input("quieres volver a tirar?: ")
    if volver_a_jugar == "no" or volver_a_jugar == "n":
         print("gracias por jugar:)")