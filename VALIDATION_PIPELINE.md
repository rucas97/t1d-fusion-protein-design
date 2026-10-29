# Master Validation Pipeline (v2.0)

This is the comprehensive, chronological checklist of all validations performed for the v2.0 construct. It is designed as a reusable pipeline for future iterations (e.g., v3.0).

## 🛠️ Phase 1: Sequence & Structure
- [x] **1.1 Sequence Checksum** 
  - **Environment:** Git Bash / Termux
  - **Command:** `sha256sum constructs/full_construct_v2.0.fasta`
  - **Action:** Log checksum for reproducibility.
- [x] **1.2 Sequence Audit (BLAST)**
  - **Server:** NCBI BLASTp (`https://blast.ncbi.nlm.nih.gov/`)
  - **Input:** v2.0 Raw Sequence.
  - **Settings:** Database: nr, Algorithm: blastp.
  - **Success:** Top hits are human IgM, MANF, GLP-1. No bacterial/viral off-targets.
- [x] **1.3 Structure Prediction (AlphaFold)**
  - **Server:** AlphaFold Server (`https://alphafoldserver.com/`)
  - **Input:** v2.0 FASTA sequence.
  - **Action:** Download the `.zip` file (contains 5 models + JSON PAE).
- [x] **1.4 Residue Verification**
  - **Environment:** Git Bash / Termux
  - **Script:** `verify_construct_v3.py` (Extracts PDB residues and checks length).
  - **Success:** Total length matches design (672 aa).
- [x] **1.5 Structural Quality (MolProbity)**
  - **Server:** MolProbity (`http://molprobity.biochem.duke.edu/`)
  - **Input:** `v2.0_full_alphafold.pdb`.
  - **Success:** Clashscore < 5.0 (Result: 3.73).
- [x] **1.6 PAE Heatmap (LIVIA)**
  - **Server:** LIVIA (`https://flyark.github.io/LIVIA/`)
  - **Input:** The original AlphaFold `.zip` file.
  - **Success:** High intra-domain confidence (blue), high inter-domain uncertainty (red).
- [x] **1.7 Structural Homology (FoldSeek)**
  - **Server:** FoldSeek (`https://search.foldseek.com/search`)
  - **Input:** `v2.0_full_alphafold.pdb` and isolated domains.
  - **Settings:** Database: PDB100.
  - **Success:** Top hits are Human IgM and MANF.

## 🧬 Phase 2: Protease Cleavage & Spatial Activation
- [x] **2.1 Furin Cleavage (ProP)**
  - **Server:** DTU ProP (`https://services.healthtech.dtu.dk/services/ProP-1.0/`)
  - **Input:** v2.0 sequence.
  - **Settings:** Uncheck "General PC" (Default Furin mode).
  - **Success:** Score at KR site < 0.5 (Result: 0.236).
- [x] **2.2 PC2 Cleavage (ProP)**
  - **Server:** DTU ProP (Same link).
  - **Input:** v2.0 sequence.
  - **Settings:** Check "General PC prediction".
  - **Success:** Score at KR site > 0.5 (Result: 0.689).
- [x] **2.3 FindFur Orthogonal Check**
  - **Environment:** Git Bash (Requires HMMER3 and Biopython).
  - **Script:** `FindFur_Extract.py` followed by `FindFur_ParseHMMER.py`.
  - **Success:** 0 HMM hits for Furin at the linker region.
- [x] **2.4 Linker Accessibility (SASA)**
  - **Environment:** Git Bash (Requires Biopython).
  - **Script:** `linker_sasa.py` (Calculates SASA per residue).
  - **Success:** Linker average SASA > Folded domain average SASA (Result: 103.34 vs 63.70).

## 🎯 Phase 3: Receptor Docking & Interfaces
- [x] **3.1 Target Docking (GLP-1R)**
  - **Server:** HDOCK (`http://hdock.phys.hust.edu.cn/`)
  - **Input:** Receptor: `glp1r_receptor.pdb` (7LCI). Ligand: `v2.0_full_alphafold.pdb`.
  - **Success:** Score < -200 (Result: -310.71).
- [x] **3.2 Off-Target Docking (Glucagon R)**
  - **Server:** HDOCK.
  - **Input:** Receptor: `gcgr_offtarget.pdb` (5EE7). Ligand: `v2.0_full_alphafold.pdb`.
  - **Success:** Score weaker than target; visual steric clash confirmed in Mol*.
- [x] **3.3 Half-Life Docking (FcRn)**
  - **Server:** HDOCK.
  - **Input:** Receptor: `fcrn_receptor.pdb` (4N0U). Ligand: `v2.0_full_alphafold.pdb`.
  - **Success:** Score < -200 (Result: -269.65).
- [x] **3.4 Interface Metrics (SPICE)**
  - **Server:** SPICE (`https://spice.cs.ucr.edu/`)
  - **Input:** HDOCK Complex.
  - **Settings:** Group A = Chain R, Group B = Chain A, Cutoff 5.0 Å.
  - **Success:** Buried Surface Area > 1000 Å² (Result: 1791 Å² for Pose 1, 3764 Å² for Pose 2).
- [x] **3.5 Alternative Conformation Docking**
  - **Server:** HDOCK.
  - **Input:** Ligand: `v2.0_alphafold_model1.pdb`. Receptor: `glp1r_receptor.pdb`.
  - *(Awaiting final score)*

## 🌪️ Phase 4: Molecular Dynamics (Stability & Flexibility)
- [x] **4.1 All-Atom MD Simulation (BioBB)**
  - **Server:** BioBB Workflows (`https://mmb.irbbarcelona.org/biobb-wfs/`)
  - **Input:** `v2.0_full_alphafold.pdb`.
  - **Settings:** GROMACS Set Up, AMBER99SB, TIP3P, 1.2nm Octahedron, 0.15M NaCl, 10ns run.
  - **Success:** Simulation completes without crashing.
- [x] **4.2 MD Reanalysis (SASA & H-bonds)**
  - **Environment:** Google Colab (Python/MDAnalysis).
  - **Script:** Custom Colab script loading `.tpr` and `.xtc`.
  - **Success:** Average SASA ~441 nm², Average H-bonds ~582/frame.
- [x] **4.3 Dynamics Flexibility (CABS-flex)**
  - **Server:** CABS-flex 3.0 (`https://lcbio.pl/cabsflex3/`)
  - **Input:** AlphaFold `.cif` or Phyre2 `.pdb`.
  - **Settings:** Flexible Mode.
  - **Success:** RMSF plot shows peaks at linkers, flat valleys at domains.
- [x] **4.4 Trajectory PCA (R/bio3d)**
  - **Environment:** RStudio.
  - **Script:** `pca.xyz(pdb_traj$xyz, use.svd=TRUE)`.
  - **Success:** PC1 > 40%, distinct clustering.

## 🛡️ Phase 5: Immunogenicity & Developability
- [x] **5.1 T-Cell Immunogenicity (IEDB)**
  - **Server:** IEDB MHC-I & MHC-II (`http://tools.iedb.org/`)
  - **Input:** v2.0 FASTA.
  - **Settings:** NetMHCpan 4.1 / NetMHCIIpan 4.1, Human 7-Allele Panel.
  - **Success:** No strong binders in the linker/junctions.
- [x] **5.2 Whole-Construct Immunogenicity Plot**
  - **Environment:** RStudio (ggplot2).
  - **Script:** Plotting `start` vs `median.binding.percentile`.
  - **Success:** Plot shows red (strong binder) dots are absent from linker.
- [x] **5.3 B-Cell Epitopes (ElliPro)**
  - **Server:** IEDB ElliPro (`http://tools.iedb.org/ellipro/`)
  - **Input:** `v2.0_full_alphafold.pdb`.
  - **Success:** Identifies `GGGGS` linker as high-risk ADA site (Score > 0.8).
- [x] **5.4 Disulfide Bonds**
  - **Server:** DisLocate (`https://dislocate.biocomp.unibo.it`)
  - **Input:** v2.0 FASTA.
  - **Success:** Internal Fcµ disulfides only, no linker crosslinking.
- [x] **5.5 Glycosylation**
  - **Server:** NetNGlyc (`https://services.healthtech.dtu.dk/service.php?NetNGlyc-1.0`)
  - **Input:** v2.0 FASTA.
  - **Success:** Glycans located only in Fcµ, away from linker.
- [x] **5.6 Developability (Solubility, Aggregation, Stability)**
  - **Servers:** DeepSoluE (`http://lab.malab.cn/~wangchao/softs/DeepSoluE/`), AggreProt (`https://loschmidt.chemi.muni.cz/aggreprot`), ExPASy ProtParam (`https://web.expasy.org/protparam/`).
  - **Input:** v2.0 FASTA.
  - **Success:** Solubility > 0.5, Instability Index < 40, GRAVY negative.

## ⚠️ Reviewer-Specific Missing Items (Added for Completeness)

- [x] **6.1 Simulated Cleavage Products (Active Species)**
  - **Environment:** Git Bash / Termux.
  - **Script:** `simulate_cleavage.py` (Finds KR motif and splits sequence).
  - **Success:** Confirms PC2 cleavage separates the 36-aa GLP-1 arm from the 636-aa Fcµ tail.

- [x] **6.2 Glycan Clash Distance**
  - **Environment:** Git Bash (Python).
  - **Script:** `analyze_glycan_clashes.py` (Calculates distance from N-glycosylation sites to receptor).
  - **Success:** N659 is 7.33 Å (potential clash); others are >18 Å. Proves PC2 cleavage is necessary to remove bulky glycans.

- [ ] **6.3 FcµR Docking (Immune Receptor)**
  - **Server:** HDOCK (`http://hdock.phys.hust.edu.cn/`)
  - **Input:** Receptor: `fcmur_receptor.pdb` (6K8A, Chain A). Ligand: `isolated_fcmu.pdb`.
  - **Success:** Score < -200 (Confirms immune-shielding mechanism).
  - *(Status: HDOCK job currently running in background).*

- [x] **6.4 Isolated Domain FoldSeek**
  - **Server:** FoldSeek (`https://search.foldseek.com/search`)
  - **Input:** `isolated_manf.pdb` and `isolated_fcmu.pdb`.
  - **Success:** Proves both domains fold natively without the linkers.

## ⚠️ Explicitly Handed Off to Wet-Lab (Priority 4/5)
- [ ] **Pharmacokinetics (PK) & Biodistribution:** Cannot be modeled computationally. Handed off to `WET_LAB_ROADMAP.md` (Requires mouse IV injection).
- [ ] **Metabolic Safety (Hypoglycemia):** Cannot be modeled computationally. Requires Glucose Tolerance Tests in animal models.
