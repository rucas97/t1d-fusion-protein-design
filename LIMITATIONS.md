# Computational Limitations & Failed Runs

This document explicitly records the limitations of the current computational pipeline and any failed runs, as required by rigorous validation audits.

## 1. Failed Runs
- **Google Colab (Making it Rain):** Failed to run due to dependency conflicts with the `parmed` library on the Colab environment.
- **BilboMD:** Could not be run because we lacked experimental SAXS data and the classic `const.inp` file required by the pipeline.
- **PELE Web Server:** Returned a 502 Bad Gateway error during the simulation attempt.

## 2. Deleted Data (Trajectory Analysis Limits)
- **MD Trajectory (`.xtc`):** The 54 MB all-atom trajectory file from the BioBB/GROMACS setup was deleted to conserve mobile device storage. 
- **Impact:** We cannot run `gmx sasa` (Solvent Accessible Surface Area) or `gmx hbond` (Hydrogen bonding over time) on the trajectory. Only the `.xvg` plots for RMSD and Radius of Gyration were retained.

## 3. Unperformed Comparative Analysis
- **Alternative Structural Models:** We did not run a structural alignment (e.g., DALI or FoldSeek) comparing AlphaFold `model_0` to `model_1` through `model_4` to verify the stability of the predicted fold.
- **Alternative Docking Poses:** We only analyzed the Top 1 docking pose from HDOCK for the on-target and off-target receptors. We did not perform a rigorous analysis of poses 2 through 10.
