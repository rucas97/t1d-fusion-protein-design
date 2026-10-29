# Independent Domain Analysis

To address the reviewer's request: *"Evaluate the MANF and immune-regulatory claims separately. Do not infer either effect from overall structural stability,"* we extracted the isolated MANF and Fcµ domains from the AlphaFold model and subjected them to independent FoldSeek analysis.

## 1. Isolated MANF Domain (Residues 47-204)
- **Tool:** FoldSeek (PDB100).
- **Result:** Top hit was `2w51` (Human mesencephalic astrocyte-derived neurotrophic factor) with a perfect structural alignment (Probability: 1.00, TM-score: 1.00, E-value: 1.06e-14).
- **Interpretation:** The MANF domain folds into the exact native human structure. 
- **Limitation:** Structural homology does not prove ER-stress protective function; it only proves the domain is structurally independent and not misfolded by the fusion architecture.

## 2. Isolated Fcµ Domain (Residues 220-672)
- **Tool:** FoldSeek (PDB100).
- **Result:** Top hits include `8bpf` ("FcMR binding at subunit Fcu1 of IgM pentamer", Human, E-value 7.62e-15) and `8gzn` (IgM-var2CSA complex, Human).
- **Interpretation:** The Fcµ domain folds perfectly into the native human IgM constant region structure.
- **Limitation:** Correct folding does not establish Treg recruitment or FcRn binding *in vivo*. It only proves the domain is structurally competent.

## Conclusion
Both domains fold independently of the flexible linkers. However, functional activity (ER-stress relief and immune modulation) requires wet-lab assays.
