---
title: "TreeGrafter Failure Modes & Tree Placement"
autolink_gene_symbols: false
---
# TreeGrafter Failure Modes & Tree Placement

[← back to TreeGrafter Inference Evaluation](../TREEGRAFTER.md)

> **Provenance.** Every count on this page comes from the sidecars
> regenerated on 2026-10-01 at commit **`943b98815`** (see
> [Results](../TREEGRAFTER.md#results-computed-at-commit-943b98815-2026-10-01)
> on the main page for the reproduce commands and the drift since the earlier
> 2026-09-06 snapshot, which had 306 down-grades).

This sub-page drills into the **299 down-graded** TreeGrafter annotations
(`REMOVE` / `MARK_AS_OVER_ANNOTATED` / `MODIFY` from the
[main evaluation](../TREEGRAFTER.md)) and asks the question directly: **does it
make sense where TreeGrafter placed the protein on the PANTHER tree?**

We answer it *without* re-running TreeGrafter, because the placement is already
recorded for every protein:

- the **graft node** (`PTN…`) the term was propagated from — in the gene's GOA `WITH/FROM`;
- the **PANTHER family** (`PTHRxxxxx`) and **subfamily** (`PTHRxxxxx:SFn`) the
  protein was assigned to — in the UniProt record (`DR PANTHER` lines), produced
  by the same PANTHER classification TreeGrafter uses.

The join (graft node + family + subfamily + propagated term + reviewer action)
is computed by [`analyze_placement.py`](analyze_placement.py) into
[`treegrafter_placement.tsv`](treegrafter_placement.tsv). 298 of the 299
cases recover a subfamily; all 299 recover a graft node.

Every one of the 299 is then assigned to one of the four failure modes below
by [`classify_failure_modes.py`](classify_failure_modes.py) →
[`treegrafter_failure_modes.tsv`](treegrafter_failure_modes.tsv). The
assignment has two layers: a per-row curated table,
[`failure_mode_curated.tsv`](failure_mode_curated.tsv) (160 `current` rows,
each with a one-line justification), which always wins; and a keyword
heuristic over the GO aspect and the reviewer's `review.reason` for the rest
(123 rows), with 16 rows left unclassified. The curated table also keeps **19
`superseded` rows** — earlier calls on annotations that are no longer
down-graded at `943b98815` (e.g. `ilvA-I`/`ilvA-II`, `K9IMD0` GO:0019731,
`mdr`, `aprA` electron transfer), each annotated with its current action —
which the classifier ignores. Six rows superseded at the 2026-09-27 refresh
(`fogD` ×4, `IRE1` GO:0070059, `K9IJK6` GO:0014909) have since re-entered the
down-graded set after follow-up reviews and are `current` again. The operational rule that separates modes 1 and 4: **if
the PANTHER *subfamily* name already describes the protein correctly and the
bad term came from a higher node, it is mode 1; if the subfamily itself is the
wrong enzyme, it is mode 4.**

Both tables are joined on `(file, term_id)`, never on the gene symbol: symbols
are not unique across the corpus (`mdh` in METEA and PSEPK, `ALB` in CANLF and
FELCA, the two PSEPK `dapF` paralogs), and a symbol-keyed join silently pulled
one organism's `review.reason` onto another's row.

**Fifty-eight of the 123 heuristic rows are decided by construction rather than
by reading the reviewer:** 51 cellular-component terms (mode 3 by aspect alone)
and 7 rows whose term is on an explicit low-information binding allowlist
(`binding`, `protein binding`, `identical protein binding`, `small molecule
binding` — mode 3 whatever the reason says). Terms that name a real ligand
(`ubiquinone binding`, `double-stranded DNA binding`, `metal ion binding`) are
*not* on that list and are decided from the reviewer's reason like any other
row. That leaves **65 rows genuinely placed by keyword**, which is the tier the
second-pass curation should target.

| Mode | annotations | share | proteins | MF | BP | CC |
|---|---:|---:|---:|---:|---:|---:|
| 1 Granularity (family / node-level or sibling term) | 149 | 50% | 122 | 81 | 68 | 0 |
| 3 Generic / out-of-context localization, binding or process *(informativeness policy)* | 93 | 31% | 85 | 18 | 24 | 51 |
| 4 Within-superfamily mis-placement | 37 | 12% | 24 | 23 | 13 | 1 |
| 2 Pseudo-enzyme / co-opted fold | 4 | 1% | 2 | 1 | 3 | 0 |
| 0 Unclassified (heuristic declines; curation queue) | 16 | 5% | 14 | 10 | 6 | 0 |

The `proteins` column counts distinct **review files**, not gene symbols: a
symbol-keyed count merges the two `mdh` proteins and other cross-organism or
paralogous symbol collisions, and reads modes 3 and 4 as 83 and 23.

The 16 unclassified rows are deliberate: the reviewer's reason states a real
problem but not in words the heuristic can safely map to a mode (`acoA`,
`ahpC`, `benB`, `cbcW` ×2, `Cgas`, `davA`, `flgG`, `groES`, `I7J3R9`, `mfd`,
`nuoM`, `PP_0094`, `PP_0301`, `PP_2608` ×2). Some do not fit any of the four modes cleanly —
`Cgas` is a lineage-specific loss of function with direct species evidence,
`cbcW` a complex-level activity on a single subunit — and are left as mode 0
rather than pushed into the nearest bucket.

## Headline: placement is usually fine — the *term* is the problem

Reading the propagated GO term against the PANTHER **subfamily name** shows that
TreeGrafter rarely puts a protein in a grossly wrong part of the tree. The
fold/family assignment is usually reasonable. What fails is the GO term
that rides along with the graft. Four failure modes account for 95% of the
down-grades (the remaining 5% are mode 0):

### 1. Family-level over-generalisation (term granularity)

The protein is placed in the right **family**, but the propagated term is the
broad *family* function while the **subfamily** already knows something more
specific (or divergent).

| Gene | Propagated term (down-graded) | PANTHER subfamily (where it landed) |
|---|---|---|
| eryAI / eryAII / eryAIII | `fatty acid synthase activity` (MODIFY) | *INACTIVE PHENOLPHTHIOCEROL SYNTHESIS **POLYKETIDE SYNTHASE*** |
| mcr-1 / mcr2 / mcr-3 / mcr-4 | `LPS core region biosynthetic process` (OVER), `phosphotransferase activity, phosphate group as acceptor` (MODIFY) | **PHOSPHOETHANOLAMINE TRANSFERASE EptA** |
| fliI ×3, sctN ×2 | `proton-transporting ATP synthase activity, rotational mechanism` (REMOVE) | SPI-1 TYPE 3 SECRETION SYSTEM ATPASE / FLAGELLUM-SPECIFIC ATP SYNTHASE (PTHR15184); the term comes from a PAINT IBD on the duplication node above the F1-β and FliI/SctN clades ([case study](rotary-atpase-leak.md)) |
| ADAR2 | `tRNA-specific adenosine deaminase activity` (REMOVE) | AT07585P-RELATED (PTHR10910:SF62); the same graft node PTN000098697 supplied the **accepted** `double-stranded RNA adenosine deaminase activity`, `double-stranded RNA binding` and `adenosine to inosine editing` |

The erythromycin PKS modules are the clearest case: the **family** is named
"fatty acid synthase" (PTHR43775) and the family-level GO term `fatty acid
synthase activity` was propagated — but the **subfamily** correctly identifies a
polyketide synthase. The mcr colistin-resistance enzymes are placed in *exactly*
the right subfamily (phosphoethanolamine transferase / EptA) yet inherited a
generic `phosphotransferase` MF and a lipid-A-vs-LPS-core process error. **The
graft point is right; the inherited term is too coarse.** `ADAR2` was filed as
mode 4 ("ADAR on the ADAT branch") on the previous snapshot; by the rule above
it is mode 1 — the graft node that supplied the wrong tRNA-specific term also
supplied the correct ADAR activity and editing terms, which the reviewer
accepted — and it has been re-filed. (`ahpC`'s `thioredoxin peroxidase
activity`, listed here before, is now mode 0: its current reason is about the
term being obsolete and the AhpF reductant, not family-level propagation.)

### 2. Pseudo-enzyme / loss of activity

Correct fold family, but the protein has lost catalytic activity or been
co-opted to a non-enzymatic role — something a tree graft cannot detect.

| Gene | Propagated term | Subfamily | Reality |
|---|---|---|---|
| OCTS1 | `glutathione transferase activity`, `glutathione metabolic process` (OVER) | GLUTATHIONE S-TRANSFERASE | Octopus **S-crystallin**: GST fold, ~1/700–1/6000 of authentic GST activity; a structural eye-lens protein (PMID:7639695, PMID:27499004, PMID:8587103) |
| A0A8B6GS20 (MTMR9) | `phosphatidylinositol dephosphorylation` (MODIFY), `negative regulation of autophagy` (OVER) | myotubularin-related | **Pseudophosphatase**: lacks the catalytic cysteine; regulates active MTMR partners |

Genuine pseudo-enzymes turn out to be **rare** in this corpus — four
annotations on two genes. The two rows the previous snapshot flagged as
contested mode-4 calls, `K9IMD0` (draculin) `GO:0019731` and `mdr`
`GO:0015421`, are no longer down-graded (`K9IMD0` is now `KEEP_AS_NON_CORE`
after a follow-up review, `mdr` `UNDECIDED` after the 2026-09-20 re-review;
both genes are still `awaiting_adjudication` in the re-review records); their
curated rows are kept as `superseded`. Two cases listed here on an earlier
snapshot were re-filed: TFP's `enzyme regulator activity` is an *outdated node
term* (specifier proteins are now known to be Fe(II)-dependent C–S lyases;
mode 1), and IRE1's `unfolded protein binding` is a generic binding term on a
sensor (mode 3).

### 3. Generic / out-of-context localization and process (an informativeness policy)

This mode is **not a grafting error**: it records the review standard's
preference for specific, core terms. Low-information CC terms (`cytoplasm`, `cytosol`, `plasma membrane`, `nucleus`)
or organism-context BP terms inherited from a distant ancestor, correct-ish but
non-core or absent from the host. Examples: `relA` → `plasma membrane`, `dinB`
→ `cytosol`, `fbp` → `sucrose biosynthetic process` (a pathway the host does
not run), and several *Pseudomonas putida* genes. Note that `zwf` →
`pentose-phosphate shunt` and the `mcr` LPS-core process call are **mode 1**,
not mode 3 — both reasons state family/node-level propagation explicitly, and
they are mode 1 in the sidecar. 51 of the 93 mode-3 rows are CC terms placed
by aspect alone; under a less strict review policy most of them would be
*retained* rather than down-graded.

### 4. **True within-superfamily mis-placement** (the cases a re-run would change)

A minority *are* placement errors: the protein lands in a structurally related
but functionally distinct subfamily of a shared fold superfamily. These are the
only down-grades where re-examining the actual graft point (or an independent
bioinformatic/structural check) would change the call.

| Gene | Propagated term (down-graded) | Landed in subfamily | Should be |
|---|---|---|---|
| **aprA** (*Desulfovibrio*) | `succinate dehydrogenase activity` (REMOVE) (its `electron transfer activity` row is now `ACCEPT`; its `anaerobic respiration` row is mode 1) | SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN (PTHR11632:SF51) | **Adenylylsulfate (APS) reductase** α-subunit — shares the FAD fumarate-reductase/SDH flavoprotein fold but reduces APS, not succinate |
| **fcs** (*P. putida*) | `medium-chain fatty acid-CoA ligase activity` (MODIFY), `fatty acid metabolic process` | 2-SUCCINYLBENZOATE–CoA LIGASE | **Feruloyl-CoA synthetase** — adjacent ANL adenylating-enzyme superfamily, wrong specific subfamily |
| **mdh** (*P. putida* and *M. extorquens*, ×2 each) | `L-lactate dehydrogenase (NAD+) activity`, `lactate metabolic process` (REMOVE) | L-LACTATE DEHYDROGENASE (PTHR43128:**SF16**; the *family* PTHR43128 is `L-2-HYDROXYCARBOXYLATE DEHYDROGENASE (NAD(P)(+))`) | **Malate dehydrogenase** — LDH/MDH superfamily node |
| **mqo1 / mqo2 / mqo3** | `(S)-2-hydroxyglutarate dehydrogenase activity` (REMOVE) | L-2-HYDROXYGLUTARATE DEHYDROGENASE, MITOCHONDRIAL | **Malate:quinone oxidoreductase** |
| **dapE**, **pepV** | `acetylornithine deacetylase activity`, `L-arginine biosynthetic process` (REMOVE) | N-ACETYL-L-CITRULLINE DEACETYLASE (PTHR43808:SF31, M20A) | **DapE** succinyl-DAP desuccinylase / **PepV** dipeptidase — ArgE branch of a mixed M20A family ‡ |
| **Q53353, lsdB, Saro_0802, Saro_2809** | `carotenoid dioxygenase activity`, `carotene catabolic process` (REMOVE/MODIFY) | CAROTENOID 9,10(9',10')-CLEAVAGE DIOXYGENASE (PTHR10543) | **Lignostilbene / resveratrol dioxygenases** (EC 1.13.11.43) — no stilbene subfamily exists |
| **ptxD** | `glyoxylate reductase (NADPH)`, `hydroxypyruvate reductase` (REMOVE) | GLYOXYLATE/HYDROXYPYRUVATE REDUCTASE B | **Phosphonate dehydrogenase** (D-2-hydroxyacid DH superfamily) |
| **mupP** | `phosphoglycolate phosphatase activity`, `DNA repair` (REMOVE) | PHOSPHOGLYCOLATE PHOSPHATASE (PTHR43434) | **MurNAc-6-phosphate phosphatase** (HAD superfamily) |
| **quiA** | `quinoprotein glucose dehydrogenase activity` (OVER) | QUINOPROTEIN GLUCOSE DEHYDROGENASE | **Quinate dehydrogenase (quinone)** |
| **kdsC**, **lytN**, **pvdD**, **davD**, **lpdV**, **ech**, **galB**, **PP_1257** | see [`treegrafter_failure_modes.tsv`](treegrafter_failure_modes.tsv) | | KdsC in a mixed CMAS/KdsC family; an amidase in a lytic-transglycosylase subfamily; a pyoverdine NRPS module carrying EntF terms; LPD-val vs LPD-glc across *P. putida* E3 paralogs; … |

‡ **dapE discrepancy, unresolved.** The `dapE` reviewer's reason for
`GO:0008777` says Q88MP5 "is assigned to the proteobacterial DapE
subfamily", but its cached UniProt record assigns it to PANTHER
`PTHR43808:SF31` *N-ACETYL-L-CITRULLINE DEACETYLASE* — the reason appears to
refer to the NCBIfam `TIGR01246` DapE signature it cites for `GO:0006526`, not
to PANTHER. The mode-4 call rests on the PANTHER subfamily and stands; the
review's wording is noted here and not changed.

Mis-placements are **12% of the down-grades (37 annotations, 24 proteins)** —
still the minority. This share was previously reported as 19% (58 annotations)
from a looser heuristic that filed any reason containing `paralog` or `rather
than` as mode 4; reasons that explicitly say *family-level propagation*
(`zwf`, `scpC`, `paaF`/`paaH`/`paaJ`, the four `aroQ` rows) now correctly land
in mode 1, which is what the operational rule above says they are.
Almost all of them are the *same* pattern: a **mixed PANTHER family whose
subfamilies are labelled by the best-studied member**, so an uncharacterised
paralog in a different substrate class inherits that member's terms
(LDH/MDH, M20A, CCD/stilbene dioxygenase, SDH/FRD/AprA).

## Lightweight graft check (PANTHER vs InterPro, no re-run)

Rather than re-install InterProScan, we read the **two classifications UniProt
already stores** for each exemplar: the PANTHER family/subfamily (the TreeGrafter
graft point that propagated the term) and the InterPro signature entries (an
independent, signature-based opinion). Computed live by
[`graft_check.py`](graft_check.py) →
[`treegrafter_graft_check.tsv`](treegrafter_graft_check.tsv) (UniProt
fetched 2026-09-27; the `review_action` column was refreshed offline at
`943b98815` with `--refresh-actions` and reads from `treegrafter_review.tsv`,
so it shows the current action — `aceK` `ACCEPT`, `NaUGT1` `UNDECIDED`, the
other eight as at selection). The first five exemplars:

| Gene | Propagated term (down-graded) | PANTHER subfamily (graft) | InterPro's specific call | Diagnosis |
|---|---|---|---|---|
| **aprA** | succinate dehydrogenase activity | SDH flavoprotein, *mitochondrial* | **IPR011803 AprA** | PANTHER **subfamily-resolution gap**: no AprA subfamily exists, so it grafted onto the nearest (mito SDH) — but InterPro *does* identify AprA. An InterPro2GO call would beat TreeGrafter here. |
| **OCTS1** | glutathione transferase activity | GLUTATHIONE S-TRANSFERASE | **IPR003083 S-crystallin** | InterPro names the lens **crystallin**; PANTHER subfamily stays "GST". Pseudo-enzyme invisible to the graft. |
| **mcr-1** | phosphotransferase, phosphate acceptor | PHOSPHOETHANOLAMINE TRANSFERASE EptA | **IPR058128 Mcr1; IPR040423 PEA_transferase** | Placement is **right** (both methods); the propagated *GO term* is just a poor ancestral-node mapping. |
| **eryAIII** | fatty acid synthase activity | *INACTIVE…POLYKETIDE SYNTHASE* | PKS ketoacyl-synthase / acyltransferase domains | Placement is **right** (both methods say PKS); the propagated term is the **family-level** FAS term. |
| **fcs** | medium-chain fatty acid-CoA ligase | 2-succinylbenzoate–CoA ligase | only generic AMP-dependent ligase domain | Correct **superfamily**; *no* database has a feruloyl-CoA-synthetase-specific entry. Substrate unresolved by either method. |

**Two conclusions from the graft check:**

1. **In 4 of 5 cases the placement is sound — the error is the GO term bound to
   the graft node**, not the tree position. Re-running TreeGrafter would
   reproduce the same (reasonable) subfamily. The fix belongs upstream in
   PAINT/PANTHER's node-to-GO mapping (propagate the subfamily-specific term;
   don't attach a catalytic MF to a pseudo-enzyme subfamily).
2. **InterPro sometimes has resolution PANTHER lacks** (`AprA`, `S-crystallin`,
   `Mcr1` — 3 of these 5). For these proteins a signature/InterPro2GO annotation would have been
   *more* specific or correct than the phylogenetic graft — a concrete argument
   for cross-checking TreeGrafter against InterPro2GO (see next steps).

## OpenScientist blinded verification (illustrative, not a validation)

> **Reference standard.** The comparison here is with the AIGR agent review
> actions recorded when each exemplar was selected (`aprA` `REMOVE`, `fcs`
> `MODIFY`, `OCTS1` `MARK_AS_OVER_ANNOTATED`, `eryAIII` `MODIFY`, `mcr-1`
> `MODIFY`, `NaPMT3` `REMOVE`, `ADAR2` `REMOVE`, `NaUGT1` `REMOVE`, `aceK`
> `MODIFY`, `ahpC` `MODIFY`). It is not with the current actions: some of
> those reviews were later revised with the reports in hand (`aceK`
> `GO:0004721` → `ACCEPT`; `NaUGT1` `GO:0080043` → `UNDECIDED`), and
> [`exemplar_independence.py`](exemplar_independence.py) →
> [`exemplar_independence.tsv`](exemplar_independence.tsv) records that 9 of
> the 10 exemplar annotations now cite the OpenScientist/Falcon report in
> their `review.supported_by`. All ten were drawn from rows that were already
> down-graded, with no accepted-annotation controls, and n = 10, so no claim
> about the check's reliability can be made. See
> [Reference standard](../TREEGRAFTER.md#reference-standard).

Each propagated term was posed to OpenScientist as a **blinded**
function-assignment hypothesis — the agent saw only *"GENE has \<propagated
term\>"* (never the reviewer's action or the PANTHER subfamily name) using the
dedicated
[`treegrafter_function_hypothesis.md`](https://github.com/ai4curation/ai-gene-review/blob/main/templates/treegrafter_function_hypothesis.md)
prompt, which asks it to actively test the failure modes. Reports and
provenance are committed under each gene's `*-hypotheses/` directory.

| Gene | Blinded verdict | Failure mode the agent assigned | Decisive evidence it found | Reviewer action at selection (unchanged) |
|---|---|---|---|---|
| **OCTS1** | REFUTED | pseudo-enzyme / activity lost (mode 2) | S-crystallin (IPR003083); lost catalytic Trp39; ~1000× lower kcat; PDB 5B7C | `MARK_AS_OVER_ANNOTATED` |
| **mcr-1** | REFUTED | wrong node term, placement right (mode 1) | EC 2.7.8.43 ⇒ correct MF is GO:0016780, not sibling GO:0016776; error traced to a TAS annotation on EptA at the `PTHR30443:SF0` node | `MODIFY` |
| **eryAIII** | REFUTED | granularity, family-vs-subfamily (mode 1) | DEBS3 type-I modular PKS (EC 2.3.1.94); family-level FAS term propagated over the PKS subfamily | `MODIFY` |
| **aprA** | REFUTED | within-superfamily mis-placement (mode 4) | APS reductase α (EC 1.8.99.2); absent covalent FAD-binding His | `REMOVE` |
| **fcs** | REFUTED | within-superfamily mis-placement (mode 4) | feruloyl-CoA synthetase (EC 6.2.1.34 ⇒ GO:0050563); aromatic vs aliphatic substrate | `MODIFY` |

(The 2026-09-20 re-review of `aprA` notes that the report's claim that a
covalent FAD-binding histidine is required by *all* SDH/FRD catalysis is
stronger than needed, and did not use it as decisive proof.) fcs required a
scope-narrowed re-run at `max_iterations=2` after the first attempt hit the
7200 s API ceiling.

## Scale-up: 10 exemplars, two providers, family heterogeneity

The exemplar set was extended to **10 genes across 10 distinct enzyme families**
(adding NaPMT3, ADAR2, NaUGT1, aceK, ahpC) and each was run **blinded on two
providers** (OpenScientist autonomous-compute + Falcon/Edison literature). The
blinded conclusions were later cited in the source reviews as
`file:…/openscientist.md` / `falcon.md` references, which is why the
comparison below uses the actions recorded at selection.

| Gene | Reviewer action at selection | Current action | OpenScientist | Falcon | Specific call |
|---|---|---|---|---|---|
| OCTS1 | OVER_ANNOTATED | same | REFUTED (pseudo-enzyme) | pseudo-enzyme | S-crystallin, structural (GO:0005212) |
| mcr-1 | MODIFY | same | REFUTED (wrong node term) | too general | pEtN transferase ⇒ GO:0016780/GO:0043838 |
| eryAIII | MODIFY | same | REFUTED (granularity) | mis-placed | DEBS3 modular PKS (EC 2.3.1.94) |
| aprA | REMOVE | same | REFUTED (mis-placed) | mis-placed | APS reductase α (EC 1.8.99.2) |
| fcs | MODIFY | same | REFUTED (mis-placed) | mis-placed | feruloyl-CoA synthetase (GO:0050563) |
| NaPMT3 | REMOVE | same | REFUTED (granularity) | mis-placed | putrescine N-MTase (EC 2.1.1.53, GO:0030750) |
| ADAR2 | REMOVE | same | REFUTED (mis-placed) | mis-placed | dsRNA/mRNA ADAR (not tRNA ADAT) |
| NaUGT1 | REMOVE | UNDECIDED | REFUTED (granularity) | mis-placed | UGT85A clade, wrong substrate |
| aceK | MODIFY | ACCEPT | too general | too general | IDH kinase/phosphatase ⇒ GO:0101014 |
| ahpC | MODIFY | same | too general | too general | AhpF-dependent peroxiredoxin |

Both providers down-graded the propagated term on all 10 genes (8 REFUTED + 2
"too general" for OpenScientist; 7 REFUTED + 3 "too general" for Falcon) and
agree with each other on the failure mode in 8/10. That matches the reviewer
action recorded at selection on all 10, but because every exemplar was chosen
from a down-graded row, this shows only that the check reproduced those ten
down-grades; how often it would down-grade an accepted annotation is
unmeasured. The current actions for `aceK` and `NaUGT1` were set with the
reports in hand, so they are not used for the comparison. Note also that the
providers' own mode labels do not always match this page's rule: both call
`ADAR2` mis-placed, but by the mode-1/mode-4 rule it is mode 1 (see above).
Cross-provider agreement shows the two agents read the same literature the same
way; on its own it does not measure accuracy.

**Family-level companion runs (Falcon).** Each PANTHER family was
characterized for whether one GO MF term is safe to propagate. **9 of 10
families were called HETEROGENEOUS** — a single substrate-specific term
mis-annotates some branches:

| Family | Verdict | Why |
|---|---|---|
| PTHR11632 (aprA) | HETEROGENEOUS | SDH + fumarate reductase; GO:0000104 over-annotates FRD |
| PTHR43775 (eryAIII) | HETEROGENEOUS | FAS + modular PKS share the ketosynthase fold |
| PTHR11571 (OCTS1) | HETEROGENEOUS | active GSTs + co-opted crystallins |
| PTHR11558 (NaPMT3) | HETEROGENEOUS | spermidine synthases + neofunctionalized PMTs |
| PTHR11926 (NaUGT1) | HETEROGENEOUS | 14 plant UGT groups, divergent substrates |
| PTHR43201, PTHR30443, PTHR10910, PTHR10681 | HETEROGENEOUS | substrate/reductant/subfamily divergence |
| **PTHR39559 (aceK)** | **HOMOGENEOUS** | single IDH kinase/phosphatase function |

The one homogeneous family (aceK) is also the one whose review was later
revised to accept the propagated term (with the reports in hand). That is a
single case, and the
other "too general" verdict (`ahpC`) sits in a family called heterogeneous
(PTHR10681), so family homogeneity does not by itself predict the verdict
here. A **family homogeneity check before single-term propagation** remains a
reasonable hypothesis to test on a larger, independent sample.

## What this means for the "re-run TreeGrafter" question

For the **bulk** of failures (modes 1–3, **82%** of the down-grades; modes 1
and 2 alone are 51% if mode 3's informativeness calls are set aside), re-running TreeGrafter would
reproduce the *same, sensible* placement — the fix belongs at the
**annotation** level (propagate the subfamily-specific term, gate
catalysis-implying MF behind active-site checks, suppress generic CC), not at
the placement level. For the **12%** in mode 4 (`aprA`, `fcs`, `mdh`,
`mqo1–3`, `dapE`/`pepV`, the stilbene dioxygenases, `pvdD`, …), the placement
itself is the suspect — and because they cluster in a handful of mixed
families (see the
[family hotspots](../TREEGRAFTER.md#family-hotspots-upstream-targets)), the
durable fix is a subfamily split or subfamily-level annotation in PAINT rather
than a per-protein re-run.

The main page's [corroboration analysis](../TREEGRAFTER.md#corroboration-treegrafter-only-vs-multi-method-vs-interpro2go-only)
adds the operational lever: every annotation on this page is by construction an
*uncorroborated* TreeGrafter call (`GO_REF:0000118`); the TreeGrafter calls
that another pipeline reproduced surface under `GO_REF:0000120` and are
accepted 78% of the time (an upper bound — reviewers could see the label).

## Suggested follow-ups

- **Blinded OpenScientist/Falcon deep-dives** on ten exemplars: run and
  compared with the actions recorded at selection (see the reference-standard
  note above); with ten down-graded rows and no controls, this is
  illustrative. Next: a fresh sample that includes accepted TreeGrafter rows
  as controls, with review actions recorded before the reports are read.
- **Classify every down-grade**: done for the current 299
  (`classify_failure_modes.py`; 160 hand-curated, 123 heuristic, 16 mode 0).
  Remaining: second-pass the **65 keyword-placed MF/BP heuristic rows** and
  the 16 mode-0 rows.
- **Active-site / pseudo-enzyme check** on mode-2 candidates (catalytic-residue
  conservation) — an upstream signal TreeGrafter lacks.
- **Feed errors upstream**: family-vs-subfamily granularity cases (mode 1) as
  candidate PAINT subfamily-annotation refinements (e.g. PTHR43775 PKS vs FAS);
  node-term errors (mcr-1's EptA/SF0 TAS) as direct GO_Central corrections.
- **Cross-check against InterPro2GO** where InterPro out-resolves PANTHER
  (`IPR011803 AprA`, `IPR003083 S-crystallin`, `IPR058128 Mcr1`).
