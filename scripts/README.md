# Analysis Scripts

This folder contains the custom scripts used for the rigorous validation of v2.0.

- `verify_construct_v3.py`: Validates exact sequence length and mutation (R587A).
- `simulate_cleavage.py`: Simulates PC2 cleavage and outputs resulting fragments.
- `extract_domains.py`: Extracts isolated MANF and Fcµ domains from the full AlphaFold model.
- `analyze_glycan_clashes.py`: Calculates distance between N-glycosylation sites and the receptor.
- `linker_sasa.py`: Calculates Solvent Accessible Surface Area (SASA) of the linkers.
- `convert_traj.py`: Converts the GROMACS binary trajectory to a text-based PDB for R.
- `PCA_analysis.R`: R script to perform SVD-based PCA on the MD trajectory.
- `pLDDT_plot.R`: R script to extract B-factors and plot per-residue AlphaFold confidence.
