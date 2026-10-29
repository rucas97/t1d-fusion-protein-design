# Computational Limitations

## 1. AlphaFold Model Variance
- **Finding:** Comparative alignment of AlphaFold models yielded a TM-score of 0.514 and RMSD of 6.81 Å.
- **Impact:** The relative orientation of the domains varies due to flexible linkers. Docking results represent binding to one specific plausible conformation.

## 2. Off-Target Docking
- **Finding:** The isolated GLP-1 peptide scored favorably against the Glucagon receptor (-285) due to shape homology.
- **Impact:** Rigid docking is blind to electrostatics. A wet-lab cAMP assay is required to definitively prove lack of cross-reactivity.

## 3. In Silico vs. In Vivo
- **Finding:** All data is generated via predictive algorithms.
- **Impact:** Computational predictions (docking scores, MD, immunogenicity) are not a substitute for experimental reality.

## 7. Critical Review: Fcµ Oligomerization
- **Finding:** The native IgM heavy chain forms pentamers/hexamers. We modeled the Fcµ domain as a monomer.
- **Impact:** The monomeric model does not account for avidity effects, receptor crosslinking, or steric clashes that would occur in a multimeric assembly. This is a major limitation of the current structural and docking predictions.

## 8. Critical Review: FcRn Recycling
- **Finding:** FcRn recycling is canonical for IgG, not IgM. 
- **Impact:** The predicted FcRn binding (-269.65) may not translate to an extended half-life in vivo for an IgM-derived construct.
