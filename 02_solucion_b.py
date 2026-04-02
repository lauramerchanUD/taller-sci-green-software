try:
    from codecarbon import EmissionsTracker
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "codecarbon", "-q"])
    from codecarbon import EmissionsTracker

import time

# ── Datos ─────────────────────────────────────────────────
estudiantes = [f"estudiante_{i % 10000}" for i in range(50000)]

# ── Medidor de carbono ────────────────────────────────────
tracker = EmissionsTracker(log_level="error")
inicio  = time.time()
tracker.start()

# ── Solución B ────────────────────────────────────────────
vistos     = set()
duplicados = set()

for estudiante in estudiantes:
    if estudiante in vistos:
        duplicados.add(estudiante)
    vistos.add(estudiante)

# ── Resultados ────────────────────────────────────────────
emisiones = tracker.stop()
tiempo    = time.time() - inicio

I   = 0.126
M   = 0.0000006
R   = len(duplicados)
SCI = ((emisiones * I) + M) / R

print("\n── Solución B ──────────────────────────────")
print(f"  Duplicados encontrados : {R:,}")
print(f"  Tiempo                 : {tiempo:.2f} segundos")
print(f"  Emisiones totales      : {emisiones:.8f} kg CO₂")
print(f"  SCI                    : {SCI:.12f} kg CO₂ por duplicado")
print("────────────────────────────────────────────\n")
