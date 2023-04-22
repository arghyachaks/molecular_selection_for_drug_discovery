# molecular_selection_for_drug_discovery
Once upon a time, in a small village, there was a chemist named Ada. Ada loved experimenting with molecules and creating new substances in her laboratory. One day, Ada received a mysterious letter with a challenge. The challenge was to find a molecule from a list of candidates that best matched a specific target. 

The list of candidate molecules was written in a special code called Simplified Molecular Input Line Entry System (SMILES). SMILES is a way to represent molecules as a sequence of characters, making it easier to store and share molecular data. The candidates were: 

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

To solve this challenge, Ada decided to use her magic tool, a quantum computer. The quantum computer could find the best solution by exploring multiple possibilities simultaneously. Ada programmed the quantum computer to create a mathematical model that represented the candidate molecules and the challenge's constraints. 

Ada defined a variable for each candidate molecule, which could take the value of 1 if the molecule was selected and 0 if it was not. She also created a variable to represent the objective value, which would measure how close each molecule was to the target. The objective value was calculated as the sum of the absolute differences between the number of atoms and bonds in the selected molecule and the target values. 

Next, Ada added a constraint to the model, ensuring that only one molecule could be selected from the list. With the objective function and constraints in place, she used the quantum computer's powerful LeapHybridCQMSampler to search for the best solution. 

The quantum computer analyzed the problem and quickly found the optimal solution. It selected the molecule with the SMILES code "CC=O" and the English name "Acetaldehyde," which had 3 atoms and 3 bonds, exactly matching the target. 

Ada was thrilled with the results and felt a great sense of accomplishment. She had successfully solved the mysterious challenge using her knowledge, creativity, and the power of the quantum computer. And so, the story of Ada's molecular adventure spread throughout the village, inspiring others to explore the fascinating world of chemistry and quantum computing.

# Installation
pip install -r requirements.txt

# Usage
- Download and install Anaconda: Go to the Anaconda download page (https://www.anaconda.com/products/individual) and download the appropriate version for your operating system. Follow the installation instructions to install Anaconda on your computer.

- Open Anaconda Navigator: Once you have installed Anaconda, open the Anaconda Navigator. You can do this by clicking on the Anaconda Navigator icon in your Applications folder (on macOS) or by searching for Anaconda Navigator in the Start menu (on Windows). 

- Launch Jupyter Notebook: In the Anaconda Navigator, click on the Jupyter Notebook icon. This will launch Jupyter Notebook in your default web browser. 

- Navigate to the notebook directory: Once Jupyter Notebook has opened in your browser, you will see a file browser. Use the file browser to navigate to the directory where your notebook "MolecularSelectionForDrugDiscovery" is located. 

- Open the notebook: Once you have located your notebook, click on it to open it. This will launch the notebook in a new browser tab. 

- Run code: You can run a cell by pressing "Shift + Enter" or by clicking the "Run" button in the toolbar

## Or run
python MolecularSelectionForDrugDiscovery.py
