# Research And Grounding

## Module Research

Use module-level deep research to establish pathway boundaries, missing steps,
candidate members, and known variants. When the task is species/pathway
satisfiability, research the combination of module + pathway/accession + taxon
or species, not only the generic pathway.

Generated provider files must be produced by the configured commands. Do not
write original prose and name it `*-deep-research-<provider>.md`. If provider
research is unavailable or manual triage is needed, write notes in a normal
project/gene/module notes file or use a clearly manual filename.

Known commands from `modules/README.md`:

```bash
just module-deep-research-perplexity peroxisome-lifecycle
just module-deep-research-openai modules/gluconeogenesis.yaml
```

If a different provider is wired in locally, follow the repo's just recipes and
record the provider-specific output path in evidence.

## Gene Review Integration

For concrete UniProt members:

- ensure the corresponding gene review exists when the module relies on that
  member;
- read the gene review's accepted core functions, non-core context, proposed
  terms, and notes;
- do not use module curation to silently override a gene review; record
  disagreements as knowledge gaps or follow-up questions;
- run `just fetch-gene <species> <gene>` only when creating a missing review
  scaffold is part of the task.

For Pseudomonas putida KT2440, the species directory is `PSEPK`.

## Identifier Discipline

- Never guess GO, UniProt, PANTHER, PTN, Rhea, ChEBI, PMID, taxon, or gene
  identifiers.
- Prefer local derived files first: gene `*-uniprot.txt`, `*-goa.tsv`,
  `interpro/panther/**`, `gocams/index.tsv`, cached GO-CAMs, and cached
  publications.
- If local files are insufficient and the identifier may have changed, look it
  up from an authoritative source.
- For GO term placement, check the aspect: MF terms belong in annoton
  `function`, BP terms in module/process concepts or annoton `processes`, and CC
  terms in context or locations.

## Evidence Placement

- Put top-level `evidence` on the `ModuleReview` for sources supporting the
  overall module boundary.
- Put node/part/annoton evidence as close as possible to the claim it supports.
- Use `notes` for curator rationale and caveats; use `knowledge_gaps` for open
  biological or curation questions.
- Keep project-history commentary in `projects/**`, not in reusable module
  descriptions.
