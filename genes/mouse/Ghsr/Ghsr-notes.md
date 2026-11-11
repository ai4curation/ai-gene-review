# Ghsr (mouse, Q99P50) review notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Ghsr is the experimentally characterised ortholog used as a reference for human GHSR (Q92847).
No ProtNLM2 output was opened or used.

### Setup
- `just fetch-gene mouse Ghsr`: 145 GOA rows, all seeded.
- Deep research failed. `just deep-research-falcon mouse Ghsr --fallback perplexity-lite` returned a falcon authentication failure ("Failed to authenticate") and then a Perplexity HTTP 401 (quota exceeded). No deep-research file exists; the review rests on the cached primary literature listed below.
- Extra papers cached: PMID:22284186 (mouse GHSR:DRD2), plus the rat source papers behind the RGD ISO rows (rat experimental rows were looked up in QuickGO for O08725).

### Evolutionary grounding
- Q99P50 is in PANTHER PTHR24243:SF7 (UniProt DR line), the same subfamily as human Q92847 and rat O08725.
- PAINT (interpro/panther/PTHR24243/PTHR24243-paint.tsv): PTN002797666 (taxon 117571, Euteleostomi) carries IBD GO:0001616 (seeds RGD:621397, Q92847, Q95254) and GO:0009755 (seeds Q92847, Q95254). PTN002797649 carries GO:0004930, GO:0007186 and GO:0005886 for the wider branch. Mouse is not a seed for GO:0001616, because MGI has no direct receptor-activity assay.
- PAINT did not propagate coreceptor activity, memory, synaptic plasticity or defecation, which are mouse-anchored experimental terms. I treat these as established in mouse only; their wider phylogenetic extent is untested.

### What is experimentally established in mouse (vs inferred)
- Established in mouse, genetic evidence: ghrelin-evoked GH release and feeding require Ghsr [PMID:15070777 "acute treatment of Ghsr-null mice with ghrelin stimulated neither GH release nor food intake"]; resistance to diet-induced obesity [PMID:16322794].
- Established in mouse, cellular/biochemical evidence: apo-GHSR1a:DRD1 heteromers in hippocampal neurons switch DRD1 to Gq-PLC-IP3-Ca2+ and drive plasticity and memory [PMID:26590421 "Real-time single-molecule analysis on hippocampal neurons revealed dimerization between apo-GHSR1a and DRD1"]. GHSR1a:DRD2 heteromers in hypothalamic neurons; ghsr-/- mice are refractory to DRD2-agonist anorexia [PMID:22284186]. Spinal defecation centre: GHSR reverses DRD2 signalling through constitutive activity, not dimerization [PMID:40441153 "neither its agonism nor dimerization with the D2 receptor is required"]. VTA synapse formation is GHSR-dependent [PMID:17060947].
- Inferred from orthologs (rat/human, same SF7 subfamily): direct ghrelin binding [PMID:10604470], Gq-specific coupling [PMID:25605885], ghrelin-bound structure [PMID:35027551], synaptic localisation [PMID:24367106, PMID:26153524], immune and vascular effects.

### Decisions worth flagging
- GO:0016520 (GHRH receptor activity) rows: MODIFY to GO:0001616, consistent with the human review. The human GO-CAM 67f85f2b00000823 also uses GO:0016520 (already raised in the human review).
- GO:0032099 negative regulation of appetite: the rat-source IMP (PMID:21778696) is an antagonist that increased food intake through GHSR, so MARK_AS_OVER_ANNOTATED. The DRD2-anorexia context is captured by coreceptor activity.
- The 10 Compara IEA rows derived from rat IEP (expression-only) annotations are REMOVE: expression change is not participation.
- PMID:16513828 IDA rows (response to food, cellular response to insulin stimulus) describe regulation of Ghsr mRNA levels, so MARK_AS_OVER_ANNOTATED.
- GO:0042802 identical protein binding (ISO from human): the human donor annotation is no longer in current GOA, so UNDECIDED.
