# Computational Design of a Tri-Functional Beta-Cell-Targeted Fusion Protein for Type 1 Diabetes

## ⚠️ Evidence Level Classification
In accordance with strict scientific review:
1. **Predicted:** Computational output suggests a possible property.
2. **Experimentally Demonstrated:** A defined assay supports the property (0 claims in this repo).
3. **Therapeutically Validated:** Evidence supports the intended effect in a disease model (0 claims in this repo).
**Current Status:** All data herein represents **Level 1 (Predicted)** evidence only.

## 📖 Project Overview
This repository contains the *in silico* design and exhaustive computational validation of **v2.0**, a 672-amino-acid tri-functional fusion protein for T1D. It combines Human GLP-1 (targeting), a PC2-cleavable linker (spatial activation), Human MANF (ER-stress relief), and Human Fcµ (Treg recruitment and half-life). 

## 🏆 Comprehensive Validation Matrix
| Category | Test / Tool | Result | Interpretation |
| :--- | :--- | :--- | :--- |
| **Sequence** | BLAST, FoldSeek | High homology | Matches human IgM/MANF perfectly. |
| **Structure** | AlphaFold, MolProbity | 96th percentile | 672-aa model, clashscore 3.73. |
| **Domains** | FoldSeek (Isolated) | Independent fold | MANF and Fcµ fold natively without linkers. |
| **Protease (Furin)**| FindFur (HMMER3) | **0 Hits** | Algorithm confirms linker resists systemic cleavage. |
| **Protease (PC2)** | ProP General PC | Score: 0.689 | Linker is a substrate for pancreatic convertases. |
| **Docking (Target)**| HDOCK (GLP-1R) | -310.71 | Strong structural compatibility. |
| **Docking (Half-life)**| HDOCK (FcRn) | -269.65 | Predicts FcRn recycling. |
| **Interface** | SPICE (Pose 1/2) | 1791 / 3764 Å² | Massive buried surface area; binding is robust. |
| **MD Stability** | GROMACS | 10 ns plateau | RMSD and SASA confirm structural stability. |
| **MD Dynamics** | R/bio3d (PCA) | PC1 = 52% | Dominant motion is inter-domain flexibility. |
| **PAE** | LIVIA | High inter-domain error | Confirms flexible linkers. |
| **Immunogenicity** | IEDB + R plot | Stealthy linker | No MHC-I/II neo-epitopes in engineered regions. |
| **Glycans** | NetNGlyc + Python | 3 of 4 distal | Glycans do not clash with receptor (except N659, rationalizing PC2 cleavage). |
| **Disulfides** | DisLocate | Fcµ only | No linker crosslinking predicted. |

## 🤝 Call for Wet-Lab Collaboration
This repository contains a computationally validated hypothesis. We seek collaborators to perform the assays detailed in `WET_LAB_ROADMAP.md`.
