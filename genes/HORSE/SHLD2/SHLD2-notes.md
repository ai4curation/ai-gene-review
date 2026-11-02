# SHLD2: paired human–horse review notes

## Biological evidence

The important distinction is shieldin-family identity versus an intact DNA-end-protection module. Human SHLD2 has experimentally distinct long/short splice products; a short product can still recruit to damage sites and assemble with shieldin while failing to suppress homologous recombination.

- [PMID:30022168: The shieldin complex mediates 53BP1-dependent DNA repair.](https://pubmed.ncbi.nlm.nih.gov/30022168/) — full text cached.
- [PMID:29789392: FAM35A associates with REV7 and modulates DNA damage responses of normal and BRCA1-defective cells.](https://pubmed.ncbi.nlm.nih.gov/29789392/) — full text cached.
- [PMID:29656893: DNA Repair Network Analysis Reveals Shieldin as a Key Regulator of NHEJ and PARP Inhibitor Sensitivity.](https://pubmed.ncbi.nlm.nih.gov/29656893/) — full text cached.

## Exact horse model

The 883-residue horse model retains the insertion absent from human canonical SHLD2, but its distal OB-domain region is divergent/gapped in the long-isoform alignment. Nuclear and damage-site recruitment are plausible; the complete NHEJ/resection-suppression mechanism is UNC for the exact model. Human Protein Atlas XML supports an additional human actin-associated pool, so the actin prediction is unresolved in horse rather than refuted as incompatible with nuclear localization.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/SHLD2/SHLD2-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Obtain a transcript-supported horse C terminus and inspect the OB folds. Distinguish long/short human isoforms in any assay transfer. Inspect the HPA antibody/cell-line context before transferring secondary actin localization.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research HORSE SHLD2 --provider falcon` failed (Edison API
"Failed to authenticate", HTTP 403), so no horse deep-research file exists. The review
uses the cached full texts of PMID:30022168, PMID:29789392 and PMID:29656893, the
abstract of PMID:34354233, the human Swiss-Prot record Q86V20 and new sequence analysis.
ProtNLM2 files were not opened.

### Identity of the benchmark accession

- Ensembl gene ENSECAG00000001626 (SHLD2) has seven protein-coding transcripts. The
  Ensembl canonical one is ENSECAT00000122467, i.e. UniProt A0A9L0TUF0 (1047 aa, 10
  exons). The benchmark A0A9L0RGD6 is ENSECAT00000102809 (883 aa, 8 exons), a
  non-canonical alternative model of the same gene. All seven are unreviewed TrEMBL entries.
- QuickGO (2026-10-20): A0A9L0TUF0 carries the gene's IBA rows (PTN001025652: nucleus,
  site of double-strand break, regulation of DSB repair via HR) and IEA ortholog transfers
  from Q86V20. A0A9L0RGD6 has no GO annotation, so the GOA seed file is empty.
- `SHLD2-bioinformatics/compare_isoforms_rereview.py` (output `RESULTS-rereview.md`,
  `compare_isoforms_rereview.json`) aligns all seven horse models to human Q86V20-1/-2.
  A0A9L0RGD6 starts at the human M1 equivalent (SHLD3-MAD2L2-binding 1-60 region present),
  keeps the 69-residue OB-B exon of the long human product and the OB-C zinc-ribbon
  cysteines (CAKC 772-775, CFSC 790-793), then diverges after horse ~811 (human iso-2 799 /
  iso-1 730). It lacks the equivalent of human iso-1 731-835: the rest of OB fold C after the
  zinc ribbon ([PMID:29789392 "occurs in a loop between OB fold C beta strands 1 and 2"]) and
  the distal part of the SHLD1-interaction region (human 652-822, UniProt Q86V20). Its last
  ~70 residues are an Arg/Gly/Pro-rich tail with no human or canonical-horse counterpart.
  This is an alternative 3' end, not a fragment; no transcript evidence was checked.

### Evolutionary grounding

PANTHER PTHR14495 has one subfamily (SF2) containing horse, human, mouse and orangutan
SHLD2; the family review `interpro/panther/PTHR14495/PTHR14495-review.yaml` lists
A0A9L0RGD6 and Q86V20 as SF2 representatives, which agrees with UniProt. PAINT placed only
three IBDs on PTN001025652 (nucleus, site of DSB, regulation of DSB repair via HR). The
human experimental terms for negative regulation of HR, positive regulation of NHEJ and
isotype switching were not propagated, and I treat that as a deliberate decision.

### Decisions

- NEW (ISO, from human via SF2/PTN001025652): nucleus and site of double-strand break. The
  recruitment module is intact, and human OB-fold mutants still localize to breaks
  [PMID:30022168 "Importantly, both mutants localized to DSB sites"].
- No process NEW. HR suppression and NHEJ promotion need the OB-fold DNA-binding module
  that is truncated in this model. In human the OB mutants that still localized were
  "defective in suppressing HR" (PMID:30022168).
- Core function: shieldin scaffold (GO:0030674) at DSB sites and nucleus, with an explicit
  caveat about the truncated C-terminus. The earlier description was rewritten as a
  project-independent summary.
- Relative to review next: the canonical horse product A0A9L0TUF0 has no review
  (folder would be genes/HORSE/SHLD2__A0A9L0TUF0). The characterized ortholog in SF2, human
  SHLD2 Q86V20, has a review (genes/human/SHLD2, status IN_PROGRESS, all annotations
  assessed).
- Modules: no shieldin/NHEJ module for eukaryotes exists in modules/ (only
  bacterial_nonhomologous_end_joining, which does not apply).

## 2026-10-21 — NEW rows withdrawn from the alternative gene model (PR #5303 review)

The re-review had proposed NEW rows (GO:0005634, GO:0035861) on this benchmark accession because GOA propagates the
gene's annotations, including PAINT IBA rows, to one representative product per gene and not to
alternative transcript models. The same terms are already annotated in GOA on the canonical horse
product of this gene (SHLD2__A0A9L0TUF0, reviewed in `genes/HORSE/SHLD2__A0A9L0TUF0/`). Filling that propagation
convention on a second product of the same gene is not a curation gap, so the rows were withdrawn
for consistency across the cohort. The gene-level function is unchanged and is recorded on the
canonical product's review; this file's description and core functions still describe it.
