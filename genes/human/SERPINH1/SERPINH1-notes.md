# SERPINH1 (HSP47 / Serpin H1 / colligin / gp46) — research notes

UniProt: P50454 (SERPH_HUMAN). Member of the serpin family but NON-INHIBITORY.

## Core identity
ER-resident, collagen-specific molecular chaperone. Despite the serpin fold, it
does NOT act as a protease inhibitor; it is a dedicated chaperone for procollagen.

- [file:human/SERPINH1/SERPINH1-uniprot.txt "FUNCTION: Binds specifically to collagen. Could be involved as a chaperone in the biosynthetic pathway of collagen."]
- [file:human/SERPINH1/SERPINH1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen."]
- [file:human/SERPINH1/SERPINH1-uniprot.txt "INDUCTION: By heat shock."]
- [file:human/SERPINH1/SERPINH1-uniprot.txt "SIMILARITY: Belongs to the serpin family."]

## Mechanism (well-established in literature)
HSP47 binds the folded triple-helical procollagen in the ER, stabilizing it and
preventing local unfolding/aggregation, and acting in quality control / preventing
premature aggregation. It travels with procollagen to the ER-Golgi intermediate
compartment (ERGIC)/cis-Golgi, where the lower pH triggers its release; HSP47 then
cycles back to the ER via its C-terminal RDEL ER-retrieval signal. It recognizes the
folded triple helix (Arg residues in Gly-Xaa-Arg repeats), not unfolded chains — so it
is a collagen-specific chaperone, NOT a general foldase or general unfolded-protein
chaperone.

- ERGIC localization directly shown: [PMID:15308636] (IDA GO:0005793 ER-Golgi intermediate compartment).
- The serpin-family TAS annotation of "serine-type endopeptidase inhibitor activity"
  (PMID:1309665, PMID:7656593) and the IBA/IEA serpin-inhibitor transfers are based on
  the serpin FOLD; HSP47 is a well-documented non-inhibitory serpin and should not be
  annotated as a functional protease inhibitor. -> MARK_AS_OVER_ANNOTATED.

## Disease
- [file:human/SERPINH1/SERPINH1-uniprot.txt "DISEASE: Osteogenesis imperfecta 10 (OI10) [MIM:613848]"] — autosomal recessive OI; reflects the essential role of HSP47 in collagen biogenesis.

## GO annotation review notes (goa.tsv)
- GO:0004867 serine-type endopeptidase inhibitor activity (IBA, IEA, TAS x3): serpin-fold
  transfer. HSP47 is non-inhibitory. -> MARK_AS_OVER_ANNOTATED (all).
- GO:0005518 collagen binding (IEA InterPro, NAS PMID:1309665, NAS PMID:7656593): CORE MF.
  ACCEPT.
- GO:0005783 endoplasmic reticulum (IBA, IDA, IEA, TAS, NAS): CORE localization. ACCEPT
  the experimentally supported ones; ER lumen (GO:0005788) is the precise compartment.
- GO:0005788 endoplasmic reticulum lumen (IEA SubCell, TAS Reactome x2): precise CORE
  localization matching UniProt. ACCEPT.
- GO:0030199 collagen fibril organization (IBA): downstream process of collagen
  biogenesis; HSP47 chaperones procollagen in ER. KEEP_AS_NON_CORE (it acts upstream in
  ER, fibril organization is extracellular/downstream).
- GO:0006457 protein folding (IEA from GO:0044183): HSP47 stabilizes folded procollagen
  rather than catalyzing folding. KEEP_AS_NON_CORE.
- GO:0044183 protein folding chaperone (IEA, by similarity to mouse): HSP47 is a
  collagen-specific chaperone. Reasonable but generic; the precise MF is collagen binding /
  collagen-specific chaperone. KEEP as MF but specific term is collagen binding. ACCEPT
  (it is a chaperone) — but core MF best captured as collagen binding.
- GO:0006986 response to unfolded protein (TAS PMID:1309665, PMID:10023073): HSP47 is heat-
  shock-induced; but it is collagen-specific and not a generic UPR chaperone. The "response
  to unfolded protein" framing is partly historical. KEEP_AS_NON_CORE.
- GO:0031012 extracellular matrix (HDA x3): HSP47 is ER-resident; ECM detection is from
  matrisome/secretome proteomics (some HSP47 co-secreted with collagen or detected in ECM
  preps). Peripheral. KEEP_AS_NON_CORE.
- GO:0045121 membrane raft (IDA PMID:25204797): cell-surface HSP47 reported in some
  contexts; minor/peripheral. KEEP_AS_NON_CORE.
- GO:0003723 RNA binding (HDA PMID:22658674): mRNA-interactome capture; generic, not a
  characterized function. MARK_AS_OVER_ANNOTATED.
- GO:0005793 ERGIC (IDA PMID:15308636): directly shown; matches the pH-dependent
  release/recycling itinerary. ACCEPT.
- GO:0005515 protein binding (IPI PMID:32814053): large HT neurodegeneration interactome
  with many partners (CDH1, ETS2, etc., none of them collagen). Uninformative; not core.
  MARK_AS_OVER_ANNOTATED.
- GO:0005737 cytoplasm (IEA Ensembl ortholog): HSP47 is ER-lumenal; cytoplasm is a coarse
  parent / ortholog transfer. MARK_AS_OVER_ANNOTATED (conflicts with ER-lumen specificity).

## Core function synthesis
1. Collagen-specific molecular chaperone (GO:0044183 / GO:0005518 collagen binding):
   binds folded triple-helical procollagen in ER lumen, stabilizes it, prevents
   aggregation, QC of collagen biogenesis.
2. Localization: ER lumen (GO:0005788), cycling through ERGIC (GO:0005793) via RDEL.
3. NOT a functional protease inhibitor despite serpin fold.
