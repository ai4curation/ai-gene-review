# CCNB1 (human, cyclin B1, UniProt P14635) — curation notes

## Identity
- HGNC:1579, gene CCNB1, 433 aa, cyclin family / Cyclin AB subfamily.
- The principal mitotic B-type cyclin. Non-enzymatic regulatory subunit of CDK1 (CDC2); the cyclin B1–CDK1 holoenzyme is historically "M-phase / maturation promoting factor" (MPF).
- UniProt FUNCTION: "Essential for the control of the cell cycle at the G2/M (mitosis) transition ... Binds and activates cyclin-dependent protein kinase CDK1/CDC2" [UniProt P14635, PMID:41100585].

## Core biology (holistic synthesis)
- Cyclin B1 accumulates through G2 and is abruptly destroyed at mitosis [PMID:2570636 "Accumulates steadily during G2 and is abruptly destroyed at mitosis"].
- Binds CDK1, induces the active kinase conformation, and confers substrate specificity and localization on the kinase. It is NOT itself a catalyst — the phosphotransfer is performed by the cyclin B1–CDK1 complex.
- Brown et al. 2007: "The cyclins activate their respective CDKs and confer substrate recognition properties" and "cyclin B confers M phase-like properties on CDK2" [PMID:17495531].
- Localization is dynamic and integral to function: cytoplasmic in interphase, shuttles through the nucleus, accumulates in the nucleus at prophase (after CDK1 phosphorylation of the cytoplasmic-retention/NES region), and localizes to centrosomes, spindle microtubules, condensed chromosomes and unattached kinetochores in mitosis.
- Jackman et al. 2003: "Cyclin B1-Cdk1 is the key initiator of mitosis" and "cyclin B1 is initially phosphorylated on centrosomes in prophase" — active complex first appears on centrosomes [PMID:12524548].
- Chen et al. 2008: "cyclin B1 is concentrated on the outer plate of the kinetochore during prometaphase"; siRNA depletion "causes inefficient attachment between kinetochores and microtubules, and chromosome alignment defects, and delays the onset of anaphase" [PMID:18195732]. Basis for kinetochore/spindle-pole localization and mitotic spindle/attachment/SAC IMP annotations.
- Destroyed at anaphase by APC/C–CDC20-dependent ubiquitination; loss of cyclin B1 inactivates CDK1 and triggers mitotic exit. (Note: in mitotic exit cyclin B1 is the SUBSTRATE of APC/C, not the executor of proteolysis — so "mitotic exit" is not proposed as a NEW participation term.)
- Confers substrate specificity toward mitotic substrates: e.g. separase regulation — "Ubiquitin-mediated destruction of securin and cyclin B1 unleashes separase in late metaphase" [PMID:34290405]; nuclear lamin phosphorylation [PMID:17495531].

## Moonlighting / non-core
- A fraction of cyclin B1/CDK1 localizes to the mitochondrial matrix and phosphorylates complex I subunits, enhancing respiration for G2/M — Wang et al. 2014: "a fraction of cyclin B1/Cdk1 proteins localizes to the matrix of mitochondria and phosphorylates a cluster of mitochondrial proteins, including the complex I (CI) subunits" and "Cyclin B1/Cdk1-mediated CI phosphorylation enhances CI activity" [PMID:24746669]. Supports mitochondrial matrix (colocalizes_with), positive regulation of mitochondrial ATP synthesis coupled electron transport, and positive regulation of G2/M (IDA) annotations. Treated as non-core.
- PTCH1 (patched) interaction regulating cyclin B1 localization: "we identified a novel interaction between cyclin B1 and patched1 (ptc1)" [PMID:11331587]; GRK2 modulates the PTCH1–cyclin B1 interaction [PMID:19502428]. Kept as non-core patched binding.

## Curation decisions summary
- Core MF: GO:0061575 cyclin-dependent protein serine/threonine kinase activator activity (IDA) and GO:0016538 regulator activity (IBA/IEA) — ACCEPT.
- Core BP: GO:0000086 G2/M transition — ACCEPT; downstream experimental mitotic IMPs (spindle organization, metaphase chromosome alignment, attachment of spindle MT to kinetochore, SAC regulation, positive regulation of mitotic cell cycle) from Chen 2008 — ACCEPT (defer to curator; full text read).
- Complex: GO:0097125 cyclin B1-CDK1 complex — ACCEPT.
- Localization (nucleus, cytoplasm, cytosol, nucleoplasm, centrosome, MTOC, spindle pole, outer kinetochore) — ACCEPT.
- GO:0005515 protein binding (48 IPI rows): REMOVE per project policy — generic, uninformative; the informative activity is captured by the kinase regulator/activator MF terms. The individual interactions (CDK1, PKMYT1, CDK5, PTCH1, DEDD, CDK5RAP3, HEI10/CCNB1IP1, UBE2K/Hip2, INCA1, UHRF2/NIRF, CDKN1B, UCH-L1, etc.) are not disputed. protein kinase binding (GO:0019901) and patched binding (GO:0005113) are MORE specific and retained.
- G1/S transition (GO:0000082, IBA): MARK_AS_OVER_ANNOTATED — the ancestral PANTHER cyclin node (PTN000019791) spans G1/S (cyclin E/A/D) and mitotic (cyclin A/B) cyclins; G1/S commitment is a cyclin E/A function that has functionally diverged and is not a cyclin B1 role.
- membrane (GO:0016020, IEA from rat ortholog): REMOVE — cyclin B1 has no transmembrane/signal features; spurious localization transfer.
- Rat-ortholog IEA pleiotropic/response terms (response to xenobiotic/mechanical/toxic/DDT/iron/fatty acid/hypoxia, negative regulation of gene expression, positive regulation of mRNA 3'-end processing, tissue regeneration, digestive tract development, ventricular cardiac muscle cell development, positive regulation of cardiac muscle cell proliferation, protein-containing complex assembly): MARK_AS_OVER_ANNOTATED — these reflect abundance/expression responses or indirect proliferation effects, not participation by cyclin B1 in the process.
- oocyte maturation, spermatogenesis, regulation of chromosome condensation (IEA from rat): KEEP_AS_NON_CORE — genuine conserved meiotic-MPF / condensin-related roles but developmental/context-specific and electronically transferred.
- mitochondrial matrix / positive regulation of mitochondrial ATP synthesis coupled electron transport / positive regulation of G2/M (Wang 2014): mito IDA ACCEPT (direct), mito IBA/IEA KEEP_AS_NON_CORE; moonlighting.

## NEW terms considered and rejected
- "mitotic exit" / APC/C-dependent catabolism: cyclin B1 is the substrate destroyed by APC/C, not the executor — necessity ≠ participation. Not proposed.
- No NEW annotations added; existing set adequately covers established functions.
</content>
