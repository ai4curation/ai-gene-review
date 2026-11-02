# Map2k3 (rat) - manual literature synthesis

No deep-research API was available for this session, so this summary was compiled
manually from the cached publications in `publications/` and from the human and mouse
ortholog records. Provenance is given inline.

## Identity

- Rat Map2k3 (MKK3, MEK3), RGD:1306620, Rattus norvegicus (NCBITaxon:10116).
- The GOA file is keyed to the TrEMBL entry F7EXM7 (434 aa, Ensembl ENSRNOP00000008679),
  which carries the same RGD cross-reference as the older TrEMBL entry B1H230 (347 aa,
  EMBL AAI60839.1). F7EXM7 is B1H230 with an 87-residue N-terminal extension: residues
  88-434 of F7EXM7 are identical to B1H230 1-347 (reviewer sequence comparison of the two
  UniProt records). The 347-residue form aligns end to end with human MAP2K3 (P46734).
  Whether the Ensembl N-terminal extension is translated is not established.
- Kinase domain F7EXM7 151-412 (PROSITE PS50011), ATP-binding Lys180, proton-acceptor
  Asp277; the activation-loop S305/T309 (SVAKT) corresponds to human Ser218/Thr222, the
  sites phosphorylated by upstream MAP3Ks [UniProtKB:P46734 MOD_RES 218/222,
  ECO:0000269 PubMed:8622669]. Belongs to the STE group, MAP kinase kinase subfamily;
  PANTHER PTHR48013:SF21 (dual specificity MAPKK 3).

## Molecular function

- Human MKK3: "Dual specificity kinase. Is activated by cytokines and environmental stress
  in vivo. Catalyzes the concomitant phosphorylation of a threonine and a tyrosine residue
  in the MAP kinase p38." [UniProtKB:P46734 CC FUNCTION].
- Activated MKK3 and MKK6 "phosphorylate and activate p38 MAP kinase" and their expression
  caused "a selective increase in p38 MAP kinase activity" [PMID:8622669 abstract].
- MKK3 and MKK6 "are specific for p38 MAP kinase, whereas the MKK4 protein kinase can
  activate both p38 MAP kinase and JNK" [PMID:10097111].
- Rat-specific direct evidence: endogenous MKK3 immunoprecipitated from perfused rat heart
  was assayed by immune-complex kinase assay with GST-p38 plus GST-ATF2 as substrates
  [PMID:20550965 methods]; "No MKK activity was detected in immunoprecipitates using control
  antibody, or in assays lacking GST-MAPK or substrate" [PMID:20550965 results]. This is a
  coupled MAPKK assay showing that rat MKK3 activates p38. It is not in GOA as an MF row.

## Biological process

- p38 MAPK cascade: MAP2K tier between MAP3Ks (ASK1, TAK1, TAO2) and p38. In rat heart,
  "Both of the known p38 activators MKK3 and MKK6 were activated by ischaemia but with
  different time courses" [PMID:20550965]; "MKK3 appeared to have a relatively high basal
  activity but was activated further by ischaemia" [PMID:20550965].
- Mouse knockouts: Mkk3-/- fibroblasts were "selectively defective in the activation of p38
  MAP kinase" by TNF and in TNF-induced IL-1/IL-6 expression [PMID:10097111]; Mkk3-/- mice
  are "defective in interleukin-12 (IL-12) production by macrophages and dendritic cells"
  [PMID:10202148]. JIP4 activates p38 "by a mechanism that requires the MAP kinase kinases
  MKK3 and MKK6" [PMID:15767678].
- ASK1 binds its substrate MKK3; MPK38-mediated ASK1 activation "was induced through the
  increased interaction between ASK1 and its substrate MKK3" [PMID:18948261, mouse].
- Rat astrocytes: "MKK3 was phosphorylated in response to LPS, and expression of
  constitutively active MKK3 ... activated CYP2E1" [PMID:14670949, abstract only].
- Cardiac: constitutively active MKK3bE transgenic mouse hearts showed p38 activation,
  contractile depression and restrictive cardiomyopathy [PMID:11593045, abstract]; this is
  a gain-of-function phenotype, not evidence of a normal role in contraction.
- Postnatal rat heart: Mkk3 protein up-regulated during postnatal development
  [PMID:9779826, abstract only] - expression evidence only.
- Human cell-context roles: VEGF-induced p38 activation and endothelial migration require
  MKK3 [PMID:22696064]; Hippo/YAP and HNF1alpha/Mirk effects are indirect (see human
  MAP2K3 review).

## Location

No rat localization data. Human MKK3 is a soluble cytosolic/nuclear protein (Reactome TAS
in the human review); no GOA CC rows exist for rat.
