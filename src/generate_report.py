import json

# Cargar métricas desde metrics.json
with open("metrics.json", encoding="utf-8") as f:
    data = json.load(f)

best = data["best_model"]
results = data["all_results"]

# Construir tabla Markdown
table_header = "| Modelo | Score | MSE |\n|--------|-------|-----|\n"
table_rows = "\n".join([
    f"| {r['model']} | {r['score']} | {r['mse']} |"
    for r in results
])

# Construir contenido del reporte
report = f"""# 📊 Reporte Final AutoML

## 🏆 Mejor Modelo
- Nombre: {best['model']}
- Parámetros: `{best['params']}`
- Score: {best['score']}
- MSE: {best['mse']}

## 📈 Comparativo de Modelos

{table_header}{table_rows}

## 🔍 Análisis
El modelo **{best['model']}** obtuvo el mejor rendimiento en términos de MSE.  
Los parámetros `{best['params']}` contribuyeron a mejorar el desempeño.  
Este resultado sugiere que los ajustes en la configuración tuvieron un impacto significativo.
"""

# Guardar en report.md
with open("report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ Reporte generado como report.md")