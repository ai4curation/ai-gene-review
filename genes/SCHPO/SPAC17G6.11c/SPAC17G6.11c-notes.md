# SPAC17G6.11c (Ghs2, O13789) notes

## Identity
- Named Ghs2 in PMID:37792890 ["We named this protein Ghs2 for its Glycoside Hydrolase Sixteen domain 2."]
- Essential, Skn1/Kre6 family (UniProt "SIMILARITY: Belongs to the SKN1/KRE6 family."), type II
  signal-anchor membrane protein: cytosolic 1-170, TM 171-191, GH16 domain 218-587 (UniProt FT).
- PMID:37792890 ["it is essential, potentially localizes to the PM, and contains a Glycoside Hydrolase 16 domain with homology to laminarinases which are β1,3 glucanases"]

## Earlier ghs2 paper (ref 33 of PMID:42786154)
- Identified as PMID:37792890 (Willet et al. 2023 PLoS Genet, MIPC/css1 paper). It is already cached and
  is the source of the GOA IMP for cell wall organization or biogenesis. In the 2026 paper the ghs2-2
  deposits and T205P/F449L mutations are cited as ref 33; the 2023 paper describes generating ghs2-2
  ["We generated a temperature-sensitive ghs2 allele (ghs2-2)"].

## Key 2026 findings (PMID:42786154, full text)
- Localization: ["GFP-Ghs2 localized to cell tips and the cell division site at both 25 °C and 36°C"];
  becomes cytoplasmic in bgs3-1 at 36 °C.
- Partner specificity: ["Ghs2 is specifically required for the proper subcellular localization of Bgs3, but not other glucan synthases"];
  ["HA3-Ghs2 and GFP-Bgs3 co-immunoprecipitated (Fig. 3b), whereas GFP-Ghs2 and RFP-Bgs4 did not"].
- Catalytic motif mutants: ["Neither mutant rescued growth of ghs2-2 cells"]; E419A is dominant negative
  and keeps Bgs3 at the surface.
- Wall chemistry (ssNMR): ["the β-1,3,6-glucopyranose containing branched glucan (BBr) of bgs3-1 and ghs2-2 was reduced by ~ 58% and ~ 17%, respectively and, β-1,6-glucan was reduced by ~ 45% and ~ 30%, respectively"].
- Inhibitor: ["Together, these data indicate that Y478 contributes to D75-4590 sensitivity, supporting a conserved inhibitor-binding site within the GH16 domain."]
- Activity NOT assayed: ["In contrast, the biochemical role of Ghs2 is unclear, although GH16 domains typically hydrolyze or transglycosylate β-glucans at various linkage sites"].
- The AF3 model's GH16 placement next to the Bgs3 pore is not confident (inter-chain PAE ~20-23 A, see
  genes/SCHPO/bgs3/bgs3-bioinformatics/RESULTS.md); only the TM-TM interface is confident. Not used as
  evidence.

## Curation decisions
- MF rows (GO:0004553 IEA, GO:0015926 IBA): MARK_AS_OVER_ANNOTATED. No hydrolase assay exists for
  any family member. The S. cerevisiae glucosidase IMP seed (PMID:10601196, checked via PubMed abstract)
  rests on hydrophobic cluster analysis, not an enzyme assay. The proposed reaction is a branching
  transglycosylation, recorded as a proposed new term plus an MF_DARK knowledge gap.
- ER rows: KEEP_AS_NON_CORE (secretory transit; acts at the PM).
- PM IBA, (1->6)-beta-glucan IBA and fungal cell wall organization IBA: ACCEPT.
- Carbohydrate metabolic process IEA: MODIFY to GO:0070880 and GO:0006078.
- Cell wall organization or biogenesis IMP: MODIFY to GO:0031505.
- NEW: cell tip (IDA), cell division site (IDA), fungal-type cell wall beta-glucan biosynthetic
  process GO:0070880 (IMP), all from PMID:42786154.
