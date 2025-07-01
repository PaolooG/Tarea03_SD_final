import csv
import json
import os
from elasticsearch import Elasticsearch, helpers

def cargar_csv_en_elasticsearch(ruta_csv, indice, es):
    with open(ruta_csv, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        acciones = []

        for fila in lector:
            doc = dict(fila)

            # Forzar que 'cantidad' sea número si existe
            if "cantidad" in doc:
                try:
                    doc["cantidad"] = int(doc["cantidad"])
                except ValueError:
                    pass  # Dejarlo como está si no se puede convertir

            # Forzar que 'fecha' esté en formato ISO si existe
            if "fecha" in doc:
                doc["fecha"] = doc["fecha"][:10]  # Asegura formato YYYY-MM-DD

            acciones.append({
                "_index": indice,
                "_source": doc
            })

        helpers.bulk(es, acciones)
        print(f"✅ Se cargaron {len(acciones)} documentos en el índice '{indice}'.")

def main():
    es = Elasticsearch("http://localhost:9200")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    ruta_conteo_por_fecha = os.path.join(base_dir, "..", "data", "conteo_por_fecha.csv")
    ruta_conteo_por_comuna = os.path.join(base_dir, "..", "data", "conteo_por_comuna.csv")
    ruta_conteo_por_tipo = os.path.join(base_dir, "..", "data", "conteo_por_tipo.csv")

    cargar_csv_en_elasticsearch(ruta_conteo_por_fecha, "conteo_por_fecha", es)
    cargar_csv_en_elasticsearch(ruta_conteo_por_comuna, "conteo_por_comuna", es)
    cargar_csv_en_elasticsearch(ruta_conteo_por_tipo, "conteo_por_tipo", es)

if __name__ == "__main__":
    main()
