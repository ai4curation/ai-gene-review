# Ent-Kaurene Oxidation to Kaurenoic Acid — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will obsolete `GO:0010241 ent-kaurene oxidation to
kaurenoic acid` (a BP describing three successive oxidations of the 4-methyl
group of ent-kaurene). The upstream rationale is that the experimental data
behind the term is adequately captured by the broader BP
`GO:0009686 gibberellin biosynthetic process`, and that any catalytic-activity
content already has a dedicated MF — `GO:0052615 ent-kaurene oxidase activity`
— which is unaffected by this obsoletion.

This project tracks the two experimental annotations called out on the upstream
list. Both impacted curation groups (UniProt and TAIR) are already marked
`DONE` on the go-annotation issue, so this is primarily a queueing /
documentation exercise — useful for keeping the AI Gene Review obsoletion log
complete and for handling the InterPro2GO mapping that is still open.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6433](https://github.com/geneontology/go-annotation/issues/6433)
- Ontology ticket: [geneontology/go-ontology#32078](https://github.com/geneontology/go-ontology/issues/32078)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| ent-kaurene oxidation to kaurenoic acid | GO:0010241 | GO:0009686 gibberellin biosynthetic process (BP); MF content moves to GO:0052615 ent-kaurene oxidase activity |

Term labels verified in OLS on 2026-05-27:
- `GO:0010241` (`ent-kaurene oxidation to kaurenoic acid`) — live, slated for obsoletion. Definition: "The three successive oxidations of the 4-methyl group of ent-kaurene to form ent-kaur-16-en-19-oate, kaurenoic acid. This process may be carried out entirely by the enzyme ent-kaurene oxidase."
- `GO:0009686` (`gibberellin biosynthetic process`) — live, proposed BP replacement.
- `GO:0052615` (`ent-kaurene oxidase activity`) — live MF (EC 1.14.14.86); not part of the obsoletion. SJM's comment on the upstream issue effectively treats `GO:0010241` as a redundant restatement of MF + BP.

SJM comments on the two experimental annotations (paraphrased from
go-annotation#6433):

- PMID:22487175 (CYP701A6, Q5Z5R4) — only shows enzyme activity assays. No BP
  evidence in the paper. SJM suggests "just removed" rather than remapped.
- PMID:9671797 (KO, Q93ZB2) — ga3-1 mutant deficient in ent-kaurene oxidase
  activity, framed in the abstract as "the first cytochrome P450-mediated
  step in the gibberellin biosynthetic pathway". SJM suggests remapping to
  GO:0009686.

## Affected experimental annotations (upstream list)

| # | Source | Accession | Symbol | Taxon | PMID | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| 1 | UniProt | UniProtKB:Q5Z5R4 | CYP701A6 | NCBITaxon:39947 (Oryza sativa Japonica Group) | PMID:22487175 | IDA | Rice ent-kaurene oxidase 2 (EC 1.14.14.86). Paper is an enzyme assay; IDA was on a BP that is really an MF claim. Already has GO:0009686 IMP on the UniProt entry, so removal of the GO:0010241 IDA does not lose biological coverage. Upstream UniProt marked DONE. |
| 2 | TAIR | UniProtKB:Q93ZB2 / AT5G25900 | KO (GA3, CYP701A3, KO1) | NCBITaxon:3702 (Arabidopsis thaliana) | PMID:9671797 | IMP | Arabidopsis ent-kaurene oxidase, chloroplastic (EC 1.14.14.86). The ga3-1 mutant phenotype underpins the gibberellin BP claim; remap to GO:0009686 is the upstream proposal. UniProt entry already lists GO:0009686 IDA. Upstream TAIR marked DONE. |

Group impact tally (from upstream): UniProt 1 (DONE), TAIR 1 (DONE).

## Mappings flagged for redirection

- `interpro2go`: `InterPro:IPR044225` (Ent-kaurene oxidase, chloroplastic — plant
  KO family, including AtKO1) → `GO:0010241`. Verified via InterPro REST on
  2026-05-27 that the family entry exists and is named "Ent-kaurene oxidase,
  chloroplastic". Once `GO:0010241` is obsoleted, the InterPro2GO mapping
  should be reviewed. The MF replacement `GO:0052615 ent-kaurene oxidase
  activity` is the cleaner target for this family because IPR044225 captures
  the catalytic family, not a BP claim; an additional `GO:0009686 gibberellin
  biosynthetic process` mapping would also be defensible since every member
  of the family is a committed step in gibberellin biosynthesis.

No UniRule, HAMAP, or UniProt-Keywords mappings to `GO:0010241` were listed by
upstream.

## Impact on this repo

Neither affected gene currently has an `*-ai-review.yaml` in this repo
(verified via `find genes -type d -iname 'CYP701*' -o -iname 'KO'` on
2026-05-27). This project is therefore a queueing exercise rather than a
re-review of existing files. Both annotations are already actioned upstream by
UniProt and TAIR, so the value of pulling these into AI Gene Review is low
relative to the open obsoletion projects (vesicle docking, hypochlorous acid,
etc.), but the genes themselves are scientifically clean examples of plant
gibberellin biosynthesis enzymes and would be useful as positive controls for
GO:0009686 / GO:0052615 annotation.

## Scope

- Organism: Arabidopsis thaliana (KO, Q93ZB2) and Oryza sativa Japonica Group
  (CYP701A6, Q5Z5R4). Plant gibberellin biosynthesis — both proteins are
  CYP701-family cytochromes P450 catalysing the three sequential oxidations of
  ent-kaurene to kaurenoic acid.
- GO branch: BP (gibberellin biosynthetic process). The MF side
  (`GO:0052615 ent-kaurene oxidase activity`) is the natural home for the
  catalytic content currently described by `GO:0010241`.
- Type of fix: structural / curation hygiene. The biology is uncontroversial;
  the obsoletion is about removing a hybrid term whose BP framing actually
  conflated three successive catalytic steps. No annotations need to be
  rebutted on biological grounds; the question is just which of MF
  (`GO:0052615`) and BP (`GO:0009686`) is the right home for each evidence
  record.

## Candidate genes for initial review

Listed in priority order. Both are optional given the upstream DONE markers.

1. **KO / GA3 (Arabidopsis, Q93ZB2)** — Higher-value review candidate of the
   two. The PMID:9671797 paper is foundational for the gibberellin biosynthesis
   pathway in plants and the gene already carries `GO:0009686 IDA` from
   UniProt. A review would mostly serve as a positive-control example for the
   `GO:0009686` + `GO:0052615` pairing.
2. **CYP701A6 (Oryza sativa, Q5Z5R4)** — Rice ent-kaurene oxidase 2. Less
   pressing because the upstream consensus (SJM) is that the IDA on
   `GO:0010241` is best simply removed: the underlying paper (PMID:22487175)
   is an enzyme assay, so the MF `GO:0052615` is the right destination, but
   that MF is not currently in the existing annotation set on the gene.

## Proposed approach

1. **Wait for obsoletion to land before pulling into AI Gene Review.** The
   ontology ticket (go-ontology#32078) is open. Both
   group-level curation tasks are already DONE upstream, so there is nothing
   urgent to do here.
2. **Flag the IPR044225 InterPro2GO mapping** as the remaining open item, and
   note that the cleanest redirect is to the MF `GO:0052615 ent-kaurene
   oxidase activity` rather than the BP `GO:0009686 gibberellin biosynthetic
   process` — the family is defined by catalytic activity, not pathway role.
3. **If gene reviews are queued**, start with Arabidopsis KO (Q93ZB2). The
   biology is canonical and well-supported; the review can serve as a positive
   control for how to handle ent-kaurene-oxidase-family annotations once the
   obsoletion lands.

## Priority

Low — both impacted curation groups marked DONE upstream. The InterPro2GO
mapping redirect is the only piece that may still benefit from a comment on
the upstream issue.

## Status

- 2026-05-27 — Project file created. Tracking go-annotation#6433 (opened
  2026-05-26) and go-ontology#32078. Obsoletion not yet applied. UniProt and
  TAIR marked DONE for the two affected experimental annotations. No
  AI Gene Review files exist for either gene. OLS confirms GO:0010241,
  GO:0009686, and GO:0052615 are all currently live; InterPro IPR044225
  confirmed via REST.
