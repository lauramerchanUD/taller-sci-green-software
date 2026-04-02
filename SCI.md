# 🧮 ¿Cómo se calcula el SCI?

```
SCI = ((E × I) + M) / R
```

---

## ⚡ E — Energía consumida (kWh)

La energía que consume tu CPU mientras corre el código.  
**CodeCarbon la mide automáticamente** — no necesitas hacer nada extra.

```
Emisiones totales : 0.00017653 kg CO₂  ← CodeCarbon lo calcula
```

---

## 🌍 I — Intensidad de carbono (kg CO₂/kWh)

Cuánto CO₂ emite la red eléctrica de tu país por cada kWh.

```
Colombia = 0.16438 kg CO₂/kWh
```
Fuente oficial: [XM — Factor de emisión del SIN colombiano](https://www.xm.com.co/noticias/en-colombia-factor-de-emision-de-co2-por-generacion-electrica-del-sistema-interconectado)  
Tiempo real: [app.electricitymaps.com/zone/CO](https://app.electricitymaps.com/zone/CO)

> El mismo código en Noruega (99% hidroeléctrica) contamina casi nada.  
> En Polonia (mayoría carbón) contamina mucho más.

---

## 🖥️ M — Carbono del hardware (fabricación)

El CO₂ emitido al fabricar tu equipo — antes de encenderlo por primera vez.

### Busca el reporte de tu equipo:

| Fabricante | Link oficial |
|---|---|
| Apple | [apple.com/environment](https://www.apple.com/environment) |
| ASUS | [esg.asus.com/en/resource/carbon_footprint](https://esg.asus.com/en/resource/carbon_footprint) |
| Dell | [dell.com/en-us/lp/dt/product-carbon-footprints](https://www.dell.com/en-us/lp/dt/product-carbon-footprints) |
| HP | [hp.com/us-en/sustainable-impact/climate-action/product-carbon-footprint.html](https://www.hp.com/us-en/sustainable-impact/climate-action/product-carbon-footprint.html) |
| Lenovo | [lenovo.com/us/en/sustainability](https://www.lenovo.com/us/en/sustainability) |

### Ejemplos reales:

| Equipo | Total ciclo vida | % Fabricación | M fabricación |
|---|---|---|---|
| MacBook Pro 14" M4 Pro | 218 kg CO₂e | 74% | 161 kg |
| ASUS Zenbook 14X OLED UX5401Z | 281 kg CO₂e | 70% | 197 kg |
| ASUS TUF Gaming A14 FA401K | 300 kg CO₂e | 78% | 233 kg |
| Zenbook 14 UM3406K | 337 kg CO₂e | 70% | 236 kg |

> ⚠️ Si no encuentras tu modelo usa **320 kg CO₂** como estimado.

### Calcula tu M por segundo:

```
M = Fabricación ÷ 126.144.000  (segundos en 4 años)
```

```
Mi equipo: _______ kg CO₂ fabricación
M = _______ ÷ 126.144.000 = _______ kg CO₂/s
```

### Actualiza el código con tu M real:

```python
# Antes (estimado genérico)
M = 0.0000006

# Después — [tu equipo] · Fuente: [URL]
M = tu_valor * tiempo
```

---

## 📏 R — Unidad funcional

Lo que define **por qué** mides. Tú lo decides según el software:

| Software | R |
|---|---|
| API | por llamada |
| ETL / batch | por ejecución |
| Query SQL | por consulta |
| **Este taller** | **por duplicado encontrado** |

---

## 🧮 El cálculo completo

```python
E = emisiones          # CodeCarbon lo mide (kg CO₂)
I = 0.16438            # Colombia · Fuente: XM / MinMinas
M = tu_valor * tiempo  # proporcional al tiempo de ejecución
R = len(duplicados)    # duplicados encontrados

SCI = ((E * I) + M) / R
```


