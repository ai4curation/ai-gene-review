# AIM33 (YML087C) — curation notes

UniProt: Q04516 | SGD: S000004552 | GeneID: 854887 | 312 aa | Chromosome XIII

## Curation conclusion

AIM33 is a poorly characterized, multi-pass membrane flavoprotein in the pyridine-nucleotide
cytochrome-reductase family. There is still no AIM33-specific enzyme assay, but that absence does
not invalidate its PAINT annotations. The IBA calls place the activity and ergosterol-process
terms on the AIM33 lineage, and AIM33 carries the expected FAD- and NAD(P)H-binding reductase
domains. In the absence of target-specific loss or active-site divergence, the correct review is
to retain those phylogenetic annotations while stating explicitly that they remain predictions.

The previous review also inferred a mitochondrial membrane location from the petite phenotype.
That was not justified. The local PANTHER loss table records loss of the ancestral mitochondrion
placement at PTN001064672, the AIM33/PGA3 subfamily node, while the current IBA places AIM33 at the
plasma membrane. A mitochondrial-genome phenotype does not establish mitochondrial localization.

## Evidence

### Protein family and topology

- UniProt Q04516 is a reviewed 312-aa protein, not 363 aa.
- UniProt assigns AIM33 to the flavoprotein pyridine nucleotide cytochrome reductase family and
  predicts FAD as cofactor.
- The protein has an FAD-binding FR-type domain (residues 70–173), an NAD-binding domain, and three
  predicted transmembrane helices (15–35, 42–62, and 180–200).
- PMID:16847258 is a genome-scale membrane-topology study. It supports the membrane-protein call,
  but its cached prose does not provide an AIM33-specific localization statement.

### PAINT interpretation

- GO:0004128 (cytochrome-b5 reductase activity, acting on NAD(P)H) is placed at PTN000452207 and
  carried to AIM33 with MCR1 and PGA3 as supporting family members.
- GO:0006696 (ergosterol biosynthetic process) is placed at PTN000452208 with MCR1 support.
- GO:0005886 (plasma membrane) is carried from PTN001064672 with PGA3 support.
- `projects/PANTHER_IBA_REVIEW/family_function_losses.tsv` records a mitochondrion loss for
  PTHR19370 at PTN001064672/PTHR19370:SF143. Thus PAINT explicitly distinguishes the AIM33/PGA3
  branch from the mitochondrial family placement; it does not support replacing plasma membrane
  with a mitochondrial or generic location.

These annotations are phylogenetic predictions, not AIM33-specific biochemical or imaging
measurements. That limitation belongs in the reasons and knowledge gaps, not in an assertion that
the PAINT calls are wrong.

### Mitochondrial-genome and respiratory-condition evidence

- PMID:19300474 identified genes whose deletion alters mitochondrial biogenesis/inheritance. The
  AIM33-specific measurement is in the supplement rather than the cached narrative text.
- UniProt currently states that AIM33 deletion *increases* mitochondrial genome loss. Later primary
  literature (PMID:40568959), restating the Hess result, says the deletion has a *reduced* frequency
  of spontaneous mitochondrial genome loss and cannot grow on non-fermentable carbon. The later
  direction is used here, with the UniProt discrepancy documented rather than treated as biological
  ambiguity.
- PMID:33984024 measured AIM33 expression in respiratory medium. AIM33 microarray signal increased
  from 94 in YPD to 1658 in YPGL in wild type and fell to 773 in the `pbp1Δ` strain (0.47 of wild
  type). The paper groups AIM33 among Pbp1-regulated genes associated with the mitochondrial-genome
  phenotype. This is expression/regulation evidence, not a catalytic or localization assay.
- PMID:40568959 found AIM33 consistently upregulated in `tda1Δ` cells during the post-diauxic phase
  in three experiments (mean log2 fold change 0.42 ± 0.10). The authors later state that AIM33 is
  mitochondrial without supplying AIM33-specific localization evidence; that sentence is not used
  to override PAINT.

## Annotation decisions

- GO:0005886 plasma membrane (IBA): **ACCEPT**. The PAINT node and explicit mitochondrial-loss event
  support lineage-specific plasma-membrane placement; direct endogenous imaging remains desirable.
- GO:0004128 cytochrome-b5 reductase activity, acting on NAD(P)H (IBA): **ACCEPT**. The PAINT
  placement plus the diagnostic reductase domains support the prediction. It is not a direct assay.
- GO:0006696 ergosterol biosynthetic process (IBA): **ACCEPT**. Retain the PAINT process placement;
  direct pathway evidence in AIM33 is still absent.
- GO:0004128 (ARBA IEA): **ACCEPT** as independent electronic corroboration of the same family-level
  prediction.
- GO:0016020 membrane and GO:0016491 oxidoreductase activity (IEA): **ACCEPT**.
- ND ontology roots: **ACCEPT** as historical no-data placeholders.

## Remaining knowledge gaps

1. Directly measure AIM33 reductase activity, donor preference, and physiological acceptor.
2. Establish endogenous localization and topology with a functional tagged allele; do not infer
   mitochondria solely from the deletion phenotype.
3. Test whether AIM33 contributes directly to ergosterol biosynthesis and identify its redox partner.
4. Reproduce the reduced-petite phenotype in a clean allele and determine how a plasma-membrane
   reductase affects respiratory competence or mitochondrial-genome inheritance.

## Provenance

- PMID:19300474 — mitochondrial biogenesis/inheritance screen.
- PMID:16847258 — global yeast membrane-topology map.
- PMID:33984024 — Pbp1-dependent expression of AIM33 in non-fermentable medium.
- PMID:40568959 — reproducible AIM33 upregulation in `tda1Δ` during post-diauxic growth and a later
  statement of the reduced-petite phenotype.
- UniProt Q04516, local GOA, and the local PANTHER family-function-loss table — sequence, topology,
  annotation-node, and loss-event evidence.
