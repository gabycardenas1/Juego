# ESTRUCTURA DE DATOS
# PROYECTO FINAL


# Importar librerías
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image, ImageDraw
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

# Cargar imágenes
ruta = "gato1.png"  
ruta1 = "personaje.png"
img = Image.open(ruta)
img1 = Image.open(ruta1)

# Crear grafo
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])
G.add_edges_from([('A', 'B'), ('A', 'F'), ('B', 'C'), ('B', 'G'), ('C', 'D'), ('C', 'H'), ('D', 'E'), ('D', 'I'), ('E', 'I'), 
                  ('F', 'G'), ('F', 'J'), ('G', 'H'), ('G', 'K'), ('H', 'I'), ('H', 'L'), ('I', 'L'), ('J', 'K'), ('J', 'M'),
                  ('K', 'L'), ('K', 'N'), ('L', 'N'), ('M', 'N'), ('M', 'O'), ('N', 'O')])
pos = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4), 'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 
       'J': (2, 0), 'K': (2, 1), 'L': (2, 2), 'M': (3, 0), 'N': (3, 1), 'O': (4, 0)}

# Definir las variables
cont = 0
pos_gato = ''
pos_personaje = ''
arr = []

# Definir funciones (POO)
def grafo(pos_g, pos_p, movimientos):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, edge_color="gray", node_color="skyblue", node_size=1500, font_size=15, font_weight="bold")

    ax = plt.gca()
    imagebox = OffsetImage(img, zoom=0.09) 
    ab = AnnotationBbox(imagebox, pos[pos_g], frameon=False)
    ax.add_artist(ab)
    imagebox1 = OffsetImage(img1, zoom=0.22)  
    ab1 = AnnotationBbox(imagebox1, pos[pos_p], frameon=False)
    ax.add_artist(ab1)

    plt.title("Gatito Rubio")
    plt.show()

def mover(pos_personaje):
    movimiento = input(f"\nEstás en el nodo {pos_personaje}. \nElige tu movimiento. \nOpciones: {list(G.neighbors(pos_personaje))}): ")
    while movimiento not in G.neighbors(pos_personaje):
        print("Movimiento no válido. Intenta de nuevo.")
        movimiento = input(f"\nElige tu movimiento.\n Opciones: {list(G.neighbors(pos_personaje))}): ")
    return movimiento

def gato(pos_g):
    movimientos_gato = list(G.neighbors(pos_g))
    return random.choice(movimientos_gato)

def puntaje(nombre, cont, lista):
    lista.append((nombre, cont))

def ordenar(puntaje):
    n = len(puntaje)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puntaje[j][1] > puntaje[j + 1][1]:
                puntaje[j], puntaje[j + 1] = puntaje[j + 1], puntaje[j]

    print("\nPuntajes ordenados (número de movimientos):")
    for name, moves in puntaje:
        print(f"{name}: {moves} movimientos")

# Lógica del juego
def iniciar_juego(nombre):

    pos_gato = 'A'
    pos_personaje = 'O'
    cont = 0
    
    while True:
        grafo(pos_gato, pos_personaje, cont)
        
        pos_personaje = mover(pos_personaje)
        cont += 1
        
        if pos_personaje == pos_gato:
            print(f"¡Has atrapado al gato! ¡Ganaste con {cont} movimientos!")
            puntaje(nombre, cont, arr)
            break
        
        pos_gato = gato(pos_gato)

        if not list(G.neighbors(pos_gato)):
            print(f"¡El gato no tiene más movimientos! ¡Ganaste con {cont} movimientos!")
            puntaje(nombre, cont, arr)
            break

        if pos_personaje == pos_gato:
            print(f"¡Has atrapado al gato después de su movimiento! ¡Ganaste con {cont} movimientos!")
            puntaje(nombre, cont, arr)
            break

# Iniciar la lógica principal del juego
print("-------------------------------------------------------------- GATITO RUBIO ---------------------------------------------------------------")
print("Bienvenido al mejor laberinto, donde tu misión es atrapar al Gatito rubio.\nNo te dejes engañar, sus movimientos te sorprenderán. ¡Suerte!")

# Definir repetición
while True:
    nombre = input("\nPara comenzar, dinos tu nombre: ")
    iniciar_juego(nombre)
    
    repetir = input("\n¿Quieres jugar otra ronda? (S/N): ").lower()
    if repetir != 's':
        break

# Tabla de puntajes
ordenar(arr)

print(f"\nGracias por jugar ;). Vuelve pronto {nombre}.")