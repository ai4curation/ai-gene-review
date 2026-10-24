# APC2 (S. cerevisiae, Q12440) - review notes

## Identity
- YLR127C / RSI1 / APC2; 853 aa; cullin family (UniProt PROSITE ProRule PRU00330). Ortholog of human ANAPC2.
- Founding papers: Kramer et al. 1998 [PMID:9430641 "Temperature-sensitive rsi1/apc2 mutants arrest in metaphase and are unable to degrade Clb2p, suggesting that Rsi1p/Apc2p is associated with the anaphase promoting complex (APC)."] and Zachariae et al. 1998 [PMID:9469814 "Apc2p is similar to the cullin Cdc53p, which is a subunit of the ubiquitin-protein ligase complex SCFCdc4 required for the initiation of DNA replication."].
- Inputs used: UniProt record, GOA tsv, falcon deep research (Edison), cached publications. Abstract-only in cache: PMID:9430641, PMID:9469814, PMID:12477395, PMID:12609981. Full text: PMID:16481473, PMID:11114178, PMID:19109423, PMID:37968396, PMID:10888670, PMID:19822757. Not cached (cited only via the deep-research file): Melloy & Holloway 2004 Genetics (Cdc23/Apc9 localisation), Vazquez-Fernandez et al. 2024 eLife (yeast APC/C cryo-EM), Rodrigo-Brenni & Morgan 2007 (Ubc4/Ubc1 K48 chains).

## Molecular role
- Apc2 + Apc11 = cullin-RING catalytic core; Apc1 bridges the Apc2/Apc11/Doc1 subcomplex to the TPR subcomplex [PMID:16481473 "one that contains Apc2 (Cullin), Apc11 (RING), and Doc1/Apc10, and another that contains the three TPR subunits (Cdc27, Cdc16, and Cdc23)"].
- apc2 delta loses Apc11 and Doc1 completely; apc11 delta only partially reduces Apc2/Doc1 [PMID:16481473 "These data suggest that Apc2 independently tethers Doc1 and Apc11."].
- Apc2 needed for Cdh1 binding (10-fold drop in apc2 delta) [PMID:16481473 "These data suggest that Apc2 is required for efficient Cdh1 binding to the APC."].
- apc2 delta APC/C has no detectable ligase activity in vitro [PMID:16481473 "Of the mutant complexes, only cdc27 Δ APC displayed detectable activity against Pds1"].
- Apc11 alone transfers ubiquitin; Apc2 not required in the minimal system, proposed to tether/position Apc11 [PMID:10888670 "While Apc2p was not required to effect ubiquitin transfer in vitro, it may function in a cellular context to tether Apc11p to APC core proteins, and to properly position the Apc11p RING-H2 finger with respect to its substrates."]. Hence contributes_to (not enables) for GO:0061630, and the NEW GO:0160072 ubiquitin ligase complex scaffold activity row (same term used for human ANAPC2 in this repo).
- Chain linkage: yeast APC/C uses Ubc4 (initiation) and Ubc1 (elongation) and builds K48 chains; no Ube2S ortholog [PMID:19822757 "However, Ubc4 and Ubc1 function sequentially to assemble K48-linked ubiquitin chains, whereas human UbcH10 and Ube2S most likely bind APC/C at the same time."]. This is the basis for MODIFY of the K11 IBA (GO:0070979 -> GO:0070936 / GO:0000209).
- Deep research: yeast Apc2 lacks the 45-residue four-cysteine zinc-binding insert of human APC2; apo yeast APC/C already holds the Apc2:Apc11 module in an E2-compatible position (Vazquez-Fernandez 2024, via deep-research file).

## Biological outputs
- Metaphase/anaphase: rsi1/apc2 ts arrest bypassed by pds1 delta [PMID:9430641 "Indeed, the anaphase block in rsi1/apc2 temperature-sensitive mutants is overcome by removal of PDS1, consistent with Rsi1p/Apc2p being part of the APC."].
- Mitotic exit: Clb2 stabilised; sic1 delta synthetic lethal [PMID:9430641 "In addition, like our rsi1/apc2 mutations, cdc23-1, encoding a known APC subunit, is also lethal with sic1Delta."]; rsi1-8 pds1 delta cells arrest in telophase (deep-research summary of the full text).
- Securin and B-type cyclins are the only obligatory APC/C targets [PMID:16481473 "Previously, we showed that the only obligatory targets of the APC for cell cycle progression are securin and the B-type cyclins"].
- Cytokinesis: apc2 delta (APC-nonessential background) delays Myo1 disassembly after ring contraction; contraction itself is normal without Cdh1 [PMID:19109423 "In the apc2 Δ strain, Myo1 patches persisted for ≥10 min after the end of ring contraction (Supplemental Figure S3B), supporting the hypothesis that the APC, with its activator Cdh1, is required for proper disassembly of Myo1-containing structures after actomyosin-ring contraction."]. GO:1903473 (positive regulation of ring contraction) therefore misfits; MODIFY to GO:0044837, following the CDH1 review precedent.
- Meiosis: Ama1 is the meiotic coactivator [PMID:11114178 "In conclusion, this study indicates that Ama1p directs a meiotic APC/C that functions solely outside mitotic cell division."]; Apc2 is present in meiotic APC/C preparations [PMID:12609981 "Both proteins were present in APC preparations from haploid cells arrested in G(1), S, and M phases and from meiotic diploid cells, indicating that they are constitutive components of the complex throughout the yeast cell cycle."]. No Apc2-specific meiotic data -> KEEP_AS_NON_CORE for GO:0051445.

## Localisation
- UniProt (Huh 2003 GFP): cytoplasm and nucleus. Tagged Cdc23/Apc9 predominantly nuclear with kinetochore/spindle foci (Melloy 2004, via deep-research file). Nucleus accepted as core site; cytoplasm kept non-core.

## Curation decisions (summary)
- GO:0005515 x3 (IntAct, Mnd2): REMOVE per protein-binding policy; the pairs are co-complex membership (Hall 2003 lists Cdc23/Apc5/Apc1, not Apc2, as direct Mnd2 partners [PMID:12609981 "Mnd2 interacted strongly with Cdc23, Apc5, and Apc1 when coexpressed in an in vitro transcription/translation reaction."]).
- GO:0005680 x5, GO:0007091 x2, GO:0010458, GO:0016567 x5, GO:0031145 x5, GO:0061630 (contributes_to), GO:0005634: ACCEPT.
- GO:0005737, GO:0051445: KEEP_AS_NON_CORE.
- GO:0007346 (ComplexPortal NAS): MODIFY -> GO:0007091 + GO:0010458 (too shallow).
- GO:0070979 IBA: MODIFY -> GO:0070936 / GO:0000209 (lineage divergence; propagation_review recorded).
- GO:1903473 IMP: MODIFY -> GO:0044837.
- NEW: GO:0160072 ubiquitin ligase complex scaffold activity, IDA PMID:16481473.
