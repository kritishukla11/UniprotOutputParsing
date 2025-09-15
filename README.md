# UniProt Query & Parsing Tools  
This repository contains Python scripts for parsing residue-level annotations from UniProt API outputs. It is intended for large protein datasets and outputs structured annotation tables for downstream analysis.  

Repository Structure: inputs/ contains example input files (UniProt ID mappings), outputs/ contains example parsed annotation outputs, scripts/ contains core parsing scripts. Key files include inputs/idmapping_2025_09_15.tsv (example UniProt ID mapping file), outputs/all_uniprot_annotations.csv (example output with parsed annotations), and scripts/uniprot_parsing.py (main script for parsing UniProt annotations).  

Installation: Clone the repository with  
`git clone https://github.com/yourusername/uniprot_query_github.git`  
Change into the directory with  
`cd uniprot_query_github`  
Install dependencies with  
`pip install -r requirements.txt`  
If requirements.txt is not created, install pandas manually.  

Usage:  
1. Prepare your input by placing your Uniprot API output file in the inputs folder, for example `inputs/sample_input.tsv`.  
2. Run the parser with  
`python scripts/uniprot_parsing.py --input inputs/sample_input.tsv --output outputs/sample_output.csv`  
3. The script will generate a CSV file with residue-level features extracted from UniProt, including binding sites, motifs, helices, sheets, and other annotated features. Example output format:
uniprot_id | residue | annotation_type | description
Q9NQ94 | 499 | Modified residue | MOD_RES 499; /note="Phosphothreonine"; /evidence="ECO:0007744|PubMed:24275569"
P04217 | 1 | Signal peptide | /evidence="ECO:0000269|PubMed:3458201"<img width="261" height="49" alt="image" src="https://github.com/user-attachments/assets/c2a25b09-bae4-4eb9-9bd6-f9c61073dc55" />

Example workflow:  
`python scripts/uniprot_parsing.py --input inputs/idmapping_2025_09_15.tsv --output outputs/all_uniprot_annotations.csv`  

Notes: UniProt queries may fail for very large batches; use smaller splits if necessary. Example input and output files are included for reference.
