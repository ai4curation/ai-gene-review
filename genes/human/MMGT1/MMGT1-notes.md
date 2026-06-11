# MMGT1 (EMC5) review notes

UniProt: Q8N4V1 (EMC5_HUMAN). 131 aa, 2-TM (TM 4-22, 44-63), N-cyt/C-cyt topology with a small lumenal loop. Gene on chromosome X. HGNC symbol MMGT1; established alias EMC5; legacy alias TMEM32.

## Core identity: EMC5, a small membrane subunit of the ER membrane protein complex (EMC)

- UniProt RecName is now "ER membrane protein complex subunit 5", with EMC5 cited from the insertase paper [PMID:29242231]. The MMGT1 / "membrane magnesium transporter 1" / TMEM32 names are legacy HGNC names.
- EMC is a ~9-10 subunit ER membrane insertase. The catalytic insertase core is EMC3 (YidC/Get1-like) plus EMC6; EMC5/MMGT1 is one of the small membrane subunits, not the catalytic subunit. EMC5 packs against EMC3/EMC6 in the cryo-EM structures (PDB 6WW7, 6Z3W, etc.).
- Function (UniProt): "Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins" [file:human/MMGT1/MMGT1-uniprot.txt].
- EMC inserts tail-anchored (TA) proteins of moderate/low hydrophobicity post-translationally, and cotranslationally inserts the first TMD (signal-anchor) of multipass proteins such as GPCRs, controlling N-exo topology.

## Experimental basis (EMC role)

- [PMID:22119785 Christianson et al. 2011] identified MMGT1/EMC5 as a component of the EMC during ERAD network mapping; basis for EMC complex membership (IDA, GO:0072546) and ER membrane localization (EXP, GO:0005789).
- [PMID:29242231 Guna et al. 2018 "The ER membrane protein complex is a transmembrane domain insertase"] — directly implicates EMC5: "we initially noticed that SQS insertion was partially impaired when the EMC5 subunit of EMC was depleted with siRNAs"; "Ablation of EMC5 or EMC6 expression by gene editing ... reduced insertion of SQS". Establishes EMC as a TA-protein insertase, reconstituted with purified complex. Basis for GO:0071816, GO:0045050 IDA/IMP, and EMC membership NAS.
- [PMID:29809151 Shurtleff et al. 2018] — EMC "binds to and promotes the biogenesis of a range of multipass transmembrane proteins, with a particular enrichment for transporters"; engages clients cotranslationally. Basis for GO:0045050 IMP and GO:0032977 membrane insertase activity (contributes_to) IMP.
- [PMID:30415835 Chitwood et al. 2018] — EMC inserts the first TMD of GPCRs co-translationally, cooperating with Sec61 to set topology. Basis for GO:0045050 IMP and GO:0032977 contributes_to IMP.
- [PMID:32439656 Pleiner et al. 2020] and PMID:32459176 O'Donnell et al. 2020 — cryo-EM structures of human EMC; defined EMC5 topology (TM helices, N-cyt/C-cyt). Basis for ER membrane IDA (GO:0005789) and EMC membership IPI (GO:0072546).
- [PMID:34918864 Gaspar et al. 2022] — Drosophila EMC (incl. EMC5/EMC6) required for biogenesis of TA proteins fan and Xport-A; EMC5 depletion in testis renders flies infertile. FlyBase-assigned IMP for GO:0032977 (contributes_to) and GO:0071816. Although Drosophila-focused, this is a curator (FlyBase) experimental annotation; not removed.

## Magnesium / metal-transporter annotations are legacy over-annotations

- The "membrane magnesium transporter 1" name and the magnesium/cobalt/iron transmembrane-transporter GO annotations trace to the mouse ortholog (UniProtKB:Q8K273), originally from overexpression electrophysiology (Goytain & Quamme, who reported Mg2+ currents on overexpression of MMgT1/MMgT2). UniProt records only: "May be involved in Mg(2+) transport (By similarity)" [file:human/MMGT1/MMGT1-uniprot.txt] and SIMILARITY "Belongs to the membrane magnesium transporter (TC 1.A.67) family" [file:human/MMGT1/MMGT1-uniprot.txt].
- In GOA, all the metal/transmembrane-transport annotations are electronic or ISS, propagated from Q8K273:
  - GO:0015095 magnesium ion transmembrane transporter activity — ISS (GO_REF:0000024) and IEA (GO_REF:0000107, from Q8K273).
  - GO:0015693 magnesium ion transport — ISS (GO_REF:0000024).
  - GO:1903830 magnesium ion transmembrane transport — IEA (GO_REF:0000108, inter-ontology link from GO:0015095).
  - GO:0015087 cobalt transporter activity / GO:0006824 cobalt ion transport — IEA from Q8K273 / inter-ontology.
  - GO:0015093 ferrous iron transporter activity / GO:0034755 iron ion transmembrane transport — IEA from Q8K273 / inter-ontology.
  - GO:0022857 transmembrane transporter activity (IBA, IEA) and GO:0055085 transmembrane transport (IEA) — generic, derived from the same transporter-family inference.
- There is no direct experimental evidence that human EMC5 is a magnesium (or cobalt/iron) channel/transporter. The consensus role is as an EMC insertase subunit. The original overexpression electrophysiology has not been reproduced as a channel function, and the protein has no recognizable channel/transporter active site; the metal currents are most parsimoniously an overexpression artifact or indirect. These annotations are marked MARK_AS_OVER_ANNOTATED (the metal-transporter MF/BP terms) and the generic transmembrane-transporter terms KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED. Magnesium transport is NOT a core function.

## Localization

- ER membrane is the principal site (EXP PMID:22119785; IDA PMID:32439656; NAS PMID:29242231). UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane".
- Golgi apparatus membrane and early endosome membrane are ISS/IEA from the mouse ortholog Q8K273 (UniProt lists them as By similarity). Kept as non-core: plausible but the dominant, functionally relevant compartment is the ER. Plasma membrane (IBA/IEA) is weakly supported and likely reflects transporter-family phylogenetic inference; kept as non-core / over-annotated.

## Protein binding (IPI) annotations

- The numerous GO:0005515 IPI annotations (PMID:22119785, 26496610, 28514442, 32296183, 32439656, 33961781, 35271311, 40355756) come from high-throughput interactome / affinity studies. The cached texts do not name EMC5/MMGT1 specifically (large-scale screens). The most informative partners (EMC2 Q15006, EMC6 Q9BV81) reflect EMC complex assembly. Bare "protein binding" is uninformative per curation guidelines → KEEP_AS_NON_CORE; the EMC complex membership term (GO:0072546) captures the informative content.

## Core functions (synthesis)

1. Structural subunit of the EMC (GO:0072546, part_of) in the ER membrane (GO:0005789).
2. As an EMC subunit, contributes to membrane protein insertion into the ER membrane: tail-anchored protein insertion (GO:0071816) and protein insertion by stop-transfer membrane-anchor sequence (GO:0045050), i.e. the EMC insertase activity (GO:0032977, contributes_to).

Magnesium transport: explicitly NOT a core function (legacy/contested).
