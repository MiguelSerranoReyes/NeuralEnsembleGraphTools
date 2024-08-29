
# Identifying Neuronal Ensembles: A Graph Theoretical Approach

This repository contains the Jupyter notebook and supporting Python code for the analysis of neuronal ensembles using graph theory, as described in the chapter "Identifying Neuronal Ensembles: A Graph Theoretical Approach".

## Contents

- `Identifying_Neuronal_Ensembles.ipynb`: The main Jupyter notebook for the analysis.
- `neurolab.py`: Python module containing utility functions used in the notebook.
- `raster.csv`: Sample data file used as an input for the demonstrations in the notebook.

## Installation

### Prerequisites

Ensure you have Python and Visual Studio Code installed on your system. You can download Python from [python.org](https://www.python.org/downloads/) and Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).

### Setup

1. **Clone the repository**

   Open Visual Studio Code, then open the terminal (Terminal -> New Terminal) and run the following commands:

   ```bash
   git clone https://github.com/MiguelSerranoReyes/NeuralEnsembleGraphTools.git
   cd NeuralEnsembleGraphTools
   ```

2. **Create a virtual environment**

   In the VSCode terminal, execute the following:

   - **On Linux:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - **On Windows:**

     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Install the required packages**

   With the virtual environment activated, install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

With the setup complete, you can now open the project in Visual Studio Code:

1. **Open VSCode**
   
   Launch Visual Studio Code, select 'File' -> 'Open Folder', and choose the directory where you cloned the repository.

2. **Start the Jupyter Notebook**

   Open the terminal in VSCode (if not already open) and run:

   ```bash
   jupyter notebook
   ```

   Navigate to `Identifying_Neuronal_Ensembles.ipynb` in the Jupyter notebook UI to open and run the notebook.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.