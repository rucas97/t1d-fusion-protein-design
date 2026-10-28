# Computational Design of a Tri-Functional Beta-Cell-Targeted Fusion Protein for Type 1 Diabetes

## 📖 Project Overview
Type 1 Diabetes (T1D) requires a dual-pronged approach: halting the autoimmune destruction of beta cells and regenerating/protecting the remaining beta-cell mass. 

This repository contains the *in silico* design and computational validation of **v2.0**, a 680-amino-acid tri-functional fusion protein. **Note:** These analyses support computational plausibility only; they do not establish therapeutic efficacy, clinical safety, or experimental stability.

## 🧬 The v2.0 Construct Architecture
1. **Targeting & Function (Human GLP-1 7-37):** Computationally modeled to bind GLP-1R.
2. **Novel PC2-Cleavable Linker (`GSG-KR-(GGGGS)2`):** Engineered to be a predicted substrate for PC2 and resist Furin cleavage.
3. **Regeneration (Human MANF):** ER-stress protective domain.
4. **Immune Shielding (Human Fcµ CH1-CH4, R595A):** Designed for Treg recruitment and FcRn recycling.

## 🏆 Computational Validation Matrix
| Validation Category | Test / Tool | Computational Result | Interpretation (In Silico) |
| :--- | :--- | :--- | :--- |
| **Protease Specificity** | ProP (PC2 & Furin) | PC2: **0.871**<br>Furin: **0.236** | Predicted to cleave in PC2-rich environments; predicted to resist systemic Furin cleavage. |
| **Immunogenicity** | IEDB (MHC-II) | Linker is stealthy | The linker/junctions are predicted to lack strong MHC-II neo-epitopes. |
| **Structure** | AlphaFold | High confidence | Structurally compatible with stable domain folding. |
| **Dynamics** | BioBB/GROMACS | RMSD plateau | Preliminary 10 ns trajectory suggests structural stability in solvation. |
| **Target Binding** | HDOCK (GLP-1R) | **-310.71** | Docking score suggests structural compatibility with GLP-1R, not measured affinity. |
| **Off-Target Safety** | HDOCK (Glucagon R) | Steric clashes | The Fc tail is predicted to sterically hinder off-target receptor activation. |
| **Half-Life** | HDOCK (FcRn) | **-269.65** | Docking suggests potential FcRn binding; requires experimental validation. |
| **Manufacturability** | DeepSoluE | **0.931** | Highly predicted to be soluble upon expression. |

## ⚠️ Important Claims to Audit & Limitations
1. **Cleavage:** PC2 prediction does not prove cleavage occurs *only* in pancreatic islets.
2. **Docking:** HDOCK scores are not measured binding affinities. They are scoring-function outputs.
3. **MD:** A 10 ns trajectory does not prove long-term thermodynamic stability.
4. **Immunogenicity:** In-silico prediction cannot prove the absence of anti-drug antibodies.
5. **Mechanism:** Fcµ-mediated Treg recruitment requires direct wet-lab evidence.

## 🤝 Call for Wet-Lab Collaboration
To move beyond computational plausibility, we seek collaborators to perform:
1. Gene synthesis and expression (to test actual solubility).
2. In vitro cleavage assays with recombinant PC2 and Furin.
3. Surface Plasmon Resonance (SPR) to measure actual binding affinity to GLP-1R and FcRn.
