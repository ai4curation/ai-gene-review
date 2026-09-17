# ARFGEF3 bioinformatics

Reproducible analyses supporting the human ARFGEF3 (BIG3) GO annotation review.
Findings are written up in [RESULTS.md](RESULTS.md).

## Run

Requires `mafft` on `PATH` (`brew install mafft`). All data is fetched live from
the UniProt and QuickGO REST APIs; `cache/` is a disposable HTTP cache and is
gitignored, so deleting it re-derives every number from the services.

```bash
cd genes/human/ARFGEF3/ARFGEF3-bioinformatics

# 1. Resolve every WITH/FROM token in the GOA file and query each IBA donor's
#    own evidence for the term it donates. Must run first: step 2 builds its
#    comparison panel from this step's output.
uv run --no-project --with requests --with biopython python resolve_withfrom.py

# 2. Ask whether ARFGEF3's Sec7 domain retains the catalytic glutamate.
uv run --no-project --with requests --with biopython python sec7_catalytic_check.py

# 3. Controls. Exits non-zero if any guard fails.
uv run --no-project --with requests --with biopython python sec7_catalytic_check.py --self-test

# 4. Are the UniProt-SubCell-derived CC rows in the right GO branch?
#    Independent of steps 1-3; can be run on its own.
uv run --no-project --with requests python subcell_mapping_check.py
```

## Design notes

- **Nothing is hand-assigned.** The comparison panel comes from the GOA WITH/FROM
  field, and the glutamic-finger alignment column is derived from the known-active
  donors rather than hardcoded.
- **The check must be able to fail.** A catalytic-residue analysis with no
  known-dead comparator cannot distinguish "the method finds Glu wherever it looks"
  from "this protein lost it", so a Glu→Ala mutant of a verified-active paralogue
  is scored alongside the real sequences and appears in the published table.
- **Loud failure over silent degradation.** Missing inputs raise and name the
  command that regenerates them; a deleted UniProt accession (which returns an
  empty record indistinguishable from a protein with no annotations) raises rather
  than being reported as a zero; a truncated QuickGO page raises rather than being
  read as a complete answer.
- **Ambiguity is data.** MOD ids that map to several UniProt entries are reported
  with their hit count instead of being collapsed to the first hit.
