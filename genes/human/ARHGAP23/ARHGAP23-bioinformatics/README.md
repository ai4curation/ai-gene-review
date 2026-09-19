# ARHGAP23 bioinformatics

Three committed, re-runnable checks behind the ARHGAP23 review. `uv sync` first.

| command | what it does |
|---|---|
| `uv run python analyze_arhgap23.py` | regenerates `results.json` and `RESULTS.md` |
| `uv run python analyze_arhgap23.py --self-test` | mutates the inputs and asserts each guard fires with its expected message |
| `uv run python mutation_test.py` | breaks each guard in a copy of the analysis and asserts the self-test catches it **by its own named guard**, plus no-op negative controls that must stay silent |
| `uv run python mutation_test.py --self-check` | exercises the harness's own protection layer: creates and modifies files and requires them to be reported with the right verb and repaired byte-for-byte |
| `uv run python check_file_quotes.py` | asserts every `file:` and `Reactome:` quote in the review YAML is verbatim in the file it cites — the citations CI does not check |
| `uv run python check_file_quotes.py --self-test` | fabricates a quote and asserts rejection; rewraps a real one and asserts acceptance |
| `uv run python check_ontology_claims.py` | re-verifies the four load-bearing ontology claims on **two** services (OLS4 and `api.geneontology.org`); a disagreement between them is a failure |
| `uv run python check_ontology_claims.py --self-test` | runs each claim predicate against a case whose answer is the opposite, so a pass is evidence of discrimination |

## The ontology claims

`GO:0005100` "Rho GTPase activator activity" is obsolete/merged into `GO:0005096`, which has
no `is_a` children — that is why the review cannot specialise either Reactome `GO:0005096` row
and records an ONTOLOGY knowledge gap instead. `GO:0035024` and `GO:0035021` are descendants of
`GO:0051056` and **not** of `GO:0007165`, which is why the `GO:0007165` row is a branch change
rather than a specialisation. Two services are used deliberately: they disagree in practice, and
QuickGO in particular silently resolves merged ids and answers for the surviving term, so it
cannot be read at face value in either direction.

## What the analysis answers

Whether ARHGAP23's RhoGAP domain retains the catalytic arginine finger, verified
**reciprocally** against a structurally resolved comparator (ARHGAP1 / PDB 1TX4) and
calibrated against controls that are known to be GAP-dead in two different ways — one that
lost the residue (OCRL) and one that kept it (ARHGAP11B). Each control's status is proved
from the repo's own GOA tables or the fetched UniProt record before the report is allowed to
describe it that way; an unverifiable credential aborts the run.

The answer is *retained*, and the report is explicit that this is worth less than it looks:
one of the two GAP-dead controls passes the same test. The result that does carry
information is that at the 25 GAP:GTPase interface positions computed from 1TX4, ARHGAP23
matches the experimentally active paralog ARHGAP21 residue-for-residue at 22.

A fifth section parses the publisher's open Source Data and Supplementary Information for
PMID:32203420 (paywalled, absent from PMC) to recover ARHGAP23's measured substrate profile
and to check the residue targeted by its published "arginine finger mutant". The mutant
designation is read out of the supplementary PDF by regex rather than written here, so the
residue number the section turns on cannot come from the author of this script.

## Network

Everything is fetched and cached under `cache/` (gitignored): UniProt REST, RCSB
(`1tx4.cif`) and the Springer supplementary files. A fetch failure is a hard error naming the
fix; there is no offline fallback and no silently degraded section.
