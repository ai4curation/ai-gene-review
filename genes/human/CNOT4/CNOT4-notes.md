# CNOT4 (O95628) review notes

## Identity
- Human CCR4-NOT transcription complex subunit 4 (CNOT4 / NOT4), HGNC:7880, UniProt O95628, gene ID 4850, chromosome 7.
- 575 aa (isoform 1). Domain architecture: N-terminal atypical C4C4 RING-type zinc finger (aa 14-57), RRM (aa 109-189), C3H1-type zinc finger (aa 190-217), predicted coiled-coil (aa 68-104), large disordered C-terminus [file:human/CNOT4/CNOT4-uniprot.txt].
- 10 alternative-splicing isoforms.

## Core molecular function: RING E3 ubiquitin ligase
- CNOT4 RING finger is a C4C4-type that is the first shown to use exclusively cysteines for metal binding; NMR structure of aa 1-78 determined [PMID:11087754 "The structure of the C4C4 ring finger of human NOT4 reveals features distinct from those of C3HC4 RING fingers"].
- CNOT4 functions as an E2-dependent RING E3 ubiquitin-protein ligase. Its C4C4 RING interacts with a subset of E2s (UBC4/5 subfamily: UbcH5B, UbcH6, UbcH9) and is a potent E3 in vitro that catalyzes assembly of polyubiquitin chains in a UbcH5B-dependent manner [PMID:11823428 "We demonstrate that CNOT4 functions as a ubiquitin-protein ligase (E3)... CNOT4 acts as a potent E3 ligase in vitro. Mutations that destabilize the E2-E3 interface abolish this activity"].
- RING residues critical for E2 (UbcH5B/UBE2D2) interaction mapped by mutagenesis: L16, C17, M18, C33, W42, R44, I45, E49, P54, R57 [file:human/CNOT4/CNOT4-uniprot.txt MUTAGEN]. Charge-swap of CNOT4 E49 + UbcH5B K63 restores binding, demonstrating a specific electrostatic E2-E3 interface [PMID:15001359 "Concomitant charge-alteration of E49 of CNOT4 and K63 of UbcH5B restored binding and re-created a functional enzyme pair"].
- CNOT4 is autoubiquitinated in vitro (PTM: autoubiquitinated) [PMID:11823428; PMID:15001359].
- EC 2.3.2.27 (RING-type E3 ubiquitin transferase) [file:human/CNOT4/CNOT4-uniprot.txt].

## E2 specificity / molecular partner
- Binds UBE2D2 (UbcH5B) via RING domain — a specific ubiquitin-conjugating enzyme binding function, not generic protein binding [PMID:15001359 "binding of the CNOT4 RING finger to the ubiquitin-conjugating enzyme (E2) UbcH5B is highly selective"; file:human/CNOT4/CNOT4-uniprot.txt SUBUNIT "Interacts (via RING domain) with UBE2D2"]. GOA records this E2 (UBE2D2 = P62837) as the IPI "protein binding" partner for PMID:15001359 [file:human/CNOT4/CNOT4-goa.tsv line WITH/FROM UniProtKB:P62837].

## Substrate ubiquitination events
- Ubiquitinates methylated RBM15: PRMT1 methylates RBM15, which is then ubiquitinated by CNOT4, controlling RBM15 turnover and RNA splicing; this regulates megakaryocyte differentiation. RBM15 = Q96T37 (the IPI partner in GOA for PMID:26575292) [PMID:26575292 "Cross-talk between PRMT1-mediated methylation and ubiquitylation on RBM15 controls RNA splicing"; file:human/CNOT4/CNOT4-goa.tsv WITH/FROM UniProtKB:Q96T37].
- Ubiquitinates ABCE1 (K48-linked) in response to mitochondrial damage. As part of co-translational/no-go decay quality control, CNOT4 (NOT4) is recruited with Pelo and ABCE1 to stalled mitochondrial outer-membrane-associated mRNPs and directly poly-ubiquitinates ABCE1 (primarily K48-linked, shown by in vitro ubiquitination with purified NOT4 as E3 and ABCE1 as substrate), generating a poly-Ub signal that recruits autophagy receptors to initiate PINK1-directed mitophagy [PMID:29861391 "Damage-induced ubiquitination of ABCE1 by NOT4 generates poly-ubiquitin signals that attract autophagy receptors to MOM to initiate mitophagy"; "NOT4 was able to directly ubiquitinate ABCE1 in vitro... ubiquitination of ABCE1 by NOT4 in vitro occurs primarily via K48-linked modification"]. Interacts with ABCE1, PINK1, PELO [file:human/CNOT4/CNOT4-uniprot.txt SUBUNIT].
- Background: yeast/Drosophila Not4 acts as a ribosome-associated E3 that ubiquitinates nascent chains / ribosomal proteins on stalled ribosomes (cited within PMID:29861391: "could also act as a ribosome-associated E3 ligase that targets NPCs on stalled ribosomes for ubiquitination and degradation (Dimitrova et al., 2009)").

## Relationship to CCR4-NOT complex (deadenylase)
- CNOT4 is the human ortholog of yeast Not4, a CCR4-NOT subunit. CCR4-NOT is the major eukaryotic mRNA deadenylase / global regulator of mRNA synthesis and decay.
- Key caveat: in human (and Drosophila) cells CNOT4/NOT4 is NOT stably incorporated into the CCR4-NOT holocomplex; it is only loosely/transiently/substoichiometrically associated. The conserved stable core is NOT1, NOT2, NOT3, CAF40, plus the CCR4a/b (CNOT6/6L) and CAF1 (CNOT7/8) deadenylases and NOT10/NOT11 [PMID:31320642 "the NOT4 subunit, which functions as an E2-dependent RING E3 ligase. It is stably incorporated within the yeast Ccr4-Not but not in Drosophila S2 and human cells"; UniProt SUBUNIT "Interacts with CNOT1 via its C-terminus but does not stably associate with the CCR4-NOT complex" (PMID:11823428)].
- Human CNOT4 was found in a separate ~200 kDa complex distinct from the core CCR4-NOT [PMID:19558367 "human CNOT4 is in a separate approximately 200 kDa complex"].
- CNOT4 contributes a CAF40-binding motif (CBM) at its C-terminus that binds the CAF40 subunit and can inhibit deadenylation, like other recruitment-factor CBMs [PMID:31320642 "a CBM from the C-terminus of NOT4 which binds to the same surface as the Bam CBM... peptide motifs from all three factors inhibit CCR4-NOT-mediated deadenylation in vitro"].
- The reconstituted recombinant human CCR4-NOT (PMID:31320642) did NOT include CNOT4; deadenylation/poly(A) tail shortening is catalyzed by CCR4a/CAF1 stimulated by NOT/CAF40 modules. So the NAS "nuclear-transcribed mRNA poly(A) tail shortening" (GO:0000289, ComplexPortal, PMID:31320642) is a complex-level/membership-derived annotation, not a CNOT4 catalytic activity.

## RNA binding
- CNOT4 has an RRM. It was captured as an mRNA-bound protein in mRNA interactome capture (HeLa polyA+ RNA crosslink) [PMID:22681889 "The mRNA-bound proteome and its global occupancy profile on protein-coding transcripts" — HDA RNA binding]. Direct RNA binding plausible via RRM but not deeply functionally characterized.

## Other / signaling
- Reported to enhance JAK/STAT pathway-dependent gene expression in Drosophila and human cells [PMID:22159038 (Gronholm et al., FASEB J 2012); cited in UniProt FUNCTION]. Publication not cached; treat as context, not core.

## Localization
- Cytoplasm and nucleus (UniProt, ECO:0000305). Associated with P-bodies and stress granules (CD-CODE) [file:human/CNOT4/CNOT4-uniprot.txt]. Cytosol annotations (Reactome TAS, ARBA) consistent.

## Interactome caveat
- PMID:32296183 (HuRI binary interactome): isoform O95628-2 vs IL36RN (Q9UBH0) is a high-throughput Y2H binary interaction with no functional/biological context; generic "protein binding" with low informativeness.

## Summary of core functions
1. RING-type E3 ubiquitin-protein ligase (C4C4 RING) that pairs specifically with UBE2D/UbcH5-family E2 enzymes (MF: ubiquitin protein ligase activity GO:0061630; ubiquitin conjugating enzyme binding GO:0031624).
2. Substrate ubiquitination in quality-control / regulatory contexts: ABCE1 (K48-linked, co-translational QC → mitophagy) and methylated RBM15 (splicing / megakaryocyte differentiation).
3. Peripheral/substoichiometric subunit of the CCR4-NOT mRNA deadenylase complex (membership real but loose; deadenylation is not a CNOT4 catalytic activity).
