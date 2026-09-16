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

datos = datos[datos["resultado"] == "Complete"]

# eliminaremos los pases que no tengan jugador o receptor
datos = datos.dropna(
    subset=["jugador_nombre", "receptor_nombre"]
)

#eliminamos los prints porque comprobamos que esta bien
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