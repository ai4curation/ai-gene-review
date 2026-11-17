# PA4912 (Q9HUQ1) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUQ1 --alias PA4912`; accession matches the
worklist. Unreviewed TrEMBL entry; no gene symbol, so the locus tag is the folder
name. No deep-research provider was used. NCBI E-utilities and Europe PMC search
were unavailable during this session; the only paper on the gene found in the
cache and UniProt is the Johnson et al. 2008 screen (PMID:18833300, full text).

### Identity and literature

- LivH-type HAAT permease, nine predicted TM helices (UniProt FT TRANSMEM),
  PF02653 BPD_transp_2, PTHR11795:SF371.
- Operon PA4909-PA4913, paralogous to braCDEFG (PA1070-PA1074)
  [PMID:18833300 "Genes PA4910 and PA4912 comprise two genes of a five gene operon predicted to be involved in transport of branched chain amino acids."].
- Phenotype [PMID:18833300 "Disruption of PA4910 resulted in reduced utilization of D-Alanine (as a nitrogen source), while PA4912 mutants had disrupted D-Alanine and D-Valine utilization (Table 2)."].
  Table 2 gives D-Alanine N +/- and D-Valine N +/- for PA4912 (strain PAK); no
  L-amino acid phenotype was recorded, although every bra mutant showed L-Ala
  defects in the same screen.

### Decisions

- ACCEPT: plasma membrane (IBA, IEA), transmembrane transporter activity (IEA),
  transmembrane transport (IEA).
- TOO_GENERAL: membrane (IEA).
- MARK_AS_OVER_ANNOTATED: L-phenylalanine transporter activity, phenylalanine
  transport (IBA; E. coli binding-protein specificity), consistent with braD/braF.
- UNDECIDED: L-valine, L-isoleucine, L-leucine transporter activity, L-leucine
  import, L-valine transmembrane transport, L-isoleucine import, L-alanine
  transport (IBA; the substrate of this paralogous system is unknown and set by
  its own binding protein), D-alanine transmembrane transport (IBA, IMP).
- Counts: ACCEPT 4, TOO_GENERAL 1, MARK_AS_OVER_ANNOTATED 2, UNDECIDED 9.

## PseudoCAP IBA-seed assessment

Node-level assessment for both nodes was recorded in genes/PSEAE/braD/braD-notes.md
(braD, PA1073, is the co-seed); the verdicts below follow it.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000209860 | GO:0055085 transmembrane transport | 3 | 50 (15 taxa) | GO:0042941 D-alanine transmembrane transport, IMP, PMID:18833300 (PseudoCAP) | SOUND | For the generic node term, a permease mutant with a nutrient-utilisation defect is adequate, and the term suits a broad HAAT permease clade (includes urea permeases). | E. coli LivH (P0AEX7; IMP/IDA BCAA transport, EcoCyc), BraD (P21627; reconstituted LIV-I) | Yes |
| PTN000765102 | GO:0042941 D-alanine transmembrane transport | 2 (P21627, Q9HUQ1) | 18 (16 taxa) | GO:0042941, IMP, PMID:18833300 (PseudoCAP) | INDIRECT-PHENOTYPE | Partial D-Ala/D-Val nitrogen-source growth defect from one Biolog screen; no uptake or binding assay for either system. Plausible, not established. | BraD (P21627), same screen and same kind of phenotype | No independent support; both seeds are the same kind of weak phenotype from one screen |

No `source_defects` were recorded, consistent with braD: the D-alanine rows are
left UNDECIDED with a suggested question rather than filed as PseudoCAP or
GO_CENTRAL defects, because the claim is plausible and not refuted. If D-alanine
transport is later shown not to occur, the PTN000765102 D-alanine IBD would fall
with both seeds.
