# PNP (human, P00491) — curation notes

## Provenance / research status
- Deep research (falcon) FAILED: Edison API returned `402 Payment Required` (no credits). No `-deep-research-*.md` file was created; none fabricated.
- Review grounded in: `PNP-uniprot.txt`, `PNP-goa.tsv`, and cached `publications/PMID_*.md` (all 19 cited PMIDs present).

## Core biology (verified)
- Cytosolic purine nucleoside phosphorylase (EC 2.4.2.1); homotrimer (~32 kDa/monomer), catalytic sites at subunit interfaces [PMID:6771276; PMID:23438750].
- Reversibly phosphorolyses the N-glycosidic bond of 6-oxopurine (deoxy)ribonucleosides: inosine, guanosine, 2'-deoxyinosine, 2'-deoxyguanosine → free base (hypoxanthine/guanine) + (2'-deoxy)-alpha-D-ribose-1-phosphate [UniProt CATALYTIC ACTIVITY; PMID:6771276; PMID:9305964].
- Highly specific for 6-oxopurines: kcat/KM for inosine 350,000-fold greater than for adenosine [PMID:9305964]. Adenine (deoxy)ribonucleosides are NOT substrates [PMID:6771276]. N243D mutant reverses specificity toward 6-aminopurines [PMID:9305964].
- Feeds free bases (hypoxanthine/guanine) to salvage (HPRT1) or to catabolism (XDH → urate) [PMID:43101 salvage IDA PMID:18938130; equilibrium favors synthesis ~50-fold, PMID:15047506].
- Alternative substrate: nicotinamide riboside (NR) and nicotinic acid riboside — mammalian PNP is the Nrk1-independent NR phosphorylase, feeding NAD+ salvage [PMID:19001417].

## Disease
- PNP deficiency (PNPD, MIM:613179): interrupts catabolism of (deoxy)inosine→hypoxanthine and (deoxy)guanosine→guanine; accumulation of dGTP is toxic to (activated) T lymphocytes → severe T-cell immunodeficiency (a cause of SCID), often with neurological features [UniProt DISEASE; PMID:3029074 E89K; PMID:16964310]. Enzyme replacement (TAT-PNP) corrects immune defect in mice [PMID:16964310] and PNP-deficient T lymphocytes in vitro (IL-2, response to stimulation) [PMID:16930574].

## Annotation-review reasoning highlights
- MF core: GO:0004731 purine-nucleoside phosphorylase activity — many IDA lines + IBA + IEA; ACCEPT.
- GO:0047975 guanosine phosphorylase activity — a substrate-specific child of 2.4.2.1; ACCEPT (EXP PMID:9305964; RHEA IEA).
- GO:0016763 pentosyltransferase activity (IEA) — correct broad parent (EC 2.4.2 pentosyltransferase); ACCEPT as non-core (broad).
- GO:0003824 catalytic activity (IEA) — root-level, uninformative; MARK_AS_OVER_ANNOTATED.
- Binding MFs (nucleoside binding GO:0001882, purine nucleobase binding GO:0002060, phosphate ion binding GO:0042301) — IDA from substrate/structure papers; ACCEPT as supporting (non-core substrate/product binding).
- GO:0005515 protein binding IPI (many, PMID:32814053 Y2H ND interactome, + Contact/binary interactome PMIDs) — uninformative; MARK_AS_OVER_ANNOTATED (policy: not REMOVE).
- GO:0042802 identical protein binding IPI — meaningful: PNP is an obligate homotrimer; ACCEPT.
- BP catabolism (inosine GO:0006148, deoxyinosine GO:0006149, deoxyguanosine GO:0006161, guanosine GO:0046115) — IBA + IDA; ACCEPT (core catabolic role).
- GO:0006204 IMP catabolic process / GO:0046059 dAMP catabolic process / GO:0006157 deoxyadenosine catabolic process (IDA PMID:6771276) — these are "acts_upstream_of_or_within" / involved_in downstream-pathway annotations. PNP does not act on nucleotides (IMP/dAMP) or on adenine nucleosides directly. Note PMID:6771276 abstract explicitly says adenine (deoxy)ribonucleosides are NOT substrates; MGI curator likely captured the pathway (PNP acts downstream in deoxyadenosine/IMP/dAMP catabolism after upstream deamination). Keep as pathway-level upstream annotations (KEEP_AS_NON_CORE) rather than remove; deoxyadenosine catabolism is relevant to PNPD (dATP/dGTP accumulation). Do not overrule the experimental curator.
- GO:0043101 purine-containing compound salvage (IDA) — ACCEPT core salvage role.
- GO:0006738 nicotinamide riboside catabolic process (IDA PMID:19001417) — ACCEPT (well supported, moonlighting-ish alternative substrate feeding NAD+ salvage).
- GO:0034355 NAD+ biosynthesis via salvage (IBA) — KEEP_AS_NON_CORE (downstream of NR catabolism; supported by PMID:19001417 for the NR-splitting step).
- GO:0009165 nucleotide biosynthetic process (IGI PMID:19001417) — broad/indirect; MARK_AS_OVER_ANNOTATED (PNP catabolizes nucleosides / provides bases; "nucleotide biosynthetic process" is a downstream consequence via salvage, over-broad).
- GO:0006139 nucleobase-containing compound metabolic process (IDA PMID:3029074) — very broad parent; MARK_AS_OVER_ANNOTATED.
- GO:0009116 nucleoside metabolic process (IEA) — broad but correct; KEEP_AS_NON_CORE.
- Immune/T-cell BPs (GO:0006955 immune response IMP; GO:0032743 pos reg IL-2 production IMP; GO:0042102 pos reg T cell proliferation IDA; GO:0046638 pos reg alpha-beta T cell differentiation IDA) — these are indirect downstream physiological consequences of the metabolic enzyme (loss → dGTP toxicity → T-cell death). KEEP_AS_NON_CORE. Supported by PMID:16930574 / PMID:16964310 (enzyme replacement rescues T-cell function).
- GO:0034418 urate biosynthetic process (IDA PMID:16964310) — downstream (PNP → hypoxanthine → XDH → urate). KEEP_AS_NON_CORE.
- GO:0009410 response to xenobiotic stimulus (IMP PMID:15047506) — PNP degrades the antiviral ddI; drug-metabolism role. KEEP_AS_NON_CORE.
- Localization: cytosol GO:0005829 (IBA is_active_in, IDA HPA, IEA SubCell, many Reactome TAS) + cytoplasm GO:0005737 (IDA) — ACCEPT (cytosol is the true location).
- Extracellular/exosome/granule CCs (GO:0070062 extracellular exosome HDA; GO:0005576 extracellular region TAS; GO:0034774 secretory granule lumen TAS; GO:1904813 ficolin-1-rich granule lumen TAS) — cytosolic enzyme detected in exosome/secretome proteomics and neutrophil-degranulation Reactome pathways; not the site of function. KEEP_AS_NON_CORE (detected there but not functional location).
</content>
