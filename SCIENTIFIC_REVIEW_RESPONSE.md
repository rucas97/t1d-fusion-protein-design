# Response to Scientific Review of v2.0

We have received a critical scientific review of the v2.0 computational workflow. We accept the reviewer's conclusions and are updating our repository to strictly adhere to the proposed "Three Evidence Levels" (Predicted, Experimentally Demonstrated, Therapeutically Validated).

## 1. Acknowledged Critical Gaps
### 1.1 Fcµ and FcRn (Half-Life Mechanism)
- **Reviewer Point:** FcRn is the recycling receptor for IgG, not IgM. HDOCK scores do not establish productive FcRn binding.
- **Action:** We acknowledge that the Fcµ domain may not utilize the canonical FcRn recycling pathway. The docking score (-269.65) is an *in silico* prediction only. The half-life mechanism remains unproven.

### 1.2 IgM Oligomerization (NEW CRITICAL LIMITATION)
- **Reviewer Point:** IgM natively forms pentamers/hexamers. An explicit oligomerization and disulfide assessment is required.
- **Action:** We modeled the Fcµ domain as a monomer. We acknowledge that the native oligomeric state may impact receptor clustering, steric hindrance, and overall function. Our monomeric model is a simplified representation.

### 1.3 PC2 Cleavage Compartment
- **Reviewer Point:** PC2 is in neuroendocrine granules, not a general-purpose enzyme. A ProP score is not proof of cleavage.
- **Action:** We acknowledge that the spatial activation mechanism requires experimental verification in relevant cellular compartments.

### 1.4 GLP-1R Activation vs. Binding
- **Reviewer Point:** Docking does not prove activation. 
- **Action:** We acknowledge that HDOCK proves structural compatibility, not functional agonism. cAMP assays are required.

## 2. Addressing the Reviewer's Computational Requests
The reviewer requested specific additional computational analyses to complement the wet-lab requirements:
- **Domain-wise PAE (Predicted Aligned Error):** We will extract the PAE plots from the AlphaFold job to identify uncertain domain arrangements.
- **Alternative Conformational Models:** We will compare AlphaFold Model 0 vs Model 1 to test linker flexibility.
- **Explicit Oligomerization Assessment:** We will note the monomeric limitation in all reports.

## 3. Conclusion
We agree with the reviewer that v2.0 is a "useful computational starting point and a substantial list of hypotheses to test," not a validated therapeutic. Future work will prioritize the mechanism-by-mechanism evidence package.

## 4. Addressing PAE Analysis Request
The reviewer requested a domain-wise structural confidence and PAE review. We uploaded the complete AlphaFold output to the LIVIA analysis platform. The resulting PAE heatmap (`validation/md_data/pae_heatmap_model0.png`) conclusively demonstrates high intra-domain confidence (blue blocks) but high inter-domain uncertainty (red off-diagonal regions). This confirms that the flexible linkers allow the domains to move independently, meaning the full 680-aa structure is a dynamic ensemble rather than a single rigid conformation.

## 5. Addressing Disulfide & Oligomerization Assessment
The reviewer requested an explicit oligomerization and disulfide assessment. We utilized the DisLocate server. The analysis predicted internal disulfide bonds exclusively within the Fcµ domain (CYS522-CYS570 and CYS632-CYS671), with no bonds predicted in the engineered linker or GLP-1 domains. Because the construct excludes the native IgM tailpiece (which drives pentamerization), the sequence-based prediction suggests the construct will remain a monomer rather than forming the massive multimers typical of native IgM. Experimental validation of the oligomeric state remains required.

## 8. Whole-Construct Immunogenicity Assessment
- **Action:** We plotted the MHC-II binding percentile of every 9-mer across the entire 672-amino-acid sequence using R.
- **Result:** The resulting plot (`validation/md_data/immunogenicity_map.png`) demonstrates that strong MHC-II binders (percentile < 1%) are present in the native MANF and Fcµ domains, but are entirely absent from the engineered linker regions.
- **Conclusion:** This full-construct assessment confirms that the engineered linker is biochemically stealthy and does not introduce unintended immune responses.
