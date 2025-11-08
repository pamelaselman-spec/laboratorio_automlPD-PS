import pandas as pd
import sys
import pickle
import json
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

df = pd.read_csv("data/processed.csv")

# Validar columna objetivo
target_col = "MedHouseVal"
print(f"Columnas disponibles: {df.columns.tolist()}")
print(f"Usando columna objetivo: {target_col}")

if target_col not in df.columns:
    raise ValueError(f"La columna objetivo '{target_col}' no se encuentra en el dataset.")

X = df.drop(target_col, axis=1)
y = df[target_col]

# Lista de modelos
model_list = ["linear", "random_forest", "gradient_boosting"]
model_params = {
    "linear": {"fit_intercept": True},
    "random_forest": {"n_estimators": 100, "max_depth": 5, "random_state": 42},
    "gradient_boosting": {"learning_rate": 0.1, "n_estimators": 100, "max_depth": 3, "random_state": 42}
}

best_score = -float("inf")
best_model = None
best_model_name = None

for name in model_list:
    if name == "linear":
        model = LinearRegression(**model_params["linear"])
    elif name == "random_forest":
        model = RandomForestRegressor(**model_params["random_forest"])
    elif name == "gradient_boosting":
        model = GradientBoostingRegressor(**model_params["gradient_boosting"])
    else:
        continue

    model.fit(X, y)
    score = model.score(X, y)

    if score > best_score:
        best_score = score
        best_model = model
        best_model_name = name

pickle.dump(best_model, open("model.pkl", "wb"))
json.dump({"model": best_model_name, "score": round(best_score, 4)}, open("metrics_train.json", "w"))