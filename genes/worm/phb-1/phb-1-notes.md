# phb-1 (Caenorhabditis elegans) — research notes

UniProt: Q9BKU4 (PHB1_CAEEL). WormBase: WBGene00004014 / Y37E3.9.
Gene name: phb-1 ("Mitochondrial prohibitin complex protein 1", prohibitin-1).
275 aa; single Band_7/SPFH (prohibitin/stomatin) domain (PF01145; IPR000163);
predicted coiled coil (residues 180–213). PANTHER family PTHR23222 (PROHIBITIN),
subfamily PTHR23222:SF0 (PROHIBITIN 1). ComplexPortal CPX-4114 (Prohibitin complex).

## One-line summary

phb-1 is one of the two obligate subunits (with phb-2) of the mitochondrial
prohibitin (PHB) complex, a ring-shaped, high-molecular-weight assembly in the
mitochondrial inner membrane. The complex — not the isolated subunit — is the
functional unit; loss of either subunit abolishes the whole complex.

## KNOWN (well supported)

- **Obligate heterodimeric/ring complex with phb-2 in the mitochondrial inner
  membrane.** "Prohibitins in eukaryotes consist of two subunits (PHB1 and PHB2)
  that together form a high molecular weight complex in the mitochondrial inner
  membrane" and, in worm, "prohibitins in C. elegans form a high molecular weight
  complex in the mitochondrial inner membrane similar to that of yeast and humans"
  [PMID:12794069 "prohibitins in C. elegans form a high molecular weight complex in the mitochondrial inner membrane similar to that of yeast and humans"].
  The two subunits "bind to each other to form a heterodimer that is assembled into
  a ring-like macromolecular structure at the inner mitochondrial membrane" and are
  "interdependent for the formation of the complex, leading the absence of one of
  them to the absence of the whole complex"
  [PMID:26092086 "which bind to each other to form a heterodimer that is assembled into a ring-like macromolecular structure at the inner mitochondrial membrane"]
  [PMID:26092086 "These two subunits are interdependent for the formation of the complex, leading the absence of one of them to the absence of the whole complex"].
  Basis for GO:0035632 (mitochondrial prohibitin complex), GO:0005743 (mitochondrial
  inner membrane). The IPI part_of annotation (PMID:19812672) is with phb-2
  (WB:WBGene00004015).

- **Essential for embryonic viability and germline/gonad development.** RNAi against
  phb-1 or phb-2 "PHB proteins are essential during embryonic development and are
  required for somatic and germline differentiation in the larval gonad"
  [PMID:12794069 "PHB proteins are essential during embryonic development and are required for somatic and germline differentiation in the larval gonad"].
  Restated later: prohibitin depletion "gives rise to a wide range of somatic and
  germline defects, spanning from complete sterility to severely reduce brood sizes
  and a morphologically abnormal somatic gonad"
  [PMID:26092086 "gives rise to a wide range of somatic and germline defects, spanning from complete sterility to severely reduce brood sizes and a morphologically abnormal somatic gonad"].
  Basis for the WB IMP annotations to embryo development (GO:0009792), gonad
  development (GO:0008406), oogenesis (GO:0048477), spermatogenesis (GO:0007283).

- **Altered mitochondrial biogenesis / organization on depletion.** "a deficiency in
  PHB proteins results in altered mitochondrial biogenesis in body wall muscle
  cells" [PMID:12794069 "a deficiency in PHB proteins results in altered mitochondrial biogenesis in body wall muscle cells"].
  Basis for GO:0007005 (mitochondrion organization). PHB-2 knockdown "influences ...
  mitochondrial proliferation" [PMID:19812672 "animal fat content and mitochondrial proliferation in a genetic-background- and age-specific manner"].

- **Context-dependent modulator of longevity, coupling to insulin/diapause signalling
  and fat metabolism.** "the mitochondrial prohibitin complex promotes longevity by
  modulating mitochondrial function and fat metabolism in the nematode Caenorhabditis
  elegans"; "prohibitin deficiency shortens the lifespan of otherwise wild-type
  animals" but "knockdown of prohibitin promotes longevity in diapause mutants or
  under conditions of dietary restriction"
  [PMID:19812672 "prohibitin deficiency shortens the lifespan of otherwise wild-type"]
  [PMID:19812672 "knockdown of prohibitin promotes longevity in diapause mutants or under conditions of dietary restriction"].
  Later restated with genotype: "prohibitin deficiency shortens the lifespan of
  otherwise wild type nematodes, while it dramatically extends the lifespan of the
  already long-lived daf-2(e1370) insulin receptor mutants"
  [PMID:26092086 "while it dramatically extends the lifespan of the already long-lived daf-2(e1370) insulin receptor mutants"].
  Depletion "influences ATP levels, animal fat content and mitochondrial
  proliferation in a genetic-background- and age-specific manner"
  [PMID:19812672 "Depletion of prohibitin influences ATP levels, animal fat content and mitochondrial proliferation"].

- **Proposed complex-level molecular roles (from yeast/mammalian work, invoked for
  the worm complex):** membrane-bound chaperone that stabilizes newly synthesized
  mitochondrial-encoded respiratory subunits, and/or membrane scaffold that recruits
  membrane proteins to a specific lipid environment.
  "The PHB complex has been shown to play a role in the stabilization of newly
  synthesized subunits of mitochondrial respiratory enzymes in the yeast
  Saccharomyces cerevisiae"
  [PMID:12794069 "the stabilization of newly synthesized subunits of mitochondrial respiratory enzymes in the yeast Saccharomyces cerevisiae"].
  "Several roles have been proposed for the mitochondrial prohibitin complex,
  including a role as a membrane-bound chaperone, which holds and stabilizes newly
  synthesised mitochondrial-encoded proteins ... and as scaffold proteins that
  recruit membrane proteins to a specific lipid environment"
  [PMID:26092086 "a membrane-bound chaperone, which holds and stabilizes newly synthesised mitochondrial-encoded proteins"]
  [PMID:26092086 "as scaffold proteins that recruit membrane proteins to a specific lipid environment"].
  Basis for GO:0050821 (protein stabilization, NAS). Note the qualifier: these are
  *proposed* roles imported largely from yeast/human, not directly demonstrated
  biochemically in worm.

## NOT known / debated (knowledge gaps)

- **The molecular mechanism of the prohibitin complex is genuinely unresolved.**
  The 2015 metabolome paper states plainly: "the true function of the mitochondrial
  prohibitin complex remains elusive"
  [PMID:26092086 "the true function of the mitochondrial prohibitin complex remains elusive"].
  Whether the complex works primarily as (a) a membrane-bound chaperone/holdase for
  nascent inner-membrane proteins, (b) a scaffold that organizes a specific
  cardiolipin/phospholipid microdomain and recruits client membrane proteins, or
  (c) a regulator of the m-AAA protease (SPG-7/paraplegin) is not settled — the
  literature proposes all three but demonstrates none as *the* mechanism in worm.
  This is both a genuine biology gap and an ontology gap: "be the structural PHB
  ring / organize an IMM lipid-protein microdomain" has no adequate GO molecular
  function term, so a structural subunit reads as MF-dark.

- **How the SAME depletion produces OPPOSITE ageing outcomes** (life-shortening in WT
  vs life-extending in daf-2 / DR / mitochondrial mutants) is mechanistically
  unexplained — the metabolic node the complex sits on is not defined.

## Annotation-relevant reasoning

- The 11 WB IMP annotations (PMID:12794069) and the 11 ARBA IEA annotations
  (GO_REF:0000117) are pairwise redundant on the same term set (regulation of
  oxidative phosphorylation, response to oxidative stress, mitochondrion
  organization, spermatogenesis, gonad development, embryo development, defecation,
  positive regulation of multicellular organism growth, regulation of nematode
  pharyngeal pumping, oogenesis). The ARBA rules appear to recapitulate the C.
  elegans phenotype literature. The IEA rows are redundant electronic echoes of the
  experimental IMP rows.
- Many of the IMP phenotype terms (defecation, pharyngeal pumping, positive
  regulation of growth, spermatogenesis, oogenesis, oxidative stress response) are
  **downstream/pleiotropic consequences** of losing an essential mitochondrial
  complex, not evidence of a dedicated phb-1 role in each named process. These are
  best kept as NON-core (pleiotropy of an essential mito gene) rather than as core
  functions. The abstract of PMID:12794069 supports embryonic + germline/gonad +
  mitochondrial biogenesis phenotypes directly; the more specific behavioural terms
  (defecation, pharyngeal pumping) are in the full text, which curators read — do
  not REMOVE, keep as non-core.
- Core: complex membership (GO:0035632), IMM localization (GO:0005743),
  mitochondrion organization (GO:0007005), protein stabilization (GO:0050821 —
  complex-level chaperone role). Structural-subunit MF ≈ structural molecule
  activity (GO:0005198); the complex's true activity is the ontology/biology gap.

## Provenance / sources

- PMID:12794069 — Artal-Sanz et al. 2003, J Biol Chem (RNAi phenotype; complex; IMM).
  Abstract-only in cache; curators (WB) read full text for the IMP/IDA rows.
- PMID:19812672 — Artal-Sanz & Tavernarakis 2009, Nature (longevity/diapause/fat).
  Abstract-only in cache. Source of IPI complex annotation (with phb-2).
- PMID:26092086 — Lourenço et al. 2015, BBA Bioenergetics (metabolome; full text in
  cache). Source of ComplexPortal IDA/NAS rows; richest verbatim source.
- UniProt Q9BKU4; PANTHER PTHR23222; ComplexPortal CPX-4114.

## Falcon deep-research synthesis (phb-1-deep-research-falcon.md, 33 citations)

The falcon report (Edison Scientific; genuine, 20-min run) reinforces and enriches
the picture above. Additional mechanistic context (grounded in review/primary
literature cited there; not all in our cached PMIDs, so used as context only, not as
verbatim supporting_text in the YAML):

- **Membrane-bound scaffold + holdase/chaperone**: "PHB-1 is not an enzyme,
  transporter, or signaling receptor. Rather, it functions as a membrane-bound
  scaffold and holdase/unfoldase-type chaperone within the inner mitochondrial
  membrane" and "Its precise biochemical activity has remained challenging to
  define" — direct confirmation of the MF-dark ontology/biology gap I recorded.
- **m-AAA protease / OPA1 / cristae**: the complex physically interacts with the
  m-AAA proteases (SPG-7/paraplegin; AFG3L2) and restrains OMA1, stabilizing long
  OPA1 (worm EAT-3) isoforms; loss → aberrant OPA1 processing, cristae disruption,
  mitochondrial fragmentation (matches the "altered mitochondrial biogenesis"
  phenotype in Artal-Sanz 2003). [Hernando-Rodríguez & Artal-Sanz 2018, Cells;
  DOI 10.3390/cells7120238]
- **Lipid organization**: interacts with cardiolipin / phosphatidylethanolamine
  metabolism; the SPFH domain may bind lipids (not biochemically proven) — one arm
  of the scaffold-vs-chaperone-vs-lipid-organizer debate.
- **Nucleoid / mtDNA**: associates with nucleoids (with ATAD3/TFAM); depletion
  reduces mitochondrial protein synthesis.
- **Mitophagy is via PHB-2, not phb-1 directly**: PHB-2 is the IMM LC3 receptor
  (LIR motif); phb-1 participates only through the heterocomplex. This is why
  phb-1 appears in the CAEEL_MITOPHAGY flagship (as part of import/proteostasis).
  [Wei et al. 2017, Cell]
- **Context-dependent longevity mechanism** (the second knowledge gap): PHB
  depletion shortens WT lifespan but extends it in daf-2 (IIS), sgk-1 and rict-1
  (TORC2) mutants and under dietary restriction; SGK-1 is a major determinant;
  requires UPRmt + autophagy (not mitophagy) and SREBP/SBP-1; strongly induces
  UPRmt via ATFS-1. [Gatsi 2014 PLoS ONE 10.1371/journal.pone.0107671;
  de la Cruz-Ruiz 2021 Aging Cell 10.1111/acel.13359; Lourenço & Artal-Sanz 2021
  Metabolites 10.3390/metabo11090636]
- **2025 in situ structure**: cryo-ET resolved the human PHB complex as a
  bell-shaped 11-subunit alternating PHB1/PHB2 assembly (~190 Å), refining the
  older "12–16 heterodimer ~1 MDa ring" model; worm stoichiometry not independently
  resolved. [Lange et al. 2025, Nat Cell Biol 10.1038/s41556-025-01620-1]

None of these change the GOA annotation actions; they corroborate keeping the
complex/localization/mito-organization/protein-stabilization terms as core and the
developmental/behavioural terms as pleiotropic non-core, and they sharpen the two
recorded knowledge gaps (mechanism; opposite-longevity node).
