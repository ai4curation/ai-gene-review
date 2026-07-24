# FANCL (Q9NW38) review notes

Human Fanconi anemia complementation group L. HGNC:20748. Synonym PHF9. 375 aa.

## Core biology (synthesis)

FANCL is the catalytic RING-type E3 ubiquitin ligase subunit of the multiprotein
Fanconi anemia (FA) core complex. Working with the dedicated E2 conjugating enzyme
UBE2T, FANCL monoubiquitinates FANCD2 (on Lys561) and FANCI (on Lys523), the key
activating step of the FA/interstrand-crosslink (ICL) repair pathway. The
monoubiquitinated FANCD2–FANCI (ID2) complex is recruited to chromatin at stalled
replication forks / ICLs and coordinates nucleolytic incision, translesion synthesis
and homologous recombination.

Domain architecture (UniProt Q9NW38): N-terminal E2-like/ELF (UBC-like) domain,
central "DRWD"/RWD-like domain, and a C-terminal RING-type zinc finger (residues
307–363, degenerate, binds 2 Zn). The UBC-RWD region (URD, ~104–294) mediates
interaction with FANCI and FANCD2; the RING binds the E2 (UBE2T). Cys307 is essential
for ligase activity (C307A abolishes activity). Trp341 is required for UBE2T binding.

Note the UniProt CAUTION: originally reported as a PHD-type zinc finger (PubMed:12724401)
but it is actually a RING-type zinc finger; PHD fingers have no ubiquitin ligase activity.

## Key evidence / provenance

- E3 ubiquitin ligase activity; essential for FANCD2 monoubiquitination:
  [PMID:12973351 "Here we report a new component of a Fanconi anemia protein complex, called PHF9, which possesses E3 ubiquitin ligase activity in vitro and is essential for FANCD2 monoubiquitination in vivo"]. Also defines involvement in FA (disease), catalytic activity, and C307/C310 mutagenesis abolishing activity.

- UBE2T is the cognate E2 that binds FANCL (E2/E3 pair):
  [PMID:16916645 "UBE2T binds to FANCL, the ubiquitin ligase subunit of the Fanconi anemia core complex, and is required for the monoubiquitination of FANCD2 in vivo"]. W341G abolishes UBE2T binding and ligase activity.

- E3 activity determined by chromatin localization, forms active E2/E3 holoenzyme on chromatin:
  [PMID:17938197 "the actual E3 ligase activity is not determined by the assembly of the FA core complex but rather by its DNA damage-induced localization to chromatin"];
  [PMID:17938197 "FANCD2 monoubiquitination is therefore not regulated by multiprotein complex assembly but by the formation of an active E2/E3 holoenzyme on chromatin"].

- Minimal reconstitution: Ube2t + FANCL monoubiquitinate FANCD2, stimulated by RWD-like domain; FANCI restricts site-specificity:
  [PMID:19111657 "we minimally reconstitute this monoubiquitination reaction with Ube2t and the FANCL protein, revealing that monoubiquitination is stimulated by a conserved RWD-like domain in FANCL"];
  [PMID:19111657 "addition of the FANCI protein enhances monoubiquitination and also restricts it to the in vivo substrate lysine residue on FANCD2"].

- FANCL also monoubiquitinates FANCI (Lys523):
  [PMID:19589784 "We also demonstrate that FANCI can be ubiquitinated on Lys-523 by the UBE2T-FANCL pair in vitro"].

- Structure of FANCL RING–Ube2T; specific E3–E2 selection:
  [PMID:24389026 "Using the Fanconi Anemia pathway exclusive E3-E2 pair, FANCL-Ube2T, we report the atomic structure of the FANCL RING-Ube2T complex"];
  [PMID:24389026 "these specific interactions are required for selection of Ube2T over other E2s by FANCL"].

- FA nuclear core complex membership / chromatin:
  [PMID:22343915 "Fanconi anemia (FA) nuclear core complex is a multiprotein complex required for the functional integrity of the FA-BRCA pathway regulating DNA repair"].
  [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex, promotes FANCD2 monoubiquitination in response to DNA damage"].
  UniProt SUBUNIT: FA complex composed of FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9 and FANCM.

- ICL repair pathway (downstream of FANCD2/FANCI monoubiquitination):
  [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase"].

## Curation decisions

- MF `ubiquitin protein ligase activity` (GO:0061630): core, ACCEPT (IBA/IEA/EXP/IDA).
- MF `ubiquitin-protein transferase activity` (GO:0004842): parent of 0061630; correct but more
  general; ACCEPT (IEA/IDA/ISS).
- BP `protein monoubiquitination` (GO:0006513): core, ACCEPT.
- BP `interstrand cross-link repair` (GO:0036297): core pathway, ACCEPT.
- CC `Fanconi anaemia nuclear complex` (GO:0043240): core location/complex, ACCEPT.
- CC `chromatin` (GO:0000785): site of active E3 holoenzyme, ACCEPT.
- CC nucleus/nucleoplasm/cytosol/cytoplasm: ACCEPT nucleus/nucleoplasm; cytoplasm/cytosol
  KEEP_AS_NON_CORE (FANCL acts in nucleus/chromatin; cytoplasmic pool by similarity/ISS).
- MF `protein binding` (GO:0005515): uninformative; MARK_AS_OVER_ANNOTATED. Most are
  high-throughput Y2H (HuRI PMID:25416956/32296183; neo-PPI PMID:35512704). The
  functionally meaningful one (PMID:24389026, partner UBE2T Q9NPD8) is better captured by
  the E2-binding term.
- MF `ubiquitin protein ligase binding` (GO:0031625, IPI with UBE2T/UBE2W which are E2s):
  the partners UBE2T (Q9NPD8) and UBE2W (Q96B02) are E2 conjugating enzymes, not E3 ligases;
  MODIFY to GO:0031624 `ubiquitin conjugating enzyme binding` (verified QuickGO/AmiGO:
  "Binding to a ubiquitin conjugating enzyme, any of the E2 proteins").
- BP `DNA repair` (GO:0006281), `DNA damage response` (GO:0006974), `protein ubiquitination`
  (GO:0016567): correct general terms, ACCEPT.
- MF `ubiquitin binding` (GO:0043130): NEW (not in GOA). ELF (E2-like fold) domain binds
  free ubiquitin non-covalently via the Ile44 patch; dispensable in vitro but required for
  efficient DNA-damage-induced FANCD2 monoubiquitination in vivo. Regulatory/non-core.
  [PMID:26149689 "the ELF domain of FANCL is required to mediate a non-covalent interaction
  between FANCL and ubiquitin"]; [PMID:26149689 "the ELF domain is required to promote
  efficient DNA damage-induced FANCD2 monoubiquitination in vertebrate cells, suggesting an
  important function of ubiquitin binding by FANCL in vivo"]. Verified GO:0043130 is a
  molecular_function via QuickGO (not obsolete). Added during Affinage reconciliation.

## Affinage reconciliation (2026-07)

Affinage record (run 2026-06-09, 22 discoveries, self-eval win) is a PMID-dense narrative
fully consistent with AIGR on the core biology. Its `mechanism_profile` GO layer is coarse
(GO:0016874 ligase activity, GO:0140096 catalytic activity acting on protein, GO:0031386
protein tag activity; nucleus/nuclear chromosome/mitochondrion) — do not import directly;
AIGR's GO:0061630 + GO:0031624 + specific locations are more precise. Incorporated
PMID:26149689 (ELF ubiquitin binding, above) as the one genuine MF the review lacked.
Affinage's moonlighting claims — K11-linked β-catenin/Wnt (PMID:22653977), ligase-independent
Parkin mitophagy (PMID:35644338), germ-cell/reproduction phenotypes (PMID:12417526,
PMID:20661450) — are single-study and/or non-human organism/tissue phenotypes; AIGR correctly
scopes them out of the human GO core-function set. Not added as annotations.
