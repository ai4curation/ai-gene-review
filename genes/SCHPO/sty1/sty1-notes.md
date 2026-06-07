# sty1 (Q09892, SPAC24B11.06c) review notes

Sty1 (aka Spc1, Phh1, Hog1-like) is the fission-yeast stress-activated MAP kinase (SAPK), the central effector of the core environmental stress response (CESR). It is the ortholog of S. cerevisiae Hog1 and mammalian p38/JNK.

## Core identity and activation
- MAP kinase of the HOG1 sub-subfamily; dual phosphorylation of the TGY/TXY motif (Thr-171/Tyr-173) activates it. UniProt: "Belongs to the protein kinase superfamily. Ser/Thr protein kinase family. MAP kinase subfamily. HOG1 sub-subfamily." MOD_RES Thr-171 phosphothreonine, Tyr-173 phosphotyrosine.
- Activated by the MAPKK Wis1, negatively regulated by Pyp1/Pyp2 tyrosine phosphatases and PP2C phosphatases. [PMID:7657164 "Pyp1 and Pyp2 are tyrosine-specific MAP kinase phosphatases that inactivate an osmoregulated MAP kinase, Sty1, which acts downstream of the Wis1 MAP kinase kinase to control cell size at division"]
- Activated by multiple stresses (broad p38-like). [PMID:8649397 "we report here that Spc1 is activated by multiple forms of stress, including high temperature and oxidative stress. In this regard Spc1 is more similar to mammalian p38"] [PMID:9136929 "Sty1 is activated by a range of environmental insults including osmotic stress, hydrogen peroxide, menadione, heat shock, and the protein synthesis inhibitor anisomycin"]

## Cascade / two-component upstream
- Mcs4 response regulator -> Wak1/Wis4 + Win1 MAPKKKs -> Wis1 MAPKK -> Sty1. [PMID:9136929 "Mcs4 acts upstream of Wak1... which transmits the stress signal to the Wis1 MEK"]
- p38MAPK cascade (GO:0038066) annotations rest on this established cascade.

## Downstream / transcription
- Phosphorylates bZIP TF Atf1; Atf1 is the key nuclear substrate. [PMID:8824588 "Atf1 associates stably and is phosphorylated by the Sty1 kinase in vitro"] [PMID:8824587 "Spc1 is required for stress-induced phosphorylation of Atf1. Atf1 is required for induction of meiotic genes and stress-response genes, such as gpd1+ and pyp2+, that are transcriptionally regulated by Spc1"]
- Drives transcription of CESR genes (gpd1, tps1, ctt1/catalase, pyp2). [PMID:8649397] [PMID:8824588]
- Regulates Pap1 oxidative-stress TF localization (nuclear accumulation upon oxidative stress, Crm1-dependent export). [PMID:9585505 "On imposition of oxidative stress, the Pap1 protein relocalizes from the cytoplasm to the nucleus in a process that is dependent on the Sty1 kinase"]
- Directly binds Rpb1-CTD and phosphorylates Ser5 of the Pol II CTD heptapeptide at stress promoters. [PMID:33410907 "Anchored Sty1 recruits Pol II through direct association with Rpb1-CTD and phosphorylates the reiterated heptad sequence at Serine 5"] -> grounds GO:0008353 RNA pol II CTD kinase activity AND chromatin localization.
- Phosphorylates Lsk1 (CTDK-I catalytic subunit) promoting Ser2 CTD phosphorylation for ste11 transcription during meiosis. [PMID:22144909 "Sty1 phosphorylates Lsk1, the catalytic subunit of CTDK-I"]

## Localization
- Cytoplasmic in unstressed cells; rapid transient nuclear accumulation on stress, requires Wis1 phosphorylation and Atf1 retention. [PMID:9585506 "Stress induces transient nuclear localization of Spc1... Nuclear retention of Spc1 requires Atf1"]
- Active nucleocytoplasmic shuttling (Pim1 import, Crm1 export). [PMID:10233152 "Nuclear import of Spc1 requires Pim1... Nuclear export of Spc1 is regulated by the export factor Crm1"]
- A fraction localizes to mitochondria (regulated by mitochondrial PP2C Ptc4). [PMID:22139357 "A fraction of Sty1 also localizes to the mitochondria"] -> grounds GO:0005758 mitochondrial intermembrane space (IDA) and GO:1903715 aerobic respiration.
- Cytoplasmic stress granule localization under stress (large scale / Puf2 study). [PMID:32071154]

## Cell-cycle control (G2/M)
- Promotes mitotic entry under normal/stress conditions; sty1 mutants have G2 delay. [PMID:7501024 "Spc1 promotes the onset of mitosis... Fission yeast spc1- mutants have a G2 delay that is greatly exacerbated by growth in high osmolarity media and nutrient limitation"]
- Also negatively regulates G2/M via Srk1 -> Cdc25 inhibition, and via Rad24/14-3-3. [PMID:18272791 "activation of Srk1 kinase, which negatively regulates cell cycle progression by inhibiting Cdc25"] [PMID:29065217 "its function as a mitotic inhibitor is very important... Spc1 targets the 14-3-3 protein, Rad24, independently of Srk1, leading to relocalization of Cdc25 and mitotic inhibition"]
- Dual role (both positive and negative regulation of G2/M) is genuine and context dependent.

## Sexual differentiation / meiosis
- Required for sexual development under nitrogen starvation; needed for ste11 induction and mating. [PMID:8824587 "Mutant spc1- cells are defective at arresting in G2 during nitrogen starvation and exhibit a poor mating ability"]
- Negatively regulates conjugation under non-starvation via Srk1. [PMID:12080074 "overexpression of srk1+ inhibits the nitrogen starvation-induced arrest in G1"] (Srk1 negatively regulates entry into sexual development; sty1 acts through Srk1.)
- Regulates ade6-M26 meiotic recombination hotspot via Atf1(Mts1) phosphorylation. [PMID:9819443 "protein-DNA interaction within cells is dependent upon the Spc1 MAP kinase, which phosphorylates the Mts1 protein"] -> grounds GO:0010520 regulation of reciprocal meiotic recombination and GO:0051445 regulation of meiotic cell cycle.

## Other processes
- Translation adaptation: binds eEF2/eIF3a; sty1 mutants recover translation poorly after stress. [PMID:18065650 "We find Sty1... to bind to the translation elongation factor... eEF2... and the translation initiation factor... eIF3a"] -> grounds GO:1990625 neg reg of cytoplasmic translational initiation in response to stress.
- Actomyosin ring integrity: SAPK downregulates CAR assembly by reducing For3 under stress. [PMID:32915139 "the SAPK pathway and its effector, MAPK Sty1, downregulates CAR assembly in S. pombe when its integrity becomes compromised... by reducing For3 levels"] -> grounds GO:1903500.
- Heterochromatin (mating-type silencing): MAPK pathway + Atf1/Pcr1 phosphorylation promote Swi6/HP1 heterochromatin assembly at mat locus. [PMID:15292231 "a phosphorylation event catalyzed by the conserved mitogen-activated protein kinase pathway is important for regulation of heterochromatin silencing by Atf1 and Pcr1"] -> grounds GO:0090055.
- Positive regulation of protein import into nucleus: Sty1 required for stress-induced nuclear accumulation of Pap1. [PMID:9585505] -> grounds GO:0042307.

## Interaction partners (for protein binding IPI annotations)
- Atf1 (P52890), Srk1 (O94547), Sin1 (SPAC19D5.01), Cmk2, Hal4 (SPAC23A1.06c / Cmk2 SPAC2... ), Ptc4 (O14156), Pin1 (SPBC28F2.12), Rnc1 (SPCC757.09c), Cdc37 etc. UniProt SUBUNIT: "Interacts with cdc37, cmk2, hal4, sin1 and srk1."
- protein binding (GO:0005515) IPI annotations are uninformative per curation guidelines; recommend replacing/keeping non-core in favor of specific MF where the partner is a substrate.

## Assessment summary
- Core MF: MAP kinase activity (GO:0004707) — strongly supported by many IDA papers. protein serine/threonine kinase activity acceptable parent. RNA pol II CTD kinase activity is a genuine specific MF (PMID:33410907).
- Core BP: stress-activated MAPK cascade / p38MAPK cascade; cellular response to osmotic and oxidative stress; regulation of G2/M.
- Over-general/uninformative: bare "protein binding" (many IPI) — KEEP_AS_NON_CORE / note guidance.
- IEA "protein kinase activity" (GO:0004672) is a less-informative parent of MAP kinase activity -> MODIFY/over-annotated relative to MAP kinase activity but acceptable as general.
