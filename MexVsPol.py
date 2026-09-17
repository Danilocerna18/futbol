import pandas as pd
import networkx as nx

datos = pd.read_csv("pases_mexico.csv")

datos = datos[
    [
        "match_id",
        "fecha",
        "oponente",
        "jugador_nombre",
        "receptor_nombre",
        "resultado"
    ]
]

datos = datos[datos["oponente"] == "Poland"]
datos = datos[datos["resultado"] == "Complete"]

# eliminaremos los pases que no tengan jugador o receptor
datos = datos.dropna(
    subset=["jugador_nombre", "receptor_nombre"]
)

# Creamos un grafo dirigido
grafo = nx.DiGraph()

# Agregamos los pases al grafo
for _, fila in datos.iterrows():
    jugador = fila["jugador_nombre"]
    receptor = fila["receptor_nombre"]

    if grafo.has_edge(jugador, receptor):
        grafo[jugador][receptor]["peso"] += 1
    else:
        grafo.add_edge(jugador, receptor, peso=1)

print("Jugadores:", grafo.number_of_nodes())
print("Conexiones:", grafo.number_of_edges())

import matplotlib.pyplot as plt

# Dibujamos el grafo
plt.figure(figsize=(10, 8))

# Definimos coordenadas fijas en la cancha (Formación 4-3-3)
posiciones = {
    # Portero
    "Francisco Guillermo Ochoa Magaña": (0, -0.85),
    
    # Defensa
    "Jesús Daniel Gallardo Vasconcelos": (-0.75, -0.45),
    "Héctor Alfredo Moreno Herrera": (-0.30, -0.60),
    "César Jasib Montes Castro": (0.30, -0.60),
    "Jorge Eduardo Sánchez Ramos": (0.75, -0.45),
    
    # Mediocampo
    "Edson Omar Álvarez Velázquez": (0, -0.30),          
    "Luis Gerardo Chávez Magallón": (-0.35, -0.05),   
    "Héctor Miguel Herrera López": (0.35, -0.05),      
    "Carlos Alberto Rodríguez Gómez": (-0.75, 0.10),   
    
    # Delanteros
    "Ernesto Alexis Vega Rojas": (-0.60, 0.45),          
    "Henry Josué Martín Mex": (0, 0.55),                
    "Hirving Rodrigo Lozano Bahena": (0.60, 0.45),        
    "Carlos Uriel Antuna Romero": (0.75, 0.25),         
    "Raúl Alonso Jiménez Rodríguez": (0, 0.80)           
}

# Acortamos los nombres para que quepan en los nodos
etiquetas = {nodo: f"{nodo.split()[0]}\n{nodo.split()[-1]}" for nodo in grafo.nodes()}

nx.draw(
    grafo,
    posiciones,
    labels=etiquetas,
    node_size=1800,
    node_color="lightgreen",
    arrows=True,
    arrowsize=12,
    width=[grafo[u][v]["peso"] / 2.5 for u, v in grafo.edges()],
    font_size=7,
    font_weight="bold"
)

plt.title("México vs Polonia - Pases (Alineación Táctica 4-3-3)")
plt.axis("off")
plt.show()