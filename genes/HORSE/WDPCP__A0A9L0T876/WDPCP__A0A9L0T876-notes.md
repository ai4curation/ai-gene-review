# WDPCP (horse, A0A9L0T876) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This review did not open or use any ProtNLM2 output. The folder is `WDPCP__A0A9L0T876` because the plain
`genes/HORSE/WDPCP` folder holds a different horse WDPCP entry (A0A3Q2KRK8) from the same Ensembl gene
(ENSECAG00000019956). A0A9L0T876 is the product of the Ensembl canonical transcript ENSECAT00000134648
(756 aa). Fetched with `just fetch-gene HORSE A0A9L0T876 --alias WDPCP__A0A9L0T876` (11 GOA rows).

**Deep research.** `just deep-research-falcon HORSE WDPCP__A0A9L0T876 --fallback perplexity-lite` failed:
Edison returned "Failed to authenticate" (HTTP 403 on /auth/login) and the perplexity-lite fallback also
failed. No deep-research file exists. The review relies on four cached full-text papers (PMID:24302887,
PMID:20671153, PMID:27158779, PMID:35427153), the human WDPCP review, the PTHR13667 PAINT table and a new
sequence analysis.

**Evolutionary grounding.**
- UniProt places A0A9L0T876 in PTHR13667:SF5, with human O95876, mouse Q8C456 and Xenopus Q32NR9.
- It is the horse WDPCP product that carries the IBA set from PAINT node PTN001007408 (taxon 6072,
  Eumetazoa): axonemal basal plate, cilium organization, nervous system development and establishment of
  protein localization. The node carries no plasma membrane, axoneme or phosphatidylinositol binding term.

**Sequence analysis** (WDPCP__A0A9L0T876-bioinformatics/RESULTS.md, analyze_canonical_model.py):
- A0A9L0T876 is identical to A0A9L0R7M2 (the model colinear with human and mouse at both ends) over
  residues 1-660. Its last 96 residues come from an alternative terminal exon that lies in an intron of the
  full-length transcript ENSECAT00000123939.
- It aligns colinearly with human WDPCP through human 692. It lacks human 693-746, which includes almost all
  of the PIP-binding last-60-residue tail mapped in mouse [PMID:35427153 "Wdpcp engages PIPs via the last
  60 C-terminal residues"] and the S708 ciliopathy residue.
- The divergence lies inside the C-terminal ~100 residues that are unresolved in the CPLANE cryo-EM maps
  [PMID:35427153 "we did not observe densities for the N-terminal ~300 residues of HsIntu/MmIntu"]. The
  propeller and solenoid are intact.

**Experimental status in horse.** No horse WDPCP product has any experimental data. Every function in the
review is inferred from mouse and Xenopus orthologs in SF5 through the PAINT node, and the review says so.

**Decisions.**
- Cilium organization, establishment of protein localization, axonemal basal plate (IBA + IEA): ACCEPT, core.
  WDPCP is the recruiting scaffold [PMID:24302887 "indicating Wdpcp is required for recruitment of proteins
  essential for ciliogenesis"].
- Axoneme (ARBA SubCell): ACCEPT, with independent mouse and Xenopus support.
- Plasma membrane (ARBA SubCell): MODIFY to cell cortex (lateral correction; no TM segment, cortical/actin
  localization of orthologs). Same as the A0A3Q2KRK8 review.
- Phosphatidylinositol binding (Ensembl Compara from mouse): REMOVE for this product, because the mapped
  binding tail is absent. The term probably applies to A0A9L0R7M2. It should not be transferred onward from
  A0A9L0T876.
- Nervous system development (IBA), embryonic digit morphogenesis, tongue morphogenesis, roof of mouth
  development (Compara from human IMP): KEEP_AS_NON_CORE. These are organismal outcomes of loss of the
  ciliary function, as in the human review. No NEW process terms were added.

**Note for transfer.** A0A9L0T876 is a poor reference for the C-terminal lipid-binding function. A0A9L0R7M2
is a better representative of the full-length horse protein.
