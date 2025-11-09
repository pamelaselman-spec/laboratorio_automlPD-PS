"# laboratorio_automlPD-PS" 
Nombre: Pamela Jacqueline Selman David
Carnet: 25002792
Noviembre 2025 - Product Development Sección V

Carpeta Data:
 - dataset_v1 : versión original proporcionada.
 - dataset_v2 : limpieza de nulos y duplicados.
 - dataset_v3 : ampliación - 1000 registros nuevos.
 - dataset_v4 : ampliación - 1000 registros nuevos.

 Para la creación de dichos datasets del v2 al v4 , se utilizaron 3 notebooks:
 - crear_datasetv2_limpieza.ipynb   : creación de dataset_v2
 - crear_datasetv3_ampliacion.ipynb : creación de dataset_v3
 - crear_datasetv3_ampliacion2.ipynb : creación de dataset_v4

 Carpeta src:
 - evaluate.py
 - preprocess.py
 - train.py
 - automl.py
 - generate_report.py


 params.yaml: parametrizaciones necesarias para ejecución del laboratorio.
 dvc.yaml : en este archivo se configura toda la organización de los archivos según los escenarios y ejecución de preprocess, train y evaluate. 

 Tanto en params.yaml como dvc.yaml se va modificando el archivo del dataset para la ejecución de cada uno de los tags de datasets de git.

 Tag v1.0 - data/dataset_v1.csv
 Tag v2.0 - data/dataset_v2.csv
 Tag v3.0 - data/dataset_v3.csv
 Tag v4.0 - data/dataset_v4.csv

 Modificación de params.yaml - se ajusta el parámetro dataset_path que es donde se coloca que dataset se utilizará.

 Modificación de dvc.yaml
    La sección de deps debe modificarse la línea de data/dataset para que tome el mismo dataset de params.yaml
        deps:
        - src/preprocess.py
        - data/dataset_v4.csv

Ejecución para cada versión o tag: (Pasos realizados):
        Nota: Cada vez que se ejecuta dvc repro este ejecuta las secciones configuradas:
            >> preprocess - src/preprocess.py
            >> train - src/train.py
            >> evaluate - src/evaluate.py

        modificar manualmente params.yaml y dvc.yaml  - data/dataset_v2
        dvc repro
        dvc commit
        git add dvc.lock
        git commit -am "🔁 Métricas con dataset_v2"
        git tag -d v2.0
        git tag -a v2.0 -m "Versión reproducible con dataset_v2"

        modificar manualmente params.yaml y dvc.yaml  - data/dataset_v3
        dvc repro
        dvc commit
        git add dvc.lock
        git commit -am "🔁 Métricas con dataset_v3"
        git tag -d v3.0
        git tag -a v3.0 -m "Versión reproducible con dataset_v3"

        modificar manualmente params.yaml y dvc.yaml  - data/dataset_v2
        dvc repro
        dvc commit
        git add dvc.lock
        git commit -am "🔁 Métricas con dataset_v4"
        git tag -d v4.0
        git tag -a v4.0 -m "Versión reproducible con dataset_v4"


Importante considerar que las métricas se almacenan en metrics_eval.json y metrics_train.json , cada tag cuenta con su versión del archivo. Para ello se puede realizar checkout de cada uno:

    git checkout v1.0
    dvc checkout
    type metrics_train.json
    type metrics_eval.json

    git checkout v2.0
    dvc checkout
    type metrics_train.json
    type metrics_eval.json

    git checkout v3.0
    dvc checkout
    type metrics_train.json
    type metrics_eval.json

    git checkout v4.0
    dvc checkout
    type metrics_train.json
    type metrics_eval.json

Comparativo entre métricas:  importante metrics diff únicamente compara 2 versiones por lo que se debe ir haciendo los comparativos necesarios para analizar entre varios datasets, por ejemplo:
    dvc metrics diff v1.0 v3.0 --targets metrics_train.json metrics_eval.json
            En el comando anterior compara las versiones 1 y 3 (dataset1 y dataset3 en los metrics_train y metrics_eval)

            Ejemplo de resultado:
            Path                Metric    v1.0    v3.0    Change
            metrics_train.json  score     0.8033  0.7449  -0.0584
            metrics_eval.json   mse       0.2619  0.3398  0.0779
    
    dvc metrics show
        este comando muestra las métricas del tag en el que está posicionado el head: 
            Path                model              mse     score
            metrics_train.json  gradient_boosting  -       0.7053
            metrics_eval.json   -                  0.3939  -

Ejecución de AUTOML:
    en comandos ejecutar : python src/automl.py  para obtener el score y mse. Esto actualiza el archivo metrics.json

Reporte Final: 
    en comandos ejecutar : python src/generate_report.py para obtener el resultado final de análisis de mejor modelo, esto a partir de metrics.json y generando report.md
