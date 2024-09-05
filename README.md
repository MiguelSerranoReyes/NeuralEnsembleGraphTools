
# Identifying Neuronal Ensembles: A Graph Theoretical Approach

Este repositorio contiene el Jupyter notebook y el código Python de soporte para el análisis de conjuntos neuronales utilizando teoría de grafos, como se describe en el capítulo "Identifying Neuronal Ensembles: A Graph Theoretical Approach".

## Contenidos

- `Identifying_Neuronal_Ensembles.ipynb`: Jupyter notebook principal para el análisis.
- `neurolab.py`: Módulo Python que contiene funciones de utilidad utilizadas en el notebook.
- `raster.csv`: Archivo de datos de muestra utilizado como entrada para las demostraciones en el notebook.

## Instalación

### Prerrequisitos

Asegúrate de tener Python y Visual Studio Code instalados en tu sistema. Puedes descargar Python desde [python.org](https://www.python.org/downloads/) y Visual Studio Code desde [code.visualstudio.com](https://code.visualstudio.com/).

#### Verificar instalación de Git

Para clonar el repositorio necesitarás Git. Para verificar si ya está instalado y configurado correctamente en tu sistema, abre la terminal y ejecuta:

```bash
git --version
```

Si ves un número de versión, Git está instalado. Si no, necesitarás instalarlo. Puedes descargar Git desde [git-scm.com](https://git-scm.com/downloads).

### Configuración de Visual Studio Code

Para configurar Python y Jupyter en Visual Studio Code, sigue estos pasos:

1. **Instalar la extensión de Python para Visual Studio Code:**

   Abre Visual Studio Code, ve a la pestaña de extensiones (icono de cuadrados en el lado izquierdo), busca 'Python', y selecciona e instala la extensión oficial de Python ofrecida por Microsoft.

2. **Instalar la extensión de Jupyter para Visual Studio Code:**

   De la misma manera, busca y instala la extensión 'Jupyter'.

3. **Instalar la extensión de Git:**

   Instala la extensión de Git para un mejor seguimiento del versionado dentro de Visual Studio Code buscando 'Git' en las extensiones y seleccionando la adecuada.

### Configuración del Repositorio

1. **Clonar el repositorio**

   Abre Visual Studio Code, luego abre la terminal (Terminal -> Nueva Terminal) y ejecuta los siguientes comandos:

   ```bash
   git clone https://github.com/MiguelSerranoReyes/NeuralEnsembleGraphTools.git
   cd NeuralEnsembleGraphTools
   ```

2. **Crear un entorno virtual**

   En la terminal de VSCode, ejecuta lo siguiente:

   - **En Linux:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - **En Windows:**

     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Instalar los paquetes requeridos**

   Con el entorno virtual activado, instala las dependencias requeridas:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Con la configuración completa, ahora puedes abrir el proyecto en Visual Studio Code:

1. **Abrir VSCode**
   
   Lanza Visual Studio Code, selecciona 'Archivo' -> 'Abrir Carpeta', y elige el directorio donde clonaste el repositorio.

2. **Iniciar el Jupyter Notebook**

   Abre la terminal en VSCode (si no está ya abierta) y ejecuta:

   ```bash
   jupyter notebook
   ```

   En la interfaz de usuario de Jupyter Notebook, navega hasta `Identifying_Neuronal_Ensembles.ipynb` para abrir y ejecutar el notebook.

   Este notebook contiene el código utilizado para el análisis descrito en el capítulo del libro. Explora y ejecuta las celdas para entender cómo se aplica la teoría de grafos al análisis de conjuntos neuronales.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Por favor, siéntete libre de hacer fork del repositorio y enviar pull requests.
