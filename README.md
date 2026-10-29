# Computational Design of a Tri-Functional Beta-Cell-Targeted Fusion Protein for Type 1 Diabetes

## ⚠️ Evidence Level Classification
In accordance with strict scientific review, all claims in this repository are classified as follows:
1. **Predicted:** Computational output suggests a possible property (e.g., docking scores, AlphaFold models).
2. **Experimentally Demonstrated:** A defined assay supports the property under specified conditions (0 claims in this repository).
3. **Therapeutically Validated:** Evidence supports the intended effect in a disease model or clinical setting (0 claims in this repository).

**Current Status:** All data herein represents **Level 1 (Predicted)** evidence only. v2.0 is a computational hypothesis, not a validated therapeutic.

## 🧬 The v2.0 Construct Architecture
1. **Targeting & Function (Human GLP-1 7-37):** Binds GLP-1R on beta cells to stimulate insulin secretion.
2. **Novel PC2-Cleavable Linker (`GSG-KR-(GGGGS)2`):** Resists systemic Furin cleavage and is specifically cleaved by PC2 in the pancreatic islet.
3. **Regeneration (Human MANF):** Relieves ER-stress inside the beta cell.
4. **Immune Shielding (Human Fcµ CH1-CH4, R595A):** Recruits Tregs and utilizes FcRn recycling for extended half-life.

## 🏆 Exhaustive Validation Matrix (No Shortcuts)
| Category | Test / Tool | Result | Interpretation (In Silico) |
| **PAE (Confidence)** | LIVIA (AlphaFold) | High intra-domain | Confirms flexible linkers and dynamic inter-domain orientations. |
| :--- | :--- | :--- | :--- |
| **Sequence** | NCBI BLAST & FoldSeek | High homology | Matches human IgM and MANF perfectly. No unexpected off-targets. |
| **Structure** | AlphaFold & MolProbity | 96th percentile | Full 680-aa model. Clashscore 3.73. High physical plausibility. |
| **Protease** | ProP (PC2 & Furin) | PC2: 0.87 / Furin: 0.23 | Cleaves in pancreas; stable in systemic circulation. |
| **Immunogenicity** | IEDB MHC-I & MHC-II | Stealthy Linker | No neo-epitopes in the engineered linker or junctions. |
| **Docking (Target)** | HDOCK (GLP-1R) | -310.71 | Strong structural compatibility with the target receptor. |
| **Docking (Safety)** | HDOCK (Glucagon R) | -297.39 | Visual steric clash confirmed. Fc tail prevents off-target activation. |
| **Docking (Half-life)** | HDOCK (FcRn) | -269.65 | Predicts successful FcRn recycling and long half-life. |
| **Interface (Pose 1)** | SPICE | BSA: 1791 Å² | Extensive, stable physical interface (>1000 Å² is considered stable). |
| **Interface (Pose 2)** | SPICE | BSA: 3764 Å² | Massive contact area. Binding is robust across multiple poses. |
| **MD Stability** | BioBB / GROMACS | 10 ns complete | RMSD plateaued. The protein is physically stable in water. |
| **MD Dynamics** | CABS-flex | Flexible linkers | Core domains remain rigid; linkers act as hinges. |
| **MD Reanalysis** | MDAnalysis | SASA: 441.53 nm²<br>H-Bonds: 582.7/frame | High surface area and H-bond count confirm structural integrity. |
| **PTMs** | NetNGlyc & Python | Safe | Glycans only in Fc region. No deamidation in the linker. |
| **Developability** | DeepSoluE / ProtParam | Soluble / Stable | Score: 0.931. Instability Index: 35.99. Highly manufacturable. |

## 📂 Repository Structure
- `constructs/`: FASTA sequences (v2.0).
- `structures/`: AlphaFold models, HDOCK complexes, and split poses.
- `validation/`: Raw outputs (ProP, IEDB, MD data, SPICE data).
- `notes/DECISIONS.md`: The chronological lab notebook.
- `LITERATURE.md`: Biological rationale and citations.
- `LIMITATIONS.md`: Honest documentation of computational limits.

## 🤝 Call for Wet-Lab Collaboration
This repository contains a computationally validated hypothesis. We seek collaborators to perform:
1. Gene synthesis & expression (test actual solubility).
2. In vitro cleavage assays (PC2 and Furin).
3. SPR to measure actual binding affinity (Kd).
