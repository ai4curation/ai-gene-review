# GCV1 notes (YDR019C, P48015)

- Glycine cleavage T-protein (aminomethyltransferase, EC 2.1.2.10) [PMID:9047339 "We have isolated the gene encoding the glycine cleavage T-protein (GCV1) of the yeast Saccharomyces cerevisiae"]; disruption abolishes GCS [PMID:9047339 "All gcv1 strains studied were unable to grow on glycine as a sole nitrogen source and lacked glycine cleavage enzyme activity"].
- GDC = P/H/T/L (Gcv2/Gcv3/Gcv1/Lpd1) [PMID:8830251 "The glycine decarboxylase complex (GDC) is composed of four subunits referred to as H-, L-, P-, and T-proteins"]. Mitochondrial [UniProt:P48015; PMID:14576278 proteomics].
- Regulated by cytoplasmic CH2-THF [PMID:10871621 "particularly those encoding the unique components of the glycine decarboxylase complex (GCV1, GCV2, and GCV3)"].

## Curation observations
- YeastPathways RCA cytosol (GLYCLEAV-PWY) is a default-compartment artefact -> REMOVE.

## 2026-11-04 audit to COMPLETE
- Provider deep research was not generated in this session (no API keys); cached abstracts and the SGD description only.
- Added reasons to every row and completed truncated quotes (all cached papers are abstract-only).
- GO:0006546 glycine catabolic process (IEA, IMP, NAS) -> MODIFY to GO:0019464 glycine decarboxylation via glycine
  cleavage system (is_a descendant, already on the gene by IBA/RCA).
- GO:0005829 cytosol RCA (GO_REF:0000123) REMOVE kept; WRONG_TERM source defect for SGD (should be mitochondrion).
- Mitochondrion rows kept at the root organelle; only one line (predicted transit peptide) for the matrix, so no
  sub-compartment NEW row.
- Summaries quoted by interpro/panther/PTHR43757/PTHR43757-review.yaml left unchanged.
