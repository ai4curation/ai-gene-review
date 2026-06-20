# NUFIP1 (nuclear FMR1-interacting protein 1) — review notes

UniProt: Q9UHK0. Gene: NUFIP1. Human.

## Function overview (synthesized)
NUFIP1 is a small zinc-finger nucleocytoplasmic shuttling protein with two distinct, well-supported roles plus historical transcription/FMRP associations:

### 1. Ribophagy receptor (headline cytoplasmic function; NOT yet in current GOA)
Upon mTORC1 inhibition/starvation, NUFIP1 redistributes from the nucleus to the cytoplasm/autophagosomes, binds ribosomes (with its partner ZNHIT3), and delivers them to autophagosomes by directly binding LC3B via a LIR motif, acting as the selective-autophagy receptor for ribosomes (ribophagy). A NUFIP1 LC3B-binding mutant cannot support ribosome degradation. Ribophagy provides metabolites supporting cell survival under starvation.
[PMID:29700228 "NUFIP1 is a ribosome receptor for starvation-induced ribophagy" — Wyant et al., Science 2018: "Upon mTORC1 inhibition, NUFIP1 redistributes from the nucleus to autophagosomes and lysosomes, where it interacts with ribosomes and delivers them to autophagosomes by directly binding to LC3B"; "a NUFIP1 mutant that does not bind LC3B cannot support ribosomal degradation"]

### 2. Box C/D snoRNP assembly factor (nuclear)
NUFIP (with ZNHIT3/NHP2L1, BCD1/ZNHIT6, and the R2TP/AAA+ ATPases TIP48/RUVBL2 and TIP49/RUVBL1) is a pre-snoRNP scaffold/assembly factor. NUFIP bridges interactions between core box C/D proteins in the pre-snoRNP, facilitating box C/D snoRNP biogenesis (rRNA processing/modification machinery).
[PMID:17636026 "we show that NUFIP bridges interactions between the core box C/D proteins in a partially reconstituted pre-snoRNP"; "four novel human biogenesis factors (BCD1, NOP17, NUFIP, and TAF9) which, along with the ATPases TIP48 and TIP49, are likely to be involved in the formation of the pre-snoRNP"]
- Interacts with ZNHIT3 (defective in PEHO syndrome). [PMID:28335020]

### 3. FMRP interaction / transcription (historical)
NUFIP1 was identified as a nuclear FMR1 (FMRP)-interacting protein, an RNA-binding nucleocytoplasmic shuttling protein associated with active synaptoneurosomes; also reported to cooperate with BRCA1 and P-TEFb (Cyclin T1) to stimulate RNA polymerase II transcription. It does NOT itself bind DNA directly (acts via protein interactions and stimulates pol II transcription).
[PMID:10556305 NUFIP identified as nuclear FMRP-interacting RNA-binding protein]
[PMID:12941608 "NUFIP1 ... is a nucleocytoplasmic shuttling protein associated with active synaptoneurosomes"]
[PMID:15107825 "BRCA1 cooperates with NUFIP and P-TEFb to activate transcription by RNA polymerase II" — yeast two-hybrid with BRCA1; stimulates activator-independent pol II transcription; associates with P-TEFb via Cyclin T1]

## Domain / binding
- Zinc-finger-containing protein. Binds RNA (and snoRNA). LIR motif mediates LC3B binding (ribophagy).
[file:human/NUFIP1/NUFIP1-uniprot.txt "FUNCTION: Binds RNA"; "Interacts with FMR1 ... Interacts with ZNHIT3"]

## Localization
Predominantly nucleus (nucleoplasm, nucleolus, perichromatin fibrils, nuclear matrix); shuttles to cytoplasm/autophagosomes upon starvation. Synapse/presynaptic active zone annotations are by IEA/ISS (Ensembl Compara ortholog transfer; synaptoneurosome association).

## Annotation judgments
- Core ACCEPT: box C/D snoRNP assembly (GO:0000492 IBA and IMP), protein-macromolecule adaptor activity (GO:0030674 IBA/IPI — scaffold/bridging role), pre-snoRNP complex (GO:0070761), snoRNA binding (GO:0030515 contributes_to), RNA binding (GO:0003723), ATPase binding (GO:0051117 — TIP48/49), nucleus/nucleolus/nucleoplasm localization, identical protein binding.
- The headline ribophagy receptor function (LC3B binding, ribosome cargo receptor) is NOT in the current GOA -> propose as NEW terms (GO:0034517 ribophagy; GO:0160247 autophagy cargo adaptor activity). Reviewer should add these.
- KEEP_AS_NON_CORE: transcription elongation factor complex (GO:0008023), positive regulation of transcription by pol II (GO:0045944), RNA processing (GO:0006396 TAS), perichromatin fibrils, nuclear matrix, protein-containing complex (generic).
- DNA binding NEGATED (GO:0003677 NOT, IDA, PMID:15107825): ACCEPT the negation — NUFIP stimulates pol II transcription via protein interactions, not direct DNA binding. Keep as-is (negated true).
- synapse / presynaptic active zone (IEA/ISS GO_REF:0000107, PMID:12941608): KEEP_AS_NON_CORE — based on synaptoneurosome association / ortholog transfer; plausible but peripheral.
- protein binding (GO:0005515) — KEEP_AS_NON_CORE (uninformative bare; many high-throughput interactome PMIDs; 28335020=ZNHIT3, 17636026=snoRNP, 25170085=Rsa1/Hit1 yeast homolog context).
