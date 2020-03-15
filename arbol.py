import threading
import random
import os
import time

mutex = threading.Lock()

arbol = list(open('/home/eduardo579/Documents/Navidad/arbol.txt').read().rstrip())

def luces(color, indices):
    apagado = True

    while True:
        for ind in indices:
            arbol[ind] = puntos_coloreados(color) if apagado else '☆'
        
        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(arbol))
        mutex.release()

        apagado = not apagado

        time.sleep(random.uniform(.5, 1.5))


def puntos_coloreados(color):
    if color == 'rojo':
        return f'\033[91m☆\033[0m'

    if color == 'verde':
        return f'\033[92m☆\033[0m'

    if color == 'amarillo':
        return f'\033[93m☆\033[0m'

    if color == 'azul':
        return f'\033[94m☆\033[0m'

amarillo = []
rojo = []
azul = []
verde = []

for i, c in enumerate(arbol):
    if c == 'Y':
        amarillo.append(i)
        arbol[i] = '☆'

    if c == 'R':
        rojo.append(i)
        arbol[i] = '☆'

    if c == 'B':
        azul.append(i)
        arbol[i] = '☆'

    if c == 'G':
        verde.append(i)
        arbol[i] = '☆' 

ty = threading.Thread(target=luces, args=('amarillo', amarillo))
tr = threading.Thread(target=luces, args=('rojo', rojo))
tb = threading.Thread(target=luces, args=('azul', azul))
tg = threading.Thread(target=luces, args=('verde', verde))

for t in [ty, tr, tb, tg]:
    t.start()

for t in [ty, tr, tb, tg]:
    t.join()