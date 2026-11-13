# SNAP25 (human, P60880) review notes

## 2026-11-13

Core function: plasma-membrane Qbc-SNARE. SNAP-25 supplies two of the four helices of the
neuronal SNARE bundle ("in which 2 helices come from SNAP-25 and 1 each from VAMP-2 and Stx1"
[PMID:26635000]); the bundle "pulls the synaptic vesicle and plasma membranes together possibly
causing membrane fusion" [PMID:11832227]. Human genetics: "Ile67Asn variant in SNAP25B is
pathogenic because it inhibits synaptic vesicle exocytosis" [PMID:25381298], and the same paper
calls SNAP-25 "essential for exocytosis of synaptic vesicles from nerve terminals and of
dense-core vesicles from endocrine cells" [PMID:25381298]. So two core functions: synaptic
vesicle priming/fusion at the presynaptic membrane, and calcium-regulated dense-core vesicle
exocytosis.

Location: no TM segment; "Membrane association requires palmitoylation." (UniProt). The paper
cited for an NAS synaptic vesicle membrane row says the opposite: "Syntaxin1 and SNAP-253 are
anchored to the presynaptic membrane, whereas VAMP-2 is located on the SV membrane"
[PMID:26635000], so that row is removed and the IEA synaptic vesicle row marked over-annotated.

Removed: neurotransmitter uptake (NAS from a GLUT4-vesicle cloning paper, PMID:8760387),
voltage-gated K+ channel activity and K+ transport (electronic; SNAP-25 binds and modulates
KCNB1, it is not a channel), and bare protein binding rows. Protein binding with syntaxin-1A
(PMID:26635000) and with the P/Q channel synprint loop (PMID:8692999) were modified to
syntaxin-1 binding and transmembrane transporter binding.

BLOC-1 complex (IDA, PMID:19546860): the paper shows "both alternatively spliced variants of
SNAP-25 (a and b) robustly interacted with BLOC-1" -- an interaction, not membership; marked
over-annotated. Neutrophil specific/tertiary granule rows from Reactome proteomics marked
over-annotated.

Open: cytoskeleton IDA (PMID:24327345, a DYRK1A fractionation paper) -- the cached text never
mentions SNAP-25, so left UNDECIDED.

GO:0005484 now carries the label "helical-bundle zippering fusogenic activity" in QuickGO; the
local term cache still has "SNAP receptor activity", which produces a label warning only.

GO has renamed GO:0005484 from "SNAP receptor activity" to "helical-bundle zippering fusogenic activity" (the GOA/QuickGO label, kept in `existing_annotations`); the validators' local ontology snapshot lags, so `core_functions` uses the old label it accepts.
