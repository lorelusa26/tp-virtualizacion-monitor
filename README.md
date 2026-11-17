# Virtualización con VirtualBox y monitoreo de recursos en Python

**Trabajo Práctico Integrador – Arquitectura y Sistemas Operativos**  
**Tecnicatura Universitaria en Programación a Distancia – UTN**

**Alumna:** Lorena Orieta  
**Video explicativo:** [Agregar enlace de YouTube]

## ¿De qué trata?

Este proyecto tiene como objetivo principal comprender de manera práctica el funcionamiento de la virtualización, mediante la creación y configuración de una máquina virtual utilizando Oracle VirtualBox.

Se utilizó una computadora con Windows como sistema anfitrión, VirtualBox como hipervisor de tipo 2 y Ubuntu Linux como sistema operativo invitado.

La máquina virtual se configuró con los siguientes recursos:

- **Memoria RAM:** 4096 MB.
- **Procesador:** una CPU virtual.
- **Disco virtual:** 25 GB.
- **Sistema operativo invitado:** Ubuntu 26.04.1 LTS.

Durante la experiencia se utilizaron comandos de Linux para identificar los recursos disponibles y observar el funcionamiento del sistema invitado.

Como actividad complementaria, se utilizaron dos programas en Python para monitorear el consumo de CPU, memoria RAM y disco, registrar mediciones y generar gráficos comparativos.

Para analizar el comportamiento de los recursos, se realizaron dos pruebas con la misma configuración:

1. **Sin carga adicional:** observación del consumo de recursos durante aproximadamente 30 segundos.
2. **Con carga de CPU:** generación de trabajo adicional sobre el procesador virtual durante aproximadamente 30 segundos.

Los resultados se registraron en archivos CSV y se representaron mediante gráficos utilizando Matplotlib.

La comparación permitió observar que el uso de CPU aumentó hasta el 100 % durante la prueba con carga, mientras que en la primera prueba se mantuvo generalmente entre 0 % y 10,1 %.

Es importante destacar que **los programas Python no constituyen la parte central del proyecto**. Fueron herramientas complementarias para observar y representar los resultados. El verdadero propósito fue investigar, experimentar y comprender cómo funciona el proceso de virtualización.

El informe final documenta el marco teórico, la configuración de la máquina virtual, las herramientas utilizadas, las pruebas, las capturas de pantalla y las conclusiones obtenidas.

## Estructura del repositorio

```text
.
├── src/
│   ├── monitor.py       # Mide CPU, RAM y disco y guarda un CSV
│   └── graficar.py      # Genera gráficos a partir de los CSV
├── resultados/          # CSV y gráficos generados en las pruebas
├── capturas/            # Evidencias del trabajo en Ubuntu
├── requirements.txt     # Dependencias de Python
└── README.md
```

Los resultados y las capturas se generaron durante la experiencia práctica dentro de Ubuntu. Las evidencias principales están incluidas en el informe final.

## Requisitos

Para reproducir la experiencia de virtualización:

- Computadora anfitriona con Windows.
- Oracle VirtualBox.
- Ubuntu Linux instalado en una máquina virtual.

Para ejecutar los programas de monitoreo:

- Python 3.10 o superior.
- Biblioteca `psutil`.
- Biblioteca `matplotlib`.
- Git para clonar el repositorio.

Las dependencias de Python se indican en `requirements.txt`.

## Cómo ejecutarlo (dentro de la VM)

### 1. Clonar el repositorio

```bash
git clone https://github.com/lorelusa26/tp-virtualizacion-monitor.git
cd tp-virtualizacion-monitor
```

### 2. Crear y activar un entorno virtual de Python

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la primera prueba: sin carga adicional

```bash
python3 src/monitor.py --etiqueta medicion --duracion 30
```

Esta ejecución permite observar el comportamiento de CPU, RAM y disco sin generar una carga adicional de procesamiento.

El archivo resultante es:

`resultados/medicion.csv`

### 5. Ejecutar la segunda prueba: con carga de CPU

```bash
python3 src/monitor.py --etiqueta con_carga --duracion 30 --carga 1
```

En esta prueba se genera una carga adicional sobre el único procesador virtual asignado a Ubuntu.

El archivo resultante es:

`resultados/con_carga.csv`

### 6. Generar los gráficos comparativos

```bash
python3 src/graficar.py resultados/medicion.csv resultados/con_carga.csv
```

El programa genera gráficos comparativos del uso de CPU y memoria RAM.

## Parámetros de `monitor.py`

| Parámetro | Descripción | Valor por defecto |
|---|---|---|
| `--etiqueta` | Nombre de la medición y del archivo CSV | `medicion` |
| `--duracion` | Duración total en segundos | `30` |
| `--intervalo` | Segundos entre mediciones | `1.0` |
| `--carga` | Procesos que consumen CPU (0 = sin carga adicional) | `0` |
| `--salida` | Carpeta donde se guarda el CSV | `resultados` |

## Resultados

Se realizaron dos mediciones breves, de aproximadamente 30 segundos cada una.

| Recurso | Sin carga adicional | Con carga de CPU |
|---|---|---|
| CPU | 0 % a 10,1 % | 100 % |
| RAM | 61,2 % a 61,3 % | 45,4 % |
| Disco | 45,3 % | 46,5 % |
| Duración | ≈ 30 segundos | ≈ 30 segundos |

La diferencia más significativa se observó en el procesador virtual, que alcanzó el 100 % de utilización durante la prueba con carga.

Las diferencias de RAM y disco no pueden atribuirse directamente a la carga de CPU, porque las pruebas se realizaron en momentos distintos y el estado del sistema pudo cambiar.

Las mediciones permitieron observar el comportamiento de los recursos asignados a Ubuntu. No constituyen una evaluación exhaustiva del rendimiento.

Los gráficos y las capturas correspondientes se encuentran documentados en el informe final del proyecto.

## Investigación y utilización de inteligencia artificial

Durante el desarrollo se utilizaron herramientas de inteligencia artificial, entre ellas ChatGPT, para investigar alternativas de monitoreo, conocer bibliotecas de Python como `psutil` y `matplotlib`, y recibir asistencia en la elaboración y comprensión de los programas.

La utilización de estas herramientas permitió complementar los conocimientos iniciales de programación y realizar las mediciones necesarias para la experiencia.

El trabajo práctico se centró en la instalación, configuración y utilización de la máquina virtual, la ejecución de comandos y la interpretación de los resultados obtenidos.

## Conclusiones

La experiencia permitió comprender cómo una computadora física puede ejecutar un sistema operativo invitado mediante un hipervisor, compartiendo recursos de procesamiento, memoria y almacenamiento.

Se comprobó que la virtualización no crea nuevos recursos físicos, sino que permite administrar y distribuir los existentes.

Los programas desarrollados en Python fueron herramientas de apoyo para registrar y representar el comportamiento de la máquina virtual.

**El aprendizaje central del proyecto fue comprender de manera práctica cómo funciona el proceso de virtualización**, relacionando los conceptos estudiados en Arquitectura y Sistemas Operativos con una experiencia real de instalación, configuración y utilización de Ubuntu dentro de VirtualBox.
