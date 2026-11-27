# CBL4 / SOS3 (Arabidopsis thaliana, O81223, At5g24270) - curation notes

## Session 1 (2026-10-19)

No deep-research provider was available in this environment, so these notes are built
directly from the cached publications (`publications/PMID_*.md`) and the UniProt record.
`full_text_available` was checked for every paper; abstract-only papers are marked (abs).

### Identity and structure

- 222 aa EF-hand protein of the calcineurin B-like (CBL) family; N-myristoylated at Gly-2,
  S-acylated at Cys-3 (UniProt PTM/LIPID lines, ECO:0000269 from PMID:11006339, PMID:18502848,
  PMID:21445098).
- Cloned as the salt-tolerance locus SOS3 [PMID:9632394 (abs) "SOS3 encodes a protein that
  shares significant sequence similarity with the calcineurin B subunit from yeast and neuronal
  calcium sensors from animals"].
- Crystal structures of Ca2+/Mn2+-bound SOS3 (dimer) and of Ca-SOS3 bound to the SOS2 C-terminal
  regulatory domain [PMID:15644219 (abs) "calcium binding is responsible for the dimerization of
  SOS3"; PMID:17499048 (abs) "SOS2 is activated by Ca-SOS3 and subsequently phosphorylates the ion
  transporter SOS1"].
- Unusual EF hands: calcium binding is weak but real [PMID:11006339 "45 Ca 2+ overlay assays
  showed that the protein is capable of binding calcium"]; the sos3-1 allele deletes three residues
  in an EF hand and "substantially reduced the capacity of SOS3 to bind calcium".

### Molecular function: Ca2+-dependent activator of CIPK kinases

- SOS3 binds and activates SOS2/CIPK24 [PMID:10725350 "SOS3 activates SOS2 protein kinase activity
  in a Ca(2+)-dependent manner"]. Binding is via the CIPK C-terminal NAF/FISL motif, which is also
  the kinase autoinhibitory domain [PMID:11402167 "the SOS3 binding motif can serve as a kinase
  autoinhibitory domain"].
- No phosphatase partner: [PMID:10725350 "no protein phosphatase has been found to interact with
  SOS3. Instead, SOS3 was found to interact with and activate a protein kinase encoded by SOS2"],
  and "no genes similar to CNA have been identified from plants". This argues against the ISS
  annotations to calcium-dependent Ser/Thr phosphatase activity and to calcineurin complex, which
  were transferred from the yeast calcineurin B regulatory subunit at cloning time (1998).
- Myristoylation is required for function in planta but not for SOS2 binding [PMID:11006339
  "Expression of the myristoylated but not the nonmyristoylated SOS3 complemented the
  salt-hypersensitive phenotype of sos3-1 plants"].
- Weaker Y2H interactions with other CIPKs (CIPK1, CIPK6, CIPK10, CIPK11, CIPK15)
  [PMID:10725350 "The interaction between SOS3 and the other SIP kinases is much weaker compared
  with the interaction with SOS2"]; NAF domain sufficient for CBL binding [PMID:11230129 (abs)].
- CIPKs phosphorylate their CBL partners at a C-terminal Ser (Ser-205 in CBL4) [PMID:22253446 (abs)].

### Membrane recruitment

- In yeast reconstitution, SOS3 is required both for SOS2 kinase activity and to recruit SOS2 to
  the plasma membrane [PMID:12070350 "SOS3 is essential for both the kinase activity of SOS2 and its
  recruitment to the plasma membrane."]; a constitutively active SOS2 cannot fully replace the
  SOS2/SOS3 complex in vivo, so recruitment is a separate essential contribution of SOS3.
- PM localization in plant cells; N-terminal targeting signals; nuclear/cytoplasmic pool
  [PMID:19832944 (abs); UniProt SUBCELLULAR LOCATION "Cell membrane", "Cytoplasm", "Nucleus" all
  ECO:0000269|PubMed:19832944].
- CBL4-CIPK6 targets the K+ channel AKT2 from ER to PM, a kinase-interaction-dependent but
  phosphorylation-independent mechanism requiring both lipid modifications of CBL4
  [PMID:21445098 "a Ca(2+) sensor modulates K(+) channel activity by promoting a kinase
  interaction-dependent but phosphorylation-independent translocation of the channel to the PM"].
  cbl4 mutants share delayed development/flowering with akt2 and cipk6.

### Physiology

- sos3 mutant: Na+/Li+ hypersensitive, cannot grow on low K+, rescued by high external Ca2+;
  accumulates more Na+ and less K+ under NaCl [PMID:9405721 "Under NaCl stress, sos3 seedlings
  accumulated more Na+ and less K+ than the wild type"].
- SOS1 Na+/H+ exchange in PM vesicles is reduced in sos3 [PMID:12034882 (abs) "SOS2 and SOS3
  regulate SOS1 transport activity"]; SOS2-SOS3 phosphorylates the SOS1 autoinhibitory domain
  [PMID:21262798].
- SOS3 acts mainly in roots; CBL10/SCaBP8 mainly in shoots [PMID:17449811 (abs) "We show that SOS3
  acts primarily in roots under salt stress"].
- Salinity-induced cytosolic alkalinisation in roots requires SOS3 [PMID:36834961 "These pHcyt
  changes were substantially reduced in mutant roots lacking a functional SOS3/CBL4 protein"].
- Actin reorganisation under salt [PMID:23052592 (abs)] - phenotype-level, mechanism unclear.

### Annotation issues to report upstream (TAIR)

1. GO:0004723 calcium-dependent protein serine/threonine phosphatase activity (ISS, PMID:9632394):
   CBL4 is a non-catalytic regulatory EF-hand protein; even calcineurin B itself lacks this activity
   (it is the catalytic A subunit's). Remove.
2. GO:0005955 calcineurin complex (ISS, PMID:9632394): no calcineurin A in plants; partner is the
   CIPK kinase. Remove.
3. GO:0042539 hypotonic salinity response (IMP, PMID:9405721): direction is wrong - the sos3
   phenotype is hypersensitivity to increased NaCl; the correct term is GO:0042538 hyperosmotic
   salinity response (which the gene already carries by IBA).

### Open questions

- Does CBL4 have a physiologically relevant role with CIPKs other than CIPK24 and CIPK6?
- How does the Ca2+ signature in the root "sodium-sensing niche" map onto CBL4 vs CBL8 activation?

## 2026-10-20: ported fixes from the parallel review branch

Source defects recorded for the TAIR rows already reviewed here: GO:0042539 hypotonic salinity response (IMP, PMID:9405721) should be GO:0042538 hyperosmotic salinity response [PMID:9405721 "which is hypersensitive to Na+ and Li+ stresses"]; the ISS calcineurin phosphatase activity (GO:0004723) and calcineurin complex (GO:0005955) rows from PMID:9632394 should be withdrawn.
