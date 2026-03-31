import random

palabras = ["python", "programacion", "computadora", "codigo", "inteligencia"]
palabra_secreta = random.choice(palabras)
progreso = ["_"] * len(palabra_secreta)

intentos_maximos = 6
letras_adivinadas = []

print("Bienvenido al Juego del Ahorcado")

while intentos_maximos > 0 and "_" in progreso:
    print(f"\nPalabra: {' '.join(progreso)}")
    print(f"Intentos restantes: {intentos_maximos}")
    print(f"Letras usadas: {', '.join(letras_adivinadas)}")
    
    letra = input("Introduce una letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, introduce solo una letra válida.")
        continue
    
    if letra in letras_adivinadas:
        print("Ya habías intentado con esa letra.")
        continue

    letras_adivinadas.append(letra)
    if letra in palabra_secreta:
        print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        # Actualizamos los guiones por la letra correcta
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                progreso[i] = letra
    else:
        intentos_maximos -= 1
        print(f"Lo siento, la '{letra}' no está.")
if "_" not in progreso:
    print(f"\n¡Felicidades! Ganaste. La palabra era: {palabra_secreta}")
else:
    print(f"\nGame Over. Te quedaste sin intentos. La palabra era: {palabra_secreta}")
