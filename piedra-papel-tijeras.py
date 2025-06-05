""""
def pedir_opcion(nombre):
    while True:
        opcion = input(f"{nombre}, ¿Qué eliges? ¿Piedra, papel o tijeras?: ").capitalize()
        if opcion in ["Piedra", "Papel", "Tijeras"]:
            return opcion
        else:
            print("Opción no válida. Por favor, intentá nuevamente.")

nombre1 = input("¿Cómo se llama el jugador 1?: ").capitalize()
nombre2 = input("¿Cómo se llama el jugador 2?: ").capitalize()

jugador1 = input(f"{nombre1}, ¿Qué eliges? ¿Piedra, papel o tijeras?: ").capitalize()
jugador2 = input(f"{nombre2}, ¿Qué eliges? ¿Piedra, papel o tijeras?: ").capitalize()

condicion1 = jugador1 == "Piedra" and jugador2 == "Tijeras"
condicion2 = jugador1 == "Papel" and jugador2 == "Piedra"
condicion3 = jugador1 == "Tijeras" and jugador2 == "Papel"

if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)
"""

# Función que pide una opción válida al jugador
def pedir_opcion(nombre):
    while True:  # Bucle que se repite hasta que se ingresa una opción válida
        opcion = input(f"{nombre}, ¿Qué eliges? ¿Piedra, papel o tijeras?: ").capitalize()  # Pide la opción y la capitaliza
        if opcion in ["Piedra", "Papel", "Tijeras"]:  # Verifica si la opción es válida
            return opcion  # Si es válida, la devuelve y sale de la función
        else:
            print("Opción no válida. Por favor, intentá nuevamente.")  # Muestra un mensaje si la opción es incorrecta

# Pide el nombre del jugador 1 y lo capitaliza (primera letra en mayúscula)
nombre1 = input("¿Cómo se llama el jugador 1?: ").capitalize()
# Pide el nombre del jugador 2 y lo capitaliza
nombre2 = input("¿Cómo se llama el jugador 2?: ").capitalize()

# Inicializa los puntos del jugador 1 en 0
puntos1 = 0
# Inicializa los puntos del jugador 2 en 0
puntos2 = 0
# Inicializa el número de ronda en 1
ronda = 1

# Bucle del juego: se repite hasta que alguien llegue a 2 puntos o se jueguen 3 rondas
while puntos1 < 2 and puntos2 < 2 and ronda <= 3:
    print(f"\n--- Ronda {ronda} ---")  # Muestra el número de ronda actual
    
    jugador1 = pedir_opcion(nombre1)  # Pide la opción del jugador 1
    jugador2 = pedir_opcion(nombre2)  # Pide la opción del jugador 2

    if jugador1 == jugador2:  # Si ambos eligieron lo mismo
        print("Empate en esta ronda.")  # Es un empate
    elif (jugador1 == "Piedra" and jugador2 == "Tijeras") or \
         (jugador1 == "Papel" and jugador2 == "Piedra") or \
         (jugador1 == "Tijeras" and jugador2 == "Papel"):  # Verifica si gana el jugador 1
        puntos1 += 1  # Suma un punto al jugador 1
        print(f"Ganó {nombre1} esta ronda.")  # Muestra que ganó el jugador 1
    else:
        puntos2 += 1  # Suma un punto al jugador 2
        print(f"Ganó {nombre2} esta ronda.")  # Muestra que ganó el jugador 2

    # Muestra el puntaje actual de ambos jugadores
    print(f"Puntaje: {nombre1} {puntos1} - {nombre2} {puntos2}")
    ronda += 1  # Avanza a la siguiente ronda

# Muestra el resultado final después del bucle
print("\n--- Resultado final ---")
if puntos1 > puntos2:  # Si el jugador 1 tiene más puntos
    print(f"{nombre1} ganó el juego 🎉")  # Muestra que ganó el jugador 1
elif puntos2 > puntos1:  # Si el jugador 2 tiene más puntos
    print(f"{nombre2} ganó el juego 🎉")  # Muestra que ganó el jugador 2
else:
    print("¡Empate! No hubo un ganador.")  # Si hay igualdad de puntos, es empate

