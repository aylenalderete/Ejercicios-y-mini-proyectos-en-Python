import random


def options_and_validate(user, computer):
    if computer == 1 and user == "piedra":
        print("Empate")
    elif computer == 1 and user == "papel":
        print("La computadora eligió Piedra. Ganaste!")
    elif computer == 1 and user == "tijera":
        print("La computadora eligió Piedra. Perdiste!")
    elif computer == 2 and user == "papel":
        print("Empate")
    elif computer == 2 and user == "piedra":
        print("La computadora eligió Papel. Perdiste!")
    elif computer == 2 and user == "tijera":
        print("La computadora eligió Papel. Ganaste!")
    elif computer == 3 and user == "tijera":
        print("Empate")
    elif computer == 3 and user == "piedra":
        print("La computadora eligió Tijera. Perdiste!")
    elif computer == 3 and user == "papel":
        print("La computadora eligió Tijera. Ganaste!")
    else:
        print("Elige una opción válida")


welcome_message = input("""Este es el juego de Piedra, Papel o Tijera. 
En esta partida jugará con la computadora, ¿qué opción eliges?
-Piedra
-Papel
-Tijera
Escriba la opción elegida: """)


def run():
    print(welcome_message)
    user = welcome_message.lower()
    computer = random.randint(1, 3)
    options_and_validate(user, computer)
            

if __name__ == "__main__":
    run()