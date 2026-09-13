# AT4G38370 (Q0WW53): evidence and exact-input prediction review

The fold-level name is reasonable. The only emitted GO term is generic catalytic activity; the TIGAR structural donor does not establish a particular phosphatase substrate or glycolytic role for AT4G38370.

## Input identity and functional boundary

Q0WW53 maps to AT4G38370 and PTHR47821:SF2. Its 225-residue sequence contains an N-terminal RHG motif. The emitted donor Q7ZVE3 is zebrafish TIGAR B. Exploratory global alignment preserves the donor catalytic histidine and proton-donor/acceptor residues, but is highly gapped and has low overall identity; the apparent mismatch at a transition-state contact is not reliable evidence of catalytic loss. No TIGAR-specific substrate assignment follows from this alignment.

## Biological evidence

- [PMID:19015259 — Structural and biochemical studies of TIGAR (TP53-induced glycolysis and apoptosis regulator).](https://pubmed.ncbi.nlm.nih.gov/19015259/): Direct TIGAR biochemistry establishes donor activity and substrate discrimination, not the substrate of the Arabidopsis protein.

> The
> recombinant human and zebra fish enzymes hydrolyze fructose-2,6-bisphosphate as
> well as fructose-1,6-bisphosphate but not fructose 6-phosphate in vitro.

## Exact non-GO claims

The complete emitted record is preserved in [AT4G38370-protnlm-source.json](AT4G38370-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Phosphoglycerate mutase-like protein

CNN (CS 2). “Phosphoglycerate mutase-like protein” is a qualified fold-level description consistent with the histidine-phosphatase domain assignment. The “-like” wording does not assert phosphoglycerate turnover or a glycolytic pathway role.

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [AT4G38370-protnlm-predictions-review.yaml](AT4G38370-protnlm-predictions-review.yaml).

## Family integration

PTHR47821:SF2 places the target among phosphoglycerate-mutase-family proteins. The histidine-phosphatase fold encompasses different phosphosugar reactions, so a common RHG catalytic motif cannot identify a substrate. It also does not establish the specialized secreted phytase architecture of another histidine-phosphatase branch.

## Evidence limits

No target-specific biochemical study was located under AT4G38370 or Q0WW53. The TIGAR primary report is abstract-only and explicitly establishes donor enzymology. The genuine Falcon synthesis supplies family hypotheses but does not establish a target reaction. The sequence comparison is exploratory: sparse global alignments are not used to call residue loss or to identify an evolved pseudoenzyme.

Exact sequence mapping: [AT4G38370-bioinformatics/RESULTS.md](AT4G38370-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.
