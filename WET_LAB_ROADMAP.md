# Wet-Lab Experimental Roadmap & Acceptance Criteria

This document outlines the experimental assays required to transition the v2.0 construct from *in silico* predictions to experimentally validated facts, directly addressing the scientific reviewer's requirements.

## Priority 1: Construct Identity & Product Architecture
*   **Assay:** Intact Mass Spectrometry & Peptide Mapping.
*   **Acceptance Criterion:** Mass matches the 75 kDa theoretical mass (minus signal peptide). Peptide mapping confirms the presence of the R587A mutation and correct domain boundaries. Disulfide mapping confirms the predicted Fcµ internal bonds.

## Priority 2: Proteolytic Processing (Spatial Activation)
*   **Assay:** In vitro cleavage assay with recombinant PC2 and Furin.
*   **Acceptance Criterion:** Incubation with Furin at pH 7.4 results in >90% intact protein (resistance). Incubation with PC2 at pH 5.5 results in specific cleavage at the KR motif, producing the expected GLP-1 and MANF-Fcµ fragments (confirmed by SDS-PAGE and Western blot).

## Priority 3: Mechanism Validation (Independent)
### 3a. GLP-1R Agonism
*   **Assay:** cAMP accumulation assay (HTRF) in GLP-1R expressing HEK293 cells.
*   **Acceptance Criterion:** Dose-dependent cAMP increase with an EC50 within 10-fold of native GLP-1 (7-37). No activation of Glucagon or GIP receptors (cross-reactivity test).
### 3b. MANF Function
*   **Assay:** ER-stress protection assay in INS-1E or human islet cells treated with Thapsigargin/cytokines.
*   **Acceptance Criterion:** >50% reduction in apoptosis (Caspase-3/7 activity) compared to untreated stressed cells.
### 3c. FcµR Binding (Immune Shielding)
*   **Assay:** Surface Plasmon Resonance (SPR) with immobilized human FcµR.
*   **Acceptance Criterion:** Measurable binding affinity (Kd) in the low micromolar to nanomolar range, confirming the HDOCK prediction.

## Priority 4: Pharmacokinetics & Biodistribution
*   **Assay:** PK study in wild-type mice (IV injection). Biodistribution via fluorescently labeled protein.
*   **Acceptance Criterion:** Serum half-life > 24 hours. Fluorescence detected in the pancreatic islets.

## Priority 5: Safety & Metabolic
*   **Assay:** Glucose tolerance test (GTT) and Insulin tolerance test (ITT) in STZ-diabetic mice. 
*   **Acceptance Criterion:** Restoration of glycemic control without inducing severe hypoglycemia (fasting glucose > 70 mg/dL).

## Priority 6: In Vivo Efficacy
*   **Assay:** NOD mouse model (spontaneous T1D).
*   **Acceptance Criterion:** Delay or prevention of diabetes onset. Histological analysis shows preserved beta-cell mass (insulin staining) and increased Treg infiltration (FoxP3 staining) in the islets.
