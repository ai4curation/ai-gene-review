# K5 / MIR2 (KSHV, UniProt P90489) — curation notes

**Provenance note.** No deep-research API keys were available in this container, so
`just deep-research` was not run and **no `-deep-research-<provider>.md` file exists for
this gene**. All material below comes from the cached publications under `publications/`,
from the UniProt flat file `K5-uniprot.txt`, and from PubMed searches (PubMed MCP). The
GONUTS wiki, which normally records the CACAO student's own evidence per PMID, is still
offline — `https://gowiki.tamu.edu/wiki/index.php/PMID:23460925` returns only
"This site is temporarily offline while we perform upgrades" (checked 2026-10-29), as the
CACAO project page also records. Fortunately the one paper behind all four CACAO rows
(PMID:23460925) is cached with `full_text_available: true`, so the CACAO rows were judged
from the paper's own figures rather than from an abstract.

## Paralog hazard: K3/MIR1 vs K5/MIR2

K3 (MIR1, P88922/Q2HR75) and K5 (MIR2, P90489) are adjacent KSHV ORFs sharing ~40% identity
and both are prototypical MARCH RING-CH E3 ligases, so nearly every K5 paper also assays K3.
This review checked, paper by paper, that K5 itself was assayed and that the result quoted is
the K5 result:

- PMID:10799607 (Ishido 2000) assays both; K5-specific result: "K5 significantly downregulated
  HLA-A and -B and downregulated HLA-C only weakly, but not HLA-E, whereas K3 downregulated all
  four HLA allotypes."
- PMID:11413168 (Coscoy & Ganem 2001) is explicitly K5-only for ICAM-1/B7.2: "We report that K5,
  but not K3, expression in BJAB cells dramatically reduces ICAM-1 and B7-2 surface expression".
- PMID:18230726 (Thomas 2008) is a K5-only paper (NKG2D/NKp80 ligands).
- PMID:21490960 (Karki 2011) is a K5-only paper (receptor tyrosine kinases).
- PMID:23460925 (Lang 2013) assays both K3 and K5 side by side; K5 is the dominant activity in
  the context of infection.
- PMID:17238276 (Bartee 2006) is a K5-only proteomics screen.
- PMID:16339411 (Uetz 2006) is the intraviral Y2H screen; the IntAct rows name P90489 as bait.

No annotation in this review rests on a result that is actually a K3 result.

## Protein architecture

256 aa, 27.9 kDa. N-terminal cytoplasmic RING-CH (RINGv) zinc finger, residues 7–66, binding
two Zn(2+) via Cys15/Cys18/Cys40/Cys43 (site 1) and Cys30/Cys32/Cys56/Cys59 (site 2)
[file:HHV8P/K5/K5-uniprot.txt "ZN_FING         7..66"]. Two helical transmembrane segments
(84–104, 125–145) leave both the RING-CH and the long C-terminal region (146–256) in the
cytosol, the topology shared by cellular MARCH proteins
[file:HHV8P/K5/K5-uniprot.txt "Multi-pass membrane protein"]. The C-terminal region is largely
disordered (179–256) and carries the trafficking motifs: a tyrosine-based endocytosis motif
beginning at Tyr156, a polyproline tract, and two acidic tracts ("DE12").

Mutational anchors:
- `C15S/C56S/C59S` → "Loss of B7-2 and ICAM-1 surface expression reduction"; `C56S/C59S` →
  "Loss of ubiquitination" [PMID:10799607, via UniProt MUTAGEN].
- `W47A` → "Complete loss of host receptor tyrosine kinases (RTKs) internalization and E3
  ubiquitin ligase activity" [PMID:21490960, PMID:23460925].
- `Y156A` → "Reduced cell surface modulation of both DC-SIGN and DC-SIGNR" [PMID:23460925].

## Core activity: membrane-bound RING-CH E3 ubiquitin ligase

The decisive biochemistry is in PMID:11756476, a cell-free reconstitution: "In vitro, addition
of a MIR2-glutathione S-transferase (GST) fusion protein to purified E1 and E2 enzymes leads to
transfer of ubiquitin (Ub) to GST-containing targets in an ATP- and E2-dependent fashion; this
reaction is abolished by mutation of the Zn-coordinating residues of the PHD domain." The same
paper names the class: "Thus, MIR2 defines a novel class of membrane-bound E3 Ub ligases that
modulates the trafficking of host cell membrane proteins."

That activity is what the whole phenotype hangs on: "expression of MIR1 and MIR2 leads to
ubiquitination of the cytosolic tail of their target proteins and that ubiquitination is
essential for their removal from the cell surface" [PMID:11756476].

## Substrate repertoire (all host integral membrane proteins)

| Substrate | Immune role | Reference |
|---|---|---|
| MHC-I (HLA-A, -B, weakly -C; not -E) | CTL recognition | PMID:10799607, PMID:10859362 |
| ICAM-1 (CD54), B7.2 (CD86) | immunological synapse, T-cell costimulation | PMID:11413168 |
| IFN-gamma receptor 1 (IFNGR1) | **type II** interferon signalling | PMID:17166914 |
| MICA, MICB (NKG2D ligands), AICL/CLEC2B (NKp80 ligand) | NK-cell activation | PMID:18230726 |
| BST-2/tetherin, ALCAM/CD166, Syntaxin-4 | virion release, CD6 ligation | PMID:17238276 |
| DC-SIGN (CD209), DC-SIGNR (CD209L) | antigen uptake, KSHV co-receptor | PMID:23460925 |
| growth-factor receptor tyrosine kinases | monocyte metabolism/proliferation | PMID:21490960 |
| CD31/PECAM, CD1d, HFE | adhesion, lipid antigen presentation, iron | reviewed in PMID:23460925 intro |

Mechanism varies by substrate — "some cellular proteins are targeted by the MARCH proteins for
endocytosis, some are blocked for exocytosis, and some targets are regulated by multiple
mechanisms" [PMID:23460925].

## PMID:23460925 (Lang 2013) — the paper behind all four CACAO rows

This is the DC-SIGN/DC-SIGNR paper; I read the full text. Figure by figure:

- **Fig. 1A/B** — host-side result only: DC-SIGN and DC-SIGNR each raise KSHV infectivity ~6-fold,
  blocked by mannan. The virus used in 1A is `Bac16ΔK3ΔK5`, i.e. **K5 is absent** from the
  infectivity experiment. "At 48 hpi, KSHV infection levels were up to 6-fold higher in 293 cells
  expressing either C-type lectin treated with ICAM-1 antibody, as compared with parental 293
  cells receiving the same treatment".
- **Fig. 1C** — the deletion-virus (IMP) experiment: "Each of the viruses encoding a functional K5
  gene (wt and ΔK3) showed significant down regulation of DC-SIGN, DC-SIGNR and MHC I from the
  cell surface. In contrast, the ΔK5 and ΔK3ΔK5 viruses only mediated weak down regulation of any
  of the examined molecules."
- **Fig. 2** — RING-CH dependence: "both K3 and K5 caused a reduction in surface expression of both
  DC-SIGN and DC-SIGNR by approximately 60% (Fig. 2). Mutation of the RING-CH domain abolished
  this effect".
- **Fig. 3** — Y156 (tyrosine-based endocytosis motif) and the acidic tracts are additionally
  required.
- **Fig. 4B/C** — endocytosis of **DC-SIGN** (the host lectin) is accelerated: "In the presence of
  K5, accumulated DC-SIGN was endocytosed following dynasore removal, with cell surface levels
  decreasing ∼60%, but total protein levels remaining static". DC-SIGNR is *not* endocytosed;
  it is blocked from exocytosis.
- **Fig. 5** — degradation: "expression of either wild-type K3 or K5 resulted in decreased protein
  levels of both DC-SIGN and DC-SIGNR. Mutation of the RING-CH domain in either K3 or K5 abrogated
  this ability."
- **Fig. 6** — co-precipitation, preferentially with the EndoH-sensitive immature lectin, placing
  the initial interaction "in a pre-Golgi compartment".
- **Fig. 7A/B** — ubiquitylation and route of destruction: "We confirmed that DC-SIGN displayed
  ubiquitylation only in the presence of K3 or K5 with an intact RING-CH domain and not in the
  presence K3 mZn or K5 mZn"; MG132 "very significantly increased ubiquitylation", so
  "degradation of DC-SIGN occurs primarily through a ubiquitylation-dependent, proteasomal
  mechanism".

**What the paper does *not* show.** It contains no assay of viral entry attributable to K5, no
T-cell or NK assay, and no type-I interferon measurement. Its own reading of the entry question is
the *opposite* of a pro-entry role for K5: "Given a role for both lectins in entry, down modulation
would reduce superinfection." K5 is an immediate-early protein expressed *after* entry, and the
authors' alternative hypothesis is egress, not entry: "The possibility also exists that DC-SIGN and
DC-SIGNR down modulation enhances viral egress, as has been demonstrated in the case of tetherin."

## CACAO row assessment (all four from PMID:23460925, 2013-03)

1. **GO:0006511 ubiquitin-dependent protein catabolic process, IDA** — matches Fig. 7A/B exactly
   (RING-CH-dependent ubiquitylation of DC-SIGN; MG132-sensitive degradation). Right process,
   right granularity, right protein. Accepted.
2. **GO:0039504 symbiont-mediated suppression of host adaptive immune response, IMP** — rests on
   Fig. 1C, where the ΔK5 virus fails to clear MHC-I, DC-SIGN and DC-SIGNR from the surface. The
   immunological consequence is not assayed *in this paper* (the authors only predict it: "it is
   likely that by reducing DC-SIGN levels in these antigen presenting cells, K3 and K5 will have
   inhibitory effects on activation of T cells"), but it is directly demonstrated elsewhere for K5
   — PMID:11413168 shows "K5-transfected B cells show substantial impairment in their ability to
   induce T cell activation". True for the gene; accepted.
3. **GO:0039648 symbiont-mediated perturbation of host ubiquitin-like protein modification, IMP** —
   the term's definition is "A process by which a symbiont alters ubiquitin-like protein modification
   of target proteins of either host or symbiont proteins", which is precisely what K5 does.
   Accepted.
4. **GO:0075509 endocytosis involved in viral entry into host cell, IMP** — **not supported.** The
   term is "Any endocytosis that is involved in the uptake of a virus into a host cell", i.e. the
   endocytic uptake of the virion itself. The endocytosis in this paper is that of **DC-SIGN**, a
   host lectin, from the cell surface, and the only entry data (Fig. 1A/B) are host-side and were
   collected with a `ΔK3ΔK5` virus. Worse, K5's effect on the two lectins would *reduce* entry, as
   the authors themselves state. This looks like a conflation of "a lectin that is a KSHV entry
   co-receptor" with "endocytosis during entry". The ARBA row for the same term (ARBA:ARBA00088611)
   is an automatic restatement of the same claim and inherits the same error.

## Localization

- Host cell ER: "Immunoelectron microscopy showed that the K5 antigen was situated mainly in the
  endoplasmic reticulum but was not present on the virion or in the nucleus" [PMID:10684303], and
  the DC-SIGN work independently places the first K5–substrate contact pre-Golgi [PMID:23460925].
- Host cell plasma membrane: "K3 and K5 exhibit 40% amino acid identity to each other and localize
  primarily near the plasma membrane" [PMID:10799607]; UniProt records "Host cell membrane
  {ECO:0000269|PubMed:10684303}" with the note "Probably exerts its effects at the plasma membrane
  during viral infection". Substrate ubiquitylation at the surface (MHC-I, MICA, RTKs) requires K5
  to be there.

Both compartments are genuinely used, at different steps: substrates are intercepted immature in
the ER/early Golgi *and* ubiquitylated at the plasma membrane.

## Interferon arm: type II, not type I

GOA carries `GO:0039502 symbiont-mediated suppression of host **type I** interferon-mediated
signaling pathway` from `UniProtKB-KW:KW-1114`. The keyword itself is generic ("Viral protein
involved in the evasion of host innate defense by inhibiting the interferon signaling pathway"),
but the GO term it maps to is type-I-specific. K5's demonstrated interferon target is IFN-gamma
receptor 1, i.e. **type II**: "we demonstrate that K3 and K5 both specifically target gamma
interferon receptor 1 (IFN-gammaR1) and induce its ubiquitination, endocytosis, and degradation,
resulting in downregulation of IFN-gammaR1 surface expression and, thereby, inhibition of IFN-gamma
action" [PMID:17166914]. No paper reports K5 acting on IFNAR or on type-I IFN signalling. The
correct child is `GO:0140884 symbiont-mediated suppression of host type II interferon-mediated
signaling pathway`; the generic parent `GO:0140886` (from KW-1091, interferon receptors) is correct
as written. The keyword-to-GO mapping is recorded as a UniProt source defect on that row.

## Open questions

- Does K5 contribute to egress by removing DC-SIGN/DC-SIGNR, the way it does by removing tetherin?
  The authors say the experiment is under way but it is unpublished here.
- Which E2 enzyme(s) does K5 use in cells? The reconstitution used purified E1/E2 generically.
- K5's effect on receptor tyrosine kinases increases growth signalling [PMID:21490960] — this is
  an immune-evasion ligase being used for a proliferative output, and whether that is selected for
  or incidental is unresolved.
