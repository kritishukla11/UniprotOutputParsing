# Import all packages
import pandas as pd
import re

# Function to parse residue + description
def parse_annotation(text):
    """
    Parse UniProt-style annotation like:
    'BINDING 199; /ligand="Zn(2+)"'
    'HELIX 244..252; /evidence="ECO:0007829|PDB:2CP..."
    """
    text = str(text)

    # Find single residue or range
    match = re.search(r"(\d+)(?:\.\.(\d+))?", text)
    if not match:
        return [], text.strip()

    start = int(match.group(1))
    end = int(match.group(2)) if match.group(2) else start

    residues = list(range(start, end + 1))

    # Description = remove leading keyword + numbers
    desc = re.sub(r"^[A-Z ]+\d+(\.\.\d+)?;?\s*", "", text).strip()
    return residues, desc

# Load data
df = pd.read_csv('../inputs/idmapping_2025_09_15.tsv',sep='\t')

# Get relevant columns
keywords = [
    "site", "binding", "dna", "nucleotide", "metal",
    "residue", "strand", "helix", "turn",
    "domain", "region", "peptide", "motif", "repeat"
]

residue_cols = [c for c in df.columns if any(k in c.lower() for k in keywords)]
print("Residue-level annotation columns:", residue_cols)

# Melt only those
melted = df.melt(
    id_vars=["Entry"], 
    value_vars=residue_cols, 
    var_name="annotation_type", 
    value_name="raw_annotation"
).dropna(subset=["raw_annotation"])

# Apply parsing
melted[["residue", "description"]] = melted["raw_annotation"].apply(
    lambda x: pd.Series(parse_annotation(str(x)))
)

# Apply parsing
expanded_rows = []
for _, row in melted.iterrows():
    residues, desc = parse_annotation(row["raw_annotation"])
    for r in residues:
        expanded_rows.append({
            "uniprot_id": row["Entry"],
            "residue": r,
            "annotation_type": row["annotation_type"],
            "description": desc
        })

# Create final dataframe
final_df = pd.DataFrame(expanded_rows)

# Save
final_df.to_csv('../outputs/all_uniprot_annotations.csv',index=False)



