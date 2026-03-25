import random

# Diccionario de categorías
words = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "general": ["casa", "perro", "auto", "mesa"],
    "ciencia": ["atomo", "celula", "energia", "masa"]
}

# Mostrar categorias disponibles
print("Categorías disponibles:")
for categoria in words:
    print("-", categoria)

# Elegir categoria
categoria_elegida = input("Elegí una categoría: ")

# Validar categoría
while categoria_elegida not in words:
    print("Categoría no válida")
    categoria_elegida = input("Elegí una categoría: ")

# Elegir palabra de la categoria
word = random.choice(words[categoria_elegida])

guessed = []
attempts = 6
score = 0

print("\n¡Bienvenido al Ahorcado!")
print()

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
