# ITGAM (CD11b; integrin alpha-M; CR3 alpha chain) - review notes

**Provenance note:** provider deep research for this gene FAILED (Falcon returned
HTTP 402 Payment Required; Perplexity is not configured in this environment). No
`ITGAM-deep-research-<provider>.md` file exists. The synthesis below replaces it and
was written manually from the UniProt record (P11215), the GOA annotation set, and
cached publications in `publications/` (fetched with `just fetch-gene-pmids` /
`just fetch-pmid`). Quotes are verbatim from the cached files.

## Identity and structure

- UniProt P11215, ITGAM_HUMAN; integrin alpha chain family; single-pass type I
  membrane protein with an inserted von Willebrand factor A-like I (alphaI/A) domain.
  [PMID:2563162 "The deduced amino acid sequence indicates the presence of an extensive extracellular
  domain with three putative metal-binding regions, (i) an amino acid region that
  is homologous to the A domain of von Willebrand factor"]
- Pairs non-covalently with ITGB2 (CD18) to form integrin alphaM-beta2 (Mac-1,
  complement receptor 3, CR3). [PMID:2563162 "consists of two noncovalently associated subunits, designated
  alpha M (Mac-1 alpha, Mol alpha, or CD11b; Mr, 170,000) and beta (Mac-1 beta,
  Mol beta, or CD18; Mr, 100,000)"]
- Expression: monocytes, macrophages, granulocytes, microglia, NK and minor B/T subsets.
  [PMID:8485905 "The C3 receptor CR3 is expressed on phagocytic cells, minor subsets of B and T
  cells, and natural killer (NK) cells."]

## Core molecular function: complement (iC3b) receptor

- The alphaM I-domain is the iC3b binding site; binding is divalent-cation dependent.
  [PMID:7524101 "A recombinant fragment representing the CR3 A-domain, a 200-amino acid region in
  the ectodomain of the CD11b subunit, bound to iC3b directly and in a divalent
  cation-dependent manner."]
- Structural basis: the C3d moiety of iC3b binds the CR3 alphaI domain; explains
  selectivity for iC3b over C3b. [PMID:24065820 "We demonstrate that the C3d moiety of iC3b harbors the binding
  site for the CR3 αI domain, and our structure of the C3d:αI domain complex
  rationalizes the CR3 selectivity for iC3b."]
- Function: recognition and phagocytosis of iC3b-opsonised particles.
  [PMID:24065820 "recognizes iC3b on complement-opsonized objects, enabling their
  phagocytosis."]
- Human genetic evidence for the phagocytic receptor role: lupus-associated R77H
  (rs1143679) reduces iC3b-mediated phagocytosis. [PMID:22586164 "A 31% reduction was
  observed in the phagocytosis of iC3b opsonised sheep erythrocytes (sRBC(iC3b))
  by 77H cells (p=0.003)"]; association with SLE [PMID:18204448 "The strongest association was at a nonsynonymous SNP, rs1143679"].
- Implication: the ligand of CR3 is a fragment of C3 (iC3b), which is deposited on
  targets by complement activation; CR3 is the receptor/effector, not a complement
  activator.

## Adhesion receptor function

- Counter-receptor for ICAM-1 (neutrophil-endothelial adhesion). [PMID:1980124 "we conclude that ICAM-1 is a counter receptor for Mac-1 and that this receptor
  pair is responsible, in part, for the adhesion between stimulated neutrophils
  and stimulated endothelial cells."]
- Other cellular counter-receptors: JAM-3/JAM-C [PMID:12208882 "JAM-3 directly bound to Mac-1, and this binding was similar in its extent to the binding of ICAM-1 or fibrinogen, which both are known ligands for Mac-1"];
  Thy-1 [PMID:15004192 "we have identified the specific interaction between human Thy-1 and the leukocyte
  integrin Mac-1 (CD11b/CD18; alphaMbeta2) both in cellular systems and in
  purified form."]; ECM protein TGFBIp [PMID:18083624 "mediates monocytes adhesion under both static
  and flow conditions mainly through integrin alphaMbeta2"]; pleiotrophin
  [PMID:28939773 "we identified the integrin Mac-1 (αMβ2, CD11b/CD18) as the receptor mediating macrophage adhesion and migration to PTN"].
- Ligand promiscuity is a known property. [PMID:15194813 "Receptortargeted studies using CD11b/CD18 have demonstrated that this integrin has great promiscuity in ligand binding with more than 30 protein or nonprotein molecules reported to date."]
- Activation dependence (kindlin-3): [PMID:19234460 "confirming a selective impairment of activation-dependent functions of αMβ2 integrin."]

## Signaling / neutrophil activation

- CD177 (NB1)-PR3 signalling complex uses Mac-1 as transmembrane adaptor; required for
  ANCA-triggered degranulation and superoxide. [PMID:21193407 "We
  establish the pivotal role of the NB1-Mac-1 receptor interaction for
  PR3-ANCA-mediated neutrophil activation."]; lipid rafts [PMID:21193407 "NB1, PR3, and Mac-1 were located
  within lipid rafts."]
- CD11b/CD18 promotes phagocytosis-induced neutrophil apoptosis (mouse KO).
  [PMID:8986723 "CD11b/CD18
  plays a novel and unsuspected homeostatic role in inflammation by accelerating
  the programmed elimination of extravasated neutrophils."]

## Microglia / CNS (mouse data; basis of ISS annotations)

- Developmental synapse pruning: microglia engulf C3-tagged retinogeniculate inputs via
  CR3. [PMID:22632727 "Taken together, these data demonstrate that phagocytic signaling through CR3 and its ligand C3 is one molecular mechanism by which microglia engulf RGC inputs."]
  CR3 KO yields eye-specific segregation defects (vertebrate eye-specific patterning).
- Disease models (Alzheimer mice): oligomeric Abeta-induced synapse engulfment requires CR3.
  [PMID:27033548 "These data demonstrate that CR3 is necessary for oAβ-dependent engulfment of synapses by microglia."]
- Fibrillar Abeta uptake/clearance partly through C3 and Mac-1. [PMID:22438044 "these results demonstrate that C3 and Mac-1 are involved in
  phagocytosis and clearance of fAβ by microglia"]; anti-CD11b reduces uptake of
  Abeta-coated particles [PMID:20199584 "antibodies against CD11b or CD18
  reduced the uptake of the artificial amyloid deposit by microglial cell showing
  that CR3 is involved in the mechanism."]. Direct Abeta binding by CR3 is not shown
  in these abstracts.
- Developmental hippocampal neuronal death and microglial superoxide require CD11b and
  DAP12. [PMID:18685038 "we show that DAP12 and CD11b control the production of
  microglial superoxide ions, which kill the neurons."]
- MPTP Parkinson model: MAC1 KO reduces microgliosis, superoxide, p47phox translocation.
  [PMID:18981141 "MAC1 plays a critical
  role in MPTP/MPP(+)-induced reactive microgliosis"]. These are downstream/indirect
  phenotypes; dopamine metabolism and protein targeting terms derived from this are
  over-interpretations.

## Curation conclusions (summary)

- Core: CR3 iC3b receptor (contributes to complement component iC3b receptor
  activity as the alphaM subunit; directly binds iC3b via alphaI domain), mediating
  recognition/phagocytosis of complement-opsonised targets, including C3-tagged
  synapses by microglia.
- Core: adhesion receptor for ICAM-1 and other counter-receptors, leukocyte adhesion to
  activated endothelium, cell-matrix adhesion (fibrinogen, TGFBIp).
- Remove: generic protein binding (HuRI Y2H hits among ER/membrane proteins; others are
  better captured as cell adhesion molecule binding), Ensembl rat-projected "response
  to X" terms, ARBA gross anatomical development term.
- C3b binding (ISS) should become iC3b binding (CR3 selectivity for iC3b).
