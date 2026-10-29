# Computational Design of a Tri-Functional Beta-Cell-Targeted Fusion Protein for Type 1 Diabetes

## ⚠️ Evidence Level Classification
In accordance with strict scientific review:
1. **Predicted:** Computational output suggests a possible property.
2. **Experimentally Demonstrated:** A defined assay supports the property (0 claims in this repo).
3. **Therapeutically Validated:** Evidence supports the intended effect in a disease model (0 claims in this repo).
**Current Status:** All data herein represents **Level 1 (Predicted)** evidence only. v2.0 is a computational hypothesis, not a validated therapeutic.

## 📖 Project Overview
This repository contains the exhaustive *in silico* design and validation of **v2.0**, a 672-amino-acid tri-functional fusion protein for T1D. It combines Human GLP-1 (targeting), a PC2-cleavable linker (spatial activation), Human MANF (ER-stress relief), and Human Fcµ (immune modulation; half-life rationale is unestablished for IgM-derived Fcµ and requires experimental PK). 

## 🏆 Exhaustive Validation Matrix
| Category | Test / Tool | Result | Interpretation |
| :--- | :--- | :--- | :--- |
| **Sequence** | BLAST, FoldSeek | High homology | Matches human IgM/MANF perfectly. |
| **Structure** | AlphaFold, MolProbity | 96th percentile | 672-aa model, clashscore 3.73. |
| **Confidence** | pLDDT (R Plot) | High domains, low linkers | Domains rigid, linkers floppy. |
| **PAE** | LIVIA Heatmap | High inter-domain error | Confirms flexible hinges. |
| **Domains** | FoldSeek (Isolated) | Independent fold | MANF and Fcµ fold natively without linkers. |
| **Protease (Furin)**| FindFur (HMMER3) | **0 Hits** | Algorithm confirms linker resists systemic cleavage. |
| **Protease (PC2)** | ProP General PC | Score: 0.689 | Linker is a substrate for pancreatic convertases. |
| **Accessibility** | SASA (Python) | Linker: 103.34 Å² | Linker is exposed; PC2 can reach it. |
| **Docking (Target)**| HDOCK + HawkDock (GLP-1R) | -310.71 / -6140.80 | Fcµ-dominated interface; GLP-1 arm sterically occluded; consistent with PC2-cleavage-dependent activation. Both scores are from clash-containing poses; require experimental validation. |
| **Docking (Safety)** | HDOCK (GCGR) | INVALID (T4L-contaminated receptor) | Re-running against clean GCGR; original -297.39 retracted. |
| **Docking (FcRn)**| HDOCK (FcRn, 4N0U) | -269.65 | Shape-compatibility only. **Does NOT establish FcRn recycling** — that mechanism requires the IgG Fc binding site, not present in Fcµ. Half-life unestablished. |
| **Docking (Immune)** | HDOCK (FcµR) | -222.03 | Structurally binds immune receptor for Treg recruitment. |
| **Interface** | SPICE (Pose 1) | 1791 Å² | Buried surface area from valid GLP-1R pose. Pose 2 (3764 Å²) retracted — see DECISIONS.md. |
| **MD Stability** | GROMACS | 10 ns plateau | RMSD and SASA confirm structural stability. |
| **MD Dynamics** | R/bio3d (PCA) | PC1 = 52% | Dominant motion is inter-domain flexibility. |
| **Immunogenicity** | IEDB + R plot | Stealthy linker | No MHC-I/II neo-epitopes in engineered regions. |
| **B-Cell Risk** | ElliPro | High risk in linker | `GGGGS` linkers are strong linear B-cell epitopes (ADA risk). |
| **Glycans** | NetNGlyc + Python | 3 of 4 distal | Glycans do not clash with receptor (except N659, rationalizing PC2 cleavage). |
| **Disulfides** | DisLocate | Fcµ only | No linker crosslinking predicted. |

## 📂 Repository Structure
- `constructs/`: FASTA sequences (v2.0).
- `structures/`: AlphaFold models, HDOCK complexes, isolated domains.
- `validation/`: Raw outputs, SPICE data, MD plots (immunogenicity, pLDDT, PCA).
- `scripts/`: All custom Python and R scripts used for analysis.
- `notes/`: Chronological lab notebook (`DECISIONS.md`).
- `MANUSCRIPT_DRAFT.md`: The drafted preprint.
- `WET_LAB_ROADMAP.md`: Experimental plan.

## 🤝 Call for Wet-Lab Collaboration
This repository contains a computationally validated hypothesis. We seek collaborators to perform the assays detailed in `WET_LAB_ROADMAP.md`.
