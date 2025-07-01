# 🚦 Tarea 3 - Sistemas Distribuidos (2025)  
### Análisis Distribuido de Eventos de Tráfico Urbano

Este repositorio contiene el desarrollo de un sistema distribuido que simula, procesa y visualiza eventos urbanos (como accidentes, atascos o presencia policial) utilizando herramientas modernas como Apache Pig, Redis, Elasticsearch, Kibana y Docker.

---

## 📌 Objetivo

Implementar un sistema distribuido modular que permita:
- Generar datos sintéticos realistas
- Preprocesar y limpiar los eventos
- Procesarlos por lotes usando Apache Pig
- Consultarlos simulando un sistema de caché con Redis
- Indexarlos en Elasticsearch
- Visualizarlos mediante dashboards interactivos en Kibana

---

## 🧱 Arquitectura del sistema

[Generador Fake] → [Preprocesador] → [Pig] → [Redis + Elasticsearch] → [Kibana]

Todos los componentes se ejecutan mediante contenedores Docker con docker-compose.

---

## 📂 Estructura del Repositorio

├── data/                    # Archivos CSV generados y procesados  
├── pig/                     # Script de procesamiento con Apache Pig  
│   └── analisis_trafico.pig  
├── preprocessor/            # Script de limpieza y normalización de eventos  
│   └── preprocesador.py  
├── processing/              # Carga de datos a Elasticsearch  
│   └── carga_a_elasticsearch.py  
├── tools/                   # Scripts para generación de datos y simulación cache  
│   ├── generador_fake_eventos.py  
│   └── generador_cache_redis.py  
├── docker/                  # Dockerfile para contenedor Pig  
│   └── Dockerfile  
├── docker-compose.yml       # Orquestación de servicios  
├── README.md                # Este archivo  

---

## ⚙️ Cómo ejecutar el sistema

1. Clonar el repositorio

git clone https://github.com/PaolooG/Tarea_03.git  
cd Tarea_03

2. Generar eventos sintéticos

python3 tools/generador_fake_eventos.py

3. Preprocesar los eventos

python3 preprocessor/preprocesador.py

4. Levantar los servicios distribuidos con Docker

docker-compose up -d --build

Esto levanta los siguientes contenedores: Redis, MongoDB, Elasticsearch, Kibana y Pig.

5. Procesar datos con Pig

docker exec -it pig bash  
cd pig  
pig analisis_trafico.pig

Luego, copiar resultados a la carpeta data/:

cp output/conteo_por_tipo/part-r-00000 /opt/pigjob/data/conteo_por_tipo.csv  
cp output/conteo_por_comuna/part-r-00000 /opt/pigjob/data/conteo_por_comuna.csv  
cp output/conteo_por_fecha/part-r-00000 /opt/pigjob/data/conteo_por_fecha.csv

6. Simular consultas con Redis

python3 tools/generador_cache_redis.py

Esto genera:
- resultados_cache.csv
- frecuencia_claves.csv

7. Cargar resultados a Elasticsearch

python3 processing/carga_a_elasticsearch.py

---

## 📊 Visualización en Kibana

1. Abre http://localhost:5601  
2. Crea los index patterns:
   - conteo_por_tipo
   - conteo_por_comuna
   - conteo_por_fecha 
3. Ve a Visualize → Create visualization  
4. Crea gráficos de barras y líneas para cada índice  
5. Agrúpalos en un dashboard completo  

---

## 📈 Resultados Esperados

- Gráficos de eventos por tipo, comuna y fecha  
- Dashboard interactivo  
- Datos sintéticos realistas y bien distribuidos  

---

## 🧪 Tecnologías Usadas

- Python 3.10  
- Apache Pig 0.17.0  
- Redis  
- Elasticsearch 7.17.13  
- Kibana 7.17.13  
- Docker + Docker Compose  
- Pandas, Matplotlib  

---

## 📄 Informe

El informe completo (Tarea_3_Sistemas_Distribuidos_2025_1.pdf) incluye:
- Justificación del diseño
- Capturas de los dashboards
- Métricas y resultados
- Reflexión final

---

## 👤 Autor

**Paolo Genta**  
Ingeniería Civil Informática y Telecomunicaciones  
Curso: Sistemas Distribuidos - 2025
