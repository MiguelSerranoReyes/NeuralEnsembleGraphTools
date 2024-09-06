
# Identifying Neuronal Ensembles: A Graph Theoretical Approach

This repository contains the Jupyter notebook and supporting Python code for the analysis of neuronal ensembles using graph theory, as described in the chapter "Identifying Neuronal Ensembles: A Graph Theoretical Approach".

## Contents

- `Identifying_Neuronal_Ensembles.ipynb`: Main Jupyter notebook for analysis.
- `neurolab.py`: Python module containing utility functions used in the notebook.
- `raster.csv`: Sample data file used as input for the demonstrations in the notebook.

## Installation

### Prerequisites

Ensure you have Python, Visual Studio Code, and Git installed on your system. We recommend using Python 3.10 or higher to ensure compatibility with all libraries and features used in this project. If you are not sure if Python is installed, you can check by opening a terminal and typing:

```bash
python --version
```

or

```bash
python3 --version
```

If a version number is displayed, Python is installed. If not, or if your version is earlier than 3.10, you will need to install or update Python. You can get Python from [python.org](https://www.python.org/downloads/) or use Anaconda, available at [anaconda.com](https://www.anaconda.com/products/distribution). Be sure to select the option to add Python to your PATH during installation.

To check if Git is installed, open a terminal and type:

```bash
git --version
```

If it shows a version number, Git is installed. If not, you can download Git from [git-scm.com](https://git-scm.com/downloads). Follow the instructions on the website to install it on your system.

For Visual Studio Code, download it from [code.visualstudio.com](https://code.visualstudio.com/). During installation, follow the on-screen instructions to ensure proper integration with the system.

### Configuring Visual Studio Code

After installation, set up your development environment:

1. **Install necessary extensions:**

   Open Visual Studio Code and go to the extensions tab (square icon on the left side of the window). You will need to install the following extensions:
   - Python (offered by Microsoft)
   - Jupyter (for working with Jupyter notebooks directly in VSCode)
   - GitLens (enhances Git integration by providing advanced visual features)

### Repository Configuration

1. **Choose the repository location:**

   Before cloning the repository, decide where you want the code to be hosted on your machine. It is important to select a suitable location where you can easily access your files.

2. **Clone the repository:**

   Open Visual Studio Code and select 'File' -> 'Open Folder' to set the folder where you will clone the repository. Then, open a terminal in Visual Studio Code (`Terminal -> New Terminal`) and use the following commands to clone the repository and change to its directory:

   ```bash
   git clone https://github.com/MiguelSerranoReyes/NeuralEnsembleGraphTools.git
   cd NeuralEnsembleGraphTools
   ```

3. **Create a virtual environment:**

   In the terminal of Visual Studio Code, create a virtual environment to manage dependencies in isolation:

   - **For Windows users:**
     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

   - **For Linux/Mac users:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

4. **Update pip and install dependencies:**

   Ensure that pip is up to date and then install the necessary dependencies for the project:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

Once everything is set up, simply double-click the `Identifying_Neuronal_Ensembles.ipynb` file in Visual Studio Code to open the Jupyter notebook. The previously installed extensions will allow the notebook to run properly.

## Contributions

Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.
