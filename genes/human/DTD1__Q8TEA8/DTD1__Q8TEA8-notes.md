# DTD1 (Q8TEA8, canonical human D-aminoacyl-tRNA deacylase 1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This folder holds the reviewed canonical product Q8TEA8 (209 aa, Swiss-Prot, Ensembl canonical
ENST00000377452). The existing `genes/human/DTD1/` folder belongs to the ProtNLM2 benchmark product
A0A2R8YCT7, which is a 127-aa translation of an NMD transcript. Following the alternative-product
convention, this folder is `DTD1__Q8TEA8` and was created with
`just fetch-gene human Q8TEA8 --alias DTD1__Q8TEA8`. No ProtNLM files or prediction-evidence folders
were opened.

### Deep research

`just deep-research-falcon human DTD1__Q8TEA8 --fallback perplexity-lite` failed. Falcon gave
"Failed to authenticate" and Perplexity returned HTTP 401 insufficient_quota, so no deep-research
file was produced. I worked from the cached primary literature, UniProt, QuickGO and PANTHER. For
orientation only, I read the gene-level falcon report in `genes/human/DTD1/` (generated for
A0A2R8YCT7 but describing the gene). It is not cited as evidence.

### Evolutionary grounding

- PANTHER (from `interpro/panther/PTHR10472/PTHR10472-entries.csv`): Q8TEA8 is in PTHR10472:SF5
  (D-AMINOACYL-TRNA DEACYLASE 1). The same subfamily contains mouse Dtd1 (Q9DD18), zebrafish dtd1
  (F1QGC8), Drosophila Dtd (Q9VGP0), yeast DTD1 (Q07648), P. falciparum DTD (Q8IIS0) and E. coli dtd
  (P0A6M4). DTD2/ATD (Q96FN9) is in a different subfamily, SF1.
- The IBA rows come from PTN000049487. For GO:0051500 the experimental donors are E. coli, yeast and
  Pf DTD, all in SF5. For GO:0006399 the donor list also includes DTD2 (SF1), so the node spans both
  subfamilies.
- PfDTD (Q8IIS0) has EXP/IDA for GO:0051499, GO:0051500 and GO:0106026, and an IDA for cytoplasm
  (QuickGO, 2026-10-21). PAINT propagated GO:0051500 and cytoplasm by IBA, but not GO:0106026
  Gly-tRNA(Ala) deacylase. The Gly-tRNA(Ala) evidence (PMID:28362257, 2017) may postdate the PAINT
  curation of this node. I treat the omission as a deliberate state of the phylogenetic assertion, so
  the GO:0106026 support recorded here is ortholog experiment (zebrafish, fly and Pf, all SF5) plus
  mechanism, not IBA.
- Human DTD1 keeps the SQFTL motif (residues 78-82) and the NDGPVT motif (137-142) with Gly139-Pro140,
  as seen in the UniProt sequence and the curated motif feature.
- The DTD2/ATD functions (Gly-transPro, L-Ala-tRNA(Thr) editing; PMID:29410408) belong to SF1 and
  are not transferred.

### What is experimentally established for human DTD1

- D-aminoacyl-tRNA deacylase activity of the purified N-terminal core [PMID:17264083 "core of DUE-B
  is shown to display both D-aminoacyl-tRNA deacylase activity and"]. ATPase activity was also
  reported in the same paper. Abstract only.
- Cellular protection against D-amino acids. Knockdown sensitizes HeLa cells to D-Tyr, D-Asp and
  D-Ser, and lowers tRNA(Tyr) and protein synthesis. The protein is enriched at the nuclear envelope
  [PMID:18700836 "found that h-DTD (human DTD) is enriched in the nuclear envelope region of"].
- Nuclear localization [PMID:15653697 "longer than its orthologs in yeast and worms and is primarily
  nuclear"].
- DNA binding in vitro through the disordered C-terminus [PMID:17264083].
- Leffak laboratory only: DUE binding at origins, interactions with Cdc45, TopBP1 and Treslin, the
  need for DTD1 in Cdc45 loading, and Cdc7/PP2A regulation (PMID:15653697, 20065034, 25258324,
  30037903). DUE-B does not complement fission yeast sld3 (PMID:22380713).
- Mitochondrion: high-throughput only (MitoCoP, PMID:34800366).

### Inferred, not measured, for human DTD1

- Gly-tRNA(Ala) deacylase activity, from SF5 orthologs including the vertebrate zebrafish dtd1
  (PMID:28362257).
- D-Tyr-tRNA(Tyr) specificity as such. It is supported by IBA and consistent with the tRNA(Tyr)
  cell data, but kinetics for the human enzyme are not in the cached abstracts.

### Decisions

- GO:0002161 (IEA) is MODIFIED to GO:0051499. GO:0006399 (IBA) is MODIFIED to GO:0106074. Both
  are correct but general, and the gene already carries the specific descendants.
- The deacylase MF rows (GO:0051499 x2, GO:0051500 IBA, GO:0106026 x2) and GO:0106074 are ACCEPT.
  The three cytoplasm rows and nucleus are ACCEPT.
- DNA binding (EXP) and mitochondrion (HTP) are KEEP_AS_NON_CORE.
- No NEW terms. I considered a DNA replication initiation process term and rejected it: the evidence
  comes from one laboratory, the activity is lineage-specific, and no comparator support was found.
  It is raised as a suggested question instead. The mouse synaptic and behavioural phenotypes
  (PMID:39428430) are downstream phenotypes and are not annotated.
- Validation: `just validate human DTD1__Q8TEA8`, `just validate-terms` and `just validate-references`
  all pass.
