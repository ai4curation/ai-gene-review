# phb-2 (Caenorhabditis elegans) — curation notes

UniProt: P50093 (PHB2_CAEEL) · WormBase: WBGene00004015 · ORF: T24H7.1
Gene: phb-2 (prohibitin-2). Obligate partner of phb-1 in the mitochondrial prohibitin (PHB) ring complex.
294 aa; SPFH/Band-7 (stomatin/prohibitin) superfamily; PANTHER PTHR23222 (PROHIBITIN), subfamily PTHR23222:SF1 (PROHIBITIN-2).

## Protein architecture (from UniProt P50093)
- TRANSMEM 20-42: "Helical; Signal-anchor for type II membrane protein" (single-pass type II membrane protein; N-in/C-out topology places most of the protein on the intermembrane-space side).
- COILED 212-237.
- Keywords: Coiled coil, Membrane, Mitochondrion, Mitochondrion inner membrane, Signal-anchor, Transmembrane, Transmembrane helix.
- SUBCELLULAR LOCATION (UniProt): "Mitochondrion inner membrane; Single-pass type II membrane protein; Intermembrane side" [ECO:0000269|PMID:12794069].
- SUBUNIT (UniProt): "High molecular weight complex that consist of phb-1 and phb-2." [PMID:12794069].
- ComplexPortal CPX-4114 "Prohibitin complex".

## KNOWN (experimentally established)

### The PHB complex: obligate phb-1/phb-2 heterodimeric ring in the inner mitochondrial membrane
- [PMID:12794069 "prohibitins in C. elegans form a high molecular weight complex in the mitochondrial inner membrane similar to that of yeast and humans"] — direct demonstration in worm (BN-PAGE etc.).
- [PMID:12794069 "Prohibitins in eukaryotes consist of two subunits (PHB1 and PHB2) that together form a high molecular weight complex in the mitochondrial inner membrane"].
- [PMID:26092086 "which bind to each other to form a heterodimer that is assembled into a ring-like macromolecular structure at the inner mitochondrial membrane"].
- [PMID:26092086 "These two subunits are interdependent for the formation of the complex, leading the absence of one of them to the absence of the whole complex"] — the two subunits are mutually dependent; loss of one abolishes the whole complex. Same obligate-partner logic as phb-1.
- [PMID:19812672 "form a ring-like, high-molecular-mass complex at the inner membrane of mitochondria"].
- Physical interaction with phb-1 curated as IPI (GO:0035632 mitochondrial prohibitin complex, with WB:WBGene00004014 = phb-1) from PMID:19812672.
- Mammalian ortholog corroboration: [PMID:28017329 "an evolutionarily conserved ~34 kDa protein that forms a large heterodimeric IMM complex with prohibitin 1 (PHB1)"] and [PMID:28017329 "PHB2 are PHB1 are only stable when bound to each other in a heterodimeric state"].

### Essential developmental role (RNAi, worm)
- [PMID:12794069 "PHB proteins are essential during embryonic development and are required for somatic and germline differentiation in the larval gonad"] — source of the WormBase IMP annotations: embryo development ending in birth/egg hatching (GO:0009792), gonad development (GO:0008406), spermatogenesis (GO:0007283), oogenesis (GO:0048477).
- [PMID:12794069 "a deficiency in PHB proteins results in altered mitochondrial biogenesis in body wall muscle cells"] — source of mitochondrion organization (GO:0007005) IMP.
- Additional WormBase IMP behavioural/growth phenotypes scored from full text (not in abstract): defecation (GO:0030421), regulation of nematode pharyngeal pumping (GO:0043051), positive regulation of multicellular organism growth (GO:0040018), regulation of oxidative phosphorylation (GO:0002082), response to oxidative stress (GO:0006979). These are pleiotropic downstream consequences of depleting an essential mitochondrial complex, not dedicated molecular functions.

### Context-dependent modulator of ageing / metabolism
- [PMID:19812672 "the mitochondrial prohibitin complex promotes longevity by modulating mitochondrial function and fat metabolism in the nematode Caenorhabditis elegans"].
- [PMID:19812672 "prohibitin deficiency shortens the lifespan of otherwise wild-type animals"] but [PMID:19812672 "knockdown of prohibitin promotes longevity in diapause mutants or under conditions of dietary restriction"] and [PMID:19812672 "prohibitin deficiency extends the lifespan of animals with compromised mitochondrial function or fat metabolism"].
- [PMID:19812672 "Depletion of prohibitin influences ATP levels, animal fat content and mitochondrial proliferation in a genetic-background- and age-specific manner"].
- Metabolome study frames the complex as a "context-dependent modulator of longevity" (PMID:26092086, title).

### phb-2-SPECIFIC role: inner-membrane mitophagy receptor (distinguishes phb-2 from phb-1)
This is the key functional distinction from phb-1.
- [PMID:28017329 "we identify the inner mitochondrial membrane protein, prohibitin 2 (PHB2), as a crucial mitophagy receptor involved in targeting mitochondria for autophagic degradation"].
- [PMID:28017329 "PHB2 binds the autophagosomal membrane-associated protein LC3 through an LC3-interaction region (LIR) domain upon mitochondrial depolarization and proteasome-dependent outer membrane rupture"].
- Direct/indirect binding asymmetry: [PMID:28017329 "PHB2 interacts directly with LC3-II, whereas PHB1 interacts indirectly with LC3-II as a result of being part of a heterodimeric complex with PHB2"]. LIR mapped to aa 121-124 (YQRL) in human PHB2; this is a PHB2-specific determinant, since the equivalent PHB1 residue does not bind LC3.
- Worm in-vivo requirement (IDA, GO:0000423 mitophagy, PMID:28017329): [PMID:28017329 "paternal inactivation of phb-2 impaired sperm-derived mitochondrial degradation in a manner similar to maternal inactivation of atg-7, a core autophagy gene previously reported to be essential for paternal mitochondrial elimination"] and [PMID:28017329 "Thus, sperm-derived phb-2 is essential for the proper degradation of paternal mitochondria"].
- Framed as conserved: [PMID:28017329 "PHB2 is required for Parkin-induced mitophagy in mammalian cells and for the clearance of paternal mitochondria after embryonic fertilization in C. elegans"].
- NOTE on granularity: the LC3-LIR direct-binding biochemistry was done on the human ortholog; the worm evidence is genetic (paternal phb-2 RNAi blocks sperm-mitochondria clearance). The molecular-function term GO:0140580 (mitochondrion autophagosome adaptor activity) captures this receptor/adaptor role and is a reasonable core MF for phb-2, with the caveat that the direct LC3 binding is inferred from the conserved mammalian ortholog.

### Drug resistance / mitochondrial localization (secondary)
- PMID:20089839: missense mutations in phb-2 (ad2154, ad2155dm) confer resistance to multiple drugs (hemiasterlin etc.) via a ROS-sensitive mechanism. Localization statement: [PMID:20089839 "C. elegans prohibitin-2 (PHB-2), a protein localized to the inner mitochondrial membrane"]. GOA uses this paper as an ISS mitochondrion localization reference.
- PMID:20188671 (HAF-1 mitochondrial UPR paper): the abstract does not mention phb-2; the GOA GO:0005739 mitochondrion HDA annotation is a high-throughput mitochondrial-proteome detection (phb-2 present in isolated mitochondria). Localization is correct but this is a proteome-scale dataset, not a phb-2-focused study.

## NOT known / knowledge gaps
1. **Molecular mechanism of the PHB ring is unresolved** (shared with phb-1). Chaperone/holdase vs membrane/lipid scaffold vs proteostasis regulator (m-AAA protease). [PMID:26092086 "the true function of the mitochondrial prohibitin complex remains elusive"]; proposed roles: [PMID:26092086 "a membrane-bound chaperone, which holds and stabilizes newly synthesised mitochondrial-encoded proteins"] and [PMID:26092086 "as scaffold proteins that recruit membrane proteins to a specific lipid environment"]. Ontology gap: no GO MF term for "structural subunit of the prohibitin ring". Documented in phb-1 review too.
2. **How mitophagy-receptor activity is integrated with the structural/scaffold role of the same protein.** PHB2 is simultaneously an obligate structural ring subunit AND the LC3-binding mitophagy receptor. In mammals the LIR mutation abrogates mitophagy without disturbing the other mitochondrial (cristae/OPA1/proliferation) functions ([PMID:28017329 "the PHB2 LIR mutation does not affect previously described mitochondrial processes controlled by prohibitins, but does abrogate the ability of PHB2 to mediate mitophagy"]) — i.e. separable activities — but whether the worm phb-2 LIR is used the same way in vivo, and how OMM rupture exposes the IMM receptor, remain to be dissected in worm.
3. **Context-dependent longevity paradox** (shared with phb-1): the same complex reduction shortens WT lifespan yet extends it in daf-2/DR/mito-mutant backgrounds; the metabolic node is undefined.

## GO annotation review plan (37 GOA annotations)
- Complex membership GO:0035632 (IDA/IPI) → ACCEPT (core; defining annotation).
- Inner membrane GO:0005743 (IDA/EXP/IEA) → ACCEPT (core localization).
- Mitochondrion GO:0005739 (IBA/IEA/HDA/ISS) → KEEP_AS_NON_CORE (correct but less specific).
- Mitochondrial membrane GO:0031966 (IDA) → KEEP_AS_NON_CORE (less specific than inner membrane).
- Membrane GO:0016020 (IEA InterPro) → MARK_AS_OVER_ANNOTATED (over-general).
- Mitochondrion organization GO:0007005 (IBA/NAS/IMP) → ACCEPT (core process).
- Protein stabilization GO:0050821 (NAS) → ACCEPT non-core / candidate complex-level activity (proposed chaperone role).
- Mitophagy GO:0000423 (IDA, PMID:28017329) → ACCEPT (core, phb-2-specific).
- protein homodimerization activity GO:0042803 (ISS from human Q99623) → review: PHB proteins form phb-1/phb-2 HETERO-dimers; the human ISS "homodimerization" is questionable for the obligate heterodimer. MARK_AS_OVER_ANNOTATED / MODIFY toward the structural/complex role. Avoid uninformative dimerization MF.
- plasma membrane GO:0005886 / cell surface GO:0009986 (ISS from human Q99623) → these transfer human PHB2 cell-surface/plasma-membrane annotations. No worm evidence; the worm protein is an IMM protein. MARK_AS_OVER_ANNOTATED (ISS transfer of a mammalian moonlighting localization not established in worm).
- Pleiotropic developmental/behavioural IMP + ARBA IEA (embryo dev, gonad dev, spermatogenesis, oogenesis, defecation, pharyngeal pumping, growth, oxphos regulation, oxidative-stress response) → KEEP_AS_NON_CORE (experimental annotations retained; downstream consequences of losing an essential complex), matching phb-1 treatment.

## Consistency with phb-1 (PR #1684, branch origin/claude/worm-phb-1-review)
phb-1 modeled with core_functions: structural molecule activity (GO:0005198) + in_complex GO:0035632 + location GO:0005743; second core fn mitochondrion organization + protein stabilization. Same knowledge_gaps (mechanism unresolved; longevity paradox). phb-2 mirrors this but ADDS the distinctive mitophagy-receptor core function (GO:0140580 / GO:0000423), which phb-1 lacks (phb-1 binds LC3 only indirectly).
