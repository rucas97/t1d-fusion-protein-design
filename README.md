# T1D Tri-Functional Fusion Protein Design

Computational design of a beta-cell-targeted fusion protein combining GLP-1R agonism (GLP-1), ER-stress protection (MANF), and Treg recruitment (Fcµ), connected by a beta-cell-optimized protease-responsive linker.

## Repository Structure
- `constructs/` — FASTA sequences of all designed versions (v1.0, v1.1, v2.0)
- `structures/` — 3D models (Phyre2 predictions, PEP-FOLD4 models, cleaned receptors)
- `validation/` — Raw outputs from ProP, IEDB, and HDOCK
- `notes/` — `DECISIONS.md` (the chronological lab notebook of design rationale)
- `manuscript/` — Drafts and figures for future publication

## Status
- [x] Research proposal drafted
- [x] v1.0 construct designed and assembled
- [x] v1.1 off-target Furin/PC2 cleavage patched
- [x] v2.0 Exendin-4 swapped for human GLP-1 (reduced immunogenicity)
- [x] 3D structural validation (Phyre2)
- [x] Linker cleavage validation (ProP)
- [x] Immunogenicity screening (IEDB)
- [ ] HDOCK Docking (Receptor-Ligand) - *In Progress*
