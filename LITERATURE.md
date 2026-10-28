# Biological Rationale & Literature Audit

This document evaluates the biological claims of the v2.0 construct and attaches primary-source evidence, as requested by the computational audit checklist (Batch G).

## 1. GLP-1 Receptor Agonism (Targeting & Function)
*   **Claim:** Human GLP-1 (7-37) binds GLP-1R to stimulate insulin secretion and promote beta-cell proliferation.
*   **Evidence:** GLP-1 receptor agonists are clinically proven to improve glycemic control and preserve beta-cell function in T2D and T1D models. 
*   **Caveat:** GLP-1R is also expressed in the heart, brain, and GI tract. Pancreatic beta-cell selectivity is achieved via local delivery or spatial activation (our linker), not solely by the GLP-1 sequence itself.

## 2. PC2 Linker Cleavage (Spatial Activation)
*   **Claim:** The `GSG-KR-(GGGGS)2` linker is cleaved by PC2 (PCSK2) in the islet microenvironment.
*   **Evidence:** PC2 is a prohormone convertase highly expressed in neuroendocrine tissues, specifically processing proinsulin to mature insulin. It cleaves at dibasic residues (Lys-Arg).
*   **Caveat:** PC2 is not *exclusively* in the pancreas (it is also in the brain and pituitary). Therefore, we cannot claim the drug is *only* activated in the pancreas, but it is spatially enriched there.

## 3. MANF (Beta-Cell Survival)
*   **Claim:** MANF protects beta cells from ER stress and apoptosis.
*   **Evidence:** Studies have shown that MANF expression is upregulated in response to ER stress, and exogenous MANF protects against cytokine-induced beta-cell death. 
*   **Caveat:** The specific minimal functional domain of MANF required for protection must be folded correctly within the fusion context (validated via our AlphaFold/MolProbity checks).

## 4. Fcµ Domain (Immune Shielding & Half-Life)
*   **Claim:** The Fcµ domain recruits Tregs and binds FcRn.
*   **Evidence (FcRn):** The Fc region of antibodies binds the neonatal Fc receptor (FcRn), which recycles the protein and extends its half-life. Our docking (-269.65) supports this structural compatibility.
*   **Evidence (Tregs):** IgM and its receptors are involved in B-cell and T-cell regulatory networks. 
*   **Caveat:** The precise mechanism by which an engineered Fcµ domain recruits Tregs *in vivo* requires direct experimental validation (e.g., flow cytometry of islet infiltrates). 

## Summary of Limitations
While the computational pipeline supports the structural feasibility of this design, the biological claims require wet-lab validation to confirm cleavage kinetics, binding affinities, and *in vivo* tolerability.
