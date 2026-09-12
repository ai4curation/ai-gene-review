# EIF2D (Ligatin, eIF2D) — research notes

UniProt P41214. Single-polypeptide non-canonical translation factor. Contains SUI1 + PUA + SWIB domains; it is the full-length protein of which MCTS1 (N-half) + DENR (C-half) are the split equivalent.

## Core function
- [PMID:20566627 "the tRNA binding to the P-site of 40 S ribosomes by a novel GTP-independent factor eIF2D ... The binding of tRNA(i)(Met) occurs after the AUG codon finds its position in the P-site ... the factor possesses the unique ability to deliver non-Met (elongator) tRNAs into the P-site of the 40 S subunit"]
- UniProt FUNCTION: "Translation initiation factor that is able to deliver tRNA to the P-site of the eukaryotic ribosome in a GTP-independent manner ... can promote release of deacylated tRNA and mRNA from recycled 40S subunits following ABCE1-mediated dissociation of post-termination ribosomal complexes."
- [PMID:20713520] Ligatin (= eIF2D) individually promotes eIF2-independent Met-tRNA recruitment and 40S recycling (release of deacylated tRNA/mRNA after ABCE1 splitting).

So core MF: translation initiation factor activity (GTP-independent P-site tRNA delivery); BP: ribosome recycling (40S recovery / ribosome disassembly), reinitiation, IRES init.

## Historical "Ligatin = trafficking receptor" conflation
- [PMID:2482295 "the first isolation and sequence of a partial cDNA clone encoding ligatin, a trafficking receptor for phosphoglycoproteins"] — this 1989 paper named "ligatin" as a phosphoglycoprotein trafficking receptor. The annotations GO:0038023 signaling receptor activity, GO:0006886 intracellular protein transport, and GO:0005737 cytoplasm (TAS PMID:2482295) derive from this. The modern molecular identity of EIF2D/Ligatin as a translation factor (Dmitriev 2010, Skabkin 2010) makes the receptor/transport functions over-annotations / mis-assignments — REMOVE or MARK_AS_OVER_ANNOTATED.

## Decisions
- translation initiation factor activity (IBA, IEA, IDA 20566627) — ACCEPT (core).
- formation of translation preinitiation complex (IBA, IEA, IDA 20713520) — ACCEPT.
- ribosome disassembly (IDA 20713520) — ACCEPT (recycling).
- IRES-dependent viral translational initiation (IDA 20713520) — KEEP_AS_NON_CORE.
- RNA binding (IEA) — KEEP_AS_NON_CORE.
- translational initiation (IEA) / protein-containing complex organization (IEA) — KEEP_AS_NON_CORE.
- cytosol/cytoplasm (IDA) — ACCEPT.
- signaling receptor activity (TAS 2482295) — REMOVE (wrong "ligatin" identity).
- intracellular protein transport (TAS 2482295) — REMOVE.
- cytoplasm TAS 2482295 — KEEP_AS_NON_CORE (localization happens to be right but provenance is the receptor paper).
