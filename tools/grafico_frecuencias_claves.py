import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("../cache/data/frecuencia_claves.csv")

# Ordenar por frecuencia descendente
df_sorted = df.sort_values(by="Frecuencia", ascending=False).head(3)  # Top 3

# Crear el gráfico
plt.figure(figsize=(12, 6))
bars = plt.bar(df_sorted["Clave"], df_sorted["Frecuencia"], color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.title("Top 3 Claves más Consultadas en Redis")
plt.xlabel("Clave (Tipo:Comuna)")
plt.ylabel("Frecuencia de Consulta")
plt.tight_layout()

# Guardar como imagen (opcional)
plt.savefig("frecuencia_claves_barras.png", dpi=300)

# Mostrar
plt.show()
