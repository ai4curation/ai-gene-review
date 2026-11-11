# SLC16A11 (horse, F6YMY3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted.

### Data and deep research
- `just fetch-gene HORSE F6YMY3 --alias SLC16A11` created the stub. It has 7 GOA rows: 2 IBA, 5 IEA.
- `just deep-research-falcon HORSE SLC16A11 --fallback perplexity-lite` failed. Falcon failed first, then the
  perplexity-lite fallback timed out at 600 s, so no deep-research file exists. The review uses the cached
  primary literature on the human ortholog together with my own sequence analysis.

### Identity / gene model
- F6YMY3 is unreviewed (PE 3), 614 aa. It is the product of the Ensembl canonical transcript
  ENSECAT00000025548 of gene ENSECAG00000023791. The same gene gives four other TrEMBL products;
  A0A9L0RBE3 (520 aa) is the most complete.
- PANTHER places it in PTHR11360:SF80 (MONOCARBOXYLATE TRANSPORTER 11), the same subfamily as human SLC16A11 Q8NCK7 and mouse Q5NC32
  [file:HORSE/SLC16A11/SLC16A11-uniprot.txt "PANTHER; PTHR11360:SF80; MONOCARBOXYLATE TRANSPORTER 11; 1."].
  This subfamily placement is the evolutionary basis for transferring function from human SLC16A11.
- Sequence comparison (SLC16A11-bioinformatics/RESULTS.md):
  - 86.5% identity to human over human residues 1-447.
  - A 73-aa disordered N-terminal extension, probably an upstream-initiation artefact. Human cDNAs carry the same kind of UniProt caution.
  - The region matching human TM12 (383-403) and the C-terminal tail is replaced by a divergent 127-aa segment.
  - A0A9L0RBE3 from the same gene keeps the conserved C-terminus, so F6YMY3 is an alternative or aberrant gene model, not the full-length product.
- PANTHER family folder `interpro/panther/PTHR11360/` holds only entries, metadata and PAINT files; there is no
  family review. Its entries list human and mouse SLC16A11 in SF80, which agrees with the UniProt cross-reference for F6YMY3.

### Literature (human ortholog)
- SIGMA 2014 [PMID:24390345 "V5-tagged SLC16A11 protein localizes to the endoplasmic reticulum."]. The protein is mostly in the ER,
  and overexpression raises intracellular TAG.
- Rusu et al. 2017 [PMID:28666119 "Consistent with our previous findings, the majority of SLC16A11REF-V5 is associated with intracellular membranes, with a portion (~5%) localized to the plasma membrane (Figure 3C)."].
  Human SLC16A11 transports pyruvate in an H+-coupled way. It interacts with BSG, and BSG promotes its cell-surface localization.
  T2D coding variants disrupt the BSG interaction.

### PAINT
- GO:0008028 IBD at PTN000888455 (taxon:6072, Eumetazoa). Its donors include human Q8NCK7.
- GO:0005886 IBD at PTN002260587.
- PTN002260587 also carries GO:0022857, which reached this gene only by InterPro2GO.
- PAINT did not propagate a pyruvate-specific term. I keep monocarboxylic acid transmembrane transporter activity as the
  MF level supported for the horse gene. Pyruvate is mentioned as the substrate shown for the human ortholog.

### Decisions
- MF GO:0008028 (IBA): ACCEPT, core.
- GO:0022857 (InterPro2GO IEA): MODIFY to GO:0008028.
- GO:0015718 (IEA): ACCEPT.
- GO:0055085: MODIFY to GO:1905039 carboxylic acid transmembrane transport. GO:1905039 is a descendant, verified by OLS ancestors of GO:1901475.
- Plasma membrane (IBA, IEA) and ER membrane (IEA): ACCEPT. Both are supported by the human ortholog data.
- No NEW terms. The hepatic lipid-metabolism phenotypes are downstream effects, not process participation.

### Relative
- Human SLC16A11 (Q8NCK7) is in the same PANTHER subfamily SF80 and is the experimental donor for the IBA rows.
- Horse has no reviewed (Swiss-Prot) SLC16A11 entry.
- No review of Q8NCK7 exists in the repo: no genes/human/SLC16A11, and no mouse Slc16a11.
- genes/EQUAS/SLC16A11 (donkey A0A9L0JV53) is the cohort partner.
