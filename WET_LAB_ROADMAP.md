# Wet-Lab Roadmap: v9.0 Smart Bomb

This document outlines the exact experimental pipeline required to validate the v9.0 construct in vitro and in vivo.

## Phase 1: Expression, Purification & Quality Control
*   **1.1 Construct Design:** Clone the v9.0 gene into a mammalian expression vector (e.g., pcDNA3.4) with an N-terminal IgG1 signal peptide and a C-terminal His-tag.
*   **1.2 Expression:** Transfect into ExpiCHO-S cells. Cultivate for 7-10 days.
*   **1.3 Purification:** Harvest supernatant, filter, and purify using Ni-NTA affinity chromatography followed by Size Exclusion Chromatography (SEC).
*   **1.4 Quality Control (QC):** 
    *   Run SDS-PAGE to confirm purity (~50 kDa for intact drug).
    *   Use LC-MS to verify the N-glycosylation at the `NST` site in the linker.
    *   Endotoxin testing (must be < 0.1 EU/ug for in vivo use).

## Phase 2: Protease Cleavage & Stability Assays (In Vitro)
*   **2.1 Granzyme B Cleavage Assay:** Incubate v9.0 with recombinant human Granzyme B at 37°C. Run on SDS-PAGE at 0, 15, 30, and 60 minutes. 
    *   *Expected:* The 50 kDa intact band should disappear, and a 23 kDa payload band (GLP-1+MANF) should appear.
*   **2.2 DPP-4 Resistance Assay:** Incubate the cleaved payload with human DPP-4 for 24 hours. Run LC-MS.
    *   *Expected:* The A2G mutation should keep the GLP-1 arm intact (no cleavage).
*   **2.3 Serum Stability:** Incubate intact v9.0 in human serum at 37°C for 7 days. 
    *   *Expected:* The intact drug should remain stable (protected by the Fc tail).

## Phase 3: Functional Assays (Cell Culture)
*   **3.1 GLP-1R Activation (cAMP Assay):** Treat INS-1 cells (rat β-cells) with the cleaved payload. Measure intracellular cAMP levels via ELISA.
    *   *Expected:* Dose-dependent cAMP increase, proving the payload activates GLP-1R.
*   **3.2 Off-Target Specificity (GCGR Assay):** Treat GCGR-expressing cells with the cleaved payload. Measure cAMP.
    *   *Expected:* No significant cAMP increase, proving the drug does not activate the glucagon receptor.
*   **3.3 ER-Stress Protection (Apoptosis Assay):** Treat β-cells with Thapsigargin (to induce ER stress). Add the cleaved payload and measure cell viability (MTT assay) and apoptosis markers (Caspase-3).
    *   *Expected:* The MANF payload should rescue the cells from ER-stress-induced death.

## Phase 4: In Vivo Efficacy (Animal Models)
*   **4.1 Pharmacokinetics (PK):** Inject v9.0 into wild-type mice (IV). Measure blood concentration over 14 days to confirm FcRn recycling half-life.
*   **4.2 Efficacy in NOD Mice:** Treat early-stage diabetic NOD mice with v9.0 (weekly injections). Monitor blood glucose, insulin levels, and islet histology.
    *   *Expected:* Halt in β-cell destruction, preservation of insulin-producing islets, and prevention of hyperglycemia.
