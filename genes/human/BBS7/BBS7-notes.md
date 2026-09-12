# BBS7 (Q8IWZ6) Gene Review Notes

## Overview
BBS7 is a core subunit of the **BBSome** (GO:0034464), an octameric, coat/adaptor-like
complex (BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP10/BBIP1) that traffics
membrane signaling-receptor cargo into and out of the primary cilium in coordination with
the small GTPase ARL6/BBS3 and intraflagellar transport (IFT). Loss of function causes
Bardet-Biedl syndrome 7 (BBS7; MIM:615984), a ciliopathy with retinal degeneration,
obesity, polydactyly, renal malformation, hypogenitalism, and intellectual disability.

## Domain architecture / structural role
- BBS7 contains a β-propeller, GAE (gamma-adaptin ear) domain, platform (pf) domain, and
  a hairpin — features shared with BBS2 and BBS9; together BBS2/BBS7/BBS9 form the
  β-propeller/GAE/platform scaffold "core" of the BBSome.
  [UniProt Q8IWZ6 InterPro: IPR056332 Beta-prop_BBS7, IPR056334 BBS7_GAE_dom, IPR056333
  BBS7_pf_dom, IPR056335 BBS7_hairpin]
- "BBS1, BBS2, BBS7, and BBS9 contain β propeller domains; BBS4 and BBS8 contain multiple
  tetratricopeptide repeat domains; and BBS5 contains two pleckstrin homology domains."
  [PMID:22500027 full text]

## Core functional findings
- The BBSome is "a complex composed of seven highly conserved BBS proteins ... localizes
  to nonmembranous centriolar satellites in the cytoplasm but also to the membrane of the
  cilium ... required for ciliogenesis but ... dispensable for centriolar satellite
  function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange
  factor." [PMID:17574030 "BBSome ... required for ciliogenesis"] — establishes BBSome
  membership (IDA), ciliary membrane localization, and ciliary membrane biogenesis role.
- BBSome mediates protein trafficking to the ciliary membrane; all BBSome subunits + ARL6
  required for BBSome ciliary entry; BBSome (with LZTFL1) regulates ciliary trafficking of
  Smoothened/SHH signaling. BBS7 specifically interacts with SMO. [PMID:22072986
  "BBS proteins and LZTFL1 regulate ciliary trafficking of ... Smoothened"; UniProt SUBUNIT
  "Interacts with SMO"]

## Assembly / chaperonin client
- "BBS7 interacts with BBS2 and becomes part of a BBS7-BBS2-BBS9 assembly intermediate
  referred to as the BBSome core complex because it forms the core of the BBSome. BBS1,
  BBS5, BBS8, and finally BBS4 are added to the BBSome core to form the complete BBSome."
  [PMID:22500027 full text]
- "BBS6, BBS12, and BBS7 interact with CCT/TRiC proteins to form a complex ... the
  BBS-chaperonin complex ... facilitates BBSome assembly ... the BBS-chaperonin complex
  plays a role in BBS7 stability." [PMID:22500027] — BBS7 is a CCT/chaperonin client; IntAct
  records BBS7–CCT2/CCT (P78371) and BBS7–BBS10/BBS12 interactions (PMID:20080638, 22500027).
- PMID:20080638 "BBS6, BBS10, and BBS12 form a complex with CCT/TRiC family chaperonins and
  mediate BBSome assembly" — BBSome membership IDA and BBS7–BBS2/BBS10/BBS12 interactions.

## Localization
- Cilium membrane and cytoplasm; centriolar satellite / centrosome / basal body.
  [UniProt SUBCELLULAR LOCATION; PMID:22072986 EXP cytoplasm; PMID:21399614 IDA centrosome]
- HPA: tissue-enhanced in retina (consistent with retinal degeneration phenotype).

## Non-canonical / candidate over-annotations
- **Transcription / proteasome (PMID:22302990):** Gascue et al. report BBS7 has a confirmed
  nuclear export signal, "interacts physically with the polycomb group (PcG) member RNF2 and
  regulate its protein levels, probably through a proteasome-mediated mechanism", and loss of
  BBS proteins leads to aberrant expression of RNF2 targets in vivo. This is a real,
  experimentally supported but non-canonical secondary activity. The WITH gene UniProtKB:Q99496
  = RNF2/RING1B (a TF/PcG protein). The MF annotation GO:0061629 (RNA Pol II-specific
  DNA-binding transcription factor binding) is supported by the BBS7–RNF2 IPI. The two BP
  annotations (GO:0006357 regulation of transcription by Pol II; GO:0032436 positive regulation
  of proteasomal ubiquitin-dependent protein catabolic process) are downstream/process-level
  effects, plausible but non-core for a structural BBSome subunit -> KEEP_AS_NON_CORE.
  full_text_available: false (abstract only in cache) — do not REMOVE experimental annotations.

- **ISS BHF-UCL block from mouse/zebrafish orthologs (GO_REF:0000024):** heart looping
  (GO:0001947), determination of left/right symmetry (GO:0007368), melanosome transport
  (GO:0032402), pigment granule aggregation in cell center (GO:0051877), fat cell
  differentiation (GO:0045444), digestive tract morphogenesis (GO:0048546). These are
  pleiotropic, organism/process-level developmental phenotypes of BBSome/cilium dysfunction
  transferred by similarity to ortholog Q08C18 (zebrafish bbs7) / Q8K2G4 (mouse). They are
  downstream consequences of the core ciliary trafficking defect, not molecular activities of
  BBS7 -> KEEP_AS_NON_CORE (pleiotropic developmental roles), except melanosome transport /
  pigment granule aggregation which reflect zebrafish melanosome assays (BBSome role in
  intracellular transport) - keep as non-core.

## protein binding (GO:0005515, IPI)
~20 IntAct/curated IPI rows to BBSome subunits (BBS1/2/9/10/12), CCT2, ALDOB, SMO-pathway,
NPHP5/IQCB1, CEP131/AZI1, JUN, CCDC28B, RNF2, and high-throughput interactome screens
(PMID:27173435, 28514442, 33961781, 40205054). Per curation guidelines, GO:0005515 is
uninformative; mark over-annotated. The biologically meaningful interactions (BBS2, CCT,
SMO, RNF2) are captured by the BBSome part_of and specific MF/process annotations.

## Reference verifications
- PMID:17574030 Nachury 2007 Cell — BBSome definition, Rab8, ciliary membrane biogenesis. VERIFIED.
- PMID:22072986 Seo 2011 PLoS Genet — LZTFL1/BBSome/SMO trafficking. VERIFIED (full text).
- PMID:22500027 Zhang 2012 JBC — BBSome sequential assembly, BBS7-BBS2-BBS9 core, chaperonin. VERIFIED (full text).
- PMID:20080638 Seo 2010 PNAS — BBS6/10/12+CCT mediate BBSome assembly. VERIFIED.
- PMID:22302990 Gascue 2012 JCS — BBS7 nuclear role, RNF2 interaction, transcription. VERIFIED (abstract).
- PMID:19081074 Loktev 2008 Dev Cell — BBIP10 discovery; BBSome context. VERIFIED.
- PMID:24550735 Chamling 2014 PLoS Genet — AZI1/CEP131 regulates BBSome trafficking. VERIFIED.
