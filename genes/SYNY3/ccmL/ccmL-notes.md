# ccmL (sll1030, P72759) notes — Synechocystis sp. PCC 6803

## Provenance of this review

- 2026-10-19: `just fetch-gene SYNY3 ccmL --uniprot-id P72759` (5 GOA rows).
- Deep research: `just deep-research SYNY3 ccmL --provider falcon` failed twice
  ("Edison API request failed: Failed to authenticate", HTTP 403). No
  deep-research file exists; the review is grounded in the UniProt record, GOA,
  and primary literature cached under `publications/`.

## Identity and structure

- 100-aa protein, CcmL/EutN family, CcmL subfamily; single BMV (Pfam PF03319)
  domain [file:SYNY3/ccmL/ccmL-uniprot.txt "Belongs to the CcmL/EutN family. CcmL subfamily."].
- Crystal structure of the Synechocystis protein (PDB 2QW7, 2.4 A) shows a
  homopentamer whose size and shape fit the vertices of an icosahedral shell
  [PMID:18292340 "Both proteins assemble to form pentameric structures whose size and shape are compatible with formation of vertices in an icosahedral shell"].
- UniProt: "The tight homopentamer forms a pore with an opening of about 5
  Angstroms in diameter" (ECO:0000269 PubMed:18292340).
- Orthologs from Thermosynechococcus, Gloeobacter and Nostoc give the same
  pentameric fold [PMID:23949415 "Facets composed of hexameric proteins are connected at the vertices by pentameric proteins"];
  [PMID:24504539 "CcmL is a small, pentameric protein that is argued to fill the vertices of β-carboxysomal shell"].

## Role in the carboxysome

- beta-carboxysome shell model: CcmK2 hexamers form facets, CcmO edges, CcmL
  vertices [PMID:22928045 "These data suggested a model for the facet structure of β-carboxysomes with CcmL forming the vertices"].
- Genetics (Synechococcus elongatus PCC 7942 ortholog): ccmL insertion mutants
  require high CO2 and make abnormal rod-shaped carboxysomes
  [PMID:8491708 "The PVU mutant has a drug marker inserted into the ccmL gene, and it possesses abnormal rod-shaped carboxysomes"].
  The rod phenotype is consistent with a vertex location
  [PMID:22928045 "Mutant carboxysomes lacking the CcmL protein have a characteristic rod-like appearance which is consistent with its location at the icosahedral vertex in structural models"].
- Function of vertices: in the alpha-carboxysome of Halothiobacillus, loss of
  the analogous CsoS4 pentamers leaves the shape largely normal but makes the
  shell leaky to CO2 [PMID:19844578 "In the absence of the CsoS4 proteins the carboxysome shell loses its limited permeability to CO(2)"].
  That is analogy (alpha-type, CsoS4 not CcmL); not shown for CcmL itself.
- Assembly: shell proteins (hexamers and pentamers) encapsulate a pre-formed
  procarboxysome core [PMID:24267892 "Subsequently, shell proteins encapsulate this procarboxysome"].
- Interactions (Synechocystis, yeast two-hybrid): CcmL binds CcmM73, linking
  the shell to the bicarbonate dehydration complex (CcmM-CcaA-CcmN)
  [PMID:17993516 "This complex, through CcmM73, also interacts with the major bacterial microcompartment shell proteins CcmK and CcmL"].
  A weak CcmL-CcmK2 interaction was seen only at high concentration (Nostoc
  ortholog) [PMID:24504539 "Förster resonance energy transfer experiments were able to show a weak interaction between CcmL and CcmK2"].

## GO assessment summary

- GO:0043886 structural constituent of carboxysome shell (IPI, IEA): correct.
  The vertex pentamer is a component of the shell; GO has no vertex-specific
  term. ACCEPT both rows.
- GO:0031470 carboxysome (IEA): correct, ACCEPT. (Direct localization in
  Synechocystis not shown in cached papers; the Synechococcus ortholog Q03512
  has IDA/EXP carboxysome annotations in GOA.)
- GO:0031469 bacterial microcompartment (IEA InterPro): true but entailed by
  carboxysome, TOO_GENERAL.
- GO:0015977 carbon fixation (IEA UniRule): CcmL catalyses nothing and supplies
  no substrate; RuBisCO performs the fixation step. Comparator check (QuickGO
  2026-10-19): the shell proteins CcmK2 (P72761) and S. elongatus CcmL (Q03512)
  carry GO:0015977 only via the same GO_REF:0000104 IEA; no shell protein has
  an experimental carbon-fixation annotation. Treated as pathway-membership
  over-annotation: MARK_AS_OVER_ANNOTATED. GO lacks a carboxysome assembly or
  CO2-concentrating-mechanism process term (OLS searches "carboxysome assembly",
  "microcompartment organization", "carbon concentrating" returned nothing).

## NCBI PGAP

- WP_010871404.1 named from NF053795.1 (equivalog, "beta-carboxysome shell
  vertex protein CcmL"), carrying GO:0031470, GO:0043886, GO:0015977. The
  WP_ record (14-APR-2026) shows these GO terms; the January 2026 genome
  annotation (GCF_000009725.1-RS_2026_01_07) does not, so the genome record lags.
- Verdict: carboxysome and shell constituent are CNN (agree with GOA/main
  review); carbon fixation is the same over-annotation as in GOA.
