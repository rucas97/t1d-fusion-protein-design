from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley

parser = PDBParser(QUIET=True)
structure = parser.get_structure("drug", "structures/v2.0_full_alphafold.pdb")
model = structure[0]

# Calculate SASA for the whole structure
sr = ShrakeRupley()
sr.compute(model, level="R")

print("Solvent Accessible Surface Area (SASA) of the Engineered Linkers:")
print("-" * 60)

# Linker 1: Residues 32-46
linker1_sasa = sum(res.sasa for res in model.get_residues() if 32 <= res.id[1] <= 46)
# Linker 2: Residues 205-219
linker2_sasa = sum(res.sasa for res in model.get_residues() if 205 <= res.id[1] <= 219)

# Calculate average SASA per residue for folded domains (e.g., MANF)
manf_sasa = sum(res.sasa for res in model.get_residues() if 47 <= res.id[1] <= 204)

print(f"Linker 1 (Res 32-46) Total SASA: {linker1_sasa:.2f} Å²")
print(f"Linker 2 (Res 205-219) Total SASA: {linker2_sasa:.2f} Å²")
print(f"MANF Domain (Res 47-204) Total SASA: {manf_sasa:.2f} Å²")
print("-" * 60)

# Compare average SASA per residue
print(f"Linker 1 Average SASA per residue: {linker1_sasa / 15:.2f} Å²")
print(f"MANF Average SASA per residue: {manf_sasa / 158:.2f} Å²")

if (linker1_sasa / 15) > (manf_sasa / 158):
    print("✅ VALIDATED: The linker is highly exposed to the solvent (high SASA), meaning PC2 can physically reach the cleavage site.")
else:
    print("⚠️ WARNING: The linker has lower SASA than the folded domains, suggesting it might be partially buried.")
