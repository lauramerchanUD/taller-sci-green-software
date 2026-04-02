# 🌱 Taller: ¿Cuánto carbono emite tu código?

## Instalación

```bash
pip install codecarbon
```

## El problema

Tienes una lista de **50.000 estudiantes** con nombres repetidos.  
Tu misión: encontrar los duplicados.

Hay dos soluciones. Ambas encuentran **exactamente los mismos duplicados**.

## Instrucciones

**Paso 1** — Corre la primera solución y anota los resultados:
```bash
python 01_solucion_a.py
```

| | Solución A |
|---|---|
| Duplicados encontrados | |
| Tiempo (segundos) | |
| SCI (kg CO₂) | |

---

**Paso 2** — Corre la segunda solución y anota los resultados:
```bash
python 02_solucion_b.py
```

| | Solución B |
|---|---|
| Duplicados encontrados | |
| Tiempo (segundos) | |
| SCI (kg CO₂) | |

---

**Paso 3** — Compara y responde:

1. ¿El resultado es el mismo?
2. ¿Cuál tardó más?
3. ¿Cuál emitió menos carbono?
4. ¿Por qué crees que hay diferencia?
5. ¿Qué pasaría si este código corriera 1.000.000 de veces al día?

---

**Paso 4** — Mira el código de ambas soluciones y discute con tu equipo:
- ¿Qué hace diferente cada una?
- ¿Cuál usarías en producción?

---

## ¿Qué es el SCI?

```
SCI = ((E × I) + M) / R

E = Energía consumida (kWh)
I = Intensidad de carbono de Colombia (0.126 kg CO₂/kWh)
M = Carbono del hardware (estimado)
R = Unidad funcional (duplicados encontrados)
```

> El SCI no mide el total — mide cuánto carbono emite **cada unidad de trabajo**.

---

## Recursos

- [Green Software Foundation](https://greensoftware.foundation)
- [CodeCarbon](https://codecarbon.io)
- [Electricity Maps — Colombia](https://app.electricitymaps.com/zone/CO)
