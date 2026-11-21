# Curation notes: bacterial de novo phosphatidic acid synthesis

Module: `modules/bacterial_phosphatidic_acid_synthesis.yaml`
Project: [LIPID_DIVIDE](../projects/LIPID_DIVIDE.md)
Branch: `lipid-divide-project`

## Boundary

Proposed boundary (module ends at phosphatidic acid, PA) was tested against the
neighbouring modules and kept.

- `modules/cdp_dag_phospholipid_synthesis.yaml` begins by activating PA with CTP
  to CDP-diacylglycerol and then runs the head-group transfers (PS/PE/PC, PI,
  PGP/PG, cardiolipin). Its concrete grounding is eukaryotic (CDS1/Tam41, PGS1,
  PSD, PEMT/Cho2-Opi3).
- `modules/bacterial_phosphatidylglycerol_cardiolipin_biosynthesis.yaml` begins
  at CDP-diacylglycerol (PgsA, RHEA:12593).
- `modules/bacterial_phosphatidylethanolamine_biosynthesis.yaml` begins at
  CDP-diacylglycerol (PssA, RHEA:16913).

All three therefore start at CDP-DAG or later, so PA is a clean, non-duplicating
join and nothing downstream is restated here. Cross-references are recorded in
the module's `notes` rather than as parts, because `connections` are
document-scoped and `module_ref` means inclusion, which would pull downstream
chemistry inside the boundary.

One residual: **bacterial CdsA** (phosphatidate cytidylyltransferase,
EC 2.7.7.41) is the single reaction between PA and CDP-DAG and is modelled in no
bacterial module (`grep -l cdsA modules/*.yaml` hits only the eukaryotic
`cdp_dag_phospholipid_synthesis.yaml` and `dmel_cardiolipin_biosynthesis_remodeling.yaml`).
This is a **curation** gap, not a knowledge gap, so per CLAUDE.md it is recorded
here and in the module `notes`, not as a `knowledge_gaps` entry. Pulling CdsA
inside would have made the module's name wrong (it would no longer end at PA)
and would have created a second home for a reaction that belongs with the
CDP-DAG modules.

Upstream is also excluded: glycerol-phosphate supply (GpsA, GlpD/GlpK; and
AraM/EgsA for G1P) and acyl donor supply (`type_ii_fatty_acid_synthesis`,
`fatty_acid_elongation_cycle`,
`bacterial_unsaturated_fatty_acid_biosynthesis`). Regulation (FapR control of
`plsX`; the PlsX/PlsY coupling of phospholipid to fatty-acid synthesis), PA
turnover, and acyl-chain remodeling are out of scope.

## Structure: why not three top-level parts

The task proposed three parts: (1) PlsX, (2) first acylation with a variant set,
(3) PlsC. Tested and adjusted.

PlsX is required **only** by the PlsY route. Rieche et al. state that
"Bacteria belonging to the phylum Xanthomonadales only contain the PlsB and PlsC
enzymes for phospholipid biosynthesis" [PMID:42286214]. A top-level obligatory
PlsX step would make the module unsatisfiable for those taxa and would
mis-describe E. coli flux, where "although PlsB plays the principal role in
1-acyl-G3P synthesis, PlsX and YgiH are also important for optimal E. coli
growth" [PMID:17645809].

Final structure (two top-level parts, satisfies the ≥2-part rule):

```
part 1  first_acylation_to_lysophosphatidic_acid        (BIOLOGICAL_PROCESS)
        variant_set first_acylation_route
          variant_kind: ROUTE, selection: ONE_OR_MORE
          ├─ acyl_phosphate_plsx_plsy_route  (METABOLIC_PATHWAY)
          │    part 1  plsx_acyl_phosphate_formation -> annoton plsx_activity
          │    part 2  plsy_g3p_acylation            -> annoton plsy_activity
          │    connection plsx -> plsy  PROVIDES_INPUT_FOR (VERIFIED)
          └─ plsb_route                      (REACTION)
               annoton plsb_activity
part 2  plsc_phosphatidic_acid_formation                (REACTION)
        annoton plsc_activity
connection  part1 -> part2  PROVIDES_INPUT_FOR (VERIFIED)
```

`variant_kind: ROUTE` because the branches use different molecular functions
(GO:0043811 + GO:0043772 vs GO:0004366), not alternative carriers of one
activity. `selection: ONE_OR_MORE` because E. coli has both. The downstream
connection is stated above the variant set, since both routes converge on the
same intermediate.

`chaining_status: VERIFIED` is set on both connections with a note: the shared
intermediates (acyl phosphate; 1-acyl-sn-glycero-3-phosphate) are not
CoA-carried, so the automated CoA-continuity matcher cannot check the links, but
the Rhea product/substrate identity is exact.

## Reaction grounding (all from the reviewed UniProt flat files)

| Step | Protein | EC | Rhea | GO MF |
|---|---|---|---|---|
| acyl-ACP -> acyl-phosphate | P71018, P27247 | 2.3.1.274 | RHEA:42292 | GO:0043811 |
| G3P -> LPA (acyl-Pi) | Q45064, P60782 | 2.3.1.275 | RHEA:34075 | GO:0043772 |
| G3P -> LPA (acyl-CoA/ACP) | P0A7A7 | 2.3.1.15 | RHEA:15325, RHEA:42300 | GO:0004366 |
| LPA -> PA | O07584, P26647 | 2.3.1.n4 / 2.3.1.51 | RHEA:42296, RHEA:19709 | GO:0003841 |

Two donor-mismatch points are recorded in the annoton `function.description`
rather than being "fixed" by inventing terms: GO:0004366 and GO:0003841 (and
GO:0003841's parents) are written with acyl-CoA donors, while the bacterial
enzymes use acyl-[ACP] (B. subtilis PlsC exclusively so). The term request for
the acyl-[ACP] LPAAT already exists in
`genes/BACSU/plsC/plsC-ai-review.yaml:proposed_new_terms`; it is not duplicated
in the module.

PlsX carries `processes: GO:0006654` in the module although its own GOA rows stop
at GO:0006644 / GO:0008654 and no `plsX` review exists. This mirrors the
refinement the completed BACSU plsY review already made (both of its generic
process rows were MODIFYed to GO:0006654) and is flagged in the annoton
description as the module's own refinement.

## PANTHER / PAINT grounding

Family ids and labels taken verbatim from `interpro/panther/panther.obo`
(`grep -A1 "^id: PANTHER:PTHRnnnnn$"`); family membership of each representative
confirmed independently from each protein's own `DR PANTHER` line in its UniProt
flat file.

| Annoton | Family | PANTHER label (verbatim) |
|---|---|---|
| plsx_activity | PTHR30100 | FATTY ACID/PHOSPHOLIPID SYNTHESIS PROTEIN PLSX |
| plsy_activity | PTHR30309 | INNER MEMBRANE PROTEIN YGIH |
| plsb_activity | PTHR12563 | GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE |
| plsc_activity | PTHR10434 | 1-ACYL-SN-GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE |

`ancestral_nodes` asserted only where the node's own IBD is for the annoton's
asserted function:

- `PTN000046632` (PTHR10434, GO:0003841, IBD) — confirmed in
  `interpro/panther/PTHR10434/PTHR10434-paint.tsv`, seeds include
  `UniProtKB:P26647`; also present in `genes/BACSU/plsC/plsC-goa.tsv` WITH/FROM.
- `PTN000285870` (PTHR12563, GO:0004366, IBD, seed `UniProtKB:P0A7A7`,
  `taxon:1236`) — confirmed in
  `interpro/panther/PTHR12563/PTHR12563-paint.tsv`. Its taxon is
  Gammaproteobacteria, narrower than the proteobacteria+actinobacteria
  distribution reported for PlsB; that limitation is stated in the node
  description rather than glossed.

**No node asserted for PlsX or PlsY.** `interpro/panther/PTHR30100/` does not
exist and `interpro/panther/PTHR30309/` has no `-paint.tsv`. The only PlsY node
reachable from GOA is `PTN001250899` (in `genes/BACSU/plsY/plsY-goa.tsv`), whose
IBD is for GO:0005886 plasma membrane, not for GO:0043772. Using it as the
ancestral node of the acyltransferase annoton would assert a clade-level
inference PAINT has not made, so it is omitted per the "if you cannot be sure,
assert no id" rule.

## Stereochemistry (the substantive point)

Handled as the task directed and consistent with the two completed reviews: the
modelled chemistry stays **G3P -> LPA -> PA** throughout. No G1P part, variant,
substrate, product or asserted molecular function.

Evidence as it stands [PMID:42286214, full text cached]:

- "whereas the GPAT PlsB is strictly stereoselective towards G3P"
- purified B. subtilis and E. coli PlsY acylate G1P as well as G3P in detergent
  with only minor differences; PlsC converts both LPA enantiomers to PA in a
  coupled liposome system
- but reconstituted in a membrane, "the levels of (R)-LPA (containing a G3P
  lipid backbone) were significantly higher compared to the levels of (S)-LPA, a
  difference that was not observed for the enzyme in detergent (Fig."
- the in vivo claim is a consistency argument from B. subtilis having PlsY as its
  sole GPAT, and the heterochiral-lipid observation itself [PMID:35767906] is a
  single unreplicated, abstract-only report

Under `projects/ENZYME_SPECIFICITY.md` this is real in vitro activity of
unestablished physiological relevance. The user's standard (model in vivo
biology, not in vitro promiscuity) therefore puts it in a module-level
`knowledge_gaps` entry (`gap_kind: BIOLOGY`, `dark_aspect: RESIDUAL_SUBGAP`),
which the `ModuleReview` schema supports as a top-level slot. The gap mirrors
the boundary/significance/resolution text already agreed in
`genes/BACSU/plsY/plsY-ai-review.yaml` and `genes/BACSU/plsC/plsC-ai-review.yaml`
rather than re-deciding it, and the GO term requests stay in those two reviews
(a `ModuleReview` has no `proposed_new_terms` slot, and duplicating them would
create two sources of truth).

One module-specific consequence is recorded that the gene reviews could not
state: the capability is confined to the **PlsY branch** of the route variant
set, since PlsB is strictly G3P-specific. That is in the branch descriptions and
in the gap's `significance`.

A second knowledge gap records that the PlsX-PlsY physical coupling is only
"probable" in UniProt; if it is an obligate assembly, the acyl-phosphate route
is one annoton with a `PROTEIN_COMPLEX` participant rather than the two ordered
reactions modelled here.

## Validation

- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_phosphatidic_acid_synthesis.yaml` -> **No issues found**
- `uv run python -m ai_gene_review.validation.module_validator modules/bacterial_phosphatidic_acid_synthesis.yaml` -> **module checks passed**, 5 warnings:
  - 4x "none of the representative members ... are in the PANTHER member index" —
    `.cache/panther/` does not exist in this checkout at all, so the index was
    never built; the index is a git-ignored build artifact. Membership was
    instead verified from each protein's own UniProt `DR PANTHER` line. Left as
    is; `just refresh-panther-members` (or `just validate-modules`) builds the
    index.
  - 1x `FAMILY_FUNCTION_UNREVIEWED` for `plsb_activity`: the cached
    `PTHR12563-review.yaml` records GO:0004366 as `UNRESOLVED` at family scope
    because PTHR12563 also holds GPAT1/GPAT2 and DAPAT proteins. This is correct
    and deliberately not suppressed: it is exactly why the annoton carries the
    PlsB-specific `ancestral_nodes` restriction and why the family
    `description` says so. Resolving it would require editing the PANTHER family
    review, which is out of scope for this task.
- `uv run ai-gene-review render-modules modules/bacterial_phosphatidic_acid_synthesis.yaml` — rendered to a scratch output dir rather than `pages/modules/`, to keep the diff to the module YAML and this notes file.
- `git diff --check` — clean.

No `-deep-research-*.md` file was generated for this module (the QC panel will
report its absence). The literature base is the cached full texts of
PMID:42286214 and PMID:17645809, the abstract-only PMID:17557823,
PMID:19282621 and PMID:35767906, and the two completed BACSU reviews, so a
provider run was not needed to settle the boundary or the structure. Never
author one by hand under that filename.

## Not verified

- B. subtilis PlsX experimental evidence rests on PMID:16021622, which is not
  cached in `publications/`; the module cites UniProt/HAMAP and PMID:17645809
  instead.
- Actinobacterial PlsB has no reviewed exemplar here and no PAINT node; only the
  gammaproteobacterial case (P0A7A7, `taxon:1236`) is grounded.
- The claim that Xanthomonadales lack PlsX/PlsY is taken from Rieche et al.
  citing Zhang and Rock 2008; the primary survey was not checked.
