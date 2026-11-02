# SLC27A5 (horse, Equus caballus) - A0A5F5PXH2

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Canonical full-length horse SLC27A5 product, reviewed as the closest characterised relative
(same gene) of ProtNLM2 benchmark accession F6X2Q2 (genes/HORSE/SLC27A5). No ProtNLM2 file or
prediction-evidence folder was opened or used.

### Setup
- `genes/HORSE/SLC27A5` already exists for F6X2Q2, so this review is in
  `genes/HORSE/SLC27A5__A0A5F5PXH2`, created with
  `just fetch-gene HORSE A0A5F5PXH2 --alias SLC27A5__A0A5F5PXH2`; stub id confirmed A0A5F5PXH2.
- The stub took `gene_symbol: ZBTB45` from UniProt (GN Name=ZBTB45 from VGNC:25152, Synonyms=SLC27A5
  from Ensembl). Set to SLC27A5: Ensembl gene ENSECAG00000046881.1, CTD 10998 (= human SLC27A5
  GeneID, file:human/SLC27A5/SLC27A5-uniprot.txt "DR   GeneID; 10998; -."), PANTHER
  PTHR43107:SF25 "LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 5", and 80.9% identity to human SLC27A5
  all identify SLC27A5. The VGNC name looks like a mapping error to the neighbouring ZBTB45 locus;
  raised as a suggested question.

### Deep research
`just deep-research-falcon HORSE SLC27A5__A0A5F5PXH2 --fallback perplexity-lite` failed: falcon
"Exception: Failed to authenticate"; perplexity-lite HTTP 401 (insufficient quota). No
deep-research file. Review uses cached primary literature: human PMID:10479480, PMID:10749848,
PMID:11980911 and mouse knockouts PMID:16618416 (Doege 2006) and PMID:16618417 (Hubbard 2006),
the latter two newly cached with `just fetch-pmid` (all abstract-only). No horse-specific
functional literature was found; every function below is inferred.

### Evolutionary grounding
- A0A5F5PXH2, human Q9Y2P5 and mouse Q4LDG0 are all PTHR43107:SF25; human SLC27A2 (O14975) is SF4.
- Alignments [file:HORSE/SLC27A5__A0A5F5PXH2/SLC27A5__A0A5F5PXH2-bioinformatics/RESULTS.md]:
  80.9% to human SLC27A5 over 690 aligned pairs, 70.8% to mouse, 47.1% to SLC27A2; AMP-binding
  motif FIYTSGTTGLPK (human 292-303) identical at horse 302-313.
- PAINT (interpro/panther/PTHR43107/PTHR43107-paint.tsv):
  - PTN001945407 (family root): GO:0004467, GO:0005324, GO:0001676, GO:0044539, GO:0005886.
  - PTN001186241 (Eumetazoa): GO:0005789 ER membrane.
  - PTN008678717 (Tetrapoda, SLC27A2+SLC27A5): GO:0008206 bile acid metabolic process.
  - GO:0047747 cholate-CoA ligase and GO:0031957 VLCFA-CoA ligase are not placed at any node.
    Not placing cholate-CoA ligase at PTN008678717 is correct, since SLC27A2 does not activate cholate
    [PMID:10749848 "Other long- and very long-chain acyl-CoA synthetases were incapable of activating cholate"].
    Horse inherits it via SF25 one-to-one orthology (Ensembl Compara projection), not via a PAINT node.
- Horse has no IBA rows in GOA; the GOA set is Ensembl Compara (GO_REF:0000107), EC/SubCell
  mapping and inter-ontology inference.

### Biology (orthologs in SF25)
- Cholate:CoA ligase, human [PMID:10749848 "exhibited cholate:CoA ligase (choloyl-CoA synthetase) activity with both"];
  wider bile acid substrates [PMID:11980911 "this enzyme also activates chenodeoxycholate, the secondary bile acids"].
- In vivo, mouse: [PMID:16618417 "the majority of gallbladder bile acids was unconjugated"], with
  total bile acids unchanged, i.e. recycling/re-conjugation, not de novo synthesis.
- LC/VLC acyl-CoA synthetase, ER, human [PMID:10479480 "For all substrates tested (C18:0, C20:0, C24:0, C26:0)"].
- Basal plasma membrane and LCFA uptake, mouse [PMID:16618416 "localized to the basal plasma membrane of hepatocytes"].
- Body weight phenotype of the knockout (PMID:16618417) is downstream; not annotated.

### Decisions
- ACCEPT: GO:0047747, GO:0004467, GO:0031957, GO:0001676, GO:0000038, GO:0005789.
- KEEP_AS_NON_CORE: GO:0005324, GO:0015909, GO:0009925, GO:0006699 (in vitro THCA activation;
  deferring to human IDA but physiological role is recycling).
- MODIFY (general -> specific term already on the gene): GO:0005783 -> GO:0005789;
  GO:0005886 -> GO:0009925; GO:0015245 -> GO:0005324; GO:0015908 -> GO:0015909.
- NEW: GO:0008206 bile acid metabolic process (ISS), matching the PAINT tetrapod-node placement
  carried by human SLC27A5 by IBA.
- GO:0002152 bile acid conjugation considered but not added: in human only BAAT carries it; raised
  as a suggested question instead (comparator check).

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0008206 bile acid metabolic process) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/HORSE/SLC27A5/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn under the rule applied across the
ProtNLM2 re-review cohorts, first raised in the review of PR #5303. The gene-level function is unchanged.

## 2026-10-23 — PR #5309 review follow-up

Core-function process GO:0008206 bile acid metabolic process, left after the 2026-10-21 withdrawal of its
NEW row, is kept under the convention accepted in PRs #5305 (MESK2) and #5308 (FTSH12): a core term stays
when core_functions supported_by cites direct evidence independent of the withdrawn row. Its support is
primary literature on SLC27A5 bile acid-CoA ligase activity and reconjugation (PMID:10749848, 11980911,
16618417), and I added the PAINT IBD row placing GO:0008206 at PTN008678717 (PTHR43107-paint.tsv), an
ancestor of horse SLC27A5. The PR reviewer preferred dropping it; it is kept for consistency across
cohorts, and no annotation row re-asserts it on this product. The earlier "NEW: GO:0008206" bullet is
superseded by the withdrawal section.
