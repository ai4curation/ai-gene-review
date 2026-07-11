# bbs-9 (C. elegans) — research notes

UniProt: O01514 (PTHB1_CAEEL). Gene: bbs-9 / C48B6.8 / WBGene00016744.
Human ortholog: BBS9 / PTHB1 (Q3SYG4). 744 aa. Reference proteome UP000001940.

## Summary of what is KNOWN

BBS-9 is a core subunit of the BBSome, the octameric ciliary coat complex (BBS-1, BBS-2,
BBS-4, BBS-5, OSM-12/BBS-7, BBS-8/TTC-8, BBS-9). In C. elegans it is expressed in ciliated
sensory neurons and is required for BBSome assembly, IFT integrity, ciliogenesis, and
cilium-dependent sensory behaviors.

### 1. BBSome membership (core CC)
- UniProt SUBUNIT: "Part of BBSome complex, that contains bbs-1, bbs-2, bbs-4, bbs-5,
  osm-12, bbs-8/ttc-8 and bbs-9 (By similarity). Interacts with bbs-1 (PubMed:22922713)."
  [file:worm/bbs-9/bbs-9-uniprot.txt]
- ComplexPortal: CPX-428 BBSome complex; TCDB 3.A.33.1.2 "the bbsome complex (bbsome) family".
- Direct experimental support for worm BBS-9 in the complex: BiFC (bimolecular fluorescence
  complementation) demonstrates BBS-1–BBS-9 pair coexistence in the same complex, and this is
  consistent with the human BBSome architecture where BBS1, 7, and 9 are close.
  [PMID:22922713 "In wild-type animals, fluorescence complementation can be observed in
  BBS-1–BBS-7 and BBS-1–BBS-9 pair, indicative of the coexistence of these three BBS proteins
  in the same complex"]
  [PMID:22922713 "This finding is also consistent with the prediction that mammalian BBS1, 7,
  and 9 locate closely to each other in the BBSome"]
- In humans, BBS2/7/9 form the "core" of the BBSome that assembles first. (background; see human
  BBSome assembly literature — not in worm cache, so cited only as background)

### 2. BBSome / IFT assembly and turnaround (core BP: intraciliary transport)
- The Wei et al. 2012 study (worm forward genetics) established that the BBSome assembles IFT
  particles at the ciliary base, binds the anterograde IFT particle, and reaches the ciliary
  tip to regulate IFT turnaround/recycling.
  [PMID:22922713 "we proposed that the in vivo function for the BBSome is to regulate the
  assembly of the IFT particles at the ciliary base"]
  [PMID:22922713 "After IFT particles are assembled at the ciliary base, the BBSome binds to
  the IFT particle like a cargo but not a structural component"]
- bbs-9 loss-of-function allele: bbs-9(jhu555) carries a nonsense mutation at Q171; in this
  mutant IFT-A and IFT-B separate and move at different rates in anterograde IFT — the
  canonical bbs-null IFT phenotype (BBSome couples IFT-A and IFT-B).
  [PMID:22922713 "jhu555, jhu590, and jhu598 were mapped to bbs-9, bbs-7, and bbs-1,
  respectively"]
  [PMID:22922713 "IFT-A and IFT-B separate and move at different rates in anterograde IFT in
  bbs-7(jhu590) (encodes BBS-7 with a nonsense mutation at Q546 site) and bbs-9(jhu555)
  (encodes BBS-9 with a nonsense mutation at Q171 site) mutants just like in other reported
  bbs null mutants"]
- BBS-9 protein itself undergoes IFT: when the BBSome is uncoupled from moving IFT
  (dyf-2(jhu616)), all BBS proteins including BBS-9 lose IFT movement and accumulate at the
  ciliary base; BBS-9 shows only "very dim ciliary staining".
  [PMID:22922713 "Some of them (BBS-1, BBS-4) totally lost the ciliary localization; the
  others (BBS-2, -5, -7, -8, -9) only showed very dim ciliary staining when compared to
  wild-type animals"]
  [PMID:22922713 "all BBS proteins completely lost IFT movement, indicating the complete
  dissociation between the BBSome and the moving IFT particles"]
- DYF-2 (IFT/WDR19) locates near BBS-9 in native IFT particles.
  [PMID:22922713 "Results from BiFC analyses suggest that DYF-2 locates near BBS-1, BBS-7 and
  BBS-9 in the native IFT particles"]

### 3. UniProt FUNCTION line (bbs-9 specific)
- "Required for proper BBSome complex assembly and its ciliary localization (PubMed:22922713).
  Required for cilia biogenesis and both the assembly and movement of intraflagellar transport
  proteins along the ciliary axoneme (PubMed:22022287, PubMed:22922713)."
  [file:worm/bbs-9/bbs-9-uniprot.txt]
- DISRUPTION PHENOTYPE: reduced body length/width, delayed larval development, decreased
  roaming (PMID:22022287); defective cilia structure with IFT protein accumulation/
  mislocalization and impaired IFT movement, disrupted BBSome assembly at the cilia base
  (PMID:22922713); defective NO/P. aeruginosa avoidance (PMID:30014846).

### 4. Sensory behavior / physiology (non-core, downstream of cilia)
- bbs-9(gk471) null is a cilia-defective mutant that fails NO and P. aeruginosa (PA14)
  avoidance — used as a positive control for cilia dependence of NO sensing, not a bbs-9
  specific molecular function.
  [PMID:30014846 "Two cilia defective mutants, osm-12(n1606) null mutants and bbs-9(gk471)
  null mutants, were both defective in avoiding the lawn of PA14 and the NO donor"]
- Mok et al. 2011 (PMID:22022287): bbs mutants show small body size, developmental delay and
  exploration defects, suppressed by loss of guanylate cyclases GCY-35/GCY-36 (cGMP signalling
  modifiers). The paper studies bbs mutants collectively (e.g. bbs-7, bbs-8) and does NOT name
  bbs-9 by symbol in the cached full text; UniProt cites it for bbs-9 FUNCTION/DISRUPTION, so
  the specific bbs-9 data are likely in supplementary strain tables not extracted here. Treat
  the developmental/cGMP-modifier findings as BBSome-general (non-core for bbs-9), and do not
  quote bbs-9-specific claims from this paper.

## Domain architecture (bioinformatics from UniProt)
- InterPro: IPR028073 PHTB1_N_dom; IPR026511 PTHB1; IPR055363 PTHB1_hp_dom; IPR055362
  PTHB1_pf_dom; IPR036322 WD40_repeat_dom_sf. Pfam PF14727 (PHTB1_N), PF23338 (PTHB1_hp),
  PF23337 (PTHB1_pf). SUPFAM SSF50978 WD40 repeat-like.
- So BBS-9 has an N-terminal β-propeller (WD40-like) plus platform/α-helical/hairpin domains —
  the canonical PTHB1 architecture shared with other BBSome β-propeller subunits (BBS1, BBS2,
  BBS7). This is a structural scaffold, not an enzyme; no catalytic motif.
- Reactome R-CEL-5620922 "BBSome-mediated cargo-targeting to cilium".

## What is NOT known (candidate knowledge gaps)
1. ONTOLOGY/BIOLOGY (MF_DARK): There is no GO molecular-function term for a BBSome coat/
   β-propeller subunit. BBS-9 has NO experimentally measured biochemical activity and — unlike
   bbs-4 — has no ISS adaptor-activity annotation in GOA at all; its only MF-adjacent GOA term
   is "membrane" (IBA, is_active_in), which is not an MF. The specific intra-BBSome contacts
   and the cargo(es) recognised by the BBS-9 β-propeller are undefined. The field states the
   BBSome's molecular activity remains unclear.
   [PMID:26150102 "the definite molecular activity of the BBSome in regulating the homoeostasis
   of ciliary membrane proteins remain unclear"] (from bbs-4 companion paper, BBSome-general)
2. BIOLOGY (RESIDUAL_SUBGAP): whether BBS-9, as a "core" (BBS2/7/9) subunit, plays a distinct
   nucleating/assembly role vs the peripheral subunits (BBS-4/BBS-5), and what its individual
   contribution to IFT-particle assembly at the base vs turnaround at the tip is, are not
   separated experimentally in the worm.

## GOA annotation inventory (8 annotations)
1. GO:0016020 membrane — IBA — GO_REF:0000033 — is_active_in
2. GO:0034464 BBSome — IBA — GO_REF:0000033 — part_of
3. GO:0060271 cilium assembly — IBA — GO_REF:0000033 — involved_in
4. GO:0034464 BBSome — IEA — GO_REF:0000002 (InterPro IPR026511) — part_of
5. GO:0005929 cilium — NAS — PMID:22922713 (ComplexPortal) — located_in
6. GO:0034464 BBSome — NAS — PMID:22922713 (ComplexPortal) — part_of
7. GO:0060271 cilium assembly — NAS — PMID:22922713 (ComplexPortal) — involved_in
8. GO:0036064 ciliary basal body — IDA — PMID:22922713 (MGI) — located_in

Note: UniProt DR also lists GO:0015031 protein transport (IEA UniProtKB-KW) but this is not in
the GOA TSV pulled for review (keyword-derived); no separate annotation to review.

## Planned actions
- BBSome membership (all 3 dup annotations: IBA, IEA, NAS): ACCEPT the primary; core CC.
- membrane (IBA is_active_in): MARK_AS_OVER_ANNOTATED — over-general/derived; the BBSome acts
  at the ciliary base/basal body and ciliary membrane; a bare "membrane" with is_active_in for
  a coat scaffold is uninformative and the qualifier is odd for a structural subunit.
- cilium assembly (IBA + NAS): ACCEPT (core BP).
- cilium (NAS located_in): KEEP_AS_NON_CORE (general; basal body is the specific CC).
- ciliary basal body (IDA): ACCEPT (core CC; experimental worm localization).
- core_functions: in_complex BBSome; molecular_function protein-macromolecule adaptor activity
  (best available MF for a coat scaffold, flag ontology gap); BP intraciliary transport,
  cilium assembly, protein localization to cilium; locations ciliary basal body, ciliary base.
