# Application of Machine Learning models for the prediction of bioconjugation processes in the synthesis of antibody-drug conjugates.

This repository contains the code that enables users to input their own bioconjugation parameters (i.e, LP system in SMILES format, mAb, bioconjugation site, buffer) obtaining as output the bioconjugation conditions predicting the DAR values. Users should run Bioconjugatio_calculator.py.

# Requirements 

This project was entirely developed with Python (version>=3.3). The required Python modules are:

* Pandas
* Numpy
* Scikit-learn
* RDKit
* XGBoost
* Sympy
* Datetime
* Openpyxl

# Project structure

* **cys_dataset_calculator.xlsx**: Dataset specifically related to cysteine (Cys) bioconjugation experiments.
* **lys_dataset_calculator.xlsx**: Dataset related to lysine (Lys) bioconjugation experiments.
* **SMILES_Cys.xlsx**: SMILES representations of molecules for Cys-related experiments.
* **SMILES_Lys.xlsx**: SMILES representations of molecules for Lys-related experiments.
* **Bioconjugation_calculator.py**: Script for running the bioconjugation calculations based on the provided datasets.
* **Bioconjugation_functions.py**: Contains helper functions used in bioconjugation calculations.
* **excel_modifier.py**: Script for modifying or processing the Excel files (e.g., cleaning data, transforming formats).
* **predictions.py**: Script for running predictions based on processed data and model
