# UniProt Query & Parsing Tools  
This repository contains Python scripts for parsing residue-level annotations from UniProt API outputs. It is intended for large protein datasets and outputs structured annotation tables for downstream analysis.  

Repository Structure: inputs/ contains example input files (UniProt ID mappings), outputs/ contains example parsed annotation outputs, scripts/ contains core parsing scripts. Key files include inputs/idmapping_2025_09_15.tsv (example UniProt ID mapping file), outputs/all_uniprot_annotations.csv (example output with parsed annotations), and scripts/uniprot_parsing.py (main script for parsing UniProt annotations).  

Installation: Clone the repository with  
`git clone https://github.com/yourusername/uniprot_query_github.git`  
Change into the directory with  
`cd uniprot_query_github`  
Install dependencies with  
`pip install -r requirements.txt`  
If requirements.txt is not created, install pandas, requests, tqdm, and regex manually.  

Usage:  
1. Prepare your input by placing a UniProt ID mapping file (TSV/CSV) inside the inputs/ folder, for example `inputs/sample_input.tsv`.  
2. Run the parser with  
`python scripts/uniprot_parsing.py --input inputs/idmapping_2025_09_15.tsv --output outputs/all_uniprot_annotations.csv`  
3. The script will generate a CSV file with residue-level features extracted from UniProt, including binding sites, motifs, helices, sheets, and other annotated features. Example output format:  
ProteinID | Residue | Feature  
P12345 | 199 | Zn(2+) binding site  
P12345 | 244 | Helix  

Example workflow:  
`python scripts/uniprot_parsing.py --input inputs/idmapping_2025_09_15.tsv --output outputs/all_uniprot_annotations.csv`  

Notes: UniProt queries may fail for very large batches; use smaller splits if necessary. Example input and output files are included for reference. Checkpoints from Jupyter (.ipynb_checkpoints/) are not needed for execution.  
