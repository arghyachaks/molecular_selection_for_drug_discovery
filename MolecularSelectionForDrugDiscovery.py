'''
Once upon a time, in a small village, there was a chemist named Ada. Ada loved experimenting with molecules and creating new substances in her laboratory. One day, Ada received a mysterious letter with a 
challenge. The challenge was to find a molecule from a list of candidates that best matched a specific target.

The list of candidate molecules was written in a special code called Simplified Molecular Input Line Entry System (SMILES). SMILES is a way to represent molecules as a sequence of characters, making it 
easier to store and share molecular data. The candidates were:

- Ethanol (CCO)
- Methylamine (CCN)
- Methoxy methane (COC)
- Methyl formate (COO)
- Oxazole (CNO)
- Isocyanic acid (CN=C=O)
- Propane (CCC)
- Acetaldehyde (CC=O)
- Hydrogen cyanide (CC#N)

Ada's goal was to find a molecule from this list that had a specific number of atoms and bonds. The target was to find a molecule with 3 atoms and 3 bonds.

To solve this challenge, Ada decided to use her magic tool, a quantum computer. The quantum computer could find the best solution by exploring multiple possibilities simultaneously. Ada programmed the 
quantum computer to create a mathematical model that represented the candidate molecules and the challenge's constraints.

Ada defined a variable for each candidate molecule, which could take the value of 1 if the molecule was selected and 0 if it was not. She also created a variable to represent the objective value, which 
would measure how close each molecule was to the target. The objective value was calculated as the sum of the absolute differences between the number of atoms and bonds in the selected molecule and the 
target values.

Next, Ada added a constraint to the model, ensuring that only one molecule could be selected from the list. With the objective function and constraints in place, she used the quantum computer's powerful 
LeapHybridCQMSampler to search for the best solution.

The quantum computer analyzed the problem and quickly found the optimal solution. It selected the molecule with the SMILES code "CC=O" and the English name "Acetaldehyde," which had 3 atoms and 3 bonds, 
exactly matching the target.

Ada was thrilled with the results and felt a great sense of accomplishment. She had successfully solved the mysterious challenge using her knowledge, creativity, and the power of the quantum computer. And 
so, the story of Ada's molecular adventure spread throughout the village, inspiring others to explore the fascinating world of chemistry and quantum computing.
'''

import numpy as np  
from rdkit import Chem  
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler 

# List of candidate molecules in SMILES format  
candidate_molecules = [  
    "CCO",  
    "CCN",  
    "COC",  
    "COO",  
    "CNO",  
    "CN=C=O",  
    "CCC",  
    "CC=O",  
    "CC#N"  
]  

# English names of the molecules  
molecule_names = [  
    "Ethanol",  
    "Methylamine",  
    "Methoxy methane",  
    "Methyl formate",  
    "Oxazole",  
    "Isocyanic acid",  
    "Propane",  
    "Acetaldehyde",  
    "Hydrogen cyanide"  
]  

# Constraints  
target_num_atoms = 3  
target_num_bonds = 3  

# Create the Constrained Quadratic Model  
cqm = ConstrainedQuadraticModel() 

# Create a binary variable for each candidate molecule  
molecule_vars = []  
for i, smiles in enumerate(candidate_molecules):  
    molecule_vars.append(dimod.Binary(f"molecule_{i}"))  

# Constraint: Only one molecule can be selected  
cqm.add_constraint(sum(molecule_vars) == 1, label="selection_constraint")

# Create a new variable to represent the objective value  
objective_var = dimod.Integer("objective")  
  
# Define the relationship between the molecule variables and the objective value  
for i, smiles in enumerate(candidate_molecules):  
    molecule = Chem.MolFromSmiles(smiles)  
    num_atoms = molecule.GetNumAtoms()  
    num_bonds = molecule.GetNumBonds()  
    objective_term = float(abs(target_num_atoms - num_atoms) + abs(target_num_bonds - num_bonds))  
      
    # Add a constraint that enforces the relationship between the molecule variable and the objective value  
    cqm.add_constraint(objective_term * molecule_vars[i] - objective_var <= 0)  
    cqm.add_constraint(-objective_term * molecule_vars[i] + objective_var <= 0)

# Set the objective function: minimize the objective value  
cqm.set_objective(objective_var) 

# Solve the CQM
DWAVE_API_TOKEN = "DEV-******"#Copy your D-wave key her
sampler = LeapHybridCQMSampler(token = DWAVE_API_TOKEN)  
sampleset = sampler.sample_cqm(cqm,label="Molecular Selection For Drug Discovery")

# Get the best solution  
solution = sampleset.first.sample  
  
# Print the selected molecule  
for var, value in solution.items():  
    if value == 1:  
        idx = int(var.split("_")[-1])  
        print(f"Selected molecule: {candidate_molecules[idx]}, English name: {molecule_names[idx]}")  

