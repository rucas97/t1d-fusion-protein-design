# T1D Tri-Functional Fusion Protein Design

Computational design of a beta-cell-targeted fusion protein for Type 1 Diabetes, combining GLP-1R agonism, ER-stress protection (MANF), and Treg recruitment (Fcµ), connected by a beta-cell-optimized protease-responsive linker.

## 🧬 Biological Rationale
Type 1 Diabetes (T1D) requires both immune tolerance and beta-cell regeneration. Single-agent therapies fail because they address only one arm of the disease. This design proposes a single molecule that acts as a "Smart First Responder":
1. **Targeting & Function (GLP-1):** Binds GLP-1R on remaining beta cells to stimulate glucose-dependent insulin secretion and promote proliferation.
2. **Regeneration (MANF):** Relieves ER-stress inside the beta cell, preventing inflammation-induced apoptosis and preserving cell mass.
3. **Immune Shielding (Fcµ):** Recruits Regulatory T-cells (Tregs) locally to suppress the autoreactive immune attack.
4. **Spatial Activation (Novel Linker):** The linker is specifically cleaved by PC2 (an enzyme enriched in pancreatic islets). This ensures the drug is stable in the bloodstream (resists Furin cleavage) and activates only at the target site.

## 📊 Validation Status (Dry-Lab Complete)
- [x] **Sequence Engineering:** Assembled v2.0 construct (Humanized GLP-1 - PC2 Linker - MANF - Fcµ_R595A).
- [x] **Structural Folding:** Phyre2 homology model confirms 93% of residues fold correctly (domains intact).
- [x] **Protease Specificity:** ProP confirms the linker is PC2-specific (score 0.87) and resists systemic Furin cleavage (score 0.23).
- [x] **Immunogenicity:** IEDB confirms the linker and junctions are highly stealthy. Exendin-4 was swapped for human GLP-1 to eliminate ADA risks.
- [x] **Receptor Docking:** HDOCK confirms the GLP-1 domain strongly binds GLP-1R (Score: -276.36).
- [x] **Dynamics:** CABS-flex confirms linker flexibility without disrupting domain folding.

## 🤝 Call for Collaboration (Wet-Lab Validation)
This repository contains a fully validated *in silico* hypothesis. To take the next step, we are seeking a wet-lab collaborator to perform:
1. **Gene Synthesis & Expression:** Synthesize the v2.0 construct (FASTA provided) and express it in CHO or HEK293 cells to check for solubility and correct folding.
2. **In Vitro Cleavage Assay:** Incubate the purified protein with recombinant PC2 and Furin to experimentally verify the specific spatial cleavage predicted by ProP.
3. **In Vivo T1D Models:** Test the protein in NOD mice (or STZ-induced diabetic mice) to measure beta-cell survival, Treg infiltration, and blood glucose restoration.

*If you are a researcher interested in testing this computationally validated design, please open an Issue or contact the repository owner.*

## Repository Structure
- `constructs/` — FASTA sequences of all designed versions.
- `structures/` — 3D models (Phyre2 predictions, PEP-FOLD4 models, HDOCK complexes).
- `validation/` — Raw outputs from ProP, IEDB, and HDOCK.
- `notes/` — `DECISIONS.md` (the chronological lab notebook of design rationale).
