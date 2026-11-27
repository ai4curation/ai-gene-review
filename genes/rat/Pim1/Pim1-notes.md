# Pim1 (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Pim1` resolved to P26794 (PIM1_RAT, 313 aa); 72 GOA rows, none
  with a PMID (all IBA/IEA/ISS/ISO). The first fetch attempt timed out at UniProt;
  the retry succeeded.
- No deep-research provider keys; literature work recorded in
  `Pim1-deep-research-manual.md`.
- PMID:20097747 (requested key paper) is a rat myocardial-infarction study of a
  hyaluronan butyric/retinoic ester (HBR); it shows only that HBR induces pim-1
  transcription in rat cardiomyocytes and Stro-1 cells ["HBR enhanced the transcription
  of vascular endothelial growth factor, hepatocyte growth factor, kdr, akt, and
  pim-1."]. It is expression evidence and does not support any NEW process term.
- Only rat-specific functional evidence for the kinase: PMID:10373478 (abstract only),
  cited by UniProt P26794 for CDC25A phosphorylation/interaction ["Pim-1 physically
  interacts with Cdc25A both in vitro and in vivo and phosphorylates Cdc25A."].
- No NEW annotations proposed. Candidate terms considered and rejected:
  - response to retinoic acid / butyrate (from PMID:20097747): expression only.
  - mitochondrion localization (PMID:20203306): mouse hearts + overexpressed GFP-Pim-1
    in NRCM; fraction not checked for ER marker in the abstract; not added.
  - autophagy regulation (PMID:30257237): overexpression phenotype only.
- Isoform issue: human/mouse have a CUG-initiated 44 kDa isoform 2 that is
  membrane-associated and carries the BMX, ABCG2 and VDR (human isoform2 residues
  135-313, which are shared) findings. Rat P26794 lists no isoforms. Rows that rest
  solely on isoform 2-specific activities (tyrosine kinase activator activity) were
  marked over-annotated; plasma membrane and ABCG2 export kept as non-core pending
  confirmation that rat has the CUG isoform.
- Manganese ion binding marked over-annotated: Mg2+ is the curated cofactor.
