# DRG2 research notes

UniProt P55039 (DRG2_HUMAN), Developmentally-regulated GTP-binding protein 2.

## Family / core function
DRG2 is a translational GTPase of the TRAFAC class, OBG-HflX-like superfamily, OBG GTPase family (the DRG/Developmentally Regulated GTP-binding protein family) [UniProt SIMILARITY: "Belongs to the TRAFAC class OBG-HflX-like GTPase superfamily. OBG GTPase family."].
- UniProt FUNCTION: "Catalyzes the conversion of GTP to GDP through hydrolysis of the gamma-phosphate bond in GTP. When hydroxylated at C-3 of 'Lys-21' by JMJD7, may bind to RNA and play a role in translation."
- Catalytic activity: GTP + H2O = GDP + phosphate + H+ (RHEA:19669), Mg2+ cofactor [PMID:29915238].
- DRG GTPases associate with translating ribosomes and partner with DFRP (DRG family regulatory protein) cofactors: DRG2 partners with DFRP2 / RWDD1. The RWDD1 interaction "confers protection to polyubiquitination and proteolytic degradation" (UniProt SUBUNIT, By similarity).
- DRG2 (and DRG1) are substrates of the JmjC oxygenase JMJD7, which catalyzes (3S)-lysyl hydroxylation; the modification may regulate RNA binding / translation role [PMID:29915238 "(3S)-lysyl hydroxylation, in two related members of the Translation Factor (TRAFAC) GTPase family"].

## Annotations review
- GO:0003924 GTPase activity (IEA + IDA PMID:29915238) — CORE MF. ACCEPT.
- GO:0005525 GTP binding (IEA, TAS) — supporting/structural; KEEP_AS_NON_CORE (the informative MF is GTPase activity; per batch guidance avoid bare GTP binding as the sole core).
- GO:0002181 cytoplasmic translation (IBA) — DRG2 is a ribosome-associated translational GTPase; the broad "cytoplasmic translation" term is the inferred process. KEEP_AS_NON_CORE (broad translation term; the specific regulatory role is not well-defined for human DRG2). Mirrors batch guidance on keeping broad translation terms non-core for ribosome-associated factors.
- GO:0003723 RNA binding (IDA PMID:29915238) — hydroxylation-dependent RNA binding. KEEP_AS_NON_CORE (real but conditional/secondary to GTPase activity).
- nucleus + cytoplasm (IDA PMID:29915238) — ACCEPT both (DRG2 is both nuclear and cytoplasmic).
- cytosol (IDA HPA; TAS Reactome) — ACCEPT.
- membrane (HDA PMID:19946888, NK-cell membrane proteome) — generic HT proteomics; MARK_AS_OVER_ANNOTATED.
- GO:0007165 signal transduction (TAS PMID:7929244) — this 1994 paper just identifies a novel GTP-binding protein repressed in SV40-transformed fibroblasts; "signal transduction" is a vague legacy inference. MARK_AS_OVER_ANNOTATED (no specific signaling pathway established; DRG2 is a translational GTPase, not a signaling GTPase).
- protein binding IPI: RWDD1 (Q9H446, DFRP2 — the key regulatory partner, recurrent across many screens), JMJD7 (P0C870, the hydroxylase), EIF4A3 (P38919), NAB2 (Q15742), TSSK3 (Q96PN8), SPRED1 (Q7Z699), JPH3 (Q8WXH2). Uninformative term -> KEEP_AS_NON_CORE; RWDD1/JMJD7 are meaningful but captured by the GTPase/regulation narrative.

## Curation conclusions
- CORE MF: GTPase activity (GO:0003924) — translational GTPase.
- Locations: cytoplasm/cytosol + nucleus.
- GTP binding, RNA binding, cytoplasmic translation = non-core. signal transduction + membrane = over-annotated.
