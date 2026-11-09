# Virtualización con VirtualBox: monitor de recursos en Python

Trabajo Práctico Integrador – Arquitectura y Sistemas Operativos
Tecnicatura Universitaria en Programación a Distancia (UTN)

**Alumna:** [Orieta,Lorena]
**Video explicativo:** [pegar acá el enlace de YouTube]

## ¿De qué trata?

Este proyecto consiste en crear una máquina virtual utilizando Oracle VirtualBox e instalar Ubuntu como sistema operativo. Dentro de esta máquina virtual se ejecuta un programa desarrollado en Python que permite monitorear el consumo de CPU, memoria RAM y disco.

Para analizar el comportamiento de los recursos, se realizaron dos pruebas con la misma configuración de la máquina virtual: una sin carga adicional y otra generando carga de trabajo sobre el procesador durante 30 segundos.

Los resultados se guardaron en archivos CSV y se representaron mediante gráficos utilizando Matplotlib. La comparación permitió observar cómo el uso de CPU aumentó hasta el 100 % durante la prueba con carga, mientras que en condiciones normales se mantuvo en valores mucho menores.

El informe PDF documenta la configuración de la máquina virtual, las herramientas utilizadas, las pruebas realizadas y las conclusiones obtenidas.

## Estructura del repositorio

```
.
├── src/
│   ├── monitor.py      # mide CPU, RAM y disco y guarda un CSV
│   └── graficar.py     # genera gráficos a partir de los CSV
├── resultados/         # CSV y gráficos de cada prueba
├── capturas/           # capturas de pantalla de los pasos en la VM
├── requirements.txt    # dependencias de Python
└── README.md
```

## Requisitos

- Python 3.10 o superior
- Librerías: `psutil` y `matplotlib`

## Cómo ejecutarlo (dentro de la VM)

```bash
# 1. Clonar el repositorio
git clone https://github.com/[usuario]/[nombre-del-repo].git
cd [nombre-del-repo]

# 2. Crear y activar un entorno virtual de Python
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar una medición de 30 segundos con 1 proceso que consume CPU
python3 src/monitor.py --etiqueta vm_2cpu_2gb --duracion 30 --carga 1

# 5. Generar los gráficos con una o más mediciones
python3 src/graficar.py resultados/vm_1cpu_1gb.csv resultados/vm_2cpu_2gb.csv
```

### Parámetros de `monitor.py`

| Parámetro      | Descripción                                   | Valor por defecto |
|----------------|-----------------------------------------------|-------------------|
| `--etiqueta`   | Nombre de la medición (nombre del CSV)        | `medicion`        |
| `--duracion`   | Duración total en segundos                    | `30`              |
| `--intervalo`  | Segundos entre mediciones                     | `1.0`             |
| `--carga`      | Procesos que consumen CPU (0 = sin carga)     | `0`               |
| `--salida`     | Carpeta donde se guarda el CSV                | `resultados`      |

## Resultados

Ver la sección "Resultados obtenidos" del informe PDF y los archivos de la
carpeta `resultados/`.
