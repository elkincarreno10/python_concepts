"""
 Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 - El juego comienza proponiendo una palabra aleatoria incompleta
   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
   la palabra a adivinar)
   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
     uno al número de intentos
   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
     al número de intentos
   - Si el contador de intentos llega a 0, el jugador pierde
 - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
   ocultando más del 60%
 - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""
from random import random
import math

def adivina_la_palabra():
    palabras = ['productivo', 'consumidor', 'futbolista', 'contador', 'defensor', 'libro']
    palabra = palabras[math.floor(random() * len(palabras))]
    letras_mostradas = math.floor(len(palabra) / 2)
    intentos = 4
    posiciones = []

    for i in range(0, letras_mostradas):
        posicion = math.floor(random() * len(palabra))
        while posicion in posiciones:
            posicion = math.floor(random() * len(palabra))
        posiciones.append(posicion)

    palabra_incompleta = ''
    for i in range(0, len(palabra)):
        if i in posiciones:
            palabra_incompleta += palabra[i]
        else:
            palabra_incompleta += '_'

    print(palabra_incompleta)
    print(f'Tienes {intentos} intentos')

    while palabra_incompleta.count('_'):
        if intentos == 0:
            print('Perdiste')
            break
        letra = input('Ingrese una letra o la palabra completa: ')
        if len(letra) == 1:
            if letra in palabra:
                cantidad = palabra.count(letra)
                posicion_letra = palabra.index(letra)
                for i in range(0, cantidad):
                    if palabra_incompleta[posicion_letra] == '_':
                        lista_palabra = list(palabra_incompleta)
                        lista_palabra[posicion_letra] = letra
                        palabra_incompleta = ''.join(lista_palabra)
                        print(palabra_incompleta)
                        if palabra_incompleta.count('_') == 0:
                            print(f'La palabra era: {palabra}')
                            print('Ganaste')
                        else:
                            print(f'Tienes {intentos} intentos')
                    else:
                        posicion_letra_repetida = palabra.find(letra, posicion_letra + 1)
                        posicion_letra = posicion_letra_repetida    
                if posicion_letra == -1:
                    print(palabra_incompleta)
                    intentos -= 1
                    print(f'Tienes {intentos} intentos')

            else:
                print(palabra_incompleta)
                intentos -= 1
                print(f'Tienes {intentos} intentos')
        else:
            if letra == palabra:
                palabra_incompleta = palabra
                print(f'La palabra era: {palabra}')
                print('Ganaste')
            else:
                print(palabra_incompleta)
                intentos -= 1
                print(f'Tienes {intentos} intentos')

adivina_la_palabra()


