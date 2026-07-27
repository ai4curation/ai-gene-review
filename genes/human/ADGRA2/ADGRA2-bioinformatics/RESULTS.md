# ADGRA2 bioinformatics — index

Hand-written index only. It deliberately **does not restate any number**: the numbers live in
the JSON outputs each script writes, and the interpretation lives in `../ADGRA2-notes.md`.
Duplicating figures here would create a fourth surface to drift, which is the failure this
campaign has hit most often.

Every script re-runs from the repo with no arguments beyond those shown, and each writes its
JSON next to itself.

| script | question | output | how to re-run |
|---|---|---|---|
| `node_reach.py` | Which genes does each PANTHER node in ADGRA2's IBA WITH/FROM actually reach, and which terms did it give them? | `node_reach.json` | `python3 node_reach.py` |
| `resolve_partners.py` | Who are the `GO:0005515` partners, are they reviewed canonical entries, and do they carry PDZ domains? | `partners.json` | `python3 resolve_partners.py ../ADGRA2-goa.tsv` |
| `check_corrections.py` | Does any cited PMID carry a retraction, erratum, expression of concern or Crossref correction? | `corrections.json` | `python3 check_corrections.py --json corrections.json <PMIDs>` |
| `check_coverage.py` | Does the review cover every GOA row exactly once, with no duplicate YAML keys or aliases? | — (exit status) | `python3 check_coverage.py` |
| `interpro_signatures.py` | Which InterPro signature licenses which GO term, and do the review's labels match InterPro? | `interpro_signatures.json` | `python3 interpro_signatures.py` |
| `projection_test.py` | Is the GDB `TAS` block a projection, and do the pseudogenes really receive the molecular function? | `projection_test.json` | `python3 projection_test.py` |
| `check_action_prose.py` | Does every annotation's prose name the action that annotation actually has, and does any reason argue a point twice? | — (exit status) | `python3 check_action_prose.py` |

## What each one found

Qualitative only — the figures live in the JSON, so there is no second surface to drift.

- **`node_reach.py`** — *negative for a defect.* The node whose human reach is exactly ADGRA2 gave
  it exactly ADGRA2's characterised biology; the generic terms sit at the heterogeneous family node.
  Specific-at-ortholog, generic-at-family is the correct direction. A null result is a finding: it
  tells the next reviewer the check was run, not skipped.
- **`resolve_partners.py`** — *every* `GO:0005515` partner is a reviewed Swiss-Prot entry at
  canonical length carrying PDZ domains, from two independent PDZ-motif assays against one
  C-terminal motif. No TrEMBL or ORFeome substitution. This is what converts bare `protein binding`
  into `GO:0030165 PDZ domain binding` rather than into a list of biological interactors.
- **`interpro_signatures.py`** — the entry covering ADGRA2's transmembrane bundle also covers
  Frizzled proteins, and `interpro2go` deliberately maps it only to generic terms. The
  GPCR-activity claim comes instead from the family-2 **extracellular hormone-receptor** entries,
  i.e. a peptide-hormone ligand-recognition signature, on a receptor with no ligand.
- **`projection_test.py`** — the GDB `TAS` block is a projection: uniform evidence and assigner
  across every entity, one generic triple, no perturbed gene anywhere because the reference runs no
  functional assay. The per-entity matrix also settles the pseudogene sub-claim in the direction the
  review needs — the entities missing the molecular-function term are protein-coding, so both
  pseudogenes are among the recipients rather than among the omissions. This is the load-bearing
  evidence for the two `REMOVE` verdicts.
- **`check_corrections.py`** — no retraction and no expression of concern on any cited PMID; one
  Author Correction, which nothing in the review depends on.
- **`check_coverage.py`** / **`check_action_prose.py`** — invariant checks rather than analyses; they
  found real defects in the review itself (a collapsed GOA row set, and an over-annotation sentence
  sitting on a `REMOVE` row) and now prevent both from recurring.

## Guards, and how to break-test them

`check_corrections.py`, `check_coverage.py`, `interpro_signatures.py`, `projection_test.py`
and `check_action_prose.py` all take `--self-test`, and each exercises its guard
in **both** directions — damage must be detected, and the clean file must pass. A self-test that
only proves failure detection cannot tell you the happy path works, and an agreement check that
fails on perfect agreement is a defect this campaign has actually seen.

`node_reach.py` and `resolve_partners.py` carry inline assertions rather than a self-test:

- `node_reach.py` asserts `numberOfHits == len(results)` after paging. This is not decoration.
  QuickGO caps this endpoint at 100 results per page and **clamps rather than erroring** on a
  larger `limit`, so a single `limit=200` request on `PTN001738137` returns 200 of 348 rows and
  looks complete. Under that truncation human ADGRA1 and ADGRA3 are absent from the result, which
  reads exactly like the known "family node misses the human paralogs" defect. The assertion is
  what turned that false positive back into a non-finding.
- `resolve_partners.py` builds its partner list from the GOA TSV rather than by hand, asserts the
  resolved count matches the parsed count, fails loudly on an accession that returns no name
  (a deleted UniProt entry is otherwise indistinguishable from an unannotated one), and tests
  Swiss-Prot status with `entryType.startswith("UniProtKB reviewed")` — because `"reviewed" in
  entryType` also matches `"unreviewed"` and silently promotes every TrEMBL entry to reviewed.
