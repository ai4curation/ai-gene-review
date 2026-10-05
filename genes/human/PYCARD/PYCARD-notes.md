# PYCARD (ASC) review notes

**Provenance note:** provider deep research for this gene FAILED (Falcon returned HTTP 402
Payment Required; Perplexity is not configured). This file is a manual literature synthesis
built from the UniProt record (Q9ULZ3), the cached publications under `publications/`, and a
targeted web search (for the Dock2 confound, below). It replaces the provider deep-research
report. No `*-deep-research-<provider>.md` file exists for this gene.

## Identity and domain architecture

- Human PYCARD, UniProt Q9ULZ3, 195 aa. Also called ASC (apoptosis-associated speck-like
  protein containing a CARD) and TMS1 (target of methylation-induced silencing 1).
- Two death-fold domains joined by a flexible linker: N-terminal pyrin domain (PYD, residues
  1-91) and C-terminal CARD (residues 107-195) (UniProt FT DOMAIN). No catalytic domain.
- First identified as a protein that aggregates into a "speck" during apoptosis of HL-60 cells
  [PMID:10567338 "one mAb recognized a 22-kDa protein that exhibited intriguing behavior by
  forming an aggregate and appearing as a speck during apoptosis induced by retinoic acid and
  other anti-tumor drugs"].
- PANTHER places it in PTHR46985 (NLRP1 family name) subfamily SF2 because it shares PYD and
  CARD domains with NLRP1/CARD8; it has no NACHT or LRR domain.

## Core function: bipartite adaptor of ASC-dependent inflammasomes

- ASC bridges sensor and caspase-1 through homotypic interactions
  [PMID:24630722 "The adaptor protein ASC bridges the sensor proteins and caspase-1 to form
  ternary inflammasome complexes, achieved through pyrin domain (PYD) interactions between
  sensors and ASC and through caspase activation and recruitment domain (CARD) interactions
  between ASC and caspase-1."].
- Two nucleation-polymerization steps: sensors nucleate ASC PYD filaments; clustered ASC CARDs
  nucleate caspase-1 CARD filaments, causing proximity-induced activation
  [PMID:24630722 "Activated AIM2 and NLRP3 nucleate PYD filaments of ASC, which, in turn,
  cluster the CARD of ASC."; "ASC thus nucleates CARD filaments of caspase-1, leading to
  proximity-induced activation."].
- NLRP3 PYD filaments seed unidirectional ASC elongation
  [PMID:35559676 "ASC adaptor protein elongation on NLRP3PYD nucleation seeds is
  unidirectional, associating exclusively to the B-end of the filament."]; the active NLRP3
  disc presents a PYD filament that recruits ASC PYD
  [PMID:36442502 "The N-terminal PYDs from all NLRP3 subunits combine to form a PYD filament
  that recruits ASC PYD to elicit downstream signalling."].
- NMR: ASC PYD self-associates and binds NLRP3 PYD via equivalent surfaces
  [PMID:27432880 "We found that ASC self-associates and binds NLRP3 PYD through equivalent
  protein regions, with higher binding affinity for the latter."]. PYD self-association depends
  on charged residues on helices 2-4 [PMID:15641782 "When expressed in cells, the PYD of ASC
  was shown to form cytoplasmic filaments through self-association."].
- Pyroptosome / speck: one per cell, made of oligomerized ASC dimers, recruits and activates
  caspase-1 [PMID:17599095 "The pyroptosome is largely composed of oligomerized ASC dimers.";
  "Only one distinct pyroptosome in each stimulated cell is formed, which rapidly recruits and
  activates caspase-1 resulting in pyroptosis and the release of the intracellular
  proinflammatory cytokines."].
- Inflammasomes using ASC:
  - NLRP1 [PMID:12191486 "The inflammasome comprises caspase-1, caspase-5, Pycard/Asc, and
    NALP1"]; immunodepletion of Pycard abolishes caspase activation and proIL-1b processing
    [PMID:12191486 "proinflammatory caspase activation and proIL-1beta processing is lost upon
    prior immunodepletion of Pycard"]. In a purified NLRP1 system ASC enhances but is not
    required [PMID:17349957 "Caspase-1 activation by NALP1 does not require but is enhanced by
    adaptor protein ASC."].
  - NLRP3 [PMID:15030775 "NALP2 and NALP3 associate with ASC, the CARD-containing protein
    Cardinal, and caspase-1 (but not caspase-5), thereby forming an inflammasome with high
    proIL-1beta-processing activity."]; NLRP3-driven IL-1b secretion requires ASC
    [PMID:15020601 "Thus, cryopyrin-mediated IL-1beta secretion requires ASC in monocytic
    cells."].
  - Pyrin/MEFV [PMID:16037825 "pyrin, like cryopyrin, can also assemble an inflammasome
    complex with ASC and procaspase-1 leading to ASC oligomerization, caspase-1 activation and
    interleukin-1beta processing"; PMID:17964261].
  - AIM2 [PMID:19158675 "AIM2 as a new receptor for cytoplasmic DNA, which forms an
    inflammasome with the ligand and ASC to activate caspase-1"; PMID:19158676; PMID:19158679].
  - IFI16 (nuclear, KSHV) [PMID:21575908 "interferon gamma-inducible protein 16 (IFI16)
    interacts with the adaptor molecule ASC and procaspase-1 to form a functional
    inflammasome"].
  - NLRP6 [PMID:30674671 "NLRP6 PYD alone is able to self-assemble into filamentous structures
    ... and can recruit the ASC adaptor using PYD-PYD interactions"; PMID:34678144
    "Recruitment of ASC via helical assembly solidifies NLRP6 condensates, and ASC further
    recruits and activates caspase-1."].
  - NLRC4: NAIP-NLRC4 can activate caspase-1 directly via its own CARD; ASC is dispensable for
    pyroptosis there but contributes to cytokine processing [PMID:25879286 "Central to the
    inflammasome is a pattern recognition receptor that activates caspase-1 either directly or
    through an adapter protein."]. NLRC4 and NLRP3 co-occupy one ASC ring in
    Salmonella-infected macrophages [PMID:24803432].
- Nuclear-to-cytosol relocation is required for inflammasome function
  [PMID:19234215 "ASC localized primarily to the nucleus in resting human
  monocytes/macrophages"; "cytosolic localization of ASC is essential for inflammasome
  function"]. PML retains ASC in the nucleus [PMID:24407287].
- Regulation: K63 ubiquitination at K174 by TRAF3 downstream of MAVS needed for specks
  [PMID:25847972]; Syk phosphorylation at Y146/Y187 [PMID:25605870]; PYD-only proteins
  POP1/POP2/POP3 compete for ASC [PMID:12656673; PMID:17178784; PMID:24531343].
- Released ASC specks act extracellularly to propagate inflammation
  [PMID:24952504 "We found oligomeric ASC particles in the serum of patients with active CAPS
  but not in that of patients with other inherited autoinflammatory diseases."].
- Noncanonical: ASC is recruited with MALT1-caspase-8 into the dectin-1/CARD9 scaffold for
  caspase-8-mediated pro-IL-1b processing [PMID:22267217].

## Downstream outputs

- IL-1b/IL-18 maturation and pyroptosis via caspase-1 and gasdermin D [PMID:29196474;
  PMID:26611636 noting "ASC is not essential for GSDMD to function" but "The induction of
  apoptosis required NLRP3 or other inflammasome receptors and ASC"].

## Inflammasome-independent and apoptotic roles (secondary, context-dependent)

- Apoptosis: originally pro-apoptotic; caspase-8-dependent apoptosis [PMID:12646168],
  caspase-9 [PMID:11103777], Bid-dependent in type II cells [PMID:16964285], Bax adaptor in
  p53 pathway [PMID:14730312 "ASC is required to translocate Bax to the mitochondria"], though
  ASC-Bax colocalization was not reproduced [PMID:16964285 "we failed to observe colocalization
  of ASC and Bax in cells"]. TMS1 is silenced by methylation in breast cancers [PMID:11103777]. These apoptotic activities are mostly from overexpression systems.
- NF-kB modulation: dual/context-dependent — can activate [PMID:11786556] or inhibit at the
  IKK level [PMID:12486103 "ASC modulates diverse NF-kappaB induction pathways by acting upon
  the IKK complex"]. Direction is inconsistent across studies.
- Cytokine/chemokine induction via MAPK: ASC suppresses DUSP10/MKP5, raising ERK/JNK
  phosphorylation and chemokine output independently of caspase-1/IL-1b
  [PMID:21487011 "ASC...affected its phosphorylation by pathogens...via suppression of the
  dual-specificity phosphatase, DUSP10/MKP5."]. P. gingivalis cytokine induction (IL-6, IL-8,
  IL-10, TNF) needs ASC [PMID:16982856].

## IMPORTANT confound for the adaptive-immunity / Dock2 / actin / T-cell / DC annotations

The dendritic-cell maturation, T-cell activation/migration, phagocytosis, macropinocytosis,
and actin-polymerization annotations trace to work on ASC-deficient mice reporting a
cell-intrinsic, inflammasome-independent role of ASC in controlling Dock2 mRNA stability and
Rac-mediated actin polymerization [PMID:21892172 "ASC shapes adaptive immunity independently
of inflammasomes by modulating Dock2-dependent Rac activation and actin polymerization in DCs
and lymphocytes."; "ASC-deficient mice showed defective antigen presentation by dendritic
cells (DCs) and lymphocyte migration due to impaired actin polymerization mediated by the
small GTPase Rac."]. The SAME authors subsequently published an Addendum reporting this is a
**passenger mutation artifact**: the Dock2 defect is present in only a subset of ASC-deficient
mouse lines, i.e. a flanking/strain confound rather than a function of ASC
[PMID:22905357 "Addendum: defective Dock2 expression in a subset of ASC-deficient mouse
lines."]. Consequently the Dock2/Rac/actin/DC/T-cell cascade of GO annotations is not safe to
treat as a direct ASC function. Annotations derived from PMID:22732093 (the human DC paper
using RNAi, not the Dock2 mouse) are on firmer ground but still describe a secondary,
non-core role. These are handled as KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / UNDECIDED, not
as core functions, and not REMOVE (experimental annotations whose full text was not fully
read).

## Subcellular localization

- Core: cytosol/cytoplasm (resting), relocating to a single perinuclear speck/inflammasome on
  activation [PMID:11103777; PMID:12191486; PMID:15030775]. Nucleus is a genuine resting
  location in monocytes [PMID:19234215]. ER/mitochondria redistribution on NLRP3 activation
  [PMID:21124315]. Golgi membrane only under HRSV infection [PMID:23229815 "Upon HRSV
  infection, the protein is mainly located in lipid rafts in the Golgi membrane."].
- Extracellular region / granule-lumen annotations are Reactome neutrophil-degranulation
  pathway memberships, not a primary ASC location (secondary).

## Consistency with NLRP3 review

Keep terminology consistent with genes/human/NLRP3: NLRP3 is the **sensor/activator** that
nucleates; ASC is the **adaptor** that polymerizes and recruits caspase-1. Core MF for ASC =
signaling adaptor activity (GO:0035591); NLRP3 also carries signaling adaptor activity for its
own nucleation step but ASC is the canonical adaptor. ASC also carries
cysteine-type endopeptidase activator activity (GO:0140608) because its CARD filament directly
drives procaspase-1 proximity-induced autoactivation. Avoid "protein binding".
