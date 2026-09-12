# IMPDH1 (human, P20839) review notes

## Verified biology (grounded in UniProt P20839, GOA, cached PMIDs, Reactome)

IMPDH1 = inosine-5'-monophosphate dehydrogenase 1 (EC 1.1.1.205). Catalyzes the
committed, rate-limiting step of de novo guanine-nucleotide synthesis:
IMP + NAD+ + H2O -> XMP + NADH + H+ (RHEA:11708). XMP is then aminated to GMP by
GMPS. UniProt FUNCTION: "Catalyzes the conversion of inosine 5'-phosphate (IMP) to
xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de
novo synthesis of guanine nucleotides".

- Homotetramer (UniProt SUBUNIT; PubMed:7903306). Contains catalytic (β/α)8 TIM barrel
  + a regulatory subdomain of two CBS (Bateman) domains (FT DOMAIN 114-173 CBS 1,
  179-237 CBS 2). Can polymerize into filaments ("rods and rings"/cytoophidia) — many
  cryo-EM structures (7RER..8U8Y).
- Cofactor K+ (UniProt COFACTOR; multiple K+ BINDING sites). Uses NAD+ (BINDING 274-276,
  324-326). Active sites: Cys331 (thioimidate intermediate), 429 (proton acceptor).
- Subcellular: Cytoplasm + Nucleus (UniProt; PubMed:14766016). HPA IDA cytosol.
- Retina-enriched (UniProt HPA: "Tissue enhanced (retina)").
- Disease: Retinitis pigmentosa 10 (RP10, MIM:180105) and Leber congenital amaurosis 11
  (LCA11, MIM:613837) — photoreceptor degeneration. Many disease variants map to the CBS
  subdomain and alter single-stranded nucleic-acid affinity but NOT enzymatic affinity
  (PubMed:16384941 variant notes).

## Moonlighting / non-core: nucleic-acid binding
PMID:14766016 (McLean et al. 2004, abstract only): IMPDHs (T. foetus, E. coli, both human
isoforms) bind single-stranded nucleic acids with nanomolar affinity via the CBS subdomain;
~100 nt per tetramer. IMPDH found in nucleus; immunoprecipitation shows binding of RNA and
DNA in vivo. Concluded "a previously unappreciated role in replication, transcription or
translation." This is a moonlighting/regulatory activity, NOT the core catalytic function.
UniProt hedges: "Could also have a single-stranded nucleic acid-binding activity and could
play a role in RNA and/or DNA metabolism." => treat DNA/nucleic-acid binding and the nucleus
localization associated with it as KEEP_AS_NON_CORE.

## GOA annotations summary (from IMPDH1-goa.tsv)
Core MF: GO:0003938 IMP dehydrogenase activity (IBA, IEA, TAS PMID:1969416).
Core BP: GO:0006177 GMP biosynthetic process (IEA); GO:0097294 'de novo' XMP biosynthetic
process (IEA/Ensembl orthology) — most precise BP for the actual reaction; GO:0006183 GTP
biosynthetic process (IBA) — one step removed (XMP->GMP->GDP->GTP), keep as non-core;
GO:0006164 purine nucleotide biosynthetic process (IEA, broad parent).
CC: GO:0005829 cytosol (IDA HPA; TAS Reactome) — core location; GO:0005737 cytoplasm
(IBA is_active_in, IEA, IDA) — core; GO:0005634 nucleus (IEA, IDA PMID:14766016) — non-core
moonlighting. Extracellular/granule-lumen (Reactome neutrophil degranulation) = bystander
secretome, non-core.

## Reactome refs
R-HSA-73794 is the actual IMP->XMP reaction (core). R-HSA-9678749/9748945 concern IMPDH
inhibitor binding / thiopurine (6TIMP) turnover (drug-metabolism context). R-HSA-6798748/
6798751/6800434 are neutrophil-degranulation exocytosis events (extracellular/granule lumen
localization by mass-spec proteomics of granules) — bystander, non-core.
