# 🌱 Taller: ¿Cuánto carbono emite tu código?

> **Ingeniería de Software Verde — Taller práctico individual**  
> Basado en los principios de la [Green Software Foundation](https://greensoftware.foundation) (2022)

---

## 🎯 Objetivo

Medir y comparar el impacto ambiental de dos algoritmos que resuelven **exactamente el mismo problema**, usando la fórmula estándar SCI (Software Carbon Intensity).

Al finalizar vas a poder responder:
- ¿Puede el mismo resultado costar diferente en carbono?
- ¿Cómo se mide el impacto ambiental del código?
- ¿Qué decisiones como desarrollador reducen emisiones?

---

## 🧰 Requisitos

- Python 3.8 o superior
- VS Code (o cualquier terminal)

---

## ⚙️ Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/lauramerchanUD/taller-sci-green-software.git
cd taller-sci-green-software
```

**2. Instala la librería de medición de carbono:**
```bash
pip install codecarbon
```

---

## 🌍 ¿Qué es el SCI y cómo se calcula?

El **Software Carbon Intensity (SCI)** es la fórmula estándar para medir el carbono de una aplicación:

```
SCI = ((E × I) + M) / R
```

A continuación, cada variable explicada y cómo obtenerla:

---

### ⚡ E — Energía consumida (kWh)

**¿Qué es?**  
La energía eléctrica que consume tu CPU mientras corre el código.

**¿Cómo se obtiene?**  
CodeCarbon la mide automáticamente. No tienes que hacer nada extra — al correr los scripts ya la está midiendo y la imprime en pantalla.

**¿Dónde aparece?**  
```
Emisiones totales : 0.00017653 kg CO₂  ← CodeCarbon calcula esto
```
También se guarda en el archivo `emissions.csv` que genera automáticamente en la carpeta del proyecto.

---

### 🌍 I — Intensidad de carbono de la electricidad (kg CO₂/kWh)

**¿Qué es?**  
Cuánto CO₂ emite la red eléctrica de tu país por cada kWh consumido. Depende de cuánta energía renovable hay en la mezcla energética.

**¿Cómo se obtiene?**  
Es un dato público por país. En este taller usamos el valor de Colombia:

```
Colombia = 0.16438 kg CO₂/kWh  (164.38 g CO₂/kWh)
```

Fuente oficial: [XM — Factor de emisión de CO₂ del SIN colombiano](https://www.xm.com.co/noticias/en-colombia-factor-de-emision-de-co2-por-generacion-electrica-del-sistema-interconectado)

Puedes consultar el valor en tiempo real de cualquier país en:  
👉 [app.electricitymaps.com/zone/CO](https://app.electricitymaps.com/zone/CO)

**¿Por qué importa?**  
El mismo código corriendo en Noruega (casi 100% hidroeléctrica) contamina mucho menos que corriendo en Polonia (mayoría carbón).

---

### 🖥️ M — Carbono del hardware (fabricación)

**¿Qué es?**  
El CO₂ emitido al fabricar tu computador — minería de materiales, manufactura, transporte. Este carbono ya existe aunque no uses el equipo.

**¿Cómo se obtiene?**  
Cada fabricante lo publica en su reporte ambiental oficial. Busca en Google:
```
[marca] [modelo] carbon footprint product sheet
```

**Links oficiales:**

| Fabricante | Link |
|---|---|
| Apple | [apple.com/environment](https://www.apple.com/environment) |
| ASUS | [esg.asus.com/en/resource/carbon_footprint](https://esg.asus.com/en/resource/carbon_footprint) |
| Dell | [dell.com/en-us/lp/dt/product-carbon-footprints](https://www.dell.com/en-us/lp/dt/product-carbon-footprints) |
| HP | [hp.com sustainable impact](https://www.hp.com/us-en/sustainable-impact/climate-action/product-carbon-footprint.html) |
| Lenovo | [lenovo.com/sustainability](https://www.lenovo.com/us/en/sustainability) |

**Del reporte extraes dos datos:**
1. Total del ciclo de vida (kg CO₂e)
2. Porcentaje de fabricación (entre 70–80% típicamente)

**Ejemplos reales:**

| Equipo | Total ciclo vida | % Fabricación | Fabricación (M total) |
|---|---|---|---|
| MacBook Pro 14" M4 Pro | 218 kg CO₂e | 74% | 161 kg CO₂e |
| ASUS Zenbook 14X OLED UX5401Z | 281 kg CO₂e | 70% | 197 kg CO₂e |
| ASUS TUF Gaming A14 FA401K | 300 kg CO₂e | 78% | 233 kg CO₂e |
| Zenbook 14 UM3406K | 337 kg CO₂e | 70% | 236 kg CO₂e |

> ⚠️ Si no encuentras tu modelo usa **320 kg CO₂** como estimado general.

**¿Cómo se convierte a kg CO₂ por segundo?**  
Se divide entre la vida útil del equipo en segundos (4 años):

```
M por segundo = Fabricación ÷ (4 × 365 × 24 × 3600)
              = Fabricación ÷ 126.144.000
```

Ejemplos:
```
MacBook Pro 14"         → 161 ÷ 126.144.000 = 0.00000000128 kg CO₂/s
ASUS TUF Gaming A14     → 233 ÷ 126.144.000 = 0.00000000185 kg CO₂/s
ASUS Zenbook 14X OLED   → 197 ÷ 126.144.000 = 0.00000000157 kg CO₂/s
```

**Calcula el tuyo:**
```
Total ciclo de vida  = _______ kg CO₂e
% de fabricación     = _______%
Fabricación          = _______ kg CO₂e
M por segundo        = _______ ÷ 126.144.000 = _______ kg CO₂/s
```

---

### 📏 R — Unidad funcional

**¿Qué es?**  
La unidad de trabajo útil que produce tu código. Define **por qué** mides.

**¿Cómo se obtiene?**  
Tú lo defines según lo que hace el código. Ejemplos:

| Tipo de software | R |
|---|---|
| API | por cada llamada |
| Proceso batch | por cada ejecución |
| Query SQL | por cada consulta |
| Este taller | por cada duplicado encontrado |

**En este taller:**  
R = número de duplicados encontrados (lo imprime el script al terminar)

---

### 🧮 Juntando todo

Con los 4 valores, el SCI se calcula así:

```python
E = emisiones          # lo midió CodeCarbon (kg CO₂)
I = 0.16438            # Colombia (kg CO₂/kWh) — Fuente: XM / UPME / MinMinas
M = tu_valor * tiempo  # carbono del hardware proporcional al tiempo
R = len(duplicados)    # duplicados encontrados

SCI = ((E * I) + M) / R
```

---

## 🔍 El problema

Tienes una lista de **5.000 estudiantes** con nombres repetidos.  
Tu misión: **encontrar los duplicados**.

Hay **dos soluciones**. Ambas encuentran exactamente los mismos duplicados.  
Tu trabajo es descubrir cuál tiene menor SCI y entender por qué.

---

## 📋 Instrucciones

### Paso 1 — Corre la Solución A

```bash
python 01_solucion_a.py
```

⏳ *Puede tardar entre 15 y 30 segundos. Es normal, déjala correr.*

| Métrica | Solución A |
|---|---|
| Duplicados encontrados (R) | |
| Tiempo (segundos) | |
| Emisiones totales — E (kg CO₂) | |
| SCI (kg CO₂ por duplicado) | |

---

### Paso 2 — Corre la Solución B

```bash
python 02_solucion_b.py
```

| Métrica | Solución B |
|---|---|
| Duplicados encontrados (R) | |
| Tiempo (segundos) | |
| Emisiones totales — E (kg CO₂) | |
| SCI (kg CO₂ por duplicado) | |

---

### Paso 3 — Completa la tabla comparativa

| Métrica | Solución A | Solución B | ¿Cuál es mejor? |
|---|---|---|---|
| Duplicados encontrados | | | |
| Tiempo (segundos) | | | |
| Emisiones totales (kg CO₂) | | | |
| SCI (kg CO₂ por duplicado) | | | |

---

### Paso 4 — Reflexiona y responde

1. ¿El resultado fue el mismo en ambas soluciones?
2. ¿Cuál tardó más? ¿Cuántas veces más?
3. ¿Cuál emitió menos carbono? ¿Cuántas veces menos?
4. Abre los dos archivos `.py` — ¿cuántos `for` tiene cada uno?
5. Si este código corriera **1.000.000 de veces al día**:
   - Solución A emitiría: _______ kg CO₂/día
   - Solución B emitiría: _______ kg CO₂/día
   - El ahorro sería: _______ kg CO₂/día
6. ¿Cuál usarías en producción? ¿Por qué?
7. ¿Qué código tuyo podrías optimizar hoy?

---

### Paso 5 — Calcula tu M y actualiza el código

Usando la sección de M de arriba, busca el reporte de tu equipo y reemplaza en los scripts:

```python
# Antes
M = 0.0000006

# Después — con tu equipo real
# [tu equipo] — Fuente: [URL]
M = tu_valor * tiempo
```

Vuelve a correr ambos scripts y observa si el SCI cambia.

---

### Paso 6 — Compara con tus compañeros

| | Yo | C1 | C2 | C3 |
|---|---|---|---|---|
| Equipo | | | | |
| M (kg CO₂/s) | | | | |
| SCI Solución A | | | | |
| SCI Solución B | | | | |

> 💡 ¿Los SCI son iguales en todos los equipos? ¿Por qué hay diferencias?

---

## 💡 ¿Qué aprendiste?

> **"El código más verde no siempre es el más corto.  
> Es el que hace el mismo trabajo quemando menos."**

Este es el principio de **Eficiencia de Carbono** de la Green Software Foundation:
> *Emitir la menor cantidad posible de carbono para entregar el mismo valor.*

---

## 📚 Recursos

- [Green Software Foundation](https://greensoftware.foundation)
- [Especificación SCI](https://sci.greensoftware.foundation)
- [CodeCarbon](https://codecarbon.io)
- [Electricity Maps — Colombia](https://app.electricitymaps.com/zone/CO)
- [Curso Microsoft Learn: Ingeniería de Software Sostenible](https://learn.microsoft.com/es-es/training/modules/sustainable-software-engineering-overview/)

---

*Taller desarrollado para la presentación de Ingeniería de Software Verde · Abril 2026*
