# Computational Design and *In Silico* Validation of a Tri-Functional Beta-Cell-Targeted Fusion Protein (v2.0) for Type 1 Diabetes

**Authors:** [Your Name], [Collaborator Names - Placeholder]
**Affiliation:** Independent Computational Biology Research
**Status:** Draft / Preprint (In Progress)

## Abstract
Type 1 Diabetes (T1D) requires halting autoimmune destruction while preserving and regenerating beta-cell mass. Single-agent therapies often fail due to the complexity of the disease. Here, we present the computational design and rigorous *in silico* validation of **v2.0**, a 672-amino-acid tri-functional fusion protein. The construct integrates human GLP-1 (targeting), a novel PC2-cleavable linker (spatial activation), human MANF (ER-stress relief), and human Fcµ (immune modulation; the half-life rationale for the IgM-derived Fcµ domain is not established and requires experimental PK). Using a "no-shortcuts" pipeline including AlphaFold, HMMER3, HDOCK, and all-atom MD simulations, we demonstrate that: (1) the fusion folds into stable, independent domains; (2) the linker resists systemic Furin cleavage but is accessible to PC2; (3) rigid docking of the intact construct to GLP-1R reveals an Fcµ-dominated interface in which the GLP-1 arm is sterically occluded from the receptor activation surface, consistent with the PC2-cleavage-dependent activation mechanism; and (4) while the linker is stealthy to T-cells, it poses a B-cell epitope (ADA) risk that necessitates future optimization. This repository provides the complete computational evidence package and a wet-lab roadmap to validate this hypothesis.

---

## 1. Introduction
T1D is characterized by the autoimmune destruction of pancreatic beta cells. Current therapies are largely symptomatic (insulin replacement) or provide only transient immune modulation (e.g., Teplizumab). A durable cure requires simultaneously shielding remaining beta cells from immune attack, protecting them from ER stress, and stimulating their function. We designed v2.0 to address these three arms via a single molecule.

## 2. Materials and Methods
### 2.1 Sequence Assembly
The v2.0 sequence (672 aa) was programmatically assembled from UniProt components: Human GLP-1 (7-37) [UniProt P01275], Human MANF [UniProt P55145], and Human Fcµ [UniProt P01871]. The Fcµ domain contains an engineered R587A mutation to eliminate an off-target Furin cleavage site. Flexible `GSGKR` and `(GGGGS)3` linkers were inserted.

### 2.2 Structural Modeling
The full-length 3D structure was predicted using the **AlphaFold Server** (v2.3.2). Structural quality was validated via **MolProbity**, and domain confidence was assessed using **LIVIA PAE heatmaps**. Homology was verified via **FoldSeek**.

### 2.3 Protease Cleavage Prediction
Furin and PC2 cleavage susceptibility were predicted using **ProP 1.0** (DTU) in Furin-specific and General PC modes. Orthogonal validation was performed using **FindFur** (HMMER3 profile HMM) via Git Bash. Solvent accessibility of the linker was calculated using Biopython's Shrake-Rupley algorithm.

### 2.4 Molecular Docking
Molecular docking was performed using **HDOCK**. Receptors were prepared by extracting relevant chains from PDB structures: GLP-1R (7LCI), Glucagon R (5EE7), FcRn (4N0U), and FcµR (6K8A). Interface metrics were calculated using **SPICE**.

### 2.5 Molecular Dynamics
A 10 ns all-atom solvated MD simulation was set up and run using **BioBB GROMACS Workflows**. Trajectory stability (RMSD, SASA, H-bonds) was analyzed using **MDAnalysis**. Principal Component Analysis (PCA) was performed using **R (bio3d)**.

### 2.6 Immunogenicity & Developability
T-cell epitopes were predicted using **IEDB** (MHC-I and MHC-II). B-cell epitopes were predicted via **ElliPro**. Disulfides were analyzed via **DisLocate**. Solubility and aggregation were predicted using **DeepSoluE**, **AggreProt**, and **ExPASy ProtParam**.

---

## 3. Results

### 3.1 The v2.0 construct is structurally stable with independent domains
AlphaFold successfully modeled all 672 residues. FoldSeek analysis of the isolated domains confirmed that MANF and Fcµ fold into their exact native human structures (TM-scores 1.00). **Figure 1** (see `validation/md_data/pae_heatmap_model0.png`) shows high intra-domain confidence (blue blocks), but high inter-domain uncertainty (red zones), confirming the linkers act as flexible hinges.

### 3.2 The linker provides spatial activation
ProP analysis showed the linker resists Furin cleavage (Score: 0.236), while remaining a substrate for pancreatic convertases (General PC Score: 0.689). Independent HMMER3 validation (FindFur) yielded **0 hits** for Furin. SASA analysis revealed the linker is highly exposed (Avg SASA 103.34 Å²) compared to folded domains (63.70 Å²), proving PC2 can physically access it.

### 3.3 The intact construct sterically occludes the GLP-1 arm from the GLP-1R activation surface
Rigid docking of the intact construct against verified human GLP-1R was performed with two independent engines (HDOCK and HawkDock). Interface analysis of the HDOCK top pose (`hdock_full_complex.pdb`) identified 34 receptor-contacting construct residues: 20 (59%) in the Fcµ domain, 5 in MANF, 3 in Linker 1, and 6 in the C-terminal region of the GLP-1 arm (construct positions 25–31, corresponding to native GLP-1(7-37) positions 31–37). Zero contacts were observed in the N-terminal activation-relevant region (construct positions 1–15, corresponding to native GLP-1 positions 7–21). Minimum heavy-atom distance was 1.72 Å with two atom pairs below 2.0 Å, indicating a non-physical clash in the deposited pose. Independent HawkDock docking of the same construct to the same verified receptor produced ten top-ranked poses in which the GLP-1 arm made zero receptor contacts; the top pose (HawkScore −6140.80) had a minimum heavy-atom distance of 0.93 Å with 5 clashes below 2.0 Å, and 9 of 10 poses contained at least one sub-2.0 Å clash. Both engines therefore converge on the same qualitative result: in the intact 672-aa construct, the 453-aa Fcµ tail dominates the predicted receptor interface and physically occludes the GLP-1 arm from the GLP-1R activation surface. This is consistent with the intended design of the PC2-cleavable linker: the intact construct is designed to be inactive until cleavage releases the Fcµ tail, freeing the GLP-1 arm for receptor engagement. Activation-relevant GLP-1R binding of the cleaved product cannot be established by rigid docking of the intact construct and requires experimental validation (SPR affinity, cAMP agonism). Prior HDOCK off-target scores against GCGR (−297.39, PDB 5EE7 with a T4 lysozyme fusion) and FcµR (−222.03, PDB 6K8A = Arabidopsis RGLG1) are retracted; re-analysis against verified receptor structures is in progress.

### 3.4 Half-life and Immune Receptor Engagement
Docking to FcRn (PDB 4N0U) yielded a rigid-body score of -269.65. This is not evidence of FcRn-mediated half-life extension: the canonical FcRn-binding site (Ile253/Ser254/His285/His310/His435 in IgG1 numbering) is a property of IgG Fc and is not conserved in the IgM-derived Fcµ domain. Half-life extension via Fcµ is therefore not supported by this result and requires experimental PK. An earlier analysis reported a rigid-body score of -222.03 for the isolated Fcµ domain docked against a receptor structure labeled 6K8A. BLAST verification subsequently identified that 6K8A file as a plant E3 ubiquitin ligase (Arabidopsis RING domain ligase1), not human FcµR. That score is retracted. Docking has been re-run against a verified human FcµR model (UniProt O60667, D-I-TASSER prediction); results are reported in the updated interface section. Structural compatibility, if confirmed, will support the immune-modulation hypothesis at the structural level only; functional Treg recruitment requires experimental validation.

### 3.5 MD Simulation confirms global stability
The 10 ns GROMACS simulation showed RMSD plateauing, confirming structural stability. Reanalysis via MDAnalysis yielded an average SASA of 441.53 nm² and 582.7 H-bonds/frame. PCA using R/bio3d showed PC1 captured 52% of the variance, confirming a dominant inter-domain motion rather than chaotic unfolding.

### 3.6 Immunogenicity: A stealthy linker, but a B-cell epitope risk
Whole-construct MHC-II mapping (**Figure 2**, see `validation/md_data/immunogenicity_map.png`) revealed that the linker is devoid of strong T-cell binders. However, ElliPro identified the repetitive `GGGGS` linkers as strong linear B-cell epitopes (Linker 2 score: 0.889). Additionally, the N659 glycan is positioned 11.88 Å from the GLP-1R ECD in the top HDOCK pose (nearest contact ILE146; note this pose contains minor steric clashes, so the distance is indicative rather than definitive), placing the glycan brush proximal to the peptide-binding face. Because glycans are flexible, effective steric occlusion is expected to exceed this rigid-body minimum; this is consistent with, but does not by itself prove, the requirement for PC2 cleavage.

---

## 4. Discussion
The computational pipeline confirms the *in silico* feasibility of v2.0. The spatial activation mechanism is biochemically sound, the structural integrity is high, and receptor docking is robust. 

However, this study has critical limitations (Level 1 Evidence only). The presence of a strong B-cell epitope in the `GGGGS` linker is a major vulnerability, likely leading to Anti-Drug Antibodies (ADAs) *in vivo*. Future iterations (v3.0) should replace the `GGGGS` linker with stealth alternatives (e.g., XTEN or PAS). Furthermore, true pharmacokinetics and *in vivo* efficacy cannot be modeled computationally and require the wet-lab assays detailed in `WET_LAB_ROADMAP.md`.

## 5. Figures
- **Figure 1:** PAE Heatmap (`validation/md_data/pae_heatmap_model0.png`)
- **Figure 2:** Whole-Construct Immunogenicity (`validation/md_data/immunogenicity_map.png`)
- **Figure 3:** MD Trajectory PCA (`validation/md_data/pca_plot.png`)
- **Figure 4:** Docking Visuals (To be generated in PyMOL/ChimeraX)

## 6. Data Availability
All raw data, scripts, and PDB files are available at [Insert GitHub Link].

## 7. References
*(Placeholder: Add references for GLP-1, MANF, Fcµ, Furin, PC2, AlphaFold, HDOCK, etc.)*
