# GNAI3 (Gi alpha-3, UniProt P08754) - curation notes

## Session 2026-10-23

### Deep research status

- `just deep-research-falcon human GNAI3 --fallback perplexity-lite` was run twice and failed both times:
  falcon (Edison) returned `Exception: Failed to authenticate`; the perplexity-lite fallback reported
  `Provider 'perplexity' not available. Available: openai, falcon, openscientist`. No deep-research file
  exists for this gene; the review below is based on the UniProt record, the GOA rows and the cached
  primary literature in `publications/`.

### Identity and family

- 354-aa G alpha subunit, G(i/o/t/z) subfamily of the G-alpha family; G-alpha domain 32-354 with G1/G2
  motifs (UniProt P08754). Initiator Met removed; N-terminal lipid anchor (UniProt: "Lipid-anchor").
- Originally cloned from differentiated HL-60 cells as "Gx alpha" [PMID:3109953 "The cDNA encodes a
  polypeptide of 354 amino acids (Mr 40,519) which is closely related to Gi alpha proteins."]

### Core molecular function: GTPase switch / G protein activity

- UniProt function: "The alpha chain contains the guanine nucleotide binding site and alternates between
  an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes
  GDP release and GTP binding." (P08754 FUNCTION, by similarity to GNAI1 P08753).
- RGS proteins act as GAPs on Gai3: [PMID:8774883 "RGS10 associates specifically with the activated forms
  of two related G-protein subunits, G alphai3, and G alphaz"] and ["RGS10 increases potently and
  selectively the GTP hydrolytic activity of several members of the G alphai family, including G alphai3,
  G alphaz, and G alpha0."]
- Structural RGS/Galpha work [PMID:18434541 "RGS domain binding consequently accelerates Galpha-mediated
  GTP hydrolysis."]; RGS2 triple mutant gains Gai-directed GAP activity [PMID:19478087 "a trio of point
  mutations to RGS2 that elicits Galpha(i)-directed binding and GAP activities"]. Abstract-only in cache;
  the curator's IDA rows (GTPase activity, GDP binding, AC-inhibiting GPCR pathway, GTP metabolic
  process) were made from the full text.

### Effectors and pathways

- Adenylyl cyclase inhibition (canonical Gi): m2 muscarinic receptors couple to AC inhibition through
  Gai3 [PMID:7608168 "We found that both the chick and human m2 mAChRs can couple to Gi alpha-1, Gi
  alpha-2, Gi alpha-3, and G(o)alpha"].
- GIRK channel: recombinant ai-3 stimulated atrial K+ channels [PMID:2535845 "r alpha i-3, activated
  either by guanosine 5'-(3-thio)triphosphate (GTP gamma S) or AlF-4, stimulated in a
  concentration-dependent manner single channel K+ currents in isolated atrial membrane patches"]. Note:
  the field subsequently attributed GIRK activation mainly to Gbetagamma; this alpha-subunit claim is
  historical and not used for a core-function term.
- TRPC5: direct Gai3 effector with cryo-EM structure [PMID:37137991 "Here, we present the cryo-electron
  microscopy structures of the human transient receptor potential canonical 5 (TRPC5)-Gαi3 complexes with
  a 4:4 stoichiometry in lipid nanodiscs."] and ["Electrophysiological analysis shows that Gαi3 increases
  the sensitivity of TRPC5 to phosphatidylinositol 4,5-bisphosphate (PIP2)"]. No GOA row captures an
  ion-channel-regulator MF; left as a suggested question rather than a NEW row.

### Non-receptor GEFs (GBA motif proteins): GIV/Girdin, DAPLE, PLCD4

- GIV is a non-receptor GEF for Gai [PMID:19211784 "We have discovered that GIV/Girdin serves as a
  nonreceptor GEF for G alpha i through an evolutionarily conserved motif"].
- Gai-GIV-EGFR complex [PMID:20462955 "GIV directly interacts with EGFR, and when its GEF function is
  intact, a Galpha(i)-GIV-EGFR signaling complex assembles"].
- Membrane recruitment of GIV activates Gai3 [PMID:27864364 "We found that in unstimulated cells GIV does
  not co-fractionate with its substrate G protein Gαi3 on cell membranes"].
- DAPLE links Frizzled to Gai [PMID:26126266 "Daple contains a Gα-binding and activating (GBA) motif,
  which activates Gαi proteins"].
- PLCD4b GBA motif [PMID:30194280 "putative GBA motifs discovered in bioinformatics searches were
  synthesized on peptide arrays and probed in batch for Gαi3 binding."]
- GoLoco/GPR proteins (GPSM1/AGS3, GPSM2/LGN, GPSM3, PCP2, RGS14) bind GDP-Gai3 (UniProt SUBUNIT;
  numerous binary-interactome IPI rows). These partner interactions are real but the generic
  `protein binding` rows are uninformative; all 17 were REMOVEd per project policy.

### Intracellular localizations and non-canonical roles

- Centrosome / midbody [PMID:17635935 "We show expression of G(ialpha1), G(ialpha2), and G(ialpha3) in the
  centrosomes and at the midbody."]. Caveat from full text: "Giα1 and Giα2 localized in the centrosomes of
  interphase and mitotic cells, but Giα3 did not, contrary to what we observed with Giα3-YFP" (endogenous
  antibody failed; YFP fusion positive). Midbody endogenous staining: "We also detected midbody Giα3 and
  RGS14 staining". Overexpression phenotype: "Both wild-type and the GTPase-deficient form of Giα3
  resulted in prolonged mitosis, although they did not affect cytokinesis." Treated as non-core.
- Plasma membrane predominant for YFP fusions [PMID:17635935 "Imaging of live cells transfected with the
  Giα-YFP constructs demonstrated that the fusion proteins were predominantly localized at the plasma
  membrane in most cells, although not in all cells"].
- Golgi: older literature cited in PMID:17635935: "(1994) reported strong plasma membrane and Golgi staining
  by an anti-Giα3 antibody in certain cells."
- Macroautophagy (HT-29 cells) [PMID:12642577 "AGS3 contains GoLoco or G-protein regulatory motifs in its
  COOH-terminal half that stabilize the GDP-bound conformation of the alpha-subunit of the trimeric Gi3
  protein. The latter is part of a signaling pathway that controls the lysosomal-autophagic catabolism in
  human colon cancer HT-29 cells."] Abstract only; nucleotide-state dependent (GDP-bound form promotes,
  GTP-bound form was earlier shown to inhibit). Kept as non-core.

### Disease

- Auriculocondylar syndrome 1 (ARCND1), dominant missense (e.g. G40R in G1 motif) [PMID:22560091 "We used
  exome sequencing of five probands and identified two novel (exclusive to the patient and/or family
  studied) missense mutations in PLCB4 and a shared mutation in GNAI3 in two unrelated probands."] and
  ["We suggest that PLCB4 and GNAI3 are core signaling molecules of the endothelin-1-distal-less homeobox
  5 and 6 (EDN1-DLX5/DLX6) pathway."]; additional case [PMID:23315542 "one heterozygous GNAI3 missense
  mutation"]. Interesting mechanistically: a Gi alpha in an EDNRA (Gq-coupled) pathway; dominant
  interference proposed.

### Background paper checked (Deutsch et al. 2026, PMID:42870023)

- smFRET of the alpha-helical domain (AHD) opening in muOR-Gi complexes. Methods state the protein used
  was Gai1, not Gai3: "The R90C and E238C substitutions were introduced into a previously published
  minimal cysteine background (C3S;C66A;C214S;C350S;C325A;C351I) of human Gαi1" and "WT Gi heterotrimer
  (Gαi1β1γ2) from Hi-5 cells was prepared similarly". Because no Gai3 was assayed, it is NOT cited in
  the GNAI3 review; it is relevant to the shared Gai-family mechanism only.

### Decisions summary

- Core: G protein activity / GTPase activity, GTP/GDP binding, Gbetagamma binding, heterotrimeric
  G-protein complex at the cytoplasmic side of the plasma membrane, adenylate cyclase-inhibiting GPCR
  signaling.
- General pathway terms (GPCR signaling pathway, adenylate cyclase-modulating, signal transduction) MODIFY
  to the adenylate cyclase-inhibiting pathway; generic `membrane` MODIFY to plasma membrane;
  `guanyl nucleotide binding` MODIFY to GTP binding.
- GTP metabolic process marked over-annotated (GTP hydrolysis by a signaling switch is not a metabolic
  role).
- Intracellular localizations (centrosome, midbody, Golgi, ER, lysosome, exosome, cytoplasm, cytosol),
  cell division and macroautophagy regulation kept as non-core.
