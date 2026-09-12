# TANK (TRAF family member-associated NF-kB activator; I-TRAF) — review notes

UniProt: Q92844 (TANK_HUMAN), 425 aa, HGNC:11562. Synonyms: ITRAF, I-TRAF.

## Summary of function

TANK is a cytoplasmic adaptor/scaffold protein with no catalytic activity. It was
originally cloned as a TRAF-interacting protein ("I-TRAF") that binds the TRAF-C
domains of TRAF1, TRAF2 and TRAF3 and was proposed to keep TRAFs in a latent state
[PMID:8710854 "I-TRAF is a novel TRAF-interacting protein that regulates TRAF-mediated signal transduction"].
Its best-established role is as one of three mutually exclusive adaptors (with SINTBAD/TBKBP1
and NAP1/AZI2) that bridge the IKK-related kinases TBK1 and IKBKE (IKKε) into signaling
complexes that drive IRF3/IRF7 phosphorylation and type I interferon induction during
antiviral innate immunity [PMID:21931631 "TANK, Sintbad ... and NAP1 ... whose functional relationship to TBK1 and IKK-i is poorly understood ... TBK1 activation was strictly dependent on the integrity of the TBK1/TANK interaction"].

The adaptors bind the same C-terminal coiled-coil 2 of TBK1 and compete for it; TANK
resides in a distinct subcellular pool from SINTBAD/NAP1 [PMID:21931631 "the individual adaptors reside in different subcellular locations ... TANK, Sintbad and NAP1 competed for binding of TBK1"].

TANK also has a separable negative-regulatory function. In response to genotoxic stress
(DNA damage) or IL-1β/LPS, TANK acts as a scaffold assembling a deubiquitination complex
with ZC3H12A (MCPIP1) and the deubiquitinase USP10, facilitating USP10-dependent
deubiquitination of TRAF6 (and IKBKG/NEMO), thereby restraining NF-kB activation
[PMID:25861989 "TANK formed a complex with MCPIP1 ... and a deubiquitinase, USP10, which was essential for the USP10-dependent deubiquitination of TRAF6 ... CRISPR/Cas9-mediated deletion of TANK ... significantly enhanced NF-kB activation by genotoxic treatment"].
TANK itself lacks a DUB domain — its GO annotations to "cysteine-type deubiquitinase
activity" (contributes_to) and "deubiquitinase activator activity" reflect this scaffolding
role, not intrinsic enzymatic activity.

Phosphorylation by IKBKE disrupts the TANK–TRAF2 interaction [UniProt SUBUNIT; PMID:10759890],
giving a phospho-switch on its TRAF-binding adaptor function.

## Domains / structure
- N-terminal coiled-coil (aa 22–62); region 1–31 needed for ZC3H12A interaction.
- TBD (TBK1-binding domain) region ~133–172 binds TBK1 and IKBKE.
- TRAF family interaction region ~172–191 (crystal structure 1L0A/1KZZ of TANK 174–194
  bound to TRAF3; binds the CD40 recognition site on TRAF3) [PMID:12005438 "Downstream regulator TANK binds to the CD40 recognition site on TRAF3"].
- C-terminal UBZ1-type zinc finger (aa 393–420) — basis of the IEA "zinc ion binding"
  keyword annotation.

## Localization
- UniProt: Cytoplasm. Experimental IDA "is_active_in cytoplasm" [PMID:21931631].
- HPA IDA: cytosol (GO:0005829) and nucleolus (GO:0005730). The nucleolus annotation
  is from a single high-throughput immunofluorescence dataset (GO_REF:0000052); there is
  no functional literature placing TANK function in the nucleolus, so it is non-core.

## Host–virus interactions (context, not core GO BP for the gene's normal function)
- Vaccinia C6 binds TANK and other TBK1 adaptors to inhibit IRF3/IRF7 [PMID:21931555].
- EMCV 3C and Seneca Valley virus 3C proteases cleave TANK to disrupt the
  TANK-TBK1-IKKε-IRF3 complex and suppress type I IFN [UniProt PTM; PMID:26363073, PMID:28566380].
  These confirm TANK's role in the antiviral IFN axis.

## Annotation assessment highlights
- Core MF: molecular adaptor activity (GO:0060090, IDA, PMID:21931631) — ACCEPT as core.
- Core BP: positive regulation of type I interferon production (GO:0032481, IDA) — ACCEPT as core.
- ubiquitin protein ligase binding (GO:0031625, IPI, PMID:11279055) — real TRAF-binding,
  informative MF; KEEP_AS_NON_CORE (more specific than bare protein binding but secondary).
- The deubiquitination-complex BP/MF terms (GO:0035800, GO:0004843 contributes_to,
  GO:1903003, GO:2000158, GO:0043124, GO:0006974, GO:0071347, GO:0071356, GO:0071479)
  are all from the single IMP study PMID:25861989 and describe the genotoxic
  NF-kB-restraining scaffold role — accept as a real but secondary (non-core) function set.
- The ~30 bare "protein binding" (GO:0005515) IPI entries are individually uninformative
  per curation guidelines (KEEP_AS_NON_CORE); the functionally meaningful partners
  (TBK1, IKBKE, TRAF1/2/3, IKBKG/NEMO, USP10, ZC3H12A) are captured by the adaptor/IFN core.
- ~30 Reactome TAS "cytosol" (GO:0005829) entries are pathway-step localizations; correct
  compartment but redundant — KEEP_AS_NON_CORE.
- GO:1902554 serine/threonine protein kinase complex (NAS, ComplexPortal, the
  TBK1-IKKε-TANK complex CPX-6089) — ACCEPT/KEEP_AS_NON_CORE as a real complex membership
  (TANK is the non-catalytic adaptor subunit of the kinase complex).
- IEA GO:0043124 (neg reg canonical NF-kB) from InterPro is corroborated by the experimental
  IMP of the same term — KEEP_AS_NON_CORE.
- GO:0051607 (defense response to virus) and GO:0060337 (type I interferon-mediated
  signaling pathway), both NAS ComplexPortal from PMID:21931631 — consistent with the
  antiviral IFN role; KEEP_AS_NON_CORE (process-level).
