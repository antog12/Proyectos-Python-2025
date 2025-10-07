# juego de preguntas matemáticas con funciones en python

#--------EJEMPLOS-------------

"""def sumar(a,b):
    print(f"{a} + {b} = {a+b}")

sumar(3,5)"""
from idlelib.debugger_r import restart_subprocess_debugger

"""def multiplicar(a,b):
    return a*b

resultado = multiplicar(2,5)
print(resultado)"""

#Construir un programa en python que haga preguntas aleatorias al usuario en python (sumas, restas, etc)
# tiene que llevar un registro de la puntuación y de la retoralimentación

import random

# definir las pregntas matemáticas

def generar_pregunta():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operador = random.choice(["+","-","*"])

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    else:
        resultado = num1 * num2

    return f"{num1} {operador} {num2} ", resultado # devuelve dos cosas, pregunta y respuesta

#iniciar el juego

def math_quiz():
    score = 0
    rounds = 5

    print("\n--- Juego de preguntas matemáticas ---")
    print("Responde correctamente a las pregunta matemáticas")

    for i in range(rounds):
        pregunta, respuesta_correcta = generar_pregunta()
        print(f"\nPregunta {i+1}: {pregunta}")
        respuesta_user = int(input("Tu respuesta: "))

        if respuesta_user == respuesta_correcta:
            print("Respuesta correcta")
            score += 1
        else:
            print(f"Respuesta incorrecta, la respuesta correcta es {respuesta_correcta}")

    print("\n---Game Over---")
    print(f"Puntuación fina es: {score}/{rounds}")

    if score == rounds:
        print("Felicidades, todas las respuestas correctas")
    elif score >= rounds // 2:
        print("Buen trabajo")
    else:
        print("Puedes mejorar")

# arrancar el juego
math_quiz()


print("OTRA OPCIÓN")

"""def generar_pregunta():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operador = random.choice(["+","-","*"])

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    else:
        resultado = num1 * num2

    return f"{num1} {operador} {num2} ", resultado

def iniciar_quiz():
    puntaje = 0
    for _ in range(5):
        pregunta, respuesta_correcta = generar_pregunta()
        respuesta_usuario = input(f"¿Cuál es el resultado de {pregunta} ? ")
        if int(respuesta_usuario) == respuesta_correcta:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es {respuesta_correcta}.")
    print(f"Tu puntaje final es {puntaje} de 5.")

iniciar_quiz()"""




















