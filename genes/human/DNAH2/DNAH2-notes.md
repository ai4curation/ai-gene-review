# DNAH2 curation notes

Deep research: falcon failed (Edison API "Failed to authenticate"); no deep-research file.

## Identity
- Q9P225, 4427 aa; stem 1-1764, AAA1-AAA6 motor and stalk (UniProt). Heavy chain of the two-headed
  I1/f inner arm with DNAH10 [PMID:30060180 "Our results also provide the first experimental
  evidence that validates Dnah10 and Dnah2 as HCs and Wdr78, Wdr63, and Casc1 as ICs of vertebrate
  Dynein-f"]. IDAf composition [PMID:40898283 "The IDAf complex comprises intermediate chains
  (DNAI3, DNAI4, DNAI7), light chains (DYNLRB1, DYNRB2, DYNLL1), and heavy chains (DNAH2, DNAH10,
  DNAH12)."]. The DNAH12 inclusion there is unconfirmed.

## Function / phenotype
- Mouse ependymal cilia: [PMID:30060180 "Depletion of Wdr78 or Dnah2 by RNAi paralyzed mouse
  ependymal cilia."]; Wdr78 associates with Dnah2 [PMID:30060180 "Wdr78 associated with Dynein-f
  subunits such as Dnah2 (a HC) and Wdr63 (IC140 orthologue)."].
- Human MMAF / SPGF45 [PMID:30811583 "The DNAH2 protein level was significantly decreased and inner
  dynein arms were absent in the spermatozoa of patients."; PMID:33771466; PMID:33968937].
- Mouse KO [PMID:33968937 "Dnah2-null males, but not females, are infertile."]; centriole/annulus
  defects and loss of DNAH1 from flagella.
- DNAH2 is present in DNAH17-mutant sperm as an IDA marker [PMID:31178125 "DNAH2 and DNALI, two
  inner dynein arm components"].
- Non-ciliary DNA repair claim (U2OS siRNA) [PMID:35402838] is not used for annotation.

## Curation decisions
- Core MF minus-end-directed microtubule motor activity; BP flagellated sperm motility and cilium
  movement involved in cell motility; CC inner dynein arm, sperm flagellum, 9+2 motile cilium.
- Light intermediate chain binding (IBA/IEA) marked over-annotated: the IBA comes from a deep node
  seeded by cytoplasmic dynein-1 heavy chains; the I1/f arm has no reported LIC, and the I1/f heavy
  chain DNAH10 localizes independently of DNALI1 [PMID:36792588 "Being a component of subspecies
  I1α, DNAH10 was not affected by the loss of DNALI1"].
- Intermediate chain binding accepted (DNAI3/DNAI4/DNAI7 in I1/f).
- cilium-dependent cell motility (IMP, NAS) modified to flagellated sperm motility.

## PANTHER / IBA check
- Human DNAH2 and mouse Dnah2 (P0C6F1) carry the same seven IBA terms in QuickGO; no family split.
- PANTHER classification routes disagree. The PANTHER geneinfo service puts Q9P225 in
  PTHR10676:SF183 ("DYNEIN AXONEMAL HEAVY CHAIN 2"), which is where the IBAs come from. The
  UniProt/InterPro cross-reference instead puts DNAH2 in PTHR46532:SF11, whose official name is
  "DYNEIN AXONEMAL HEAVY CHAIN 12" (interpro/panther/PTHR46532/PTHR46532-entries.csv; name from
  interpro/panther/panther.obo). This looks like a DNAH2/DNAH12 mix-up in the InterPro-side PANTHER
  assignment. It does not affect the GOA IBAs.
