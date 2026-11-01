# K3 / MIR1 (KSHV, HHV-8 type P isolate GK18, UniProt P90495) — curation notes

Reviewer: claude-code (CACAO audit batch 2). Date: 2026-10-29.

**Deep research was unavailable for this gene.** No deep-research API keys are
provisioned in this container, so `just deep-research` was not run and no
`K3-deep-research-<provider>.md` file exists. The literature below was assembled
by hand from the cached publications in `publications/`, from papers fetched for
this review with `just fetch-pmid`, and from the curated UniProt record
`K3-uniprot.txt`. The GONUTS wiki (`gowiki.tamu.edu`), which would have recorded
the CACAO students' own evidence statements, was **offline** at the time of
review ("This site is temporarily offline while we perform upgrades"), so the
students' reasoning could not be inspected directly; each CACAO row below was
therefore judged against the cited paper itself.

## What the protein is

K3 (ORF K3, also IE1B, MIR1 — modulator of immune recognition 1) is a 333-residue
KSHV membrane protein with an N-terminal cytosolic RING-CH (RINGv) zinc finger,
two transmembrane helices, and a long cytosolic C-terminal tail. It and its ~40%
identical paralog K5/MIR2 are the prototypes of the MARCH family of membrane-bound
RING-CH E3 ubiquitin ligases [PMID:23460925 "K3 and K5 each contain a RING-CH type
zinc finger domain at their N-termini, and are the prototypical members of the
MARCH (membrane-associated RING-CH containing) family of proteins"].

The N-terminal domain was first called a plant homeodomain but the NMR structure
(PDB 1VYX) showed it is a variant RING: [PMID:15465811 "it is conclusively
demonstrated that the K3 N-terminal domain is a variant"] member of the RING family,
with the canonical [PMID:15465811 "binding two zinc ions in a stable cross-brace motif"]
arrangement, and it is the E2-docking surface — the domain was [PMID:15465811 "found
to interact with the cellular ubiquitin-conjugating enzymes UbcH5A to -C"] and UbcH13.
UniProt records eight Zn-coordinating residues (Cys9, Cys12, Cys24, His26, Cys34,
Cys37, Cys50, Cys53) in the RING-CH-type zinc finger (residues 1-60).

## Catalytic activity and mechanism

K3 is a bona fide E3: [PMID:11756476 "cells expressing either MIR1 or MIR2 display
ubiquitination of their endogenous MHC-I chains"], and the activity requires the
zinc finger — [PMID:11756476 "The NH2-terminal region of both proteins harbors a Zn
finger of the PHD/LAP subfamily"] whose disruption ablates downregulation.
Unusually, MIR1/K3 can ubiquitinate non-lysine residues:
[PMID:15994556 "Here, we found that MIR1, but not MIR2, promoted"] down-regulation of
MHC I lacking cytoplasmic lysines, and [PMID:15994556 "ubiquitination required a
cysteine residue in the intracytoplasmic tail of MHC I"]. UniProt assigns
EC 2.3.2.36 on this basis (cysteine-to-cysteine ubiquitin transfer).

## Substrates and the immune-evasion phenotype

**MHC class I (the core target).** K3 strips all four tested HLA allotypes from
the surface — [PMID:10799607 "K3 downregulated all four HLA allotypes"],
[PMID:10799607 "A dramatic downregulation of HLA-A2, HLA-B2705, HLA-Cw4, and HLA-E
was observed in the K3-expressing GFP-positive cell population"] — and does so by
accelerating endocytosis rather than by ER retention:
[PMID:10799607 "K3-expressing cells exhibited a rapid endocytosis of class I molecules"];
[PMID:10859362 "they act to enhance endocytosis of MHC I from the cell surface;
internalized class I chains are delivered to endolysosomal vesicles, where they
undergo degradation"]. The ubiquitin mark is the internalization and sorting
signal: K3 [PMID:12006494 "promotes ubiquitylation of class I after export from the
endoplasmic reticulum."] and this provides the [PMID:12006494 "signal for class I
internalization at the plasma membrane"], after which class I enters the
TSG101-dependent late endocytic pathway.

**IFN-gamma receptor 1 (type II interferon, not type I).** [PMID:17166914 "K3 and K5
both specifically target IFN-γR1 and induce its ubiquitination, endocytosis, and
degradation, resulting in downregulation of IFN-γR1 surface expression"], with the
functional consequence that [PMID:17166914 "tyrosine-phosphorylated STAT1
(pY701-STAT1) was markedly reduced in BJAB-K3 and BJAB-K5 cells"]. The documented
interferon target of K3 is therefore the **type II (IFN-gamma) pathway**; no paper
found here shows K3 blocking type I IFN (IFNAR) signalling. This matters for the
GO:0039502 row, which the UniProt keyword mapping places on type I.

**CD1d.** UniProt cites PubMed:15864354 for CD1D as a K3/K5 target.

**DC-SIGN (CD209) and DC-SIGNR (CLEC4M)** — the CACAO paper, see below.

**Timing in the real infection.** K3 is not redundant with K5 but sequential:
[PMID:24899205 "while K5 acts immediately upon entry into the lytic phase,
K3-mediated downregulation of MHC-I was evident during later stages of lytic
replication"].

## Localization

Two curated locations, both from PubMed:10799607 per UniProt. Ishido et al. put the
bulk near the plasma membrane — [PMID:10799607 "cross sections of transfected cells
demonstrated that K3 and K5 were localized near the plasma membrane"] — while Coscoy
and Ganem, using a KDEL-GFP marker and calnexin, put the steady-state bulk in the ER:
[PMID:10859362 "Thus, at steady state the bulk of the K3 and K5 chains are localized
within the ER"]. These are not contradictory: K3 is made and resides largely in the
ER/pre-Golgi, and acts on its targets at or near the plasma membrane. The 2013 paper
adds that K3 engages immature, EndoH-sensitive lectin, so that
[PMID:23460925 "the initial interactions between the viral proteins and DC-SIGN or
DC-SIGNR is likely to occur in a pre-Golgi compartment with immature forms of these
two lectins"].

## The CACAO reference: PMID:23460925 (Lang et al. 2013, PLoS ONE) — full text available

All four CACAO rows on this gene cite this one paper. What it actually shows **for
K3** (as distinct from K5):

- **Fig. 2 (flow cytometry, 293 DC-SIGN / DC-SIGNR stable lines + GFP-K3):**
  [PMID:23460925 "both K3 and K5 caused a reduction in surface expression of both
  DC-SIGN and DC-SIGNR by approximately 60%"], and
  [PMID:23460925 "Mutation of the RING-CH domain abolished this effect"]. The same
  figure records K3's effect on endogenous MHC I:
  [PMID:23460925 "In the presence of wild-type K3 or K5, surface levels of MHC I were
  reduced about 80–90%."]
- **Fig. 3:** the tyrosine-based endocytosis motif, in addition to the RING-CH
  domain, is needed; notably K3 Y/A still downregulates MHC I.
- **Fig. 4 (dynasore washout, THP-1 and 293):**
  [PMID:23460925 "K3 expression also caused increased endocytosis of DC-SIGN relative
  to vector expressing cells"], but no endocytosis of DC-SIGNR was seen.
- **Fig. 5A (western blot):** [PMID:23460925 "expression of either wild-type K3 or K5
  resulted in decreased protein levels of both DC-SIGN and DC-SIGNR"], RING-CH
  dependent.
- **Fig. 6 (GST pull-down):** [PMID:23460925 "Pull-down of GST-tagged proteins followed
  by WB showed that both DC-SIGN and DC-SIGNR co-precipitated with both K3 and K5"],
  preferentially the immature EndoH-sensitive form.
- **Fig. 7A/B (HA-Ub pull-down, MG132/chloroquine):**
  [PMID:23460925 "We confirmed that DC-SIGN displayed ubiquitylation only in the
  presence of K3 or K5 with an intact RING-CH domain and not in the presence K3 mZn
  or K5 mZn."] and
  [PMID:23460925 "These results indicate that degradation of DC-SIGN occurs primarily
  through a ubiquitylation-dependent, proteasomal mechanism"], with a lysosomal
  fraction.

**Paralog hazard, handled.** The paper's title names both proteins, and K5 dominates
the infection experiments: in the recombinant-virus arm
[PMID:23460925 "Each of the viruses encoding a functional K5 gene (wt and ΔK3) showed
significant down regulation of DC-SIGN, DC-SIGNR and MHC I from the cell surface."],
[PMID:23460925 "with K5 playing a dominant role in this context"]. But every figure
from Fig. 2 onward assays K3 **in its own right**, with its own wild-type, mZn, Y/A,
Y/F, P/A and DE12 constructs, so the K3 annotations from this paper are not
mis-attributed paralog data. The one caveat is scope: K3's activity on these lectins
is shown in exogenous expression, not in the context of infection.

**Viral entry — what the paper does and does not show.** DC-SIGN and DC-SIGNR are
entry-enhancing co-receptors for KSHV: [PMID:23460925 "It has been documented that
DC-SIGN can act a co-receptor for KSHV, not sufficient for entry by itself, but
capable of enhancing viral infectivity"]. That is a property of the **host lectins**,
and the paper's Fig. 1 measures it in cells expressing no viral MARCH protein at all
(Bac16 ΔK3ΔK5). K3 is on the opposite side of that transaction: it **removes** the
entry co-receptor. The CACAO row GO:0075509 "endocytosis involved in viral entry into
host cell" therefore reads the wrong actor into the term — it is the virion that is
endocytosed in that term's definition ("Any endocytosis that is involved in the uptake
of a virus into a host cell"), not a host receptor. K3 is, in addition, expressed
*after* entry (immediate-early / late lytic), so it cannot participate in uptake of
the virion that delivered it.

## Intraviral interactions (PMID:16339411)

The two IPI `protein binding` rows come from the Uetz/Haas herpesviral yeast
two-hybrid interactome. The partners are KSHV (HHV-8 type M) proteins: P88941, an
uncharacterized 110-aa product, and P88951, the ribonucleoside-diphosphate reductase
small subunit (RIR2). The abstract is all that is cached
(`full_text_available: false`) and reports only the network-level result
[PMID:16339411 "revealed 123 and 173 interactions"]; there is no functional follow-up
for either pair, and neither partner is a known K3 ubiquitination substrate. Bare
`GO:0005515` is uninformative here and no better molecular function can be inferred
from the screen, so the protein-binding policy applies (REMOVE as uninformative, which
does not assert that the Y2H interactions are false).

## Summary of review decisions

| Term | Evidence | Source | Action |
|---|---|---|---|
| GO:0006511 ubiquitin-dependent protein catabolic process | IDA | **CACAO**, PMID:23460925 | ACCEPT |
| GO:0006511 (same) | IEA | ARBA | ACCEPT |
| GO:0039504 symbiont-mediated suppression of host adaptive immune response | IMP | **CACAO**, PMID:23460925 | MODIFY → GO:0046776 |
| GO:0039504 (same) | IEA | ARBA | MODIFY → GO:0046776 |
| GO:0039648 symbiont-mediated perturbation of host ubiquitin-like protein modification | IMP | **CACAO**, PMID:23460925 | ACCEPT |
| GO:0039648 (same) | IEA | ARBA | ACCEPT |
| GO:0075509 endocytosis involved in viral entry into host cell | IMP | **CACAO**, PMID:23460925 | MODIFY → GO:0044077 |
| GO:0075509 (same) | IEA | ARBA | MODIFY → GO:0044077 |
| GO:0005515 protein binding (x2) | IPI | IntAct | REMOVE (policy) |
| GO:0061630 ubiquitin protein ligase activity | IEA (EC) | UniProt | ACCEPT |
| GO:0016567 protein ubiquitination | IEA | UniPathway | ACCEPT |
| GO:0008270 zinc ion binding | IEA | InterPro/KW | ACCEPT |
| GO:0046872 metal ion binding | IEA | KW | TOO_GENERAL |
| GO:0016740 transferase activity | IEA | KW | TOO_GENERAL |
| GO:0020002 host cell plasma membrane | IEA | SubCell | ACCEPT |
| GO:0044165 host cell endoplasmic reticulum | IEA | SubCell | ACCEPT |
| GO:0039502 suppression of host **type I** IFN signalling | IEA | KW-1114 | MODIFY → GO:0140884 (type II) |
| GO:0140886 suppression of host IFN signalling | IEA | KW-1091 | MODIFY → GO:0140884 (type II) |
| GO:0052170 suppression of host innate immune response | IEA | KW-1090 | KEEP_AS_NON_CORE |
| GO:0052031 perturbation of host defense response | IEA | KW | TOO_GENERAL |

## CACAO failure-taxonomy note

One new-ish shape and one known one:

1. **Wrong actor in a two-sided interspecies term** (GO:0075509). The paper contains
   both "K3 drives endocytosis of a host receptor" and "the host receptor enhances
   virion entry". The CACAO term fuses them into "K3 is involved in endocytosis for
   viral entry", which asserts K3 does something the paper attributes to the lectin,
   and in the opposite direction (K3 destroys the co-receptor). This is adjacent to
   the catalogued "own-process term for a host-directed activity" shape, but inverted:
   here the host's own process is attributed to the symbiont. Call it *actor
   substitution across the host/symbiont boundary*.
2. **Right pathway, wrong granularity** (GO:0039504). The term is true of K3 and the
   paper does assay the relevant readout (MHC I surface levels, Fig. 2/3), but the
   paper and the wider literature support the specific child
   GO:0046776 (suppression of host antigen processing and presentation via MHC class I).

Two rows (GO:0006511 IDA, GO:0039648 IMP) are clean: right protein, right assay,
right term, correct evidence code. Across the four CACAO rows, two are accepted as
written and two need a term change — in both cases the student read the right paper
and ran the right figures, and the failure is entirely in term choice. That matches the
batch-1 conclusion recorded in `projects/CACAO.md`.
