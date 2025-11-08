## 📊 Comparativo de métricas y hashes entre versiones

### Tabla de resultados

| Tag   |   score |    mse | hash_train                       | hash_eval                        |
|:------|--------:|-------:|:---------------------------------|:---------------------------------|
| v1.0  |  0.7449 | 0.3398 | 7861cd61a5c07967b6bbc7977b856618 | 2b98d2b41ee804bdb419a3801f528ea9 |
| v2.0  |  0.7449 | 0.3398 | 7861cd61a5c07967b6bbc7977b856618 | 2b98d2b41ee804bdb419a3801f528ea9 |
| v3.0  |  0.7449 | 0.3398 | 12b25432fd9e2dea48605c8bfc196658 | 7f9174044ee8898ca6e9bded0cbb54a1 |

### Conclusiones

- La mejor puntuación de entrenamiento (`score`) se obtuvo en **v1.0** con un valor de **0.7449**
- El menor error de evaluación (`mse`) se alcanzó en **v1.0** con un valor de **0.3398**
- Esto sugiere que la versión **v1.0** tiene el mejor desempeño general en evaluación.
- Los hashes `md5` permiten verificar que los archivos versionados por DVC son distintos entre versiones.

---

Este reporte fue generado automáticamente a partir de versiones reproducibles con Git y DVC.