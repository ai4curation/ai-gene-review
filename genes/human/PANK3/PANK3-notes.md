# PANK3 (Pantothenate kinase 3) — review notes

UniProt: Q9H999 (PANK3_HUMAN); HGNC:19365; Gene ID 79646; MANE NM_024594.4 / NP_078870.1;
370 aa; chromosome 5. EC 2.7.1.33. Type II pantothenate kinase family.

## Core biology (grounded in UniProt Q9H999 and cited primary papers)

- **Molecular function / reaction.** PANK3 catalyzes the phosphorylation of
  (R)-pantothenate + ATP → (R)-4'-phosphopantothenate + ADP + H+ (Rhea:16373; EC 2.7.1.33),
  the first and rate-determining step of coenzyme A (CoA) biosynthesis.
  [file:human/PANK3/PANK3-uniprot.txt "Catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis"]
  [PMID:30927326 "Pantothenate kinase generates 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) biosynthesis"]
- **Pathway.** Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 1/5
  (UniPathway UPA00241, UER00352; Reactome R-HSA-196783 Coenzyme A biosynthesis).
  [file:human/PANK3/PANK3-uniprot.txt "Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-"]
- **Kinetics.** KM = 14–17 uM pantothenate; KM = 175–311 uM ATP.
  [file:human/PANK3/PANK3-uniprot.txt "KM=14 uM for pantothenate"]
  [file:human/PANK3/PANK3-uniprot.txt "KM=311 uM for ATP"]
- **Quaternary structure.** Homodimer with two equivalent active sites formed by head-to-tail
  juxtaposition of the monomers; each protomer adopts an actin kinase / ASKHA fold.
  [file:human/PANK3/PANK3-uniprot.txt "SUBUNIT: Homodimer"]
  [PMID:20797618 "two equivalent active sites formed by a head-to-tail juxtaposition of the monomers"]
  [PMID:17631502 "we report the homodimeric structures of the catalytic cores of PanK1alpha and PanK3 in complex with acetyl-CoA"]
- **Allosteric regulation (feedback inhibition).** Two conformations — a catalytically
  incompetent (open) state stabilized by acetyl(acyl)-CoA binding, and a catalytically
  competent (closed) state stabilized by ATP binding. Inhibited by acetyl-CoA and its
  thioesters (compete with the ATP-binding site); also inhibited by sulfonylureas and
  thiazolidinediones; activated by oleoylethanolamide and acyl-carnitines.
  [file:human/PANK3/PANK3-uniprot.txt "Inhibited by acetyl-CoA and its thioesters"]
  [PMID:27555321 "feedback-inhibited by acetyl-CoA"]
  [PMID:27555321 "master regulator of CoA biosynthesis"]
  [PMID:30927326 "A fundamental characteristic of mammalian PANKs is their stringent feedback regulation by acetyl‐CoA and other CoA thioesters"]
- **Active site / mutagenesis.** Glu138 = proton acceptor (catalytic base); Arg207 binds
  pantothenate; Gly19 in the P-loop is required for ATP binding. E138A/E138V and R207A abolish
  activity; G19V abolishes ATP binding; S195V is refractory to acetyl-CoA inhibition and raises
  the pantothenate KM ~10-fold.
  [file:human/PANK3/PANK3-uniprot.txt "E->A: Loss of catalytic activity"]
  [PMID:27555321 "PANK3(G19V) cannot bind ATP"]
  [PMID:30927326 "Glu138 functions as the catalytic base essential for the kinase reaction, and Arg207 binds the pantothenate substrate"]
- **Two protomers are functionally coupled** (cooperative allosteric switching), demonstrated
  with an engineered PANK3/PANK3(G19V) heterodimer.
  [PMID:27555321 "biochemical analyses of an engineered PANK3/PANK3(G19V) heterodimer confirmed that the two active sites are functionally coupled"]

## Subcellular location

- PANK3 is **cytosolic** and soluble (live-cell imaging of ZsGreen1-tagged isoforms). The
  downstream CoA enzymes are cytosolic, consistent with PANK3 supplying phosphopantothenate there.
  [PMID:23152917 "Mouse PanK2 and both human and mouse PanK3 were cytosolic with a diffuse pattern, indicating that these proteins were soluble and not associated with structural components of the cell"]
  [file:human/PANK3/PANK3-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]
- The nuclear location seen in the PanK family belongs to the **PanK1alpha** isoform (N-terminal
  NLS), not PanK3. PanK1beta and PanK3 are essentially the catalytic core with a short N-terminal
  extension.
  [PMID:23152917 "Both human and mouse PanK1beta localized to the cytosol"]

## Tissue expression

- Highly expressed in liver; PanK3 is found in all cell types examined.
  [file:human/PANK3/PANK3-uniprot.txt "TISSUE SPECIFICITY: Highly expressed in the liver"]
  [PMID:23152917 "PanK3 is found in all cell types examined thus far"]

## Annotation-review decisions (summary)

- **Core MF:** GO:0004594 pantothenate kinase activity (IDA/IMP/IBA/IEA — all ACCEPT). Also
  GO:0005524 ATP binding (phosphate donor; ACCEPT). Core BP: GO:0015937 coenzyme A biosynthetic
  process (ACCEPT). Core location: GO:0005829 cytosol (ACCEPT).
- **KEEP_AS_NON_CORE:** GO:0005737 cytoplasm (less precise parent of cytosol); GO:1905502
  acetyl-CoA binding (allosteric feedback-inhibitor ligand — real, but regulatory not catalytic);
  GO:0019842 vitamin binding (generic; = pantothenate substrate binding, subsumed by the kinase
  MF); GO:0042803 protein homodimerization activity (structural feature underlying cooperative
  allostery).
- **MARK_AS_OVER_ANNOTATED:** GO:0005634 nucleus (IBA and IPI) — contradicted by the direct
  cytosolic-imaging result; nuclear location belongs to PanK1alpha. Also GO:0016310 phosphorylation
  (IDA/IMP x3) — an uninformative high-level parent superseded by the substrate-specific
  pantothenate kinase activity (MF) and CoA biosynthetic process (BP) terms.
- No REMOVE calls: per policy, experimental (IDA/IMP/IPI/EXP) annotations and the generic
  regulatory-binding terms are flagged as over-annotated or kept-as-non-core rather than removed.

## Reference verbatim-quote gotchas (for future editors)

- PMID:30927326 cached text contains **no ASCII "ATP" string** and uses Unicode non-breaking
  hyphens for "acetyl‐CoA" in the full-text section. The plain "Pantothenate kinase generates
  4'-phosphopantothenate ..." sentence is available in ASCII in the Abstract section (line ~41)
  and is the safe quote. Do not quote acetyl-CoA / ATP verbatim from this paper.
- PMID:17631502 and PMID:27555321 are **abstract-only** in the cache (full_text_available: false);
  quotes were taken from the abstract. PMID:27555321 uses a middle-dot "·" in
  "AMPPNP·Mg2+·pantothenate" — quote it with the middle dot.
- PMID:20797618 and PMID:23152917 have full text cached.

## Provenance / files used

- genes/human/PANK3/PANK3-uniprot.txt (authoritative UniProt Q9H999)
- genes/human/PANK3/PANK3-goa.tsv (GOA source for existing_annotations)
- publications/PMID_17631502.md, PMID_20797618.md, PMID_23152917.md, PMID_27555321.md,
  PMID_30927326.md
