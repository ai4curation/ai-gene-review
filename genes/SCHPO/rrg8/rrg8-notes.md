# rrg8 (SPAC31G5.06, UniProt O14106) — curation notes

Journal of research for the AI GO-annotation review of the fission yeast gene **rrg8**.

## Identity

- **Systematic name:** SPAC31G5.06 (chromosome I, S. pombe strain 972 / ATCC 24843)
- **PomBase standard name:** `rrg8` ("Required for Respiratory Growth 8"). Note: the UniProt entry
  (O14106, entry `RGG8_SCHPO`) currently lists the gene name as `rgg8`; this is a lagging/variant
  spelling. PomBase (authoritative for S. pombe nomenclature) gives `rrg8`, product
  "mitochondrial tRNA 5'-end processing protein Rrg8"
  (PomBase API `dataset/latest/data/gene/SPAC31G5.06`, `name: "rrg8"`). This review uses `rrg8`.
- **UniProt accession:** O14106 (Swiss-Prot, but `PE 4: Predicted` — protein existence only predicted).
- **Length:** 234 aa; MW ~27.5 kDa. One low-complexity region (aa 209–225, per PomBase).
- **PomBase characterisation status:** "biological role inferred"; taxonomic distribution "fungi only";
  "predominantly single copy (one to one)".
- **S. cerevisiae ortholog:** YPR116W = **RRG8** (SGD:S000006320, UniProt Q06109), alias **MTA1**
  (PomBase `ortholog_annotations` → YPR116W, taxon 4932; SGD alias record).

## Domain / bioinformatic analysis (done inline)

- **No recognized domains or family signatures.** The UniProt record (cached
  `rrg8-uniprot.txt` and live `rest.uniprot.org/uniprotkb/O14106.txt`, checked 2026-07-06) has
  **no** InterPro / Pfam / PANTHER / PROSITE / SUPFAM / Gene3D / SMART / CDD cross-references, and
  `just fetch-gene` reported "No PANTHER family found". InterPro protein API returns no matched entries.
- **No FUNCTION comment** in UniProt; feature table lists only a single CHAIN (1..234) — no annotated
  TRANSIT peptide, signal peptide, transmembrane, or catalytic domain. (Absence of an annotated
  mitochondrial transit peptide does not exclude one; the record does not carry TargetP/MitoFates
  predictions and PomBase/orthology place the protein in mitochondria — see below.)
- **Conclusion from sequence:** rrg8 is a genuinely "dark" protein — no fold/domain/EC assignable
  from sequence, no derivable molecular function. This is consistent across S. pombe and its
  budding-yeast ortholog.

## What is KNOWN

### Mitochondrial localization and role in mitochondrial tRNA 5' processing (via ortholog, ISO)
The two functional GO annotations on rrg8 (GO:0005739 mitochondrion; GO:0097745 mitochondrial tRNA
5'-end processing) are **ISO** (`GO_REF:0000024`) transferred from the S. cerevisiae ortholog
RRG8/MTA1 (with/from `SGD:S000006320`), per PomBase annotation_details (ids 124631, 124632).

The budding-yeast ortholog is functionally characterised:
- SGD summary for YPR116W/RRG8/MTA1: "Protein of unknown function; required for efficient 5'
  processing of mitochondrial tRNAs, for respiratory growth and mitochondrial genome maintenance;
  ... localizes to the matrix side of the inner mitochondrial membrane" (SGD locus S000006320).
- [PMID:30759361 "5' processing of Saccharomyces cerevisiae mitochondrial tRNAs requires expression of multiple genes", "we identify four novel genes MTA1, MTA2, GEP5 and PET130 of the Saccharomycetaceae family that are necessary for an efficient processing of mitochondrial tRNAs"] — MTA1 = the RRG8 ortholog. Null mutants have severely reduced mt-tRNA levels; ts mutants accumulate pre-tRNA transcripts. [PMID:30759361 "Mta1p, Mta2p, Pet130p, and Gep5p are associated with the mitochondrial inner membrane and are all extracted and sediment in sucrose gradients as high molecular weight complexes, where they may be present in a common complex with Rpm2p"] and [PMID:30759361 "co-immunopurification of Rpm2 with Mta1p"]. Rpm2p is the protein subunit of yeast mitochondrial RNase P — the enzyme that carries out 5' pre-tRNA cleavage. So the ortholog is an **accessory factor associated with mitochondrial RNase P**, not the established catalytic component.
- [PMID:19751518 "identified ten previously uncharacterized genes essential for respiratory growth (RRG1 through RRG10)"] — this is the paper that named RRG8. Its Table 5 lists "RRG8 / YPR116w / Unknown function, GFP-tagged protein in mitochondria", with mitochondrial localization "+", and after cytoduction "Translation activity ... Absent" and "Nucleoids ... Altered", i.e. loss of RRG8 damages mitochondrial genome maintenance and mitochondrial protein synthesis.

### Essentiality / phenotype in S. pombe
- PomBase `deletion_viability: inviable`; single-locus phenotypes FYPO:0002061 "inviable vegetative
  cell population" and FYPO:0002111 "inviable tapered vegetative cell" (microscopy evidence,
  [PMID:23697806], [PMID:20473289]).
- Why essential in S. pombe but only respiratory-deficient (viable) in S. cerevisiae: fission yeast
  cannot survive loss of mtDNA. [PMID:20473289 "Loss of mtDNA is lethal in fission yeast but not in budding yeast where “petite” mutants lacking mtDNA are viable and mitochondrial translation is not essential"]. A mitochondrial-gene-expression factor is therefore expected to be essential in S. pombe even though its budding-yeast ortholog is a viable respiratory (pet) mutant — this cross-species pattern strengthens (rather than weakens) the mitochondrial functional assignment.

### Expression
- Detected at RNA and protein level; protein level increases during meiotic division
  ([PMID:39367033], meiotic proteomics; PomBase gene-expression annotations, ext during GO:0007127
  meiosis I / GO:0072690). [PMID:23101633] quantitative transcriptome/proteome, expression during
  quiescence (GO:0072690).

## What is NOT known (knowledge gaps — the primary deliverable)

1. **Molecular function is unknown.** No domain, no catalytic motif, no EC. Even in the
   better-studied budding-yeast ortholog the protein is "of unknown function". Its association with
   RNase P (co-IP with Rpm2p) suggests an accessory/scaffolding or assembly role in the mitochondrial
   RNase P holoenzyme, but no biochemical activity has been demonstrated. rrg8 is NOT shown to be the
   nuclease; GO:0097745 is a *process* (BP) annotation, not a molecular-function claim.
2. **Direct role of the S. pombe protein is inferred, not measured.** The mitochondrion and mt-tRNA
   5' processing annotations are ISO from S. cerevisiae; there is no direct S. pombe biochemistry or
   in-organello assay for rrg8 itself.
3. **Precise submitochondrial location and topology in S. pombe** are not established (ortholog is on
   the matrix side of the inner membrane).
4. **Whether rrg8 is a stable subunit of, or a transient assembly factor for, mitochondrial RNase P**
   is unresolved.

## Annotation review decisions (summary)

| Term | Evidence | Decision | Rationale |
|------|----------|----------|-----------|
| GO:0005739 mitochondrion (is_active_in, ISO from SGD) | ISO | ACCEPT (core CC) | Ortholog mitochondrial (inner membrane); PomBase curated this as the sole CC. |
| GO:0097745 mitochondrial tRNA 5'-end processing (involved_in, ISO) | ISO | ACCEPT (core BP) | Well-supported by ortholog genetics/biochemistry (PMID:30759361, 19751518). |
| GO:0003674 molecular_function (ND) | ND | ACCEPT | Honest "no data" for MF — matches the true knowledge gap; keep. |
| GO:0005737 cytoplasm (located_in, IEA GO_REF:0000044 / SubCell) | IEA | MARK_AS_OVER_ANNOTATED | From a C-terminally YFP-tagged high-throughput screen (PMID:16823372); a mitochondrial matrix-side inner-membrane protein. PomBase does not annotate cytoplasm. Broad/likely-artefactual for this protein. |
| GO:0005634 nucleus (located_in, IEA GO_REF:0000044 / SubCell) | IEA | MARK_AS_OVER_ANNOTATED | Same high-throughput dual cyto/nuclear call; inconsistent with orthology-based mitochondrial localization and not curated by PomBase. |

Note on the cytoplasm/nucleus calls: UniProt SubCellular Location cites the Matsuyama YFP ORFeome
screen (PMID:16823372). C-terminal fluorescent tags can disrupt or mask C-terminal / cleavable
mitochondrial targeting information, and high-throughput screens frequently produce cytosolic/nuclear
"leftover" signal for low-abundance organellar proteins. Per CLAUDE.md, IEA electronic inferences may
be argued against on biological grounds; these are not experimental annotations. I therefore flag them
as over-annotations rather than REMOVE.

## Deep research provenance note

The `deep_research_wrapper.py` (falcon → perplexity-lite fallback) was run twice in the foreground
(2026-07-06) and **hung with no output** (timed out at 200 s / 590 s, exit 124), producing no file.
Per project policy I did NOT fabricate a `-deep-research-*.md`. All assertions above are grounded in
the cached UniProt record, GOA TSV, PomBase and SGD REST APIs (authoritative ortholog annotation), and
cached primary publications (PMID:30759361, 19751518, 20473289, 23697806, 16823372, 39367033,
23101633), with verbatim quotes recorded inline.
