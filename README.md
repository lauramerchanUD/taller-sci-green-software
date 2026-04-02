# 🌱 Taller: ¿Cuánto carbono emite tu código?

> **Ingeniería de Software Verde — Taller práctico individual**  
> Basado en los principios de la [Green Software Foundation](https://greensoftware.foundation) (2022)

¿Sabías que dos algoritmos pueden dar **exactamente el mismo resultado** pero uno contaminar mucho más que el otro? En este taller lo vas a medir con datos reales.

---

## 🧰 Requisitos

- Python 3.8 o superior
- VS Code o cualquier terminal

---

## ⚙️ Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/lauramerchanUD/taller-sci-green-software.git
cd taller-sci-green-software
```

**2. Instala CodeCarbon:**
```bash
pip install codecarbon
```

> 💡 **¿Qué es CodeCarbon?**  
> Es una librería Python que mide cuánta energía consume tu CPU mientras corre tu código y lo convierte en kg de CO₂ según la red eléctrica de tu país. Solo necesitas instalarla — el resto lo hace automáticamente.

---

## 🔍 El problema

Tienes una lista de **5.000 estudiantes** con nombres repetidos.  
Tu misión: **encontrar los duplicados**.

Hay **dos soluciones**. Ambas encuentran exactamente los mismos duplicados.  
Tu trabajo es descubrir cuál tiene menor impacto ambiental y entender por qué.

---

## 📋 Paso a paso

### Paso 1 — Corre la Solución A

```bash
python 01_solucion_a.py
```

> ⏳ Puede tardar más de 2 minutos. Es normal, déjala correr.

Anota los resultados:

| Métrica | Solución A | Solución B |
|---|---|---|
| Duplicados encontrados (R) | | |
| Tiempo (segundos) | | |
| Emisiones totales — E (kg CO₂) | | |
| SCI (kg CO₂ por duplicado) | | |

---

### Paso 2 — Corre la Solución B

```bash
python 02_solucion_b.py
```

Completa la columna de Solución B en la tabla anterior.

---

### Paso 3 — Reflexiona

Responde estas preguntas en tu documento de entrega:

1. ¿El resultado fue el mismo en ambas soluciones?
2. ¿Cuál tardó más? ¿Cuántas veces más?
3. ¿Cuál emitió menos carbono? ¿Cuántas veces menos?
4. Abre los dos archivos `.py` — ¿cuántos `for` tiene cada uno? ¿Qué estructura de datos usa cada uno?
5. Si este código corriera **1.000.000 de veces al día**:
   - Solución A emitiría: _______ kg CO₂/día
   - Solución B emitiría: _______ kg CO₂/día
   - El ahorro sería: _______ kg CO₂/día
6. ¿Cuál usarías en producción? ¿Por qué?
7. Busca el reporte de carbono de tu equipo (ver [SCI.md](SCI.md)) y calcula tu M real. ¿Cambia el SCI?

---

## 📤 Entrega

Envía un documento **Word o PDF** con:

- ✅ Tabla comparativa con los resultados de ambas soluciones
- ✅ Respuestas a las 7 preguntas de reflexión
- ✅ Tu M calculado con el reporte oficial de tu equipo y la fuente

---

## 🧮 ¿Cómo se calculó el SCI?

```
SCI = ((E × I) + M) / R

E = Energía consumida (kWh)      → la mide CodeCarbon automáticamente
I = Intensidad de carbono        → Colombia = 0.16438 kg CO₂/kWh (Fuente: XM)
M = Carbono del hardware         → fabricación de tu equipo
R = Unidad funcional             → duplicados encontrados
```

> 📖 Para entender cada variable en detalle y calcular tu M real, ver [SCI.md](SCI.md)

---

## 💡 Conclusión

> *"El código más verde es el que hace el mismo trabajo quemando menos."*  
> — Principio de **Eficiencia de Carbono**, Green Software Foundation

---

## 📚 Recursos

- [Green Software Foundation](https://greensoftware.foundation)
- [CodeCarbon](https://codecarbon.io)
- [Electricity Maps — Colombia](https://app.electricitymaps.com/zone/CO)
- [XM — Factor de emisión CO₂ Colombia](https://www.xm.com.co/noticias/en-colombia-factor-de-emision-de-co2-por-generacion-electrica-del-sistema-interconectado)
- [Microsoft Learn: Ingeniería de Software Sostenible](https://learn.microsoft.com/es-es/training/modules/sustainable-software-engineering-overview/)

---
*Taller — Ingeniería de Software Verde · Abril 2026*
