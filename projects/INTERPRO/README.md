---
title: "InterPro mapping review — supporting material"
---

# InterPro mapping review — supporting material

Supporting material for the [InterPro Mapping Review project](../INTERPRO.md).

## Contents

- `extract_suspect_interpro_mappings.py` — reproducible extractor. Walks every
  `genes/*/*/*-ai-review.yaml`, finds the annotations sourced from InterPro2GO
  (`original_reference_id: GO_REF:0000002`), recovers the source InterPro entry id(s)
  from the matching `*-goa.tsv` (the `WITH/FROM` column), joins in the reviewer's
  action, and writes the two TSVs below.
- `suspect_interpro_mappings.tsv` — one row per reviewed InterPro2GO annotation
  (gene, InterPro id(s), GO term, action, suspect flag, proposed replacement, reason).
- `interpro_family_priorities.tsv` — one row per InterPro entry, aggregating how often
  it produced an accepted vs a suspect mapping across all reviewed genes. This is the
  ranked worklist for family-level deep research (entries that repeatedly produce
  suspect mappings first).
## Proposed interpro2go edits (SSSOM)

- `interpro2go.sssom.yaml` — canonical SSSOM mapping set: the family-deep-research verdicts
  expressed as proposed edits to InterPro2GO (one row per reviewed `(InterPro entry, GO term)`;
  `exactMatch` = sound, `broadMatch` = over-broad/demote, `exactMatch` + `predicate_modifier: Not`
  = remove). Source of truth.
- `interpro2go.terms.yaml` — **generated** nested term-tuple form (do not edit by hand) for GO
  label validation.
- `sssom_to_terms.py` — regenerates the `.terms.yaml` from the `.sssom.yaml`.

```bash
just validate-interpro-mappings   # SSSOM structure + GO term/label validation
```

## Before proposing a removal

A removal row (`exactMatch` + `predicate_modifier: Not`) drops the term from every protein the
entry matches, including the members for which it is correct. Before adding one, run two checks
and record the result at the end of the row's `comment`, starting "Rule cover (...)".

1. **Sole-source check.** List the reviewed annotations of the term whose only InterPro source is
   this entry. Those genes lose the annotation outright. Read their review actions: if reviewers
   accepted the term on most of them, the removal costs correct annotations and the note must say so.

   ```bash
   # genes whose only InterPro source for GO:0005524 is IPR000719
   awk -F'\t' '$4=="GO:0005524" && $3=="IPR000719" {print $1"/"$2, $6}' \
     projects/INTERPRO/suspect_interpro_mappings.tsv
   ```

2. **Rule-cover check.** Find what else still supplies the term to the members that should keep it:
   - **Another InterPro entry.** Grep the current interpro2go file for the term. Site-level and
     catalytic entries, such as the kinase ATP-binding site IPR017441, often already carry it.
   - **A UniRule.** Search the UniProt UniRule API for the term and for the family name. HAMAP,
     PIRSR, PIRNR and RU rules can require a site, exclude a domain with a negative condition, or
     limit the taxon. That is how the Cu/Zn SOD rule UR000000113 excludes the copper chaperone CCS.
     Check the EC-to-GO mapping too, because many rules assign an EC number rather than a GO term.

   ```bash
   curl -sS https://current.geneontology.org/ontology/external2go/interpro2go | grep 'GO:0005524'
   curl -sS 'https://rest.uniprot.org/unirule/search?query=GO:0005524&size=50&format=json'
   curl -sS https://current.geneontology.org/ontology/external2go/ec2go | grep '^EC:1.15.1.1 '
   ```

   The local cache in `rules/unirule/` is incomplete: it holds no PIRSR rules and lacks
   UR000000113, so query the live API.

Then choose the request that fits:

- **Wrong for every member:** remove; add the correct term to the entry if one exists.
- **Right for a subset that another entry or a rule already covers:** remove, and cite the covering
  source in the note.
- **Right for a subset that nothing covers:** remove only together with a request for the covering
  rule or mapping. Otherwise propose narrowing (`broadMatch`) rather than removal.

## Family deep research (generated process)

Family deep research is generated, not hand-written. It is wired the same way as gene
deep research:

- `templates/interpro_family_research.md` — the deep-research prompt template.
- `scripts/deep_research_interpro_family.py` — wrapper that loads the cached InterPro
  metadata as context and runs `deep-research-client`.
- `just deep-research-interpro-family <IPR> [provider]` — the recipe (in
  `project.justfile`); provider defaults to `falcon` (Edison). Output:
  `interpro/<db>/<ID>/<ID>-deep-research-<provider>.md`.

```bash
just deep-research-interpro-family IPR000719          # falcon (Edison) by default
```

## Regenerate

```bash
uv run python projects/INTERPRO/extract_suspect_interpro_mappings.py
```

An annotation is counted "suspect" when its review `action` is anything other than
`ACCEPT` (MODIFY, REMOVE, MARK_AS_OVER_ANNOTATED, KEEP_AS_NON_CORE, UNDECIDED). The TSVs
are regenerated from the current state of the reviews, so re-run after new reviews land.
