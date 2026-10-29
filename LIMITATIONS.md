# Computational Limitations

## 1. AlphaFold Model Variance
- **Finding:** TM-align of Model 0 vs Model 1 yielded a TM-score of 0.514.
- **Impact:** The relative orientation of domains varies due to flexible linkers. Docking represents binding to one specific conformation.

## 2. Pharmacokinetics & Biodistribution
- **Finding:** HDOCK scores are structural predictions, not measures of half-life.
- **Impact:** Actual PK and biodistribution require animal models.

## 3. Protease Prediction Outages
- **Finding:** DeepCleave, PROSPER, and PiTou servers were offline.
- **Impact:** We relied on ProP and FindFur (HMMER3). While FindFur returned 0 hits, a wet-lab cleavage assay is required.

## 4. MD Simulation Length
- **Finding:** The MD simulation was 10 ns.
- **Impact:** This is a short timescale. It confirms local stability but does not establish long-term thermodynamic equilibrium.

## 5. B-Cell Immunogenicity of the Linker
- **Finding:** ElliPro analysis identified the `GGGGS` linkers as high-scoring linear B-cell epitopes (Score 0.889 and 0.587).
- **Impact:** Repeated `GGGGS` motifs are highly flexible and exposed, which makes them prone to generating Anti-Drug Antibodies (ADAs). This is a known limitation of GS-linkers in biologic drugs. Future iterations (v3.0) should replace the `GGGGS` linker with a less immunogenic alternative (e.g., XTEN or PAS linkers) if ADA formation becomes an issue in vivo.
