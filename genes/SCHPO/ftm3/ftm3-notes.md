# ftm3 (SPAC750.04c) — curation notes

UniProt: **P0CU06** (secondary AC Q9P332), entry name `YLZ4_SCHPO`.
PomBase: **SPAC750.04c**, standard name **ftm3**.
Taxon: *Schizosaccharomyces pombe* (strain 972 / ATCC 24843), NCBITaxon:284812.

## Summary of identity (KNOWN)

- **146 aa**, MW ~17.2 kDa. RecName in UniProt: "UPF0742 protein SPAC750.04c".
- PomBase product description: **"sub-telomeric 5Tm protein family Ftm3"**; characterisation
  status **"conserved unknown"** (from PomBase gene page / API).
- Domain content: Pfam **PF09437 (Pombe_5TM, "Pombe specific 5TM protein")**, matched **twice**
  in the sequence per the UniProt record (`Pfam; PF09437; 2`); InterPro **IPR018291
  ("5TM-prot_SCHPO")**. UniProt SIMILARITY: "Belongs to the **UPF0742 family**."
  [UniProt P0CU06 record: `DR Pfam; PF09437; Pombe_5TM; 2.`; `CC -!- SIMILARITY: Belongs to the UPF0742 family.`]
- UniProt annotates a single TMHMM-predicted transmembrane helix (TRANSMEM 38..60, ECO:0000255),
  despite the family being called "5TM" — the "5TM" is the family/Pfam name, not a per-protein
  UniProt feature count here.
- Genomic context: chromosome I, sub-telomeric region; part of a telomeric segmental duplication.
  Paralogs in the Ftm family: **ftm1 (SPAC977.01), ftm2 (SPAC977.02), ftm4 (SPAC750.05c),
  ftm5, ftm6, ftm7** (PomBase). Also related: SPBPB2B2.17c (UPF0742).
  [PomBase gene page SPAC750.04c: "Has paralogs: ftm4, ftm1, ftm2, ftm5, ftm6, ftm7"]

## Localization evidence (KNOWN, by homology only for ftm3 itself)

- UniProt SUBCELLULAR LOCATION for ftm3/P0CU06: "Cytoplasm {ECO:0000250|UniProtKB:P0CU07}.
  Nucleus membrane {ECO:0000250|UniProtKB:P0CU07}; Single-pass membrane protein {ECO:0000305}.
  Note=Localizes to cytoplasmic dots and the nuclear envelope. {ECO:0000250|UniProtKB:P0CU07}."
  — i.e. ftm3's own localization is **inferred by similarity (ISS/ECO:0000250) from the paralog
  P0CU07 = ftm2 (SPAC977.02)**, not measured directly on ftm3.
- The paralog **ftm2/P0CU07/SPAC977.02** has **experimental** localization to cytoplasm and
  nuclear/nucleus membrane from the genome-wide YFP ORFeome localization study
  **PMID:16823372** (Matsuyama et al. 2006, "ORFeome cloning and global analysis of protein
  localization in the fission yeast Schizosaccharomyces pombe", ECO:0000269|PubMed:16823372
  on the P0CU07 record). The GOA ISS annotations on ftm3 carry `with: UniProtKB:P0CU07`
  (QuickGO TSV) / `with: SPAC977.02 (ftm2)` (PomBase) — same source, family transfer.
- The two GOA IEA CC annotations (GO:0005737 cytoplasm, GO:0031965 nuclear membrane;
  GO_REF:0000044, UniProtKB-SubCell mapping) are electronic re-statements of the same
  UniProt SubCell locations, so they are consistent with — and derivative of — the ISS calls.

## Expression / process context (KNOWN, high-throughput only)

- PomBase carries a biological-process annotation **GO:0042149 "cellular response to glucose
  starvation"** for ftm3, evidence **ECO:0000058 (expression microarray/RNA-level)**, reference
  **PMID:34460892** (Tarhan & Çakır 2021, "Transcriptome sequencing and screening of genes
  related to glucose availability in Schizosaccharomyces pombe by RNA-seq analysis"), qualified
  as "RNA level decreased." This is a **transcript-abundance response**, not a demonstrated
  functional role in the glucose-starvation program; the full text does not name ftm3.
- **This GO:0042149 annotation is NOT in the QuickGO GOA TSV pulled for this review** (the TSV
  contains only the two CC IEA, two CC ISS, and the ND MF/BP placeholders). Since the review
  covers the GOA set, it is not added to `existing_annotations`; it is recorded here as context.
- ftm2 deletion (ftm2delta) is viable with normal cell morphology under standard conditions
  (PomBase phenotype), consistent with the family being dispensable/redundant. No ftm3-specific
  deletion phenotype is documented.

## NOT known (knowledge gaps)

- **Molecular function**: unknown. No enzymatic activity, no ligand/substrate, no binding partner
  is established. Pfam PF09437 (Pombe_5TM / UPF0742) has **no functional annotation** and is
  essentially *Schizosaccharomyces*-restricted ("Pombe specific"), so no cross-kingdom orthology
  informs function. PomBase MF = ND (GO_REF:0000015).
- **Biological process**: unknown beyond the transcriptional glucose-availability response above;
  PomBase BP = ND in GOA. No pathway membership demonstrated.
- **Role of sub-telomeric location / family expansion**: unknown; whether the Ftm family has a
  coherent shared function (e.g. in a membrane process) or represents rapidly-evolving
  sub-telomeric genes of low/conditional function is not established.
- **Topology / true TM count**: family is named "5TM" but the UniProt feature table on ftm3
  lists only one predicted TM helix; membrane topology is not experimentally determined.

## Curation decisions (rationale)

- **GO:0005737 cytoplasm (ISS, GO_REF:0000024, with P0CU07)** and **GO:0031965 nuclear membrane
  (ISS)**: KEEP_AS_NON_CORE. Grounded in experimental localization of the paralog ftm2 via a
  reliable genome-wide study; a defensible localization call for an otherwise uncharacterized
  protein, but localization is not a "core function" and is by-similarity for ftm3 itself.
- **GO:0005737 cytoplasm (IEA, GO_REF:0000044)** and **GO:0031965 nuclear membrane (IEA)**:
  KEEP_AS_NON_CORE. Electronic SubCell->GO restatements of the same UniProt locations; redundant
  with the ISS calls but not wrong.
- **GO:0003674 molecular_function (ND, GO_REF:0000015)** and **GO:0008150 biological_process
  (ND)**: ACCEPT. ND placeholders correctly record that MF/BP are unknown; keeping them is the
  honest representation for a "conserved unknown" gene.
- No `protein binding` or speculative MF/BP terms are proposed. `core_functions` is intentionally
  minimal (localization only, non-core); `knowledge_gaps` carries the primary content.

## Provenance of sources used

- UniProt P0CU06 record (`genes/SCHPO/ftm3/ftm3-uniprot.txt`) — domains, TM, subcell, family.
- QuickGO GOA TSV (`genes/SCHPO/ftm3/ftm3-goa.tsv`) — the 6 reviewed annotations.
- PomBase gene pages/API for SPAC750.04c (ftm3) and SPAC977.02 (ftm2) — standard name, product
  description, characterisation status "conserved unknown", paralog list, GO:0042149.
- UniProt P0CU07 record (rest.uniprot.org) — paralog ftm2 experimental localization (PMID:16823372).
- PMID:16823372 (cached, abstract-only) — genome-wide localization study underlying the ISS.
- PMID:34460892 (cached, full text) — glucose-availability RNA-seq behind GO:0042149 context.
- Pfam/InterPro PF09437 / IPR018291 — "Pombe specific 5TM protein", no functional annotation.

Deep research: falcon and perplexity-lite both failed (falcon template-variable error;
perplexity 401 quota). Review grounded in UniProt + GOA + PomBase + cached literature per
CLAUDE.md fallback guidance; no fabricated content.
