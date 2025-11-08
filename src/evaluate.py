import pandas as pd
import pickle
import json
from sklearn.metrics import mean_squared_error

df = pd.read_csv("data/processed.csv")
target_col = "MedHouseVal"

print(f"Columnas disponibles: {df.columns.tolist()}")
print(f"Usando columna objetivo: {target_col}")

if target_col not in df.columns:
    raise ValueError(f"La columna objetivo '{target_col}' no se encuentra en el dataset.")

X = df.drop(target_col, axis=1)
y = df[target_col]

model = pickle.load(open("model.pkl", "rb"))
y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
json.dump({"mse": round(mse, 4)}, open("metrics_eval.json", "w"))