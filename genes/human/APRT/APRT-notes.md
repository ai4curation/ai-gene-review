# APRT (human, P07741) review notes

## Deep research status
- `just deep-research human APRT --provider falcon` was run but FAILED (exit 1, no output file produced).
  No `-deep-research-*.md` was fabricated. Review grounded in UniProt (`APRT-uniprot.txt`),
  seeded GOA (`APRT-goa.tsv`), and cached `publications/PMID_*.md`.

## Core biology (verified)
- APRT = adenine phosphoribosyltransferase, EC 2.4.2.7, cytosolic purine SALVAGE enzyme.
  Reaction: adenine + PRPP -> AMP + diphosphate (UniProt writes it reverse: AMP + PPi = PRPP + adenine,
  Rhea:16609). [file:APRT-uniprot.txt CATALYTIC ACTIVITY / PATHWAY]
- Provides "the only known mechanism for the metabolic salvage of adenine resulting from the polyamine
  biosynthesis pathway or from dietary sources" [PMID:15196008 abstract].
- Homodimer; cytoplasm/cytosol. KM adenine ~4 uM, PRPP ~8.9 uM. [PMID:15196008]
- Structure: 9 beta-strands, 6 alpha-helices, type I PRTase fold; crystallized with AMP product
  (PDB 1ZN7/1ZN8...). [PMID:15196008]
- Belongs to purine/pyrimidine phosphoribosyltransferase family (type I PRTase, PRTase_dom Pfam PF00156).
- Complete amino acid sequence of erythrocyte enzyme established; N-terminus acetylated; 179/180 residues,
  subunit ~19.5 kDa. [PMID:3531209]

## Disease
- APRT deficiency (APRTD, MIM:614723): adenine not salvaged -> oxidised by xanthine dehydrogenase to
  insoluble 2,8-dihydroxyadenine (DHA) -> 2,8-DHA nephrolithiasis, interstitial nephritis, CKD/renal failure.
  Many APRTD missense variants documented (Japanese M136T = APRT*J most common; Icelandic D65V). [UniProt DISEASE, PMID:15196008]

## Mg cofactor
- Type I PRTases use a Mg2+-PRPP complex as substrate; Mg is the catalytic divalent cation.
  Annotate GO:0000287 magnesium ion binding as cofactor in core_functions (family-level / mechanistic).

## Annotation-specific notes
- MF GO:0003999: IBA + IEA + IDA(PMID:15196008) + TAS(PMID:3531209). Core, ACCEPT.
- BP GO:0006168 adenine salvage & GO:0044209 AMP salvage: IBA + IEA. Core process. ACCEPT.
- GO:0002055 adenine binding, GO:0016208 AMP binding: substrate/product binding, mechanistic; IBA/IEA/IDA.
  ACCEPT (support the MF; keep as non-core molecular detail).
- GO:0032263 GMP salvage, GO:0032264 IMP salvage (IEA GO_REF:0000107, Ensembl ortholog transfer):
  APRT is adenine-specific (does NOT act on guanine/hypoxanthine -> those are HPRT). These IEA
  ortholog-mapped process terms are wrong for APRT -> REMOVE (clearly wrong IEA inference).
- GO:1901363 heterocyclic compound binding (IEA ARBA): far too generic / uninformative; adenine binding
  is the informative term. MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding IPI (x2, TTC19/Q6DKK2 via PMID:32296183; SPRED1/Q7Z699 via PMID:32814053):
  bare protein binding, uninformative, high-throughput Y2H/interactome. Per policy do NOT REMOVE
  experimental IPI -> MARK_AS_OVER_ANNOTATED.
- Cytoplasm/cytosol (GO:0005737, GO:0005829): correct location. ACCEPT the well-supported ones
  (IDA HPA, IBA); keep duplicates.
- GO:0070062 extracellular exosome (HDA x3): large-scale exosome proteomes; contaminant-type CC.
  MARK_AS_OVER_ANNOTATED (not functional localization).
- GO:0005576 extracellular region + GO:0034774 secretory granule lumen (Reactome neutrophil
  degranulation R-HSA-6798748): APRT appears in neutrophil granule proteome; not its functional site.
  MARK_AS_OVER_ANNOTATED.
