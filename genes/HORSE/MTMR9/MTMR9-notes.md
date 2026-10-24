# MTMR9 notes


## 2026-09-08 paired review

Selected accession A0A9L0T3C1; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/MTMR9/MTMR9-notes.md). [Sequence comparison](MTMR9-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

MTMR9 lacks intrinsic phosphatase catalysis but dimerizes with active MTMR6, MTMR7 and MTMR8. Human MTMR6/MTMR9 and MTMR8/MTMR9 studies directly measure altered catalytic rates, substrate preferences, cellular phosphoinositide levels and downstream phenotypes. The 2009 study also finds increased partner abundance consistent with stabilization. The 2012 study distinguishes the MTMR6/R9 anti-apoptotic role from MTMR8/R9 inhibition of autophagy. These are positive reasons to retain regulatory and process participation claims. The molecular-function distinction between generic phosphatase regulation and binding specifically to a protein phosphatase still needs attention because the experimentally studied partners are lipid phosphatases.

Sources: [PMID:19038970](https://pubmed.ncbi.nlm.nih.gov/19038970/), [PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research (`just deep-research HORSE MTMR9 --provider falcon --fallback perplexity-lite`) failed: falcon "Failed to authenticate", perplexity-lite HTTP 401 insufficient quota. No deep-research file was written; the review uses the cached abstracts and the human SF56 ortholog record instead.

### Identity of the benchmark accession (alternative gene model)

- A0A9L0T3C1 (507 aa, TrEMBL, no GN line) is the product of Ensembl transcript ENSECAT00000122597 of horse gene ENSECAG00000014120 (MTMR9, chr2). The gene has three protein-coding models ([RESULTS-rereview.md](MTMR9-bioinformatics/RESULTS-rereview.md), script `compare_models_rereview.py`):
  - A0A5F5PR89 (549 aa, ENSECAT00000074905): full length, 98.0% identical to human Q96QG7, no gaps, same C-terminus (…ETEDGMQESP).
  - F7CCR9 (553 aa, ENSECAT00000015118, Ensembl canonical; the member that receives PANTHER IBAs from PTN002246859): its alternative last exon replaces the conserved coiled-coil tail (…KVNILRRQLAELETEDGMQESP) with an unrelated sequence (…CLKFLLLWFL), so it lacks roughly the distal half of the partner-binding coiled coil.
  - A0A9L0T3C1 (507 aa): identical exon set to A0A5F5PR89 except that it skips the 126-nt exon at chr2:59745643-59745768, removing 42 residues (human 98-139, `ALSTLDSITLMYPFFYRPMFEVIEDGWHSFLPEQEFELYSSA`) at the GRAM/phosphatase-like domain junction. The coiled coil (466-500) and the inactive catalytic loop region (identical to human) are retained.
- So the benchmark accession is an in-frame exon-skipped splice isoform, not the canonical product. There is no Swiss-Prot horse MTMR9 entry; the human-equivalent full-length product is A0A5F5PR89.
- gene_symbol in the review is left as the accession, following the pipeline convention for UniProt records without a GN line.

### Evolutionary grounding

- Human Q96QG7, mouse Q9Z2D0 and bovine A7MB43 are all PTHR10807:SF56 (MTMR9); the horse gene is in SF56 too, and its canonical member F7CCR9 inherits IBAs from PAINT node PTN002246859 (GO:0019903 protein phosphatase binding, GO:0010507 negative regulation of autophagy; sole donor Q96QG7). PAINT did not propagate the human EXP/IDA terms phosphatase activator activity, positive regulation of phosphatase activity or protein stabilization; I did not use PAINT to transfer them.
- Phosphatase activator activity rests instead on two independent mammalian experiments: human MTMR9 on MTMR6/MTMR8 [PMID:19038970 "MTMR9 increased the 3-phosphatase activity of MTMR6 up to 6-fold."; PMID:22647598 "Complex formation between the active myotubularins and MTMR9 increases their catalytic activity and alters their substrate specificity"] and mouse MTMR9 on MTMR7 [PMID:12890864 "The binding of MTMR9 increased the Ins(1,3)P2 phosphatase activity of MTMR7."]. Human+mouse (Euarchontoglires) and horse (Laurasiatheria) share the boreoeutherian ancestor, so parsimony puts the activity at least there.
- Partner binding uses the coiled coil [PMID:12890864 "The coiled-coil domain of MTMR9 was sufficient for binding to MTMR7."], which A0A9L0T3C1 retains. The effect of the exon skip is untested.

### Annotation decisions (5 rows)

- GO:0005783 ER (IEA SubCell): KEEP_AS_NON_CORE (partial ER pool in human, PMID:19038970).
- GO:0005829 cytosol (IEA ARBA): ACCEPT (soluble cytoplasmic protein; human IDA cytoplasm). Used as core location.
- GO:0030234 enzyme regulator activity (IEA ARBA): MODIFY → GO:0019211 phosphatase activator activity (true but general; matches human review).
- GO:0032587 ruffle membrane (IEA SubCell): KEEP_AS_NON_CORE (macropinocytosis, PMID:24591580 "MTMR6 that dephosphorylates PI(3)P to PI, and its binding partner MTMR9, are required for macropinocytosis.").
- GO:0048471 perinuclear region (IEA SubCell): KEEP_AS_NON_CORE.
- No NEW rows. Negative regulation of autophagy and protein phosphatase binding are carried by the gene's PANTHER representative F7CCR9 via IBA; I did not add them to this splice isoform. Autophagy is a cellular readout of MTMR8/MTMR9 knockdown, not a step MTMR9 itself performs, and the binding term adds little beyond the activator MF.

### Changes from the 2026-09-08 review

The old description said only that the sequence "has an internal or terminal difference". I rewrote it to name the exon-skip isoform. I changed enzyme regulator activity from ACCEPT to MODIFY → phosphatase activator activity. I replaced citations of RESULTS.md with RESULTS-rereview.md (RESULTS.md is kept in references) and added PMIDs 19038970, 12890864, 16787938 and 24591580 (newly cached) as references.

### Relative to review next

A0A5F5PR89, the full-length human-equivalent product of the same gene, has no review (future folder `genes/HORSE/MTMR9__A0A5F5PR89`). F7CCR9 is the Ensembl canonical, but it has a divergent C-terminal coiled coil.
