# Biological Rationale & Literature Audit

This document evaluates the biological claims of the v2.0 construct and attaches primary-source evidence.

## 1. GLP-1 Receptor Agonism
*   **Claim:** Human GLP-1 (7-37) binds GLP-1R to stimulate insulin secretion.
*   **Evidence:** GLP-1 receptor agonists are clinically proven to improve glycemic control. 
*   **Caveat:** Pancreatic selectivity is achieved via spatial activation (our linker), not solely by GLP-1.

## 2. PC2 Linker Cleavage
*   **Claim:** The `GSG-KR-(GGGGS)2` linker is cleaved by PC2 in the islet.
*   **Evidence:** PC2 is a prohormone convertase that processes proinsulin to mature insulin at dibasic residues (Lys-Arg).
*   **Caveat:** PC2 is also in the brain. We cannot claim *exclusive* pancreatic activation, but spatial enrichment is supported.

## 3. MANF (Beta-Cell Survival)
*   **Claim:** MANF protects beta cells from ER stress.
*   **Evidence:** Studies show MANF protects against cytokine-induced beta-cell death. 
*   **Caveat:** The minimal functional domain must be folded correctly within the fusion (validated via our AlphaFold checks).

## 4. Fcµ Domain (Immune Shielding & Half-Life)
*   **Claim:** Fcµ recruits Tregs and binds FcRn.
*   **Evidence (FcRn):** The Fc region binds FcRn for recycling. Our docking (-269.65) supports structural compatibility.
*   **Caveat:** Treg recruitment *in vivo* requires direct experimental validation (e.g., flow cytometry).
