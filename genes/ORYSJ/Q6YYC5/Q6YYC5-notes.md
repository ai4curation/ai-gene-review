# Q6YYC5 (Os08g0135400) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No notes file existed before this session. ProtNLM2 prediction files were not opened or used.

### Identity
- Q6YYC5 is the full-length, single RAP gene model product of Os08g0135400 (401 aa, TrEMBL, sequence
  version 1; Gramene transcript Os08t0135400-01). It is not a fragment or isoform: it is the same
  length as its Arabidopsis ortholog AtRGLG4 (Q9SAL0, 401 aa) and carries the complete vWA (Pfam Copine
  PF07002 / SMART VWA) plus C-terminal RING (356-389) architecture. No other UniProt entry for this
  locus is canonical (secondary accession A0A0P0XBJ8 merged).

### Evolutionary placement
- PANTHER PTHR45751:SF16 "E3 UBIQUITIN-PROTEIN LIGASE RGLG4" (UniProt DR line). The family entries table
  (interpro/panther/PTHR45751/PTHR45751-entries.csv) places Q9SAL0 RGLG4 in SF16, RGLG1 Q9SS90 in SF15,
  RGLG2 Q9LY87 in SF29, RGLG5 Q8LB88 in SF30, and (oddly) RGLG3 Q8RX26 in SF11. So the SF16 ortholog is
  AtRGLG4.
- PAINT (PTHR45751-paint.tsv): node PTN002247669 carries IBD for GO:0004842 and GO:0005634 (seeds
  AT1G79380=RGLG4, AT3G01650=RGLG1, AT5G14420=RGLG2, AT5G63970=RGLG3) and GO:0016567 (seed RGLG1 only).
  Not propagated: plasma membrane (RGLG1/2 IDA, PMID:17586653) and K63-linked ubiquitination (RGLG1 IDA,
  PMID:17586653). Treated as deliberate curator decisions.
- Pairwise global identity to all five Arabidopsis RGLGs is ~54-60% (Q6YYC5-bioinformatics/RESULTS-rereview.md),
  so identity cannot pick the ortholog; the PANTHER subfamily does.

### Corrections to the previous review
- The prior file called AT1G79380/Q9SAL0 "RGLG1" in places; it is RGLG4.
- It said AtRGLG4 showed in vitro auto-ubiquitination; the PMID:27497447 abstract reports
  auto-ubiquitination for RGLG3 and GRXS17 ubiquitination with UBC30 ["GRXS17 is ubiquitinated and degraded
  in an RGLG3- and RGLG4-dependent manner in planta"].
- It claimed a myristoylation-compatible N-terminus implying plasma-membrane association. Q6YYC5 starts
  MGGVIG: position 6 is Gly, not the Ser/Thr of the N-myristoylation consensus (AtRGLG1 MGGGNS, AtRGLG2
  MGTGNS). Claim dropped.
- It treated the "Copine_C" InterPro hit as a separate calcium/membrane module. In RGLGs this is the
  copine-type vWA domain; there are no C2 domains, so no calcium-dependent phospholipid binding is inferred.
- Removed the reliance on ProtNLM2 in an annotation reason.

### Ortholog localization evidence
- PMID:25788731 (full text): "Confocal images showed that GFP-RGLG3 and GFP-RGLG4 were present in both the
  cytoplasm and nucleus"; fractionation: "FLAG-RGLG3 and FLAG-RGLG4 were detected in both fractions".
  This is the source of the AtRGLG4 IDA nucleus/cytoplasm rows that EnsemblPlants transferred.

### Decisions
- GO:0004842 (IBA, IEA): MODIFY -> GO:0061630 ubiquitin protein ligase activity (refinement).
- GO:0005634 nucleus (IBA, IEA): ACCEPT. GO:0005737 cytoplasm (IEA): ACCEPT.
- GO:0016567 protein ubiquitination (IBA): ACCEPT.
- No NEW terms. Jasmonate/FB1 cell-death phenotypes of rglg3 rglg4 are organismal phenotypes and were not
  transferred.

### Relative to review next
- AtRGLG4, Q9SAL0, ARATH, same PANTHER subfamily SF16; no review in the repo.
- No module in modules/ covers RGLG ligases (searched for RGLG/PTHR45751).
