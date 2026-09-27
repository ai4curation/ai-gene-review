# vha-1 (Q21898) — V-type proton ATPase 16 kDa proteolipid subunit c 1 — curation notes

## Identity

- UniProt Q21898 (VATL1_CAEEL, reviewed), WormBase R10E11.8, 169 aa, four-transmembrane
  proteolipid of the V-ATPase V0 c-ring (IPR002379 ATPase proteolipid c-like domain;
  IPR000245 / IPR011555 V-ATPase proteolipid subunit C). Orthologue of human ATP6V0C and
  yeast Vma3. C. elegans has three 16 kDa proteolipid genes (vha-1, vha-2, vha-3) plus the
  Vma16-like vha-4.
- Subunit c carries the buried glutamate that binds and carries protons as the c-ring
  rotates; it is the proton-conducting element of the V0 sector (UniProt, by similarity).

## Literature

### Oka, Yamamoto & Futai 1997 (PMID:9305897, abstract only)

- Cloning and expression: "The vha-1 and vha-2 (vacuolar-type H+-ATPase) genes in
  Caenorhabditis elegans encode putative 16-kDa proteolipids and are tandemly localized on
  chromosome III" [PMID:9305897]. "The deduced amino acid sequences of the two genes
  exhibit about 60% identity with the homologues from yeast, mouse, and cow" [PMID:9305897].
- Expression: "the three vha genes may be highly expressed in the H-shaped excretory cell,
  rectum, and a pair of cells posterior to the anus" [PMID:9305897]. The NAS annotations
  (membrane; proton transmembrane transport) rest on this identity-level inference.

### Oka & Futai 2000 (PMID:10846178, abstract only)

- RNAi of vha-11 (subunit C) causes embryonic lethality and later sterility due to failed
  ovulation; "Similar results were obtained for RNA interference of the V-ATPase
  proteolipid genes" [PMID:10846178]. Basis of the IMP annotations to embryo development
  and ovulation; these are organism-level requirements for organellar acidification, not
  functions vha-1 executes itself.

### Kontani, Moskowitz & Rothman 2005 (PMID:15866168, abstract only)

- fus-1 (V-ATPase subunit e) represses EFF-1-dependent epidermal fusion; "loss of other
  V-ATPase subunits also causes widespread hyperfusion" [PMID:15866168]. Basis of the
  IMP/IGI annotations to regulation of syncytium formation. The GOA IGI partner is
  WB:WBGene00001159.

### Rao, Isaac & Keen 2011 (PMID:21070894, abstract only)

- geLC-MS/MS of a detergent-resistant membrane fraction: "A total of 44 proteins were
  identified from the lipid raft fraction using geLC-MS/MS" [PMID:21070894]. The abstract
  does not list the proteins; VHA-1 presence in the list cannot be verified here.

### Bohnert & Kenyon 2017 (PMID:29168500, full text cached)

- vha-13 RNAi blocks oocyte aggregate clearance and "Knockdown of other V-ATPase subunits
  produced similar protein-aggregation phenotypes" [PMID:29168500]; acidic lysosomes
  accumulate "in maturing, proximal oocytes in a V-ATPase-dependent manner" [PMID:29168500].
  vha-1 is one of the subunits in Extended Data Fig. 3 (per the GOA IMP row); basis of the
  IMP lysosomal lumen acidification annotation.

### Other (UniProt-cited, not in GOA rows)

- PMID:16785323 (Liegeois 2006): V0 sector in apical exosome secretion / endocytosis.
- PMID:28581477 (Sinclair 2017): V-ATPase needed for processing/secretion of HRG-7 from the
  intestine.

## Assessment

- Molecular function: proton transmembrane transporter activity (GO:0015078) is the
  subunit-level activity; the c-ring is the proton carrier. GO:0046961 (rotary
  proton-transporting ATPase) is the complex-level activity; the InterPro IEA is acceptable
  at the complex level and matches how human ATP6V0C is reviewed.
- Location: membrane (IBA/IEA/NAS) is correct but generic; the demonstrated compartment in
  C. elegans is the lysosome (V-ATPase-dependent acidification).
- Developmental / physiological phenotypes (embryogenesis, ovulation, repression of
  epidermal fusion) are kept as non-core: they follow from loss of organellar
  acidification rather than from a distinct activity of the proteolipid.
- Membrane raft (HDA) cannot be verified from the abstract; small hydrophobic proteolipids
  commonly partition into detergent-resistant fractions, so this is weak evidence for a
  functional raft location.
- Synaptic vesicles: no vha-1-specific neuronal data in the GOA set; no NEW annotation.
