# PFAS (O15067) — review notes

## Identity and function

- **Gene/protein**: PFAS = phosphoribosylformylglycinamidine synthase (FGAM synthase; FGAMS);
  also called formylglycinamide ribonucleotide amidotransferase (FGAR-AT / FGARAT). UniProt
  `PUR4_HUMAN`, O15067. HGNC:8863. EC 6.3.5.3.
- **Reaction (RHEA:17129)**: N2-formyl-N1-(5-phospho-β-D-ribosyl)glycinamide (FGAR) + L-glutamine
  + ATP + H2O → 2-formamido-N1-(5-O-phospho-β-D-ribosyl)acetamidine (FGAM) + L-glutamate + ADP +
  phosphate + H+.
- **Pathway**: fourth step of de novo purine synthesis (DNPS); IMP biosynthesis via de novo pathway.
  [PMID:10548741 "phosphoribosylformylglycineamide amidotransferase (FGARAT) gene, which encodes the
  fourth step of this pathway"]. Deep research (falcon) unavailable — HTTP 402, out of credits.
- **Domain architecture (UniProt)**: N-terminal FGAR-AT / PurL synthetase region (ATP-binding,
  Mg2+-binding) + C-terminal class-I glutamine amidotransferase (GATase-1) domain (residues
  1064–1302; catalytic Cys1158 nucleophile). Glutamine amidotransferase keyword.
- **Localization**: cytoplasm/cytosol [UniProt SUBCELLULAR LOCATION: Cytoplasm; Reactome R-HSA-73812
  "the enzyme is cytosolic"]. Also detected in B-cell exosome proteome (HDA, PMID:20458337) as one of
  539 proteins — non-specific mass-spec catalog, not a functional localization.
- **Biology**: houses-keeping DNPS enzyme; a component of the purinosome (multi-enzyme DNPS complex).
  No well-established Mendelian disease; of interest in cancer metabolism / nucleotide demand.

## Publications (all abstract-only in cache)

- **PMID:10548741** (Patterson et al., Gene 1999): cloned the human FGARAT cDNA/genomic clone;
  P1 clone complements purine-auxotroph AdeB CHO mutants deficient in FGARAT activity+protein;
  maps to 17p13. Source of the IDA MF (`enables GO:0004642`) and NAS BP (`de novo IMP`) annotations.
- **PMID:27590927** (Baresova et al., Mol Genet Metab 2016): CRISPR-Cas9 knockouts of individual DNPS
  enzymes in HeLa; substrate accumulation and impaired purinosome assembly. Source of MGI IMP/IDA
  annotations. Abstract frames DNPS ("ten reactions catalysed by six enzymes") without naming PFAS;
  full text (not cached) assays the FGAR-AT step. Per curation policy, defer to MGI curator.
- **PMID:20458337** (Buschow et al., Immunol Cell Biol 2010): B-cell exosome MS proteome, 539 proteins;
  source of HDA extracellular-exosome CC.

## Annotation decisions (summary)

Core: MF GO:0004642 (FGAM synthase activity); BP GO:0006189 (de novo IMP biosynthesis) and
GO:0006164 (purine nucleotide biosynthetic process); CC GO:0005829 (cytosol).

- `GO:0004642` MF (IBA, IEA, TAS x1, IMP, IDA x2): ACCEPT — well-supported core MF.
- `GO:0005737` cytoplasm (IBA, IEA): ACCEPT.
- `GO:0005829` cytosol (TAS Reactome): ACCEPT — most specific correct CC.
- `GO:0006189` de novo IMP (IBA-absent; IEA, IMP, IDA, NAS): ACCEPT core BP.
- `GO:0006164` purine nucleotide biosynthetic process (IBA): ACCEPT (broader parent, correct).
- `GO:0006541` L-glutamine metabolic process (IEA, Ensembl ortholog): KEEP_AS_NON_CORE — true
  (glutamine is the amide donor) but a side/co-substrate process, not the core purine-synthesis role.
- `GO:0009410` response to xenobiotic stimulus (IEA, Ensembl rat ortholog): MARK_AS_OVER_ANNOTATED —
  not the enzyme's core function; over-propagated from a rat ortholog phenotype.
- `GO:0009168` purine ribonucleoside monophosphate biosynthesis (TAS Reactome): ACCEPT (pathway-level).
- `GO:0006177` GMP biosynthetic process (IMP acts_upstream_of_or_within; IDA involved_in):
  KEEP_AS_NON_CORE — downstream branch (IMP→GMP); PFAS acts upstream via IMP, not a GMP-synthesis enzyme.
- `GO:0044208` de novo AMP biosynthesis (IMP, IDA): KEEP_AS_NON_CORE — downstream branch (IMP→AMP).
- `GO:0097294` de novo XMP biosynthesis (IMP, IDA): KEEP_AS_NON_CORE — downstream branch (IMP→XMP).
- `GO:0070062` extracellular exosome (HDA): MARK_AS_OVER_ANNOTATED — bulk MS catalog, not a
  functional/biosynthetically meaningful localization for a cytosolic DNPS enzyme.

Downstream-branch BPs (GMP/AMP/XMP) capture that loss of PFAS depletes all purine nucleotides
(acts_upstream_of_or_within is the correct qualifier), but the enzyme's own reaction is upstream at
the IMP-precursor step, so these are non-core. Per policy, experimental (IMP/IDA/HDA) annotations
whose full text is uncached are not REMOVEd.
