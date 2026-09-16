import pandas as pd

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

# Mostrar las primeras filas para ver que nuestra limpieza funciono
print(datos.head())

# Mostrar info de datos limpios
print("\nCantidad de pases completados:", len(datos))

# Mostrar los partidos que tenemos
print("\nPartidos:")
print(datos[["match_id", "fecha", "oponente"]].drop_duplicates())