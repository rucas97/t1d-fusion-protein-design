# Design Decision Log

Log **why** we made each key choice, not just what we chose.
This becomes the "Methods rationale" section of the manuscript.

## Format
### YYYY-MM-DD — [Short decision title]
- **Decision:** What was chosen.
- **Alternatives considered:** What else was on the table.
- **Rationale:** Why this one won.
- **References:** Supporting literature (if any).

---

### 2025-XX-XX — Initial hypothesis locked
- **Decision:** Adopt the Exendin-4 – linker – MANF – linker – Fcµ architecture.
- **Alternatives considered:** De novo ZnT8 binder; Harmine + Exendin-4 dual-agent.
- **Rationale:** De novo binder design is computationally heavy for a $0 budget
  with limited GPU access; Exendin-4 gives us a validated targeting arm plus
  GLP-1R agonism in one module. Harmine is a small molecule, not a protein,
  so it doesn't fit a single-molecule fusion design.
- **References:** (to be added from PubMed)

### 2025-XX-XX — Linker design strategy: PC2-cleavable chimeric linker
- **Decision:** Adopt a chimeric linker with a central PC2 cleavage motif (KR) flanked by flexible glycine-serine spacers. Candidate 1: `GSG-KR-(GGGGS)2`.
- **Alternatives considered:** (1) Generic (GGGGS)3 (non-cleavable baseline). (2) Other protease motifs (furin, MMP). (3) Rigid linkers (EAAAK)n.
- **Rationale:** PC2 is enriched in pancreatic islets and beta cells, providing a spatial activation signal. The flexible GS spacers ensure protease accessibility and independent domain folding. This design is novel for T1D fusion proteins and directly addresses the "islet-specific biology" gap.
- **References:** PC2 specificity (K-R↓) and islet expression [0†L28-L35, 7†L19-L24]. Linker flexibility and protease access [8†L28-L48].

### 2025-XX-XX — ProP validation of PC2-cleavable linker (Candidate 1, corrected)
- **Tool:** ProP 1.0b (DTU Health Tech), General PC prediction mode
- **Input:** Full fusion sequence: Exendin-4 – GSG-KR-(GGGGS)2 – mature human MANF (UniProt P55145, residues 25–182) – (Fcµ placeholder pending)
- **Result:**
  - Intended KR site (pos 44, `PSGSGKR|GG`): score **0.871**, predicted cleavage ✅
  - Highest non-intended site (pos 172, `RVKELKK|IL`): score **0.193**, NOT predicted
  - All other Arg/Lys sites: score < 0.16, not predicted
- **Interpretation:** The designed KR motif is a strong predicted substrate for proprotein convertases. The authentic mature MANF sequence introduces no additional predicted cleavage sites. The linker concept passes this validation step.
- **Caveat:** Fcµ domain not yet included in the construct; this validation covers the N-terminal half only. Will re-run once the full fusion is assembled.
- **Sequence source:** UniProt P55145 (MANF_HUMAN, SV=3), mature chain residues 25–182.

### 2025-XX-XX — Immunogenicity screening (IEDB MHC-II)
- **Tool:** IEDB MHC-II Binding Prediction (NetMHCIIpan 4.1 EL)
- **Alleles:** Human 7-Allele Panel
- **Input:** Exendin-4 - GSG-KR-(GGGGS)2 - MANF
- **Results:**
  - **Novel Linker:** Best binding percentile was 79% (very low risk). The PC2 linker is predicted to be non-immunogenic.
  - **MANF Domain:** A few moderate binders (percentile ~0.5-1%), consistent with a human self-protein.
  - **Exendin-4 Domain:** Strong binders found (percentile 0.08% - 0.4%). This is expected, as Exendin-4 is a non-human (Gila monster) sequence.
- **Decision:** To minimize long-term ADA (Anti-Drug Antibody) risk, we must swap Exendin-4 for a human GLP-1 receptor agonist sequence (e.g., human GLP-1 7-37) in the next design iteration.
