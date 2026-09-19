# ARHGAP6 curation notes

Working journal for the PAINT-campaign review of human ARHGAP6 (UniProtKB:O43182,
HGNC:676, X p22.3). Append-only.

## 1. Sources used, and what the deep-research provider missed

Deep research: **affinage** (`ARHGAP6-deep-research-affinage.md`). Trust gates clear
(accession O43182 matches the local UniProt record, organism human,
`self_evaluation_pairwise: win`, `faith_pct: 100.0`).

Affinage's narrative is accurate as far as it goes, and it gets the central point
right: it names the separability of the GAP and actin-remodelling activities and
anchors it to PMID:10699171. But its citation list (11 PMIDs) **omits the two papers
that carry the most GO-relevant experimental content**, and both are omitted for the
same reason — the title does not say what the paper is about:

| PMID | Why a title-driven search misses it |
|---|---|
| **18434237** | Title misspells the gene as **"ARGHAP6"** and leads with "phospholipase C-delta1". A search on the correct symbol does not hit the title. |
| **19038263** | Titled for the *partner* ("novel HERG regulator") and for *C. elegans*; spells the gene out as "rho-GTPase activating protein 6" rather than ARHGAP6. |

A EuropePMC `TITLE:"ARHGAP6" OR TITLE:"ARGHAP6" OR TITLE:"RhoGAPX-1"` search returns
17 records and **does not include PMID:19038263** — confirming the mechanism rather
than just asserting it. Both papers were found by searching the *function*
(`ARHGAP6 AND phospholipase` in PubMed returns exactly these two) and by following
the UniProt `DR GO` block. Neither paper is in UniProt's `RN` reference list either:
that list holds the two cloning/function papers (PMID:10699171, PMID:9417914) plus
four large-scale sequence and phosphoproteomics submissions, so it offered no route
to them.

Both are now cached: `publications/PMID_18434237.md` (abstract only) and
`publications/PMID_19038263.md` (**full text via PMC**).

## 2. The central curation question: two (really three) separable activities

PMID:10699171 (Prakash et al. 2000) is the primary functional paper and is
abstract-only in our cache (`full_text_available: false`), but the abstract states
the separability directly:

[PMID:10699171 "Mutation of a conserved arginine residue in the rhoGAP domain
prevents the loss of stress fibers but has little effect on process outgrowth."]

[PMID:10699171 "These results suggest that ARHGAP6 has two independent functions:
one as a GAP with specificity for RhoA and the other as a cytoskeletal protein that
promotes actin remodeling."]

The mouse knockout of the rhoGAP domain alone is normal:

[PMID:10699171 "Surprisingly, loss of the rhoGAP function of Arhgap6 does not cause
any detectable phenotypic or behavioral abnormalities in the mutant mice."]

**A third output, also GAP-independent, is established by the two missed papers.**
ARHGAP6 binds and activates PLCδ1:

[PMID:18434237 "ARHGAP6 protein bound PLC-delta1 and regulated its activity by
masking the binding sites for inhibitory phospholipids."]

[PMID:18434237 "Under in vitro conditions, ARHGAP6 protein activated PLC-delta1."]

[PMID:18434237 "The activity of PLC in cells overexpressing ARHGAP6 increased
approximately 6-fold compared to control cells."]

and a second, independent lab shows that an ARHGAP6 output runs through PLC and
survives loss of GAP function:

[PMID:19038263 "ARHGAP6 effects were maintained when we introduced a dominant
negative rho-GTPase, or ARHGAP6 devoid of rhoGAP function, indicating ARHGAP6
regulation of HERG is independent of rho activation."]

[PMID:19038263 "However, ARHGAP6 lost effectiveness when PLC was inhibited."]

So the picture is one protein with a catalytic RhoA-GAP arm and **two** arms that do
not need it.

### Why the actin core function gets no `molecular_function`

The GAP-independent actin role is defined entirely by what it is *not* (not
GAP-dependent) and by cell-biological observation: co-localisation with F-actin
through an N-terminal region, and recruitment of F-actin into growing processes
[PMID:10699171 "The ARHGAP6 protein co-localizes with actin filaments through an
N-terminal domain and recruits F-actin into the growing processes."]. No direct
biochemical activity is demonstrated — no measured actin binding, no nucleation, no
bundling, no capping. Attaching a GAP molecular function would contradict the very
evidence that defines the role; attaching an invented structural or binding MF would
assert a mechanism nobody has measured.

`molecular_function` is optional on `CoreFunction`, so the slot is **left empty**,
and the entry's own description says why. This is a statement about the *evidence*,
not a claim that GO lacks a suitable term — a negative claim about the ontology is
not needed here and is not made.

## 3. Arginine finger: checked, with controls, and it settles less than it looks

See `ARHGAP6-bioinformatics/RESULTS.md` (`check_arginine_finger.py`).

- Anchor: ARHGAP1/p50RhoGAP, whose arginine finger is resolved in the RhoA
  transition-state complex **PDB 1TX4**. The anchor position is *verified*, not
  asserted: 1TX4 chain A author residue 85 is ARG and its ±6 window
  (`TTEGIFRRSANTQ`) is identical to the window around UniProt Q07960 position 282.
  The literature's "Arg85" is construct numbering; the offset is 197.
- **ARHGAP6 RETAINS the arginine finger at R433.** Domain alignment to the anchor
  and UniProt's own `Arginine finger` SITE feature agree, and R433 is the residue
  the literature mutates: [PMID:19038263 "Mutation of the conserved arginine at
  position 433 to a glycine (R433G) abolishes the rhoGAP activity of ARHGAP6"].
  All 8 panel members agree between alignment and UniProt feature.
- **The panel shows residue identity and curated activity are decoupled in both
  directions**, so retention on its own proves nothing:
  - ARHGAP11B **retains** R87 and carries two curated `NOT|enables GO:0005096` IDA
    rows (PMID:25721503, PMID:27957544).
  - ARHGAP36 — ARHGAP6's closest paralog, sharing InterPro IPR037863 (RHOGAP6/36) —
    has **T258** in the arginine column and still carries a positive `enables
    GO:0005096` IBA. OCRL substitutes **Q757** and carries a positive IDA.

What actually supports the GAP call is the functional evidence (the R433G mutant
fails to clear stress fibres), not the residue. And because R433G is a clean
loss-of-GAP reagent, it is also what makes the GAP-*independence* claims arguments
from a working mutant rather than from a residue being present:
[PMID:19038263 "expression of ARHGAP6R433G, like WT ARHGAP6, significantly reduced
HERG current amplitude"].

## 4. Three BHF-UCL annotations exist in UniProt and are missing from GOA

See `ARHGAP6-bioinformatics/RESULTS-goa-divergence.md`
(`check_goa_uniprot_divergence.py`).

UniProt's cross-reference block lists 15 GO terms; QuickGO/GOA lists 14; three are in
UniProt only:

- `GO:0016004 phospholipase activator activity` (IDA:BHF-UCL)
- `GO:0043274 phospholipase binding` (IPI:BHF-UCL)
- `GO:0141214 positive regulation of phospholipase C/protein kinase C signal transduction` (IDA:BHF-UCL)

This is **not** term obsolescence: all three are active on both OLS4 and
`api.geneontology.org` (checked on two independent services, because these are known
to disagree; QuickGO also reports them active but that would have been a third
endpoint of a service already consulted).

And the missing rows are still load-bearing. GOA is currently serving **six** ISO
annotations — mouse Arhgap6 (O54834, GO_REF:0000119) and rat Arhgap6 (A0A8I6AAE4,
GO_REF:0000121) — whose WITH/FROM column names **O43182** as the source for exactly
these three terms. The projections are orphaned: their stated human source is not in
the human record any more.

Because `just fetch-gene` seeds `existing_annotations` from the GOA TSV, these rows
would otherwise never be reviewed at all. They are therefore entered as `action: NEW`
— not as new curation, but as pre-existing BHF-UCL curation that has fallen out of
the feed the review is built from. The reason field on each says so.

## 5. Reactome puts ARHGAP6 in the RAC3-GAP tier on a co-immunoprecipitation

GOA carries `enables GO:0005096` TAS from **Reactome:R-HSA-9018806 "RAC3 GAPs
stimulate RAC3 GTPase activity"**. Reactome's own summary places ARHGAP6 in the top
tier — "shown to bind RAC3 **and stimulate its GTPase activity**" — citing a single
paper, "Li et al. 2016", which resolves to PMID:26628301. That paper's only Rac3
experiment is a co-IP:

[PMID:26628301 "Co-immunoprecipitation assay was performed to validate the
interaction between Arhgap6 and Rac3 (Ras-related C3 botulinum toxin substrate 3)."]

It never measures GTPase activity. Reactome's *other* ARHGAP6 event,
R-HSA-8981637 ("RHOA GAPs"), is by contrast backed by Prakash et al. 2000
(PMID:10699171) **and** Müller et al. 2020 (PMID:32203420), a family-wide
substrate-specificity screen [PMID:32203420 "Through a family-wide characterization
of substrate specificities, interactomes and localization, we reveal at the systems
level how RhoGEFs and RhoGAPs contextualize and spatiotemporally control Rho
signalling."].

**Action taken: ACCEPT, not REMOVE or MARK_AS_OVER_ANNOTATED.** The GO term
`GO:0005096` is substrate-agnostic and ARHGAP6 genuinely enables it (for RhoA), so
the row's assertion is true; what is unsupported is the *route* Reactome took to it.
Unsupported is not contradicted. The problem is recorded in `review.reason` and in
`propagation_review` (`root_cause: SOURCE_WEAK_OR_INFERRED`,
`failure_modes: [SOURCE_EVIDENCE_WEAK]`) rather than by downgrading a true statement.

GO cannot express the distinction directly. `GO:0005096` has **zero** descendants —
confirmed on two independent services (OLS4 `hierarchicalChildren` = 0;
`api.geneontology.org` subgraph descendants = 0). QuickGO returns one child,
`GO:1902773 GTPase activator complex`, but via **`capable_of`**, and it is a cellular
component, not a specialisation of the activity. So there is no "Rho GTPase activator
activity" term to MODIFY to. The GO mechanism for substrate lives on the enzyme as
`has input`; raised as a `suggested_questions` entry.

## 6. Half the annotation set is one PDZ interaction

See `ARHGAP6-bioinformatics/RESULTS-pdz-interactome.md`
(`check_pdz_interactome.py`). 22 of the 44 GOA rows are `GO:0005515 protein binding`
IPI from one reference, PMID:36115835 (Gogl et al., a quantitative fragmentomics /
holdup assay). All **22 of 22** partners carry PDZ domains, and ARHGAP6 ends in
`...LPETLV`, a canonical class I PDZ-binding motif (`-X-S/T-X-Φ`: T at −2, V at 0).

So these are one binding determinant measured once, not 22 independent findings. They
are real, but `protein binding` is the least informative MF available and the partners
are scaffolds rather than substrates. All 22 → `KEEP_AS_NON_CORE`.

## 7. What was deliberately NOT proposed

The HERG/IKr result (PMID:19038263) is well controlled — overexpression plus shRNA
knockdown of endogenous ARHGAP6 in an atrial myocyte line, with surface-biotinylation
quantification — and is mechanistically the most interesting GAP-independent output.
It is **not** proposed as a `NEW` annotation: it is one paper from one lab, largely in
heterologous systems, and the effect is routed through PLC rather than exerted
directly on the channel, which makes it an indirect effect of the kind the repository
guidance asks us not to annotate. It is recorded as a reference finding, described in
the PLC core function, and raised as a `suggested_questions` / `suggested_experiments`
item instead.

## 8. Other decisions worth recording

- `GO:0030041 actin filament polymerization` (NAS, PMID:10699171) →
  `MARK_AS_OVER_ANNOTATED`. The paper shows **recruitment of existing F-actin** into
  processes; GO:0030041 is defined as "Assembly of actin filaments by the addition of
  actin monomers to a filament", which is not what was measured. Not removed: the
  biology is adjacent and the term is not contradicted.
- `GO:1902533 positive regulation of intracellular signal transduction` (IEA,
  GO_REF:0000107) is an Ensembl-Compara transfer from mouse O54834, whose own row for
  that term is an **IDA by BHF-UCL from PMID:10699171** — a paper that studied human
  ARHGAP6. So this is human evidence returning to the human record by way of the mouse
  entry. Kept as non-core on granularity grounds; no circularity enum is asserted,
  because the human record does not carry the term directly and calling it circular
  would overstate the case.
- MGI's `enables GO:0005096` IDA on mouse Arhgap6 cites PMID:25211221, a paper titled
  for **Arhgap28**. Per repository guidance this is *not* treated as a mis-attribution:
  the curator read the full text, which our cache does not have, and comparator GAPs
  are routinely assayed in such papers. Recorded as a supporting source without
  challenge.
