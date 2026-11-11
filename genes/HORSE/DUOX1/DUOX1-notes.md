# DUOX1 notes


## 2026-09-08 paired review

Selected accession A0A9L0SQG9; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/DUOX1/DUOX1-notes.md). [Sequence comparison](DUOX1-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

The heme-containing membrane oxidase/dehydrogenase machinery transfers reducing equivalents from NADPH through FAD and hemes to oxygen. The extracellular peroxidase-like domain is a different structural region. Direct biochemical work finds that the isolated human peroxidase-like domain lacks heme binding and intrinsic peroxidase activity; the C. elegans homolog behaves differently. The human NOT-peroxidase annotation is therefore supported, without negating the heme required by the membrane oxidase. High- and low-calcium structures of DUOX1–DUOXA1 establish EF-hand-dependent conformational regulation. The selected horse deletion removes major elements of that regulatory region, making exact-sequence transfer much less secure than ordinary family identification. Hormone synthesis requires coupling peroxide production to separate peroxidases and the appropriate tissue context.

Sources: [PMID:19460756](https://pubmed.ncbi.nlm.nih.gov/19460756/), [PMID:33420071](https://pubmed.ncbi.nlm.nih.gov/33420071/), [PMID:25761904](https://pubmed.ncbi.nlm.nih.gov/25761904/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not open the ProtNLM2 files and uses none of their output.

### Deep research
`just deep-research HORSE DUOX1 --provider falcon` failed ("Exception: Failed to authenticate"; all providers failed), so no deep-research file exists. The review rests on cached primary literature: PMID:33420071 (full text), PMID:19460756 (abstract), PMID:11514595 (full text). It also uses the human DUOX1 review (genes/human/DUOX1), the PTHR11972 PAINT table and family review, and a new sequence analysis.

### Identity of A0A9L0SQG9 (an alternative gene model, not the canonical product)
New analysis: [compare_horse_models_rereview.py](DUOX1-bioinformatics/compare_horse_models_rereview.py), output in [RESULTS-rereview.md](DUOX1-bioinformatics/RESULTS-rereview.md) and results-rereview.json. It aligns all four horse DUOX1 TrEMBL products (PTHR11972:SF75) with human Q9NRD9.
- Horse gene ENSECAG00000023918 has four protein-coding transcripts. The UniProt gene-centric canonical for horse DUOX1 is **F6YEX2** (1516 aa, Ensembl canonical ENSECAT00000026134). The benchmark accession **A0A9L0SQG9** (1452 aa) is the product of the non-canonical transcript ENSECAT00000123284.
- In A0A9L0SQG9, canonical coding exons 18 and 19 (226 and 94 nt) are replaced by a single 23-nt coding segment. This is an in-frame loss of 297 nt, or 99 residues, corresponding to human 775-873 in the cytosolic loop between TM1 and TM2. The missing segment holds EF-hand 1 (0% present) and 64% of EF-hand 2, leaving 6 of 15 human Ca2+ ligands. Those 6 are mainly the structural Ca2+ site in the peroxidase-homology domain plus Glu875. EF-hand 3 is intact.
- Everything else is intact: signal peptide, all 7 TM helices, the ferric-reductase (heme) domain, and the FAD and NADPH domains. All 13 heme, 8 FAD and 11 NADPH contact residues match human. Identity to human is 91.4% over paired residues.
- None of the horse models matches human exactly. The canonical F6YEX2 ends at human residue 1516, so it lacks the C-terminal 35 residues and 5 of 11 NADPH contacts; it is probably a truncated 3' model. A0A9L0SA70 lacks human 963-1004, and A0A9L0SBC0 lacks 561-606 (part of TM1). No horse DUOX1 entry is Swiss-Prot reviewed.
- Interpretation: the catalytic core of A0A9L0SQG9 is complete, but it lacks the calcium-sensing EF-hand module. PMID:33420071 notes that "mutations of any of these calcium-binding sites abolished calcium activation". Whether this transcript makes a protein in horse tissue is not known.

### Evolutionary grounding
- PANTHER places the horse protein in PTHR11972:SF75 (DUAL OXIDASE 1), the same subfamily as human DUOX1. DUOX2 is a separate subfamily, SF67 (horse F6QB25).
- PAINT: GO:0016174 NAD(P)H oxidase H2O2-forming activity is an IBD at PTN000944147, seeded by Q9NRD9 (DUOX1), Q9NRD8 (DUOX2), rat and pig DUOX, Drosophila and worm Duox. Plasma membrane (GO:0005886) is an IBD at PTN001735877 with Q9NRD9 among its seeds. No PAINT node in PTHR11972 asserts peroxidase activity, response to oxidative stress or oxidant detoxification; I read that as deliberate.
- No horse functional study exists, so every function here is inferred from orthology.

### Decisions (7 GOA rows + 1 NEW)
- GO:0004601 peroxidase activity (IEA, IPR010255): **REMOVE**. Human DUOX1 has a curated NOT IDA (PMID:19460756: the purified domain has no heme and no activity). The record's PROSITE PRU00298 caution reports missing conserved residues. Only the C. elegans domain is active. PMID:11514595 reported activity in lysates and is now DISPUTED.
- GO:0005886 plasma membrane: **ACCEPT**.
- GO:0006979 response to oxidative stress (IEA, from the peroxidase superfamily signature): **MARK_AS_OVER_ANNOTATED**. It assumes a peroxide-consuming peroxidase, but DUOX1 generates oxidant. The previous review had KEEP_AS_NON_CORE.
- GO:0016020 membrane: **MODIFY** to plasma membrane. The previous review had UNDECIDED.
- GO:0016491 oxidoreductase activity: **MODIFY** to GO:0016174 (PAINT IBD, full cofactor-residue conservation). The previous review had UNDECIDED. The missing EF-hands affect regulation, not the catalytic core.
- GO:0020037 heme binding: **ACCEPT**. The heme is bound by the TM domain, although the IEA came from the peroxidase-domain signature.
- GO:0098869 cellular oxidant detoxification (GO_REF:0000108, derived from GO:0004601): **REMOVE**. The previous review had UNDECIDED.
- NEW GO:0050665 hydrogen peroxide biosynthetic process (ISS from human IDA PMID:33420071). DUOX1 catalyses the step itself, so this is participation, not necessity.
- The gene_symbol field was corrected from the accession to DUOX1. The description was rewritten as an orthology-based summary that states the model's deletion.

### Relative to review next
The canonical product of the same gene, F6YEX2 (UniProt gene-centric canonical, Ensembl canonical, PTHR11972:SF75), has no review in the repo. It would go in genes/HORSE/DUOX1__F6YEX2, because genes/HORSE/DUOX1 is keyed to A0A9L0SQG9. Note that F6YEX2 is itself C-terminally truncated relative to human. The closest experimentally characterised ortholog, human DUOX1 (Q9NRD9, same subfamily, PAINT seed), already has a COMPLETE review in genes/human/DUOX1.

### Family review and modules
interpro/panther/PTHR11972/PTHR11972-review.yaml lists A0A9L0SQG9 under SF75 together with human Q9NRD9, which agrees with UniProt's PANTHER cross-reference, so there is no placement disagreement. The family review marks peroxidase activity as UNRESOLVED (contested). Here the contest is resolved toward NOT for mammalian SF75, on the basis of the purified-protein result and the residue caution. No module under modules/ mentions DUOX1, Q9NRD9 or DUOX.

## 2026-10-21 — NEW rows withdrawn from the alternative gene model (PR #5303 review)

The re-review had proposed NEW rows (GO:0050665) on this benchmark accession because GOA propagates the
gene's annotations, including PAINT IBA rows, to one representative product per gene and not to
alternative transcript models. The same terms are already annotated in GOA on the canonical horse
product of this gene (DUOX1__F6YEX2, reviewed in `genes/HORSE/DUOX1__F6YEX2/`). Filling that propagation
convention on a second product of the same gene is not a curation gap, so the rows were withdrawn
for consistency across the cohort. The gene-level function is unchanged and is recorded on the
canonical product's review; this file's description and core functions still describe it.
