riddles = {
    1 : "Adivinanza: ¿Cómo se denomina a un perro con fiebre?",
    2 : "Adivinanza: Existe un ser vivo capaz de beber agua con los pies. ¿Cuál es?",
    3 : "Adivinanza: Siempre va por la tierra sin ensuciarse. ¿Qué es?"
}

riddle_answers = {
    1: "Hot dog",
    2: "Un arbol",
    3: "La sombra"
}

def answer_and_validate(option):
    answer = input(str(riddles[option]) + " Inserta tu respuesta: ").lower()
    if riddle_answers[option] == answer:
        print("Sii, adivinaste! La opción correcta era " + str(riddle_answers[option]))
    else:
        print("No adivinaste. La opción correcta era " + str(riddle_answers[option]))

def run():
    user_response = int(input("Juego de adivinanzas, tenes solo un intento. Elegir una opción: 1, 2 o 3: "))
    if user_response == 1:
        answer_and_validate(user_response)
    elif user_response == 2:
        answer_and_validate(user_response)
    elif user_response == 3:
        answer_and_validate(user_response)
    else:
        print("Debes elegir una opción válida")
        run()



if __name__ == "__main__":
    run()