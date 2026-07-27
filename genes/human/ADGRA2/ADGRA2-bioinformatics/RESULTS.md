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

## Guards, and how to break-test them

`check_corrections.py --self-test`, `check_coverage.py --self-test` and
`interpro_signatures.py --self-test` each exercise their guard
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
