# sil1 (SPAC1071.03c) — S. pombe — curation notes

UniProt: Q9UTR0 (`YL33_SCHPO`, "Uncharacterized protein C1071.03c", 338 aa, PE=4 Predicted).
PomBase standard name: **sil1**; product (PomBase): "nucleotide exchange factor for the ER lumenal Hsp70 chaperone, Sil1".
Characterisation status (PomBase): **"biological role inferred"** — i.e. no dedicated experimental characterisation in fission yeast; function assigned by orthology. Deletion viability: **viable**.
Taxonomic distribution (PomBase): eukaryotes only, fungi and metazoa.

## Identity / orthology (KNOWN with high confidence)

- Orthologs (PomBase `ortholog_annotations`): human **SIL1** (HGNC:24624) and *S. cerevisiae* **SIL1/YOL031C** (Sil1p). So the pombe protein is the fission-yeast member of the SIL1/BAP (BiP-associated protein) family.
- UniProt family/domain signatures: InterPro **IPR050693 "SIL1/FES1/HPBP1"**; **IPR011989 ARM-like** and **IPR016024 ARM-type fold**; Gene3D **1.25.10.10 (Leucine-rich Repeat Variant / ARM)**; SUPFAM **SSF48371 ARM repeat**. PANTHER family **PTHR19316 "Hsp70 Nucleotide Exchange Factors and Inhibitors"**, subfamily **PTHR19316:SF18 "HSP70-BINDING PROTEIN 1"**. [file:SCHPO/sil1/sil1-uniprot.txt DR lines]
- The armadillo-repeat/ARM-type fold is the structural hallmark of the SIL1/HspBP1 class of Hsp70 nucleotide-exchange factors (distinct from the Hsp110/Grp170 class and the BAG/GrpE classes).

## Domain / sequence reasoning (inline, from sil1-uniprot.txt)

- 338 aa. UniProt/TMHMM predict a single N-terminal transmembrane / signal-anchor helix (**TRANSMEM 20..40**, ECO:0000255; PomBase TM 20..42, TMHMM). UniProt CC gives SUBCELLULAR LOCATION: Membrane, single-pass membrane protein (ECO:0000305, i.e. inferred, not experimental).
- Interpretation: the N-terminal hydrophobic segment is most consistent with an **ER-targeting signal/signal-anchor** for a lumenal ER protein of the SIL1 family. Canonical Sil1 orthologs are ER-lumenal (S. cerevisiae Sil1p is lumenal with an HDEL-type ER-retention signal; human SIL1 has a cleaved signal peptide and a C-terminal ER-retrieval signal). The pombe C-terminus ends "...PWPKKYNI" — I do **not** see a canonical HDEL/KDEL tetrapeptide, so the exact ER-retention mechanism in pombe is unresolved from sequence alone (a genuine uncertainty; do not over-assert lumenal topology). The UniProt "single-pass membrane protein" call is an automatic ECO:0000305 inference from the one predicted TM and should be read cautiously — for the ER-lumenal SIL1 family this hydrophobic stretch is more likely a signal/anchor than a bona fide type-II membrane topology.
- No catalytic motifs expected: SIL1-family NEFs are non-enzymatic; they act as an ARM-fold "clamp" on the Hsp70 nucleotide-binding domain to accelerate ADP release (nucleotide exchange), not as an enzyme.

## Function (KNOWN by orthology; NOT directly shown in pombe)

The SIL1/Sil1p family are **nucleotide-exchange factors (NEFs) for the ER Hsp70 BiP** (Kar2p in *S. cerevisiae*):

- *S. cerevisiae*: "The chaperone activity of Kar2p is regulated by its intrinsic ATPase activity that can be stimulated by two different nucleotide exchange factors, namely Sil1p and Lhs1p ... the IIB domain of Kar2p is sufficient for binding of Sil1p, and point mutations within IIB specifically blocked Sil1p-dependent activation while remaining competent for activation by Lhs1p." [PMID:20430899 "Interactions between Kar2p and its nucleotide exchange factors Sil1p and Lhs1p are mechanistically distinct", abstract]
  - This establishes both (a) the **adenyl-nucleotide exchange activity on BiP/Kar2** (grounds GO:0000774) and (b) that BiP in yeast has **two functionally distinct NEFs** (Sil1p and Lhs1p) — the basis for the redundancy knowledge gap in pombe (pombe has an Lhs1/Grp170-type NEF too).
- Human SIL1: loss-of-function mutations cause **Marinesco–Sjögren syndrome** (cerebellar ataxia, cataracts, myopathy, intellectual disability); human SIL1 is a BiP NEF. [WebSearch of review literature — e.g. "BiP and its Nucleotide Exchange Factors Grp170 and Sil1", PMC4356644; not cached, used for background only]
- Structural mechanism (Sil1–BiP complex): Sil1 acts as a clamp on the BiP ATPase (nucleotide-binding) domain, rotating lobe IIb away from the ADP-binding pocket to promote nucleotide release. [background, review literature; not cached]

## Pombe-specific evidence (what actually exists for THIS gene)

All pombe annotations for sil1 are indirect (IBA/IEA/ISO) or high-throughput:
- GOA (see sil1-goa.tsv):
  - GO:0000774 adenyl-nucleotide exchange factor activity — **IBA** (GO_REF:0000033), PANTHER PTN007671284 with S. cerevisiae SGD:S000000305, SGD:S000005391 and human UniProtKB:Q9H173.
  - GO:0005783 endoplasmic reticulum — **IBA** (GO_REF:0000033).
  - GO:0016020 membrane — **IEA** (GO_REF:0000044) from UniProt SubCell SL-0162 (the single predicted TM).
  - GO:0006616 SRP-dependent cotranslational protein targeting to membrane, translocation — **ISO** (GO_REF:0000024) transferred from S. cerevisiae SGD:S000005391.
- PomBase phenotypes (all from genome-wide/HTP screens, none a dedicated sil1 study):
  - `sil1Δ` is viable with normal cell morphology (FYPO:0002060/0002177). Deletion collection: PMID:20473289.
  - Broad drug/stress-resistance and -sensitivity phenotypes (e.g. resistance to cadmium/cycloheximide/diamide/hydroxyurea/various salts; sensitivity to bleomycin/brefeldin A/caffeine/EGTA/lithium/X-rays) from phenomics profiling. PMID:37787768 ("Broad functional profiling of fission yeast proteins using phenomics and machine learning") — note this paper explicitly targets *poorly characterized / 'priority unstudied'* proteins.
  - FYPO:0004806 "incomplete cell wall disassembly at cell fusion site" from a mating-morphology screen. PMID:28410370 ("A systematic screen for morphological abnormalities during fission yeast sexual reproduction ...").
  - 13 genetic interactions from network/interactome screens (PMID:23050226, PMID:22681890).
  These are consistent with a general ER-proteostasis housekeeping role (drug/stress pleiotropy, brefeldin-A sensitivity implicating secretory-pathway function) but do **not** independently establish the molecular BiP-NEF activity in pombe.

## KNOWN vs NOT-KNOWN summary

KNOWN (high confidence, by orthology + domain):
- Member of the SIL1/HspBP1 ARM-fold family of Hsp70 nucleotide-exchange factors; ortholog of ScSil1p and human SIL1.
- Expected molecular function: adenyl-nucleotide exchange factor activity on the ER Hsp70 BiP (GO:0000774).
- Expected localization: endoplasmic reticulum (GO:0005783). N-terminal hydrophobic signal/anchor (aa ~20-40).
- Non-essential in pombe (viable deletion).

NOT KNOWN / genuine gaps (pombe-specific):
- No direct biochemical demonstration in *S. pombe* that Sil1 stimulates nucleotide exchange on pombe BiP.
- The pombe BiP partner and the degree of functional redundancy with the pombe Lhs1/Grp170-type NEF are not experimentally defined; whether Sil1 NEF activity is individually required in vivo (vs redundant) is unknown — mirrors the two-NEF (Sil1/Lhs1) situation in *S. cerevisiae*.
- In-vivo clients / physiological pathways (e.g. specific secretory cargo, cell-fusion/cell-wall phenotype mechanism) are not established; phenotype data are HTP-screen-level only.
- Exact membrane topology / ER-retention mechanism (no canonical HDEL/KDEL evident by eye) is unresolved.

## Annotation review plan

- GO:0000774 adenyl-nucleotide exchange factor activity (IBA): ACCEPT as core MF — well-supported by orthology + family; more informative than "protein binding".
- GO:0005783 endoplasmic reticulum (IBA): ACCEPT as core localization.
- GO:0016020 membrane (IEA, SubCell): MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE — derived from a single predicted TM; "membrane" is uninformative and the SIL1 family is ER-lumenal-associated; ER (GO:0005783) is the meaningful compartment. Keep but non-core.
- GO:0006616 SRP-dependent cotranslational protein targeting to membrane, translocation (ISO from Sc): UNDECIDED / KEEP_AS_NON_CORE — this ISO transfer reflects Sil1p's participation in ER protein import as a Kar2p co-factor in *S. cerevisiae*; it is a downstream process attribution, not the core NEF MF, and is not directly shown in pombe. Do not REMOVE (curator ISO from experimental Sc annotation); treat as non-core / process-level.

## References gathered
- PMID:20430899 — Sc Sil1p/Lhs1p NEFs for Kar2p; abstract cached-quotable. HIGH relevance (ortholog function basis).
- PMID:28410370 — pombe mating morphology screen (source of FYPO:0004806). LOW/MEDIUM (HTP phenotype only).
- PMID:37787768 — pombe phenomics/ML broad profiling (source of stress phenotypes; flags sil1 as poorly characterized). LOW/MEDIUM.
- GO_REF:0000033 (IBA), GO_REF:0000024 (ISO), GO_REF:0000044 (SubCell IEA) — evidence pipelines.
