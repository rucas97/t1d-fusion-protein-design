import MDAnalysis as mda

# USE THE FULL PATHS HERE (Replace F:/FindFur_Analysis with your actual path)
tpr_path = "F:/FindFur_Analysis/biobb.MDsetup.tpr"
xtc_path = "F:/FindFur_Analysis/biobb.MDsetup.xtc"

u = mda.Universe(tpr_path, xtc_path)
protein = u.select_atoms("protein")

print("Writing trajectory.pdb...")
with mda.Writer("trajectory.pdb", protein.n_atoms) as W:
    for ts in u.trajectory:
        W.write(protein)
print("Conversion complete.")
