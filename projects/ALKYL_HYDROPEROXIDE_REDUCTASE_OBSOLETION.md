# Alkyl Hydroperoxide Reductase Activity — Obsoletion & Replacement

## Overview

A GO obsoletion has retired one molecular function term and merged its
annotations into a broader, more accurate term:

- **GO:0008785 alkyl hydroperoxide reductase activity** (MF, obsolete)

Replaced by:

- **GO:0102039 NADH-dependent peroxiredoxin activity** (MF;
  EC 1.11.1.26; RHEA:62628)

The rationale, captured in the upstream go-ontology ticket, is that
GO:0008785 was defined with a substrate-specific stoichiometry
(octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol) that is
more specific than the specificity of any known gene product, and
"alkyl hydroperoxide reductase" is listed by Expasy as a synonym of
EC 1.11.1.26 — i.e. exactly the broader term GO:0102039.

This project tracks the impact on AI Gene Review and queues the
affected genes for review. Neither gene is currently in this
repository.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6396](https://github.com/geneontology/go-annotation/issues/6396)
- Ontology ticket: [geneontology/go-ontology#31961](https://github.com/geneontology/go-ontology/issues/31961)
- Ontology obsoletion PR: [geneontology/go-ontology#32015](https://github.com/geneontology/go-ontology/pull/32015) — **merged**, so the obsoletion is already in production.
- The closely-related "alkyl hydroperoxide reductase complex" CC term
  GO:0009321 had its `comment` updated by the obsoletion PR to point
  to GO:0102039 — it is **not** obsolete and remains the right CC for
  the AhpC/AhpF complex.

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| alkyl hydroperoxide reductase activity | GO:0008785 (obsolete) | GO:0102039 NADH-dependent peroxiredoxin activity |

### Affected experimental annotations (from upstream issue body)

Only 2 direct experimental annotations remain on the books; both
need to be moved from GO:0008785 to GO:0102039.

| Group | Gene | Species | Source ID | Reference | Evidence | PANTHER | Status |
|---|---|---|---|---|---|---|---|
| EcoliWiki | AhpF | E. coli K-12 (NCBITaxon:83333) | EcoCyc:EG11385-MONOMER | PMID:11717276 | IGI (with ahpC, katE, katG) | — | pending move to GO:0102039 |
| PseudoCAP | PA3529 | P. aeruginosa PAO1 (NCBITaxon:208964) | UniProtKB:Q9HY81 | PMID:21674802 | IDA | PTHR10681 | pending move to GO:0102039 |

No InterPro2GO, UniProt-Keywords, or UniRule mappings to GO:0008785
were listed in the upstream issue.

## Impact on this repo

No genes annotated to GO:0008785 are currently reviewed here.
Searches under `genes/ECOLI/` and `genes/PSEAE/` for AhpF / PA3529
returned no matches.

So **no existing reviews need refresh** for the obsoletion itself,
but two prokaryotic redox-enzyme reviews are now natural follow-on
work since the obsoletion is in production and the annotation
migration is the only remaining loose end upstream.

The PANTHER family **PTHR10681** (alkyl hydroperoxide reductase
subunit F / thioredoxin reductase-like) appears in the with/from
column for the PA3529 IDA annotation. Any IBA propagation from this
family will also need to be reviewed once GOA pipelines pick up the
obsoletion, but per the upstream issue no IBA migrations are listed
as separate items, so this is opportunistic rather than required.

## Scope

- **Organisms**: E. coli K-12 (existing organism dir `genes/ECOLI/`)
  and P. aeruginosa PAO1 (existing organism dir `genes/PSEAE/`).
- **GO branches**: MF only — the obsoletion is a substrate-specificity
  collapse to the broader EC 1.11.1.26 term. No BP or CC changes.
- **Type of fix**: terminological — the biology (NADH-dependent
  peroxide reduction) is unchanged; reviews would evaluate whether
  GO:0102039 captures the gene's core function or whether more
  specific peroxiredoxin descendants are appropriate.
- **Related complex term**: GO:0009321 alkyl hydroperoxide reductase
  complex (CC) is **not** obsoleted and remains the correct cellular
  component for AhpC/AhpF holocomplex annotations.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting
and confirm UniProt accessions. Neither is currently in the repo.

### Tier 1 — direct annotation, well-characterized

1. **AhpF** (E. coli K-12, EcoCyc:EG11385-MONOMER) — the FAD-containing
   NADH-dependent disulfide reductase subunit of the AhpC/AhpF system.
   Reduces oxidized AhpC (the peroxiredoxin subunit) at the expense
   of NADH. The IGI annotation from PMID:11717276 was made together
   with ahpC, katE, and katG, so the biological context (peroxide
   detoxification in concert with catalases) is well-defined. A clean
   ACCEPT/MODIFY review target for the obsoletion migration.

### Tier 2 — direct annotation, less canonical

2. **PA3529 / Q9HY81** (P. aeruginosa PAO1) — IDA annotation from
   PMID:21674802 by PseudoCAP. PANTHER family PTHR10681 places it in
   the AhpF-like family. Verify gene symbol (PseudoCAP uses locus
   tag) and whether UniProt has a recommended gene name before
   creating the review folder. Slightly lower priority than AhpF
   only because the E. coli enzyme is the textbook reference for the
   activity.

## Proposed approach

1. **Obsoletion has landed.** GO:0008785 is already obsolete in the
   ontology (PR #32015 merged). The 2 direct annotations in the
   upstream tracker have **not yet been migrated** as of project
   creation date — that is the open work upstream issue #6396 is
   tracking.
2. **Start with E. coli AhpF.** Run `just fetch-gene ECOLI AhpF`
   (or whichever capitalization UniProt prefers) and confirm the
   GOA pull picks up the obsoletion: GO:0008785 should appear as an
   obsolete term (with replaced_by annotation) and any new IBA pulls
   should already use GO:0102039. Review per CLAUDE.md.
3. **Follow with P. aeruginosa PA3529** (Q9HY81). The gene symbol
   may differ between UniProt and PseudoCAP — verify before
   creating the folder.
4. **Cross-reference GO:0009321** (alkyl hydroperoxide reductase
   complex, CC) — this term is intact and is the appropriate CC for
   the AhpC/AhpF holocomplex. If reviewing the cognate **AhpC**
   subunit becomes relevant downstream, it can be added as a Tier 3
   later but is not in scope here (no direct annotation to the
   obsoleted MF).
5. **Defer IBA-propagation review** for PTHR10681 until the next GOA
   release reflects the obsoletion; the upstream issue lists no IBA
   migration as required, so this is opportunistic.

## Priority

**Low.** Only 2 direct annotations are affected and the ontology
change is already in production. The opportunity here is that AhpF
and PA3529 are otherwise unreviewed prokaryotic redox enzymes that
would extend the repo's bacterial coverage, not that any existing
review is blocked.

## Status

- 2026-05-12 — Project file created. Upstream annotation issue
  #6396 still open (no comments). Ontology obsoletion PR
  geneontology/go-ontology#32015 already merged. No gene reviews
  started in this repo.
