# FBXW7-AS1 / B0L3A2 (DEspR, "DEAR") — curation notes

Session 2026-10-08 (MICROPROTEINS Tier 4). Contested-peptide case: UniProt
B0L3A2 (DESPR_HUMAN, PE1, 85 aa, single TM) sits on the locus HGNC calls
`FBXW7-AS1`, "RNA, long non-coding", antisense to *FBXW7* exon 5.

## Locus and existence

- The ORF is interrupted at codon 14 by a `TGA` in the reference genome. UniProt
  records RNA editing as the resolution: "The nonsense codon (UGA) at position 14
  is modified to a sense codon (UGI), which is the equivalent of UGG. ADAR is
  responsible of FBXW7-AS1 expression and RNA-editing" (UniProt RNA EDITING, cited
  to PMID:33853558). The originating laboratory reports ADAR1 CRISPR knockout
  abolishing DEspR protein [PMID:33853558, "we show that ADAR1-dependent DEspR
  expression, via CRISPR/cas9-knockout studies"].
- Protein-level evidence is antibody-based: anti-DEspR mAb pull-down from isolated
  cell membranes gives a 17.5 kDa glycosylated band that shrinks after PNGase F,
  and this is explicitly *not* corroborated by mass spectrometry — "We note that
  although DEspR was detected consistently in denatured conditions via Western blot
  analysis of membrane protein pull-down products using 5g12e8 and 6g8g7 anti-DEspR
  mAbs, MS did not detect DEspR-specific peptides" [PMID:27301377]. The authors
  attribute non-detection to the known difficulty of small glycosylated single-TM
  proteins.
- Cell-surface presentation is reproducible across cell types and laboratories by
  flow cytometry: "To determine the cell surface expression of DEspR on circulating
  immune cells, we used flow cytometric analysis" [PMID:34789851 — Maine Medical
  Center, with the originating lab as co-authors], and "Blocking anti-DEspR murine
  precursor and humanized antibodies bind cell-surface DEspR, internalize, and
  co-translocate with gal1/gal3 nuclear shuttling proteins to the nucleus"
  [PMID:33853558].

So: the *locus* designation (lncRNA) and the *protein* entry (PE1) are in open
conflict, and the protein-existence evidence is antibody-only. Plasma-membrane
localisation is nevertheless the best-supported single claim about this entry.

## The receptor claim, and why it is contested

- Origin: a rat brain cDNA isolated by antisense-oligonucleotide screening under
  "molecular recognition theory", reported as a dual ET-1/angiotensin II receptor
  with "a single predicted transmembrane region with distinct ET-1 and AngII
  putative binding domains" and "ET-1- and AngII-induced coupling to a Ca2+
  mobilizing transduction system" [PMID:9508787].
- The angiotensin half did not hold outside Dahl S rats: "mouse Dear does not bind
  ANG II, similar" to Dahl R rat Dear [PMID:16293765], and UniProt carries a CAUTION
  to that effect. The ligand pair was reassigned to ET-1 plus the VEGF-A *signal
  peptide* (VEGFsp).
- Human evidence (PMID:24465725) is: anti-DEspR mAb staining of DEspR+ Cos1
  transfectants displaced by ligand — "7c5b2-immunostaining of DEspR+Cos1 cell
  transfectants was effectively blocked by the antigenic peptide and by ET1" — plus
  competition FACS with VEGFsp and ET1, and ligand-specific phosphoproteomics:
  "DEspR-mediated signaling activated phosphoproteins implicated in angiogenesis
  with some overlap with VEGF-VEGFR2 signaling pathways (FAK, PKCa, ERK1/2), but
  also distinct from VEGF-VEGFR2". The authors' own summary is deliberately modest:
  "Collectively, these findings support the functionality of VEGFsp- and ET1-binding
  to DEspR."
- The endothelin field has not taken the receptor up. Watts: "The pharmacology and
  physiology of DEAR has not been developed" [PMID:19907001]. Thorin & Clozel: "All
  these data come from one group of scientists, and the physiology and pharmacology
  of DEAR has not been studied in depth" [PMID:21081213]. The Davenport et al.
  IUPHAR review states "Current evidence only supports the existence of two
  subtypes, ETA and ETB, according to NC-IUPHAR nomenclature" and "No further
  Family A GPCRs have been identified that might bind ET peptides"
  [PMID:26956245] — note this is a statement about **Family A GPCRs**, so it is not
  a direct refutation of an 85-aa single-pass protein, but it shows the field does
  not count DEspR among ET receptors.

Per CLAUDE.md ("do not overrule curators from incomplete evidence") and the Tier 4
addendum on contested peptides, the experimental rows are not removed. They are
instead corrected where the **GO term definition** does not fit the protein, which
is an ontology question rather than a re-reading of the experiments:

- `GO:0004962 endothelin receptor activity` is defined as "Combining with endothelin
  and transmitting the signal across the membrane by activating an associated
  G-protein; promotes the exchange of GDP for GTP on the alpha subunit of a
  heterotrimeric G-protein complex" (QuickGO). No G-protein coupling has ever been
  shown for this 85-aa single-pass protein — the 1998 rat work showed Ca2+
  mobilisation, the 2014 human work phosphoproteomics. The ET-1-binding,
  signal-transmitting claim is better expressed by
  `GO:0004888 transmembrane signaling receptor activity` plus
  `GO:0017046 peptide hormone binding`.
- `GO:0086100 endothelin receptor signaling pathway` is likewise "A G
  protein-coupled receptor signaling pathway initiated by endothelin binding" →
  `GO:0007166 cell surface receptor signaling pathway`.
- `GO:0038085 vascular endothelial growth factor binding` is "Binding to a vascular
  endothelial growth factor". The reported ligand is the VEGF-A **signal peptide**,
  and UniProt states the protein "Does not bind the VEGFA mature protein". So the
  term overstates the claim; `GO:0005048 signal sequence receptor activity` (with
  `GO:0042277 peptide binding` as the generic fallback) matches what was assayed.
- `GO:0038084 vascular endothelial growth factor signaling pathway` requires VEGF
  binding its receptor; the paper's own phosphoproteomics is explicitly "distinct
  from VEGF-VEGFR2". → `GO:0007166`.

## Protein-binding row

The `GO:0005515` IPI row cites PMID:17446437 with EDN1 (P05305) and VEGFA (P15692)
as partners. That paper is a human SNP-haplotype association study — "Here we
report the association of human ATP1A1 (P<0.000005) and Dear (P<0.03)" with
hypertension — and the cached record is abstract-only. Bare protein binding carries
no functional information (CLAUDE.md), and the two ligand interactions it points at
are already covered by the ligand-binding rows, so the row is removed; removal does
not assert the interactions are false.

## No new annotations proposed

Mouse knockout lethality with "impaired angiogenesis, dysregulated neuroepithelial
development" [PMID:16293765] is a necessity phenotype in another species, with the
human protein's own existence contested; it does not pass CLAUDE.md's participation
test for a `NEW` angiogenesis process term, and no ISS row exists to review. Nothing
is proposed as NEW.

## Core function

One activity is recorded: a cell-surface, ET-1/VEGFsp-binding signalling receptor at
the plasma membrane, with the directionality and mechanism flagged as unresolved.
`protein binding` is not used.
