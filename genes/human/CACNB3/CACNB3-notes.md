# CACNB3: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/CACNB3/CACNB3-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Evidence: cached publications, UniProt P54284, PANTHER 19.0 classification and PAINT data (interpro/panther/PTHR11824), and the falcon deep-research report.

### Identity
- P54284 is the reviewed canonical UniProt entry CACB3_HUMAN (484 aa, isoform 1 / beta3a, the displayed sequence). It is not a fragment, isoform or alternative gene model. Five isoforms are listed; the review folder is keyed to the canonical product.
- Domains: SH3 (59-128), GK-like domain that mediates alpha1 interaction (195-345, by similarity to rat P54287), disordered N and C termini.

### Evolutionary placement
- PANTHER 19.0: human CACNB3 (P54284), mouse Cacnb3 (P54285) and rat Cacnb3 (P54287) are all in PTHR11824:SF8 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-3). Paralogs: CACNB1 SF17, CACNB2 SF9, CACNB4 SF7.
- All ISS rows come from rat Cacnb3 (P54287), i.e. a within-subfamily ortholog transfer.
- PAINT: the IBDs reaching CACNB3 sit on the family-root node PTN000930213 (VGCC complex, calcium ion transport, high voltage-gated calcium channel activity). The GO:0008331 IBD is seeded only by mouse Cacnb1. The GO:0035249 (PTN000214435) and GO:0007268 (PTN002625095) IBDs seeded by Cacnb4/Cacnb2 do not reach CACNB3, which I take as deliberate; no synaptic-transmission terms are proposed.
- Family review interpro/panther/PTHR11824/PTHR11824-review.yaml (GO:0005246 family-wide) agrees; no subfamily disagreement.

### Key evidence
- Human beta3 modulates VDCC activity in oocytes [PMID:8119293 "The cloned H beta 3 subunit was further expressed in Xenopus oocytes to demonstrate its ability to modulate VDCC activity."]
- Beta3 with cardiac alpha1 [PMID:7679112 "it increases peak currents, modulates the voltage dependence of activation, and accelerates activation"]
- Human CaV1.3 and CaV2.2 reconstituted with beta3 [PMID:11160515 "N-type currents, formed from transiently transfected alpha(1B)/alpha(2)delta-1/beta(3)"]
- Cryo-EM of human CaV2.2 with beta3 [PMID:34234349 "comprising the core α1 and the ancillary α2δ-1 and β3 subunits"]
- Mouse knockout (ortholog, SF8) [PMID:9751781 "in sympathetic beta3-/- neurons, the L- and N-type current was significantly reduced relative to wt"]; [PMID:12161429 "low expression of N-type calcium channels (alpha1B)"]
- Channel-independent IP3R interaction in rat Ins-1 cells [PMID:34426509 "Cavβ3 interacts with the IP3 receptor in isolated β-cells, controls IP3-dependent Ca2+-signaling independently of Cav channel functions"]. Recorded as a suggested question, not annotated.

### Changes from the previous version
- Previous version reused one quote (PMID:8119293) for nearly every row; each row now cites row-appropriate evidence.
- GO:0005245 (all three rows, including contributes_to) -> MODIFY to GO:0005246 calcium channel regulator activity; GO:0008331 IBA -> MODIFY to GO:0005246.
- GO:0006816 and GO:0070588 -> MODIFY to GO:0061577 (the specific descendant already on the gene).
- Protein binding: CACNA1C rows -> MODIFY to GO:0044325 transmembrane transporter binding; GEM -> GO:0031267 small GTPase binding; the other HT partners -> REMOVE (GO:0005515 policy).
- Cytoplasm EXP (PMID:34234349): UNDECIDED -> ACCEPT (abstract now cached and supports it).
- Cytosol (Reactome) and membrane (IDA) -> KEEP_AS_NON_CORE.
- GO:0045933 muscle contraction (NAS) and GO:0098903 repolarization (ISS) -> MARK_AS_OVER_ANNOTATED: downstream physiology not tested for beta3; the main skeletal/cardiac beta subunits are beta1a/beta2.
- T-tubule rows stay UNDECIDED.
- Status set to COMPLETE; description rewritten; core functions split into gating regulation and alpha1 surface expression.

### Relative
- The closest experimentally characterized relative is mouse Cacnb3 (P54285, MGI:103307), in the same PANTHER subfamily SF8. It has knockout electrophysiology and in vivo data. There is no review in the repo (no genes/mouse/Cacnb3). Rat Cacnb3 (P54287) is the ISS donor and also has no review.
- Modules: none in modules/ mention CACNB3 or its rodent orthologs.
