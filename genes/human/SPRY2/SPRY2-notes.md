# SPRY2 (human, O43597) curation notes

## 2026-10-01 initial review

Context: reviewed as a negative-feedback regulator of RTK/Ras-ERK signalling for the ERK cascade module (Sprouty/SPRED paralog variants of one feedback step). Comparators: SPRY4 (core MF GO:0004860) and CBL.

### Mechanism summary (with provenance)

- GRB2 sequestration downstream of FGFR: [PMID:16893902 "This PXXPXR motif binds directly to the N-terminal Src homology domain 3 of Grb2"]; [PMID:16893902 "We present evidence that Spry2 can compete with the RasGEF (guanine nucleotide exchange factor) SOS1 for binding to Grb2, resulting in the inhibition of phosphorylation of ERK1/2"]. The motif is SPRY2-specific: [PMID:16893902 "Spry2 is considerably more inhibitory than Spry1 or Spry4, and this correlates with the binding to Grb2 via a C-terminal proline-rich sequence that is found exclusively on Spry2"].
- GRB2 binding is gated by PP2A dephosphorylation and blocked by TESK1: [PMID:17974561 "Tesk1 nullifies the inhibitory effect of Spry2 by abrogating its interaction with the adaptor protein Grb2 and interfering with its serine dephosphorylation upon bFGF and FGF receptor 1 stimulation by impeding its binding to the catalytic subunit of protein phosphatase 2A"]. Note: TESK1 inhibits SPRY2, the reverse of SPRY4, which inhibits TESK1 kinase.
- RAF/SYK antagonism: [PMID:26809508 "Mechanistically, we show that SPRY2 attenuates the B-cell receptor (BCR) and MAPK-Erk signaling by binding to and antagonizing the activities of RAF1, BRAF, and spleen tyrosine kinase (SYK) in normal B cells and CLL cells"]; [PMID:19690147 "Mutation of these six serines to nonphosphorylatable alanines increased the ability of Sprouty2 to inhibit growth factor-induced MAPK activation"]. No purified in vitro kinase assay found, so "kinase inhibitor" rests on binding plus cellular antagonism.
- CBL inhibition (EGFR potentiation): [PMID:12815057 "hSpry2 is tyrosine-phosphorylated upon stimulation by either FGFR or EGF and subsequently binds endogenous c-Cbl with high affinity"]; [PMID:15962011 "Sprouty2 therefore acts as an inducible inhibitor of EGFR downregulation by targeting both the Cbl and CIN85 pathways"]; [PMID:17974561 "does not affect its inhibition of Cbl-mediated ubiquitination of the epidermal growth factor receptor"]; [PMID:18273061 "showed Sprouty2 to have the highest binding affinity to c-Cbl"]. SPRY4 lacks CIN85 sites and does not block EGFR downregulation [PMID:15962011 "Moreover, Sprouty4, which lacks CIN85-binding sites, does not inhibit EGFR downregulation"].
- Receptor-dependent sign: [PMID:12815057 "hSpry2 inhibits the fibroblast growth factor receptor (FGFR)-induced mitogen-activated protein kinase pathway but conversely prolongs activity of the same pathway following epidermal growth factor (EGF) stimulation"].
- Endogenous SPRY2 survival function goes through CBL: [PMID:18070883 "endogenous hSPRY2-mediated regulation of apoptosis requires c-Cbl and is manifested by the ability of hSPRY2 to sequester c-Cbl and thereby augment signaling via growth factor receptors"].
- Localization: [PMID:10887178 "human Sprouty2 (hSpry2), which, although generally located in the cytosol, co-localized with microtubules"]; [PMID:10887178 "the Spry proteins underwent rapid translocation to membrane ruffles following EGF stimulation"]; S-acylation is needed for plasma membrane targeting [PMID:33037124 "mutations that perturbed S-acylation also led to a loss of plasma membrane localisation of sprouty-2 in PC12 cells"].
- PLC-gamma: [PMID:20719962 "Overexpression of Spry1 and Spry2 was associated with decreased PLCγ phosphorylation and decreased PLCγ activity"]. Not annotated; raised as a question.

### Decisions worth recording

- 77 protein binding IPIs: CBL rows MODIFY to GO:1990948 (functional papers) or GO:0031625 (binding-only papers); GRB2 rows MODIFY to GO:0140311 protein sequestering activity; CIN85 to SH3 domain binding; PP2A subunits to PP2A binding; TESK1 to protein kinase binding; caveolin-1 and all high-throughput Y2H rows REMOVE (uninformative, not denying interactions).
- GO:0043539 kinase activator activity (IMP, PMID:18070883): MODIFY to GO:1990948; the paper itself attributes the effect to c-Cbl sequestration.
- GO:0042059 negative regulation of EGFR signalling (IBA from Drosophila Spry): MARK_AS_OVER_ANNOTATED, functional divergence/sign inversion in mammalian SPRY2.
- GO:0016525 negative regulation of angiogenesis (IMP, PMID:24177325): UNDECIDED. Cached full text says Sema6A, not SPRY2, mediated the effect, and supplementary data are unavailable.
- GO:0030291 / GO:0019901 from PMID:20736167 (SPRED/DYRK1A paper): the cache is abstract-only and about SPREDs. PMC full text (PMC2975161, via WebFetch) reports Tau phosphorylation reduced with Spry2 + DYRK1A, so KEEP_AS_NON_CORE.
- No NOT annotations in GOA for SPRY2.
- NEW: GO:1990948 ubiquitin ligase inhibitor activity (SPRY2 performs the step itself by occupying the CBL TKB domain).

### Paralog comparison (for module)

The shared family activity is GO:0004860 (RAF antagonism; IBA at PTN000961788). SPRY2 adds two features of its own: GRB2-SH3 sequestration through the PXXPXR motif, and CBL/CIN85 sequestration that inverts the sign of its effect on EGFR. SPRY4 instead directly inhibits TESK1 and lacks the CBL-inhibitory output.
