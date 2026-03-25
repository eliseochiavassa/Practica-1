import random

# Diccionario de categorías
words = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "general": ["casa", "perro", "auto", "mesa"],
    "ciencia": ["atomo", "celula", "energia", "masa"]
}

print("¡Bienvenido al Ahorcado!")

while True:
    # Mostrar categorías
    print("\nCategorías disponibles:")
    for categoria in words:
        print("-", categoria)

    # Elegir categoría
    categoria_elegida = input("Elegí una categoría: ")

    while categoria_elegida not in words:
        print("Categoría no válida")
        categoria_elegida = input("Elegí una categoría: ")

    # Copia de la lista para no repetir palabras
    palabras_disponibles = words[categoria_elegida].copy()

    # Elegir palabra sin repetir
    word = random.choice(palabras_disponibles)
    palabras_disponibles.remove(word)

    guessed = []
    attempts = 6
    score = 0

    print("\nNueva palabra!")

    while attempts > 0:
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        if "_" not in progress:
            score += 6
            print("¡Ganaste!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")

        print()

    else:
        score = 0
        print(f"¡Perdiste! La palabra era: {word}")

    print("Puntaje:", score)

    # Preguntar si quiere seguir
    seguir = input("\n¿Querés jugar otra ronda? (s/n): ")
    if seguir.lower() != "s":
        print("Gracias por jugar!")
        break
