import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6
score = 0  # NUEVO

print("¡Bienvenido al Ahorcado!")
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
        score += 6  #  SUMA SI GANA
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
        score -= 1  #  RESTA SI FALLA
        print("Esa letra no está en la palabra.")

    print()

else:
    score = 0  #  SI PIERDE
    print(f"¡Perdiste! La palabra era: {word}")

print("Puntaje:", score)  # SCORE FINAL
