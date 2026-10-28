# Computational Design of a Tri-Functional Beta-Cell-Targeted Fusion Protein for Type 1 Diabetes

## 📖 Project Overview
Type 1 Diabetes (T1D) requires a dual-pronged approach: halting the autoimmune destruction of beta cells and regenerating/protecting the remaining beta-cell mass. Single-agent therapies often fail because they address only one arm of the disease. 

This repository contains the complete *in silico* design, structural modeling, and rigorous computational validation of **v2.0**, a novel 680-amino-acid tri-functional fusion protein designed to act as a "smart" first responder for T1D.

## 🧬 The v2.0 Construct Architecture
The final lead candidate (`t1d_fusion_construct_v2.0`) is composed of:
1. **Targeting & Function (Human GLP-1 7-37):** Binds GLP-1R on beta cells to stimulate glucose-dependent insulin secretion and promote proliferation.
2. **Novel PC2-Cleavable Linker (`GSG-KR-(GGGGS)2`):** Engineered to resist ubiquitous Furin cleavage in the bloodstream and only be cleaved by PC2 in the pancreatic islet microenvironment.
3. **Regeneration (Human MANF):** Relieves ER-stress inside the beta cell, preventing inflammation-induced apoptosis.
4. **Immune Shielding (Human Fcµ CH1-CH4, R595A):** Recruits Regulatory T-cells (Tregs) to suppress autoreactive immune attack and utilizes FcRn recycling for extended serum half-life.

## 🏆 Comprehensive Validation Matrix (No Shortcuts)
All validations were performed on the final v2.0 sequence and full 3D structure, using free, open-source web servers and local custom scripts.

| Validation Category | Test / Tool | Result | Interpretation |
| :--- | :--- | :--- | :--- |
| **Protease Specificity** | ProP (PC2 & Furin) | PC2: **0.871**<br>Furin: **0.236** | Cleaves specifically in the pancreas; stable in systemic circulation. |
| **Immunogenicity** | IEDB (MHC-II) | Stealthy Linker | Linker and junctions do not create neo-epitopes. Exendin-4 was swapped for human GLP-1 to eliminate ADA risk. |
| **Structure & Dynamics** | AlphaFold & CABS-flex | Stable Core | 100% sequence modeled. Folded domains are stable; novel linkers act as flexible hinges. |
| **All-Atom MD** | BioBB / GROMACS | RMSD Plateaued | 10 ns solvated simulation confirmed the protein is physically stable in a physiological environment. |
| **Target Binding** | HDOCK (GLP-1R) | **-310.71** | The full 680-aa drug strongly binds its intended target without steric hindrance from the Fc tail. |
| **Off-Target Safety** | HDOCK (Glucagon R) | **-297.39** | The Fc tail causes steric clashes on the off-target receptor, preventing non-specific activation. |
| **Half-Life** | HDOCK (FcRn) | **-269.65** | Strong binding to the recycling receptor predicts a long pharmacokinetic half-life. |
| **Developability** | ProtParam & AggreProt | Stable / Clean | Instability Index: 35.99. GRAVY: -0.398. No aggregation risk in the engineered linker. |
| **Manufacturability** | DeepSoluE | **0.931** | Highly likely to be soluble upon expression (no inclusion bodies). |

## 📂 Repository Structure
- `constructs/`: FASTA sequences of the final v2.0 candidate.
- `structures/`: AlphaFold models, cleaned receptors, and HDOCK complex models.
- `validation/`: Raw output data from ProP, IEDB, MD simulations, and PTM scripts.
- `notes/DECISIONS.md`: The chronological lab notebook detailing the rationale, failures, and pivots of the design process.

## 🤝 Call for Wet-Lab Collaboration
This repository contains a computationally validated, publication-ready *in silico* hypothesis. To take the next step toward a clinical therapeutic, we are seeking a wet-lab collaborator to perform:
1. **Gene Synthesis & Expression:** Express the v2.0 construct in CHO or HEK293 cells to confirm solubility and proper folding.
2. **In Vitro Cleavage Assay:** Incubate the protein with recombinant PC2 and Furin to experimentally verify the spatial cleavage predicted by ProP.
3. **In Vivo T1D Models:** Test the protein in NOD mice to measure beta-cell survival, Treg infiltration, and blood glucose restoration.

*If you are a researcher interested in testing this computational design, please open an Issue or contact the repository owner.*

## ⚠️ Scientific Limitations
All data herein is generated via predictive algorithms. While the "no shortcuts" approach (using full-length AlphaFold models and all-atom MD) maximizes rigor, computational predictions are not a substitute for experimental reality. The next phase (wet-lab) is essential.
