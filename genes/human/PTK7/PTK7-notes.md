# PTK7 (human, Q13308) review notes

## Deep research status

- 2026-10-20: `just deep-research-falcon human PTK7 --fallback perplexity-lite` failed.
  Falcon returned `403 Forbidden` at the Edison auth endpoint (`Failed to authenticate`),
  and the perplexity-lite fallback also exited non-zero. No deep-research file exists.
  The review below is based on literature cached in `publications/` and read directly.

## Evolutionary grounding

- PANTHER: PTHR45080 (family name "CONTACTIN 5"; a heterogeneous Ig-superfamily family that
  also contains L1CAM/NrCAM, hemicentins, MDGAs), subfamily PTHR45080:SF21 "INACTIVE
  TYROSINE-PROTEIN KINASE 7" (UniProt DR line). Mouse Ptk7 Q8BKG3 and chick PTK7 Q91048 are
  in the same subfamily (interpro/panther/PTHR45080/PTHR45080-entries.csv).
- PAINT nodes reaching PTK7 (interpro/panther/PTHR45080/PTHR45080-paint.tsv):
  - PTN000701324 (Amniota, taxon:32524): cell-cell junction + regulation of canonical Wnt
    signaling; seeded only by human Q13308. This is the PTK7-clade node.
  - PTN002895062 (Eumetazoa): plasma membrane (seeds L1CAM, Q13308) and homophilic cell-cell
    adhesion (seeds fly FBgn0017590 and mouse L1cam MGI:96721). No PTK7-clade seed for adhesion.
  - PTN002895063 (no taxon recorded): axon, neuronal cell body, axon guidance receptor activity,
    synapse organization; seeds are all L1-family neuronal CAMs (L1CAM P32004, MGI:96721,
    RGD:61941, RGD:619777). No PTK7-clade experimental support.
- Mouse Ptk7 experimental annotations (QuickGO, Q8BKG3) are almost all
  `acts_upstream_of_or_within` developmental phenotypes (neural tube closure GO:0001843,
  establishment of planar polarity GO:0001736, convergent extension GO:0060026, etc.) plus
  NOT kinase activity (PMID:15019986). PAINT did NOT propagate any of the PCP/developmental
  terms to PTN000701324; treated as a deliberate decision (they are phenotype-level calls).

## Key literature (read)

- Pseudokinase: UniProt "Does not bind ATP"; [PMID:24107129 "CCK4 (colon carcinoma kinase 4)/PTK7
  (protein tyrosine kinase 7) [56], BubR1 [35], IRAK3/IRAK-M [57] and MviN [28] were not
  catalytically active in vitro in previously published studies, consistent with our
  observations that they do not bind ATP"]; structure of human PTK7 pseudokinase domain
  [PMID:32619402 "ATP binding to PTK7 and ROR2 is prevented by projection of a tyrosine
  side-chain from the β5/αD hinge region (Y877 and Y555 respectively) into the adenine ring
  binding site"].
- Original cloning: [PMID:7478540 "These define CCK-4 as a catalytically inactive member of the
  RTK family of proteins"].
- Canonical Wnt, human cells (HCT116 knockdown) + mouse MEFs + Xenopus: positive role,
  beta-catenin binding to the kinase-like domain [PMID:21132015].
- Canonical Wnt, opposite sign: Xenopus/Drosophila and luciferase reporters (human PTK7
  constructs used in reporter assays) show PTK7 inhibits canonical signaling; Wnt3a
  co-precipitation by soluble PTK7 required soluble Fz7 [PMID:21772251]. Berger 2017 review notes
  "studies analyzing direct interaction of PTK7 and Wnt ligands are currently lacking"
  [PMID:28424771]. Canonical Wnts induce Fz7-dependent caveolin endocytosis and lysosomal
  degradation of PTK7 [PMID:28420671].
  => sign of the canonical-Wnt effect is context dependent; IBA "regulation of" is the
  right level.
- PCP: mouse Ptk7 mutant neural tube/stereocilia defects, genetic interaction with Vangl2
  [PMID:15229603]; Xenopus PTK7 recruits Dsh to membrane with Fz7 [PMID:19004858];
  mouse cochlea: Ptk7 is not required for Dvl2 membrane recruitment, acts via myosin II
  [PMID:22560610]; MDCK/mouse: PTK7-Src at cell-cell contacts regulates ROCK2/actomyosin
  [PMID:24703874]. None of these is a human-protein experiment; in GO terms most are
  acts-upstream phenotypes.
- Human cell biology: MT1-MMP (MMP14) sheds PTK7 at Pro621-Leu622; membrane PTK7 at cell
  junctions and leading edge, enforced expression reorganizes actin and inhibits invasion
  [PMID:20837484]. Endothelial tube formation/migration (sPTK7 decoy, siRNA) [PMID:18471990];
  AML migration/survival [PMID:20558616]; HCT116 knockdown apoptosis [PMID:21103379].
- Disease: human PTK7 variant P545A in idiopathic scoliosis patient fails to rescue zebrafish
  ptk7 [PMID:25182715].

## Decisions summary

- REMOVE protein kinase activity (IEA InterPro2GO) - pseudokinase, contradicted.
- ACCEPT NOT ATP binding.
- MODIFY CTNNB1 IPI protein binding -> beta-catenin binding (GO:0008013); REMOVE HuRI
  keratin-associated / MDFI etc. bare protein binding rows.
- Neuronal IBA terms from PTN002895063 (axon guidance receptor activity, axon, neuronal cell
  body, synapse organization) and derived IEA axon guidance: MARK_AS_OVER_ANNOTATED. The node
  is seeded exclusively by L1-family neuronal CAMs; PTK7 is studied mainly as an epithelial
  PCP regulator and has no PTK7-clade evidence for these.
- Homophilic cell-cell adhesion IBA: MARK_AS_OVER_ANNOTATED (seeds L1cam and fly klingon only).
- No NEW process terms: the PCP role rests on mouse/Xenopus phenotype data, PAINT declined to
  propagate it, and a NEW PCP term for human would be a phenotype-to-process transfer.
