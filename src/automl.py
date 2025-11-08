import yaml
import json
import subprocess
import os

# Leer configuraciones desde params.yaml
with open("params.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)

results = []

# Iterar sobre cada configuración de modelo
for model_cfg in config["automl"]["models"]:
    model_name = model_cfg["name"]
    print(f"\n🔁 Ejecutando entrenamiento para: {model_name}")

    # Guardar configuración actual en archivo temporal para que train.py la lea
    with open("src/temp_model_config.json", "w", encoding="utf-8") as f:
        json.dump(model_cfg, f)

    # Ejecutar train.py como script
    subprocess.run(["python", "src/train.py"], check=True)

    # Leer métricas generadas por train.py
    try:
        with open("metrics.json", encoding="utf-8") as f:
            metrics = json.load(f)
    except Exception as e:
        print(f"⚠️ No se pudo leer metrics.json: {e}")
        metrics = {}

    results.append({
        "model": model_name,
        "params": model_cfg,
        "score": metrics.get("score"),
        "mse": metrics.get("mse")
    })

# Seleccionar el mejor modelo según menor mse
best = min(results, key=lambda x: x["mse"] if x["mse"] is not None else float("inf"))

# Guardar resultados en metrics.json
with open("metrics.json", "w", encoding="utf-8") as f:
    json.dump({"best_model": best, "all_results": results}, f, indent=2)

print(f"\n✅ Mejor modelo: {best['model']} con mse = {best['mse']}")