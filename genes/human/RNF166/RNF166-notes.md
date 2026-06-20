# RNF166 (RING finger protein 166) review notes

UniProt: Q96A37 (RN166_HUMAN), 237 aa. EC 2.3.2.27. RING-type E3 ubiquitin ligase.
Member of a subfamily of small C3HC4 RING ligases together with RNF114, RNF125, RNF138
[PMID:26456228 "RNF125 and its homologous proteins RNF114, RNF138, and RNF166 form a
subfamily of small C3HC4 RING ubiquitin ligases"].

## Domain architecture
- RING-type zinc finger 33..73 (catalytic; recruits ubiquitin-charged E2) [UniProt FT].
- C2HC RNF-type zinc finger 98..117 (mediates substrate/target interaction) [UniProt FT;
  PMID:26456228 "RNF166 interacts with TRAF3 and TRAF6 via its zinc finger domain"].
- C-terminal UIM (ubiquitin-interacting motif) ~221..237 [UniProt FT].
- Catalytic Cys33/Cys36 are essential: C33A/C36A is ligase-dead.
  [UniProt MUTAGEN 33/36; PMID:27880896 "a ligase-dead RNF166 mutant (RNF166 C33A, C36A)
  was unable to drive p62 ubiquitination"]

## Core molecular function
- RING-type E3 ubiquitin-protein ligase / ubiquitin-protein transferase (EC 2.3.2.27).
  Demonstrated in vitro with UBA1 (E1), UBE2D2 (E2), HA-ubiquitin, GST-RNF166, SUMO-p62.
  [PMID:27880896 "we used an in vitro ubiquitination assay with recombinant UBA1 (E1),
  E2 enzymes, HA-ubiquitin, GST-RNF166, and SUMO-p62...ubiquitination of p62 was observed
  only in the presence of all defined proteins and the E2 enzyme UBE2D2"]
- Zinc ion binding (RING + C2HC Zn fingers) [UniProt KW Zinc-finger; BINDING residues].

## Substrates / processes
- SQSTM1/p62 — RNF166 directly catalyzes K29- and K33-linked polyubiquitination of p62 at
  K91 and K189. This is an ATYPICAL (non-degradative) ubiquitination that promotes xenophagy
  (antibacterial selective autophagy) of cytosol-adapted bacteria (Listeria, Shigella).
  [PMID:27880896 "RNF166 catalyzes K29- and K33-linked polyubiquitination of p62 at residues
  K91 and K189"; "RNF166 limits intracellular replication of Shigella and...the E3 ligase
  activity of RNF166 is important for this function"]
  - RNF166 is required for early recruitment of autophagy adaptors p62 and NDP52, and of
    ubiquitin and LC3, to bacteria; localizes to bacteria with p62.
    [PMID:27880896 "controls the recruitment of ubiquitin as well as the autophagy adaptors
    p62 and NDP52 to bacteria"]
  - NOTE: K29/K33-linked polyubiquitination of p62 here is NOT proteasome-targeting; the
    IBA "ubiquitin-dependent protein catabolic process" / "proteasome" framing from
    GO_Central is the family-level default and only partially fits RNF166's verified biology
    (xenophagy/autophagy, not proteasomal degradation of p62).
- TRAF3 and TRAF6 — RNF166 enhances RNA virus (SeV/EMCV)-induced K63-linked ubiquitination
  of TRAF3 and TRAF6, potentiating VISA(MAVS)-mediated IFN-beta production (innate antiviral
  immunity). RNF166 binds TRAF3/TRAF6 via its zinc finger; RING domain required for the
  positive effect. RNF166 acts downstream of VISA, upstream of TBK1.
  [PMID:26456228 "RNF166...potentiates RNA virus-triggered IFN-beta production by enhancing
  the ubiquitination of TRAF3 and TRAF6"; "K63-linked rather than K48-linked ubiquitination
  of TRAF3 and TRAF6 was decreased...when RNF166 was knocked down"]

## Subcellular location
- Cytoplasm; forms cytosolic dots/aggregates; relocalizes to intracellular bacteria.
  [UniProt SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:26456228}; PMID:26456228
  "Overexpressed RNF166 localized predominantly in the cytosol as dots"]

## Interactors (UniProt IntAct)
- PRKN, TARDBP, UBE2D4, UBE2K, XAF1. UBE2D4/UBE2K are E2 enzymes (consistent with RING E3).

## Annotation-call reasoning
- ubiquitin protein ligase activity (GO:0061630) — ACCEPT core MF (EXP/IDA in vitro,
  ligase-dead mutant; IBA also). genuine RING E3.
- ubiquitin-protein transferase activity (GO:0004842) IEA EC mapping — ACCEPT (synonymous
  catalytic MF; EC 2.3.2.27 experimentally established by PMID:27880896).
- protein polyubiquitination (GO:0000209) IBA — ACCEPT core BP (K29/K33 chains on p62; K63
  on TRAF3/6).
- ubiquitin-dependent protein catabolic process (GO:0006511) IBA — MARK_AS_OVER_ANNOTATED:
  RNF166's verified ubiquitination of p62 (K29/K33) and TRAF3/6 (K63) is non-degradative
  (signaling/autophagy), so a generic catabolic/proteasomal framing is a family-level
  over-propagation not supported by the gene-specific evidence. Defer/keep cautious.
- protein ubiquitination (GO:0016567) IEA UniPathway — KEEP_AS_NON_CORE (generic parent of
  the specific polyubiquitination).
- zinc ion binding (GO:0008270) IEA — ACCEPT (RING + C2HC Zn fingers; structurally required).
- cytoplasm (GO:0005737) IEA + EXP — ACCEPT (active compartment; EXP from PMID:26456228).
- protein binding (GO:0005515) bare IPI — KEEP_AS_NON_CORE per curation guidelines.
- Missing but supportable (not in GOA): autophagy / xenophagy, innate immune response,
  defense response to bacterium, positive regulation of type I IFN production.
