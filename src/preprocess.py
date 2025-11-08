import pandas as pd
import sys
import yaml
import os

try:
    # Cargar parámetros
    params = yaml.safe_load(open(sys.argv[1]))
    dataset_path = params["dataset"]

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset no encontrado: {dataset_path}")

    # Cargar datos
    df = pd.read_csv(dataset_path)

    # Validaciones básicas
    if df.empty:
        raise ValueError("El dataset está vacío.")
    
    # Limpieza
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # Codificación de variables categóricas
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("category").cat.codes

    # Guardar resultado
    df.to_csv("data/processed.csv", index=False)
    print("Preprocesamiento exitoso.")

except Exception as e:
    print(f"Error en preprocess.py: {e}")
    sys.exit(1)