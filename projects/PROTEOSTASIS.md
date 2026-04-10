---
species: [human]
---
# Human Proteostasis Network Project

## Working Premise

The Proteostasis Consortium workbook and survey manuscripts define a manually curated taxonomy of
the human proteostasis network (PN). This project uses that taxonomy as a systems scaffold for GO
review and project planning, not as direct GO annotation truth.

Existing GO annotations, primary literature, and local gene review YAMLs remain the basis for
annotation decisions. The PN dataset is most useful for scoping, prioritization, branch-aware
comparison, and identifying roles that may be missing or underrepresented in GO.

## Immediate Conclusions From Initial Triage

| Finding | Status | Notes |
|---------|--------|-------|
| Human UPB overlap with PN workbook | 33/33 genes | All human genes from `UNFOLDED_PROTEIN_BINDING` are present in the PN workbook |
| UPB vs PN consistency | 29/33 straightforward | Most corrected UPB calls fit the PN classification cleanly |
| Boundary cases | 4 genes | `AHSA1`, `AIP`, `GRPEL1`, `PTGES3` are proteostasis components but are broader than direct unfolded-protein binding |
| Added value beyond GOA | Real but uneven | Strongest value is curated systems placement and some cross-branch roles, not direct GO term replacement |

## Data Sources

- Human Proteostasis Network 2.0 workbook
- Survey manuscripts:
  - `Survey of the Human PN MS1 Translation Folding Transport`
  - `Survey of the Human PN MS2 ALP`
  - `Survey of the Human PN MS3 UPS`
- Existing GOA files and `*-ai-review.yaml` files in `genes/human/*`
- Existing `UNFOLDED_PROTEIN_BINDING` project as the overlap-first seed set

## How To Use The PN Data

1. Use the PN workbook as a curated proteostasis universe for prioritizing genes and interpreting
   large gene sets.
2. Use `Branch/Class/Group/Type/Subtype` to cluster genes by proteostasis role before doing
   detailed GO review.
3. Use workbook-only placements as candidate review leads:
   `check whether GOA is missing this biology`, not `import this as GO`.
4. Use multi-branch assignments to find proteostasis hubs that are likely to expose cross-system
   annotation issues.
5. Use the manuscripts to understand inclusion logic, scope boundaries, and why some branches are
   intentionally broader than strict quality-control biology.

Do not use the PN data as if it were:

- a direct GO annotation source
- sufficient evidence on its own for MF/BP assertions
- proof that a gene has direct unfolded-protein-binding or chaperone activity

## Workflow

### Phase 1: Overlap-First Seed Set

Start with the 33 human genes already reviewed in `UNFOLDED_PROTEIN_BINDING`.

For each gene, compare:

- existing GOA annotations
- current local review YAML
- corrected UPB interpretation
- PN Branch/Class/Group/Type/Subtype placement

Record one of four outcomes:

- `already_captured`: the corrected GO interpretation is already reflected in GOA or local review
- `candidate_missing_role`: the PN resource suggests a biologically plausible role not captured in GOA
- `pn_only_context`: the PN resource adds systems context but not a clean GO-annotatable role
- `scope_boundary_case`: the gene belongs in proteostasis broadly, but direct UPB/chaperone annotation would be too broad

First-pass priority genes:

- `HSPA1A`, `HSPA8`
- `DNAJB1`, `DNAJB6`
- `CLU`
- `SYVN1`, `UGGT1`
- `GRPEL1`
- `AHSA1`, `PTGES3`

These genes are the highest-yield set because they cover core chaperones, holdases,
chaperone-mediated autophagy, ER quality control, NEF biology, and HSP90-system boundary cases.

### Phase 2: Core Chaperone And Folding Modules

Expand from the overlap set into nearby PN modules:

- HSP70 system
- J-domain co-chaperones
- small HSPs / holdases
- HSP90 system
- CCT/TRiC and prefoldins
- nucleotide exchange factors and foldase/holdase handoff factors

Main questions:

- Is the core MF already captured precisely in GO?
- Does the PN classification reveal missing pathway context or secondary roles?
- Does the UPB review logic generalize cleanly to nearby family members?

### Phase 3: Proteostasis Boundary Modules

Review the modules most likely to produce over-annotation if handled naively:

- ER glycoproteostasis and ER quality-control sensors
- ERAD / retrotranslocation / p97-associated systems
- chaperone-mediated autophagy and CASA interfaces
- transport factors and organelle-specific QC machinery

Goal:

Separate direct chaperones and foldases from sensors, adaptors, transport factors, and degradation
machinery that are proteostasis-relevant but not equivalent to unfolded-protein binding.

### Phase 4: Multi-Branch Hub Analysis

Prioritize PN components that appear in multiple branches or with multiple distinct annotations.

These genes are especially useful for:

- cross-branch consistency checks
- finding non-core vs core annotations
- building project summaries that show how proteostasis subsystems connect

Initial hub-like examples to explore after the UPB overlap set:

- `VCP`
- `HSPA8`
- `SQSTM1`
- `SYVN1`
- `CLU`

### Phase 5: Ontology-Gap Capture

Track ontology gaps separately from routine curation.

Known gaps already exposed by the UPB project:

- holdase chaperone activity
- misfolded protein sensor activity
- co-chaperone MF representation

Rule:

Do not let NTR work block routine gene review. Standard review should continue while gap cases are
captured in a separate project section.

### Phase 6: Project Deliverables

- `PROTEOSTASIS.md` as the project overview and synthesis document
- branch-specific priority gene lists
- a PN-vs-GOA consistency table
- a candidate missing-role table
- a small ontology-gap registry
- a final synthesis explaining how PN taxonomy and GO annotations complement each other

## Suggested Working Tables

These do not need to exist yet, but they are the right artifacts to create early:

- `projects/PROTEOSTASIS/pn_upb_overlap_human.tsv`
- `projects/PROTEOSTASIS/priority_genes.tsv`
- `projects/PROTEOSTASIS/candidate_missing_roles.tsv`
- `projects/PROTEOSTASIS/ontology_gaps.md`

Recommended columns for the overlap table:

- `gene_symbol`
- `pn_branch`
- `pn_class`
- `pn_group`
- `upb_corrected_call`
- `goa_status`
- `verdict`
- `notes`

## Initial Biological Framing

This project should treat unfolded-protein binding as one mechanistic slice of proteostasis, not as
the definition of proteostasis itself.

That means:

- the UPB project supplies mechanistic precision
- the PN workbook supplies systems architecture
- the most informative work will come from genes that sit at the interface between chaperoning,
  transport, autophagy, ER quality control, and ubiquitin-mediated turnover

## Current Status

- [x] Create dedicated branch and worktree for `PROTEOSTASIS.md`
- [x] Review PN workbook structure and manuscript framing
- [x] Confirm complete overlap of the 33 human UPB genes with the PN workbook
- [x] Check first-pass consistency of corrected UPB calls against PN placement
- [ ] Create first overlap table for the 33 human genes
- [ ] Expand to branch seeds outside the 33-gene overlap set
- [ ] Capture candidate missing GO roles suggested by PN-only placements
- [ ] Draft a first branch-by-branch synthesis
