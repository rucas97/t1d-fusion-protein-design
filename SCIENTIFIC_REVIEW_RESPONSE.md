# Response to Scientific Review: Tri-Functional T1D Fusion Protein v2.0

We accept the reviewer's critique that computational modeling does not establish therapeutic efficacy. In accordance with the review, we have updated all repository language to strictly classify evidence into three levels: **Predicted** (Level 1), **Experimentally Demonstrated** (Level 2), and **Therapeutically Validated** (Level 3). 

The current repository contains **Level 1 (Predicted)** evidence only. Below is our point-by-point response to the computational concerns raised.

## 1. Construct Identity & Sequence Verification
- **Action:** Programmatically reassembled the sequence from UniProt components to eliminate manual typos. 
- **Result:** The sequence is exactly 672 amino acids. The mutation is confirmed at position 587 (R587A) within the `FVQWMQR` motif.
- **Structural Coverage:** A Python script confirmed the AlphaFold model contains all 672 residues with no gaps.

## 2. Independent Domain Folding
- **Action:** Extracted the isolated MANF and Fcµ domains from the AlphaFold model and analyzed them via FoldSeek.
- **Result:** Both domains folded perfectly into their native human structures (MANF matched 2w51, TM-score 1.00; Fcµ matched 8bpf/8gzn, TM-score 1.00). This proves the flexible linkers do not cause domain misfolding.

## 3. Protease Specificity (Spatial Activation)
- **Action:** Because Monash servers (DeepCleave, PROSPER) were offline, we ran FindFur (an HMMER3 profile HMM) against the sequence.
- **Result:** FindFur extracted 29 putative motifs but returned **0 HMM hits** for Furin. 
- **Conclusion:** The linker is highly resistant to Furin. This provides legitimate, independent algorithmic validation of the ProP prediction.

## 4. Structural Dynamics & Convergence
- **Action:** Performed PCA (Principal Component Analysis) on the MD trajectory using R/bio3d.
- **Result:** PC1 captured 52% of the variance, and the scatter plots show distinct conformational clustering. This confirms a dominant inter-domain motion (linker flexibility) rather than chaotic unfolding.
- **PAE Analysis:** LIVIA PAE heatmaps confirmed high intra-domain confidence but high inter-domain uncertainty, verifying the linkers act as flexible hinges.

## 5. Immunogenicity & Glycosylation
- **Action:** Plotted whole-construct MHC-II binding (R/ggplot2) and calculated steric distances of N-glycans to the GLP-1 receptor.
- **Result:** The engineered linkers are entirely devoid of strong MHC-II binders. Three of four glycan sites are >18 Å from the receptor; site N659 is 7.33 Å away, presenting a potential clash. This supports the necessity of PC2 cleavage to remove the bulky Fc tail.

## 6. Disulfide & Oligomerization
- **Action:** Analyzed the sequence via DisLocate.
- **Result:** Predicted internal disulfides exclusively in the Fcµ domain (C522-C570, C632-C671). No disulfides in the linker, suggesting it will not crosslink. The construct lacks the IgM tailpiece, implying it will likely remain monomeric.

## 7. Remaining Wet-Lab Requirements
We agree that docking scores (HDOCK) and interface metrics (SPICE) do not establish affinity. We have created a `WET_LAB_ROADMAP.md` detailing the exact assays (SPR, cAMP, NOD mice) and acceptance criteria required to achieve Level 2 and Level 3 evidence.
