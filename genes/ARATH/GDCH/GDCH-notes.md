# GDCH (GDH1, At2g35370, UniProt P25855) - curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are a manual literature summary built only from cached publications (`publications/PMID_*.md`)
and the UniProt record (`GDCH-uniprot.txt`). No `-deep-research-*.md` file exists for this gene.

Nomenclature: UniProt gene name GDH1 (synonyms GCDH, GDCH, GDCSH); this is the glycine cleavage
H protein 1, NOT glutamate dehydrogenase (also abbreviated GDH1 in Arabidopsis). Folder alias GDCH.

## Identity

- Glycine cleavage system H protein 1, mitochondrial; 165 aa precursor, transit peptide 1-34
  (cleavage after Phe-34 shown experimentally, PubMed:25862457), lipoyl-binding domain 56-138,
  N6-lipoyllysine at K97 (by similarity / PROSITE rule). GcvH family (HAMAP MF_00272, TIGR00527,
  PANTHER PTHR11715).
- Arabidopsis has three H-protein genes [PMID:22303256 "three genes for H-protein (At2g35370,
  At2g35120 and At1g32470)"].

## Molecular function: a carrier, not an enzyme

- [PMID:22303256 "H-protein is not an enzyme component of the complex but a cofactor that interacts
  with all three enzymes of the complex."]
- [PMID:17496108 "H protein carries no enzymatic activity but interacts as a mobile substrate via its
  lipoamide arm one after the other with P, T, and L protein"]
- [PMID:19860829 "H-protein has no catalytic activity itself but is a substrate of the three
  enzymatically active subunits, P-, T- and L-protein."]
- [PMID:11286922 "the lipoate-dependent H-protein that plays a pivotal role, acting as a mobile
  substrate that commutes successively between the other three proteins"]
- UniProt: [file:ARATH/GDCH/GDCH-uniprot.txt "The H protein shuttles the methylamine group of glycine
  from the P protein to the T protein."] and "Binds 1 lipoyl cofactor covalently."
- Lipoylation of the H protein is required for GDC function in vivo: the classical gld1 mutant is in
  mtKAS, needed for lipoate synthesis [PMID:22303256 "The mutant is deficient in a
  3-oxoacyl-(acyl-carrier-protein) synthase (At2g04540, Mt-kas 1) that is required for lipoylation of
  H-protein"].

### How to express this in GO

- GDCH has no catalytic MF. The relevant MF is GO:0140104 molecular carrier activity ("Directly
  binding to a specific ion or molecule and delivering it either to an acceptor molecule or to a
  specific location"; "a carrier moves with its substrate/cargo"), which matches the swinging
  lipoyl arm carrying the aminomethyl intermediate (and then electrons) between P, T and L. PomBase's
  GO-CAM for S. pombe gcv3 uses the same term.
- GO:0031405 lipoic acid binding (used by modules/glycine_cleavage_system.yaml and the human GCSH
  review) is a weaker fit: the lipoate is a covalently attached prosthetic group (N6-lipoyllysine),
  so "binding lipoic acid" describes the cofactor attachment, not the activity. Not proposed as NEW.
- GO has GO:0140414 phosphopantetheine-dependent carrier activity for ACP-type carriers but no
  lipoyl-dependent equivalent; proposed as a new term (child of GO:0140104).
- In GO the H protein's reaction role is also visible as an input in the P/T/L reaction definitions
  (GO:0004375 is written with "lipoyl-L-lysyl-[glycine-cleavage complex H protein]" as substrate).

## Complex, location, expression

- Part of the leaf GDC; H1 (At2g35370) and H3 (At1g32470) are present in about equal amounts and
  redundant, H2 absent from leaf mitochondria [PMID:32311173 "whereas the H-isoproteins GCS-H1 and
  GCS-H3 are fully redundant as indicated by their about equal amounts"] (abstract only). Leaf GDC
  ratio about 1L2-4P2-8T-20H in Arabidopsis.
- Mitochondrial: N-terminal processing of At2g35370 observed in isolated mitochondria
  [PMID:25862457 "two glycine decarboxylase (GDC) H proteins (At2g35370 and At1g32470)"].
- Light-induced, leaf-predominant expression [PMID:7480320 "Glycine decarboxylase is a mitochondrial
  enzyme complex, which is the site of photorespiratory CO2 and NH3 release."; gdcH promoter GUS
  study] (abstract only).
- Nucleus, ER, cytosol and thylakoid HDA rows conflict with the experimentally processed
  mitochondrial presequence and are treated as proteomic contaminants.

## Physiology

- H-protein amount limits GDC flux: overexpression of an H protein enhanced photosynthesis and growth
  in Arabidopsis [PMID:22982108], and guard-cell manipulation altered stomatal behaviour
  [PMID:40219652]. Both used the Flaveria pringlei H protein (FpGDCH) transgene, so these are not
  direct evidence about At2g35370 itself and are not used to support annotations of GDCH.
- No Arabidopsis gdch1 knockout phenotype is described in the cached literature; with H3 redundant,
  a single mutant would be expected to be mild (an inference, not a result).

## Annotation decisions (summary)

- ACCEPT: mitochondrion (IBA/IEA/ISM), glycine cleavage complex (IBA/IEA), GO:0019464 (IBA/IEA).
- REMOVE: nucleus, ER, cytosol, thylakoid HDA (contaminant detections of a mitochondrial matrix
  protein).
- NEW: GO:0140104 molecular carrier activity; GO:0009853 photorespiration (carrier/cofactor case per
  CLAUDE.md: the H protein does part of the work of the step by carrying the intermediate; comparator
  check: SHM1, GLYK, HPR, GGAT1, PLGG1 carry GO:0009853 in Arabidopsis; GDC subunits do not).
