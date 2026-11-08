"""
graficar.py - Genera gráficos a partir de los CSV de la carpeta resultados.

Uso:
    python3 src/graficar.py resultados/vm_1cpu_1gb.csv resultados/vm_2cpu_2gb.csv
Cada CSV se dibuja como una línea; se guardan dos imágenes (CPU y RAM).
"""

import csv
import os
import sys

import matplotlib
matplotlib.use("Agg")  # permite generar imágenes sin entorno gráfico (VM Server)
import matplotlib.pyplot as plt


def leer_csv(ruta):
    segundos, cpu, ram = [], [], []
    with open(ruta, newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            segundos.append(float(fila["segundo"]))
            cpu.append(float(fila["cpu_pct"]))
            ram.append(float(fila["ram_pct"]))
    return segundos, cpu, ram


def graficar(rutas, columna, titulo, salida):
    plt.figure(figsize=(8, 4))
    for ruta in rutas:
        segundos, cpu, ram = leer_csv(ruta)
        etiqueta = os.path.splitext(os.path.basename(ruta))[0]
        plt.plot(segundos, cpu if columna == "cpu" else ram, label=etiqueta)
    plt.title(titulo)
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Uso (%)")
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(salida, dpi=120)
    plt.close()
    print(f"Gráfico guardado: {salida}")


def main():
    rutas = sys.argv[1:]
    if not rutas:
        print("Indicá al menos un archivo CSV. Ejemplo:")
        print("  python3 src/graficar.py resultados/vm_1cpu_1gb.csv")
        sys.exit(1)
    graficar(rutas, "cpu", "Uso de CPU", "resultados/grafico_cpu.png")
    graficar(rutas, "ram", "Uso de RAM", "resultados/grafico_ram.png")


if __name__ == "__main__":
    main()
