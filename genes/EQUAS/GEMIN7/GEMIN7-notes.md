# GEMIN7 (donkey, Equus asinus) - A0A9L0ICL9

DONKEY40 cohort review. Unreviewed TrEMBL entry, 206 aa, "Gem-associated protein 7"; PANTHER PTHR14679:SF1; Pfam Gemin7; Sm domain 140-206.

## Sources
- Donkey UniProt `GEMIN7-uniprot.txt` (ARBA function/subunit/location text).
- Donkey GOA `GEMIN7-goa.tsv`: 7 IEA rows (2 TreeGrafter GO_REF:0000118: spliceosomal snRNP assembly, Sm-like protein family complex; 3 SubCell; 1 InterPro2GO; 1 combined RNA binding).
- Human ortholog Q9H840 UniProt fetched to `GEMIN7-bioinformatics/human-Q9H840-uniprot.txt`. No human/mouse GEMIN7 review in repo.
- Cached (abstract-only): PMID:12065586, PMID:15939020, PMID:17178713, PMID:18984161.

## Sequence
- Donkey 76-206 align ungapped to complete human GEMIN7 (1-131) at 87.79% identity; 75-residue N-terminal extension [file:EQUAS/GEMIN7/GEMIN7-bioinformatics/RESULTS.md].

## Biology
- Component of SMN complex; colocalizes with SMN in cytoplasm and gems; binds SMN and Gemin6; binds Sm proteins, especially SmE [PMID:12065586 "Gemin7 is a component of the SMN complex and colocalizes with SMN in the cytoplasm and in gems"].
- Gemin6-Gemin7 heterodimer with Sm folds, no Sm sequence similarity [PMID:15939020 "Although Gemin6 and Gemin7 have no significant sequence similarity with Sm proteins, both adopt canonical Sm folds."].
- SMN, Gemin8 and Gemin7 form the centre of the SMN complex [PMID:17178713 "SMN, Gemin8, and Gemin7 in its center"].
- SMN complex catalyses snRNP core formation [PMID:18984161 "the SMN complex as a catalyst of spliceosomal snRNP formation"].

## Decisions
- ACCEPT: spliceosomal snRNP assembly, nucleoplasm, cytoplasm, SMN-Sm protein complex, Gemini of Cajal bodies, Sm-like protein family complex.
- MARK_AS_OVER_ANNOTATED: RNA binding (Sm-domain InterPro mapping; no GEMIN7 RNA-binding evidence).
- NEW: SMN complex (GO:0032797), human IDA exists; not in donkey GOA.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Deep research
- `just deep-research-falcon EQUAS GEMIN7 --fallback perplexity-lite` failed: falcon "Failed to authenticate"; perplexity-lite fallback HTTP 401 (insufficient quota). No deep-research file was produced. Review uses the cached literature below.
- Newly cached: PMID:33754639 (S. pombe SMN complex structure, full text), PMID:16314521 (Golembe 2005, abstract only; cached for context, not cited).

### Identity: the benchmark accession is an alternative gene model
- Three donkey UniProt entries come from one Ensembl gene ENSEASG00005033816.1: A0A9L0ICL9 (206 aa, benchmark), A0A9L0IFN2 (179 aa) and A0A9L0J5X5 (131 aa) [file:EQUAS/GEMIN7/GEMIN7-bioinformatics/RESULTS-rereview.md].
- A0A9L0J5X5 (131 aa) is exactly A0A9L0ICL9 residues 76-206; it has the same length as human Q9H840 and horse A0A9L0T0I7 (99.24% identical to horse, 87.79% to human). A0A9L0J5X5 is the canonical-length donkey product; none of the donkey entries is Swiss-Prot reviewed.
- The benchmark model is an N-terminally extended alternative transcript product (+75 aa). It lacks no Gemin7 region; the Sm-like domain (140-206) is intact. Translation of the extension is not established.

### Evolutionary grounding
- PANTHER PTHR14679 (GEM-ASSOCIATED PROTEIN 7) has a single subfamily SF1 containing human Q9H840, mouse Q9CWY4, bovine Q17QA0 and S. pombe Gem7 G2TRR1 (interpro/panther/PTHR14679/PTHR14679-entries.csv); the donkey protein is in SF1. No disagreement on subfamily placement (no family review under interpro/panther/PTHR14679 beyond metadata/entries).
- QuickGO: human GEMIN7 IBA rows (spliceosomal snRNP assembly; Sm-like protein family complex) come from PTN001027441 with donors S. pombe SPBC32F12.16 and human Q9H840. PAINT did not place SMN complex (GO:0032797, human IDA) or RNA binding at the node; treated as deliberate.
- S. pombe SMN complex contains Gemin2, 6, 7, 8 and Sm proteins; Gemin8 on the SMN platform recruits Gemins 6 and 7 [PMID:33754639 "This creates a central platform onto which Gemin8 binds and recruits Gemins 6 and 7."].

### Changes vs previous review
- GO:0120114 Sm-like protein family complex: ACCEPT -> MODIFY to GO:0034719 SMN-Sm protein complex (true but general; specific descendant already carried).
- Removed the prior NEW row for GO:0032797 SMN complex: it is a descendant of GO:0034719, which the gene already carries (redundancy rule for NEW), and PAINT did not propagate it. Raised as a suggested question instead. core_functions.in_complex changed to GO:0034719 accordingly.
- Other rows unchanged in action (snRNP assembly ACCEPT; RNA binding MARK_AS_OVER_ANNOTATED; nucleoplasm, cytoplasm, gems, SMN-Sm complex ACCEPT); reasons updated with phylogenetic basis.
- Description rewritten to state the gene-model status and the conserved Gemin8-Gemin6/7 architecture.

### Relative to review next
- Same-gene canonical product A0A9L0J5X5 (donkey GEMIN7, 131 aa) has no review; folder would be genes/EQUAS/GEMIN7__A0A9L0J5X5.
- Modules: none include GEMIN7. modules/dmel_smn_complex.yaml covers the Drosophila SMN complex (no Gemin6/7 there) and is related only.
