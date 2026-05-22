# Ergothioneine Biosynthesis Variant-Pathway Terms — Obsoletion

## Overview

A GO obsoletion retires the two variant-pathway children of
GO:0052699 ergothioneine biosynthetic process. These children encode
*how* ergothioneine is made (bacterial vs fungal route), which is a
level of pathway-variant detail that upstream curators have decided is
beyond GO scope (better captured by MetaCyc pathways or GO-CAMs). All
affected annotations move to the parent term.

- **GO:0052704 ergothioneine biosynthesis from histidine via gamma-glutamyl-hercynylcysteine sulfoxide** (BP, bacterial route, *still active* — awaiting annotation migration)
- **GO:0140479 ergothioneine biosynthesis from histidine via hercynylcysteine sulfoxide synthase** (BP, fungal route, **already obsolete** — had zero direct annotations)

Both replaced by:

- **GO:0052699 ergothioneine biosynthetic process** (BP, active)

Per the upstream ontology decision, the two MetaCyc variant pathways
(`MetaCyc:PWY-7255` ergothioneine biosynthesis I (bacteria) and
`MetaCyc:PWY-7550` ergothioneine biosynthesis II (fungi)) are added as
`narrowMatch` cross-references on GO:0052699 rather than being
preserved as distinct GO classes.

This project tracks the impact on AI Gene Review. No genes in scope are
currently reviewed here.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6402](https://github.com/geneontology/go-annotation/issues/6402) — **open**
- Ontology ticket: [geneontology/go-ontology#32018](https://github.com/geneontology/go-ontology/issues/32018) — **closed**
- Earlier note on the same problem: [geneontology/go-ontology#11163](https://github.com/geneontology/go-ontology/issues/11163)
- Affected annotations spreadsheet: [Google Sheet](https://docs.google.com/spreadsheets/d/1-DrrK_JPPMuU9Bzlp9jyG9b6bg2LpcDs5N06u2bPF-0/edit?gid=0#gid=0)
- Impacted groups (per upstream issue): UniProt — 4 annotations to GO:0052704

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Status | Replacement |
|---|---|---|---|
| ergothioneine biosynthesis ... via gamma-glutamyl-hercynylcysteine sulfoxide | GO:0052704 | active (migration pending) | GO:0052699 ergothioneine biosynthetic process |
| ergothioneine biosynthesis ... via hercynylcysteine sulfoxide synthase | GO:0140479 | already obsolete | GO:0052699 ergothioneine biosynthetic process |

The fungal-route term GO:0140479 carried **zero** direct experimental
annotations, so it was obsoleted directly. The bacterial-route term
GO:0052704 is still active because the four UniProt experimental
annotations (plus a large IEA pool) must be migrated to GO:0052699
before it can be retired — that migration is what go-annotation#6402
tracks.

## Affected experimental annotations (verified via QuickGO 2026-05-21)

All four direct experimental annotations are to **GO:0052704**, all on
genes of the *Mycolicibacterium smegmatis* mc(2)155 *egt* operon, all
IDA (ECO:0000314), all from the same study (PMID:20420449, the in vitro
reconstitution of the mycobacterial ergothioneine pathway), all
assigned by UniProt, qualifier `involved_in`.

| Gene | UniProt | Locus | Protein name | Taxon |
|---|---|---|---|---|
| egtB | A0R5N0 | MSMEG_6249 | Hercynine oxygenase (sulfoxide synthase) | NCBITaxon:246196 |
| egtC | A0R5M9 | MSMEG_6248 | Gamma-glutamyl-hercynylcysteine sulfoxide hydrolase | NCBITaxon:246196 |
| egtD | A0R5M8 | MSMEG_6247 | Histidine N-alpha-methyltransferase | NCBITaxon:246196 |
| egtE | A0R5M7 | MSMEG_6246 | Hercynylcysteine sulfoxide lyase | NCBITaxon:246196 |

NCBITaxon:246196 = *Mycolicibacterium smegmatis* (strain ATCC 700084 /
mc(2)155); UniProt mnemonic suffix `MYCS2`.

Each annotation simply moves to **GO:0052699 ergothioneine
biosynthetic process** — the obsoletion is terminological, not a change
of biology. The four enzymes catalyze consecutive steps of the same
pathway, so the parent BP term is the correct shared placement.

### IEA pool (auto-migrated)

GO:0052704 also carries roughly **2,247 IEA annotations** (mostly
`egtB` orthologs across bacteria) assigned via `GO_REF:0000108`
(automatic logical inference). These will be regenerated against
GO:0052699 automatically once GO:0052704 is obsoleted and the inference
pipeline re-runs — no per-annotation work is needed here.

### Parent-term annotations (unaffected)

GO:0052699 already carries 2 direct experimental annotations —
*Schizosaccharomyces pombe* `egt1` (O94632) and `egt2` (O94431), both
IMP from PMID:24828577. These are on the surviving parent term and are
**not** affected by the obsoletion.

## Impact on this repo

No genes annotated to GO:0052704 or GO:0140479 are currently reviewed
in this repo:

- `genes/MYCS2/` — does not exist (no *M. smegmatis* genes reviewed yet)
- `genes/SCHPO/egt1/`, `genes/SCHPO/egt2/` — do not exist

So **no existing review needs a refresh** for the obsoletion itself.
The opportunity is that the *M. smegmatis* *egt* operon is a compact,
well-characterized four-enzyme biosynthetic pathway with no coverage in
this repo, and the obsoletion is a natural trigger to add it.

## Scope

- **Organisms**: the four directly affected genes are all
  *M. smegmatis* mc(2)155. The fungal route (S. pombe egt1/egt2) is on
  the surviving parent term and is opportunistic, not required.
- **GO branches**: BP only — a variant-pathway-specificity collapse to
  the broader parent term. No MF or CC changes.
- **Type of fix**: terminological — the chemistry (histidine →
  ergothioneine) is unchanged. Reviews would confirm GO:0052699 is the
  right BP anchor and that each enzyme also has a precise cognate MF.

## Candidate genes for initial review

Verify each with `just fetch-gene MYCS2 <gene>` before starting and
confirm UniProt accessions. None are currently in the repo. The four
genes form one operon and are best reviewed together as a small batch.

### Tier 1 — direct experimental annotation, well-characterized

1. **egtD / A0R5M8** (MSMEG_6247) — histidine N-alpha-methyltransferase;
   catalyzes the first committed step, SAM-dependent triple methylation
   of L-histidine to hercynine. The cognate MF (a histidine
   N-methyltransferase activity) should anchor the review; BP anchors on
   GO:0052699 post-obsoletion.
2. **egtB / A0R5N0** (MSMEG_6249) — hercynine oxygenase / sulfoxide
   synthase; the signature non-heme-iron enzyme that forms the C–S bond
   between hercynine and cysteine (or gamma-glutamylcysteine). Most
   mechanistically studied step of the pathway.
3. **egtC / A0R5M9** (MSMEG_6248) — gamma-glutamyl-hercynylcysteine
   sulfoxide hydrolase; a glutamine-amidotransferase-class enzyme that
   removes the gamma-glutamyl group.
4. **egtE / A0R5M7** (MSMEG_6246) — hercynylcysteine sulfoxide lyase;
   PLP-dependent C–S lyase that produces ergothioneine in the final
   step.

All four are characterized in PMID:20420449 (Seebeck FP, 2010, *J Am
Chem Soc* — in vitro reconstitution of mycobacterial ergothioneine
biosynthesis), which is the single reference behind every affected
annotation.

### Tier 2 — opportunistic, fungal route

5. **egt1 / O94632** and **egt2 / O94431** (*S. pombe*) — already
   annotated to the surviving parent GO:0052699; not affected by the
   obsoletion. Reviewing them would extend SCHPO coverage but is not
   required by this ticket.

## Proposed approach

1. **Fungal obsoletion has already landed** (GO:0140479 is obsolete);
   the bacterial-route obsoletion (GO:0052704) is pending the
   annotation migration tracked in the still-open go-annotation#6402.
   The replacement target is unambiguous (the parent GO:0052699), so
   reviews can proceed now and simply anchor BP on GO:0052699.
2. **Review the four *M. smegmatis* *egt* genes as one batch.** Run
   `just fetch-gene MYCS2 egtD` (and egtB/egtC/egtE), then `/review`
   per CLAUDE.md. Because the four enzymes share one pathway and one
   reference (PMID:20420449), the literature work is largely shared.
3. **For each gene, anchor on the cognate molecular function** — the
   pathway membership (GO:0052699) is the BP; the per-enzyme catalytic
   activity (methyltransferase, oxygenase/sulfoxide synthase,
   amidotransferase/hydrolase, C–S lyase) is the more informative MF
   and should drive `core_functions`. Look up precise MF terms via the
   OLS MCP rather than guessing IDs.
4. **Do not create reviews for the ~2,247 IEA `egtB` orthologs** — they
   are auto-migrated by the logical-inference pipeline.
5. **Defer the S. pombe egt1/egt2 pair** unless SCHPO ergothioneine
   coverage is wanted independently; they are on the surviving parent
   term and unaffected.

## Priority

**Low-medium.** Only four direct experimental annotations are affected
and the migration is mechanical (variant-pathway term collapsed to its
parent). No existing review in this repo is blocked. The opportunity —
not the urgency — is that the *M. smegmatis* *egt* operon is a clean,
fully reconstituted four-enzyme pathway with a single well-cited
reference and no coverage here, making it an efficient small batch if
the repo wants to extend *Mycolicibacterium* coverage.

## Status

- 2026-05-21 — Project file created. Upstream annotation issue #6402
  open; ontology ticket #32018 closed. GO:0140479 (fungal route)
  already obsolete; GO:0052704 (bacterial route) still active pending
  migration of 4 UniProt experimental annotations + ~2,247 IEA to the
  parent GO:0052699. No gene reviews started in this repo for the
  *M. smegmatis* egtB/egtC/egtD/egtE operon.
