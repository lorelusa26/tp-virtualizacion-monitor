"""
monitor.py - Monitor de recursos del sistema.

Registra cada cierto tiempo el uso de CPU, RAM y disco del sistema donde
se ejecuta (en este trabajo: dentro de una máquina virtual) y guarda los
datos en un archivo CSV para analizarlos después.

Uso:
    python3 src/monitor.py --etiqueta vm_1cpu_1gb --duracion 30 --intervalo 1
    python3 src/monitor.py --etiqueta vm_2cpu_2gb --duracion 30 --carga 1
"""

import argparse
import csv
import multiprocessing
import os
import platform
import time
from datetime import datetime

import psutil


def _consumir_cpu():
    """Bucle infinito que mantiene un núcleo ocupado (genera carga)."""
    while True:
        pass


def iniciar_carga(cantidad):
    """Lanza 'cantidad' procesos que consumen CPU para poder ver cambios."""
    procesos = []
    for _ in range(cantidad):
        p = multiprocessing.Process(target=_consumir_cpu, daemon=True)
        p.start()
        procesos.append(p)
    return procesos


def detener_carga(procesos):
    for p in procesos:
        p.terminate()


def mostrar_info_sistema():
    """Muestra datos del entorno: sirve para comprobar que estamos en la VM."""
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    print("=" * 50)
    print("INFORMACIÓN DEL SISTEMA")
    print(f"  Sistema operativo : {platform.system()} {platform.release()}")
    print(f"  Nombre del equipo : {platform.node()}")
    print(f"  Arquitectura      : {platform.machine()}")
    print(f"  Núcleos de CPU    : {psutil.cpu_count()}")
    print(f"  RAM total         : {ram_gb:.2f} GB")
    print(f"  Python            : {platform.python_version()}")
    print("=" * 50)


def monitorear(etiqueta, duracion, intervalo, carpeta):
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, f"{etiqueta}.csv")

    # Primera llamada "de calentamiento": cpu_percent devuelve 0.0 la primera vez.
    psutil.cpu_percent(interval=None)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["segundo", "hora", "cpu_pct", "ram_pct",
                           "ram_usada_mb", "disco_pct"])
        inicio = time.time()
        while True:
            transcurrido = time.time() - inicio
            if transcurrido >= duracion:
                break
            # interval=intervalo hace que la medición espere ese tiempo.
            cpu = psutil.cpu_percent(interval=intervalo)
            memoria = psutil.virtual_memory()
            disco = psutil.disk_usage("/")
            fila = [
                round(time.time() - inicio, 1),
                datetime.now().strftime("%H:%M:%S"),
                cpu,
                memoria.percent,
                round(memoria.used / (1024 ** 2), 1),
                disco.percent,
            ]
            escritor.writerow(fila)
            print(f"[{fila[1]}] CPU {cpu:5.1f}% | RAM {memoria.percent:5.1f}% "
                  f"| Disco {disco.percent:5.1f}%")
    return ruta


def main():
    parser = argparse.ArgumentParser(description="Monitor de recursos del sistema")
    parser.add_argument("--etiqueta", default="medicion",
                        help="nombre de la medición (nombre del CSV)")
    parser.add_argument("--duracion", type=int, default=30,
                        help="duración total en segundos")
    parser.add_argument("--intervalo", type=float, default=1.0,
                        help="segundos entre mediciones")
    parser.add_argument("--carga", type=int, default=0,
                        help="cantidad de procesos que consumen CPU (0 = sin carga)")
    parser.add_argument("--salida", default="resultados",
                        help="carpeta donde se guarda el CSV")
    args = parser.parse_args()

    mostrar_info_sistema()
    procesos = iniciar_carga(args.carga) if args.carga > 0 else []
    try:
        ruta = monitorear(args.etiqueta, args.duracion, args.intervalo, args.salida)
    finally:
        detener_carga(procesos)
    print(f"\nListo. Datos guardados en: {ruta}")


if __name__ == "__main__":
    main()
