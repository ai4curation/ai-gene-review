---
title: "TCDB -> GO Methodology Notes"
---

# TCDB → GO Methodology Notes

**Parent project:** [TCDB.md](../TCDB.md)

## What exists, and what doesn't

Two separate things are easy to conflate:

1. **TC references on GO terms — these exist, but are neglected leads.** GO
   carries TC references on molecular-function terms, as term-level `xref: TC:`
   clauses and as definition dbxrefs (`def: "…" [TC:…]`). These are largely
   neglected and the term-vs-definition distinction is not meaningful, so treat
   both alike, as **sources**. Extract them from `go-basic.obo`:

   ```bash
   uv run python extract_go_tc_xrefs.py --stats
   # 202 TC references on 170 non-obsolete MF terms / 185 TC systems / 63 families
   uv run python extract_go_tc_xrefs.py -o tc2go.from_go.sssom.yaml
   ```

   Every emitted row is `skos:relatedMatch` + `semapv:UnspecifiedMatching` — an
   unreviewed lead. Whether it is safe to **propagate** (a protein with the TC id
   inheriting the GO term) is curated by hand, per entry, in `tc2go.sssom.yaml`,
   whose header documents the propagation rule: `exactMatch` when the member set
   is mono-specific at the cited TC level (usually a 5-level system, e.g.
   `TC:2.A.22.1.1` SERT → `GO:0005335`), `narrowMatch` when the GO term is only a
   subfamily property (usually a 3-level family) and must not propagate wholesale.

2. **An `external2go` *annotation pipeline* — this does not exist.** Every other
   source-audit project here hangs off a public mapping file (`ec2go`, `rhea2go`,
   `interpro2go`, …); TCDB has none:

   ```bash
   # ec2go, rhea2go, ... are present; tc2go is not
   curl -sL http://current.geneontology.org/ontology/external2go/ | grep -o 'external2go/[a-z0-9_]*' | sort -u
   curl -sIL http://current.geneontology.org/ontology/external2go/tc2go   # no such file
   ```

So GO's curated term-xrefs are **never propagated to the proteins** that carry a
`DR TCDB;` cross-reference — there is no forward `GO_REF` volume (as there is for
RHEA's `GO_REF:0000116`). That reframes the project: the mapping partly exists,
but the *pipeline* is missing, so we (a) extract GO's existing xrefs, (b)
characterise the extra material TCDB publishes in `go.py`, and (c) measure the
structural protein-level gap that the missing pipeline leaves behind.

## Direction 1 — What TCDB publishes: the `go.py` dump

TCDB serves its own per-protein GO associations as a flat TSV:

```bash
curl -sL https://tcdb.org/cgi-bin/projectv/public/go.py -o tcdb_go.tsv
# format:  GO-id <TAB> TC-number(5-level) <TAB> family-name
head -1 tcdb_go.tsv
# GO:0008076	1.A.1.1.1	The Voltage-gated Ion Channel (VIC) Superfamily
```

This is **not a curated mapping** — it is an aggregation of the GO terms found on
the member proteins of each TC system, so a single TC number carries a bag of GO
terms spanning all three aspects (a channel *activity* MF, its
`plasma membrane`/`integral component of membrane` CC, its `transmembrane
transport` BP, and incidental `protein binding`). To turn it into a `tc2go`
candidate we keep only the **transporter-activity molecular-function** slice:

```bash
uv run python tcdb_go_probe.py --tcdb-go   # rows, distinct TC/GO, aspect skew, noise
```

The MF filter uses the `is_a` closure of the two transporter-activity roots,
fetched live from QuickGO (no local go-db needed):

```bash
curl -sL 'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0022857/descendants?relations=is_a'
curl -sL 'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005215/descendants?relations=is_a'
```

Only ~13% of `go.py` rows survive this filter. [`build_tc2go.py`](build_tc2go.py)
then aggregates the surviving 5-level TC numbers up to the **TC family** (3-level),
attaches the current QuickGO label, drops obsolete terms, and emits SSSOM:
`exactMatch` when a family has a single surviving MF term (mono-specific),
`narrowMatch` when it has several (poly-specific → the term is a subfamily
property). Mirrors [`GLYCOBIOLOGY/build_cazy2go.py`](../GLYCOBIOLOGY/build_cazy2go.py).

```bash
uv run python build_tc2go.py --min-support 2 -o tc2go.generated.sssom.yaml
```

## Direction 2 — Reverse gap ("falls through the cracks")

A UniProtKB entry can carry a TCDB cross-reference and yet have **no GO
transporter-activity term**. With no `tc2go`, this is the expected steady state,
and its size is the argument for building one. Measured directly from the UniProt
REST API — no go-db required:

```bash
# reviewed entries carrying any TCDB xref
curl -sIL 'https://rest.uniprot.org/uniprotkb/search?query=(database:tcdb)+AND+(reviewed:true)&size=0' | grep -i x-total-results
# ...of those, how many lack a transporter-activity MF term (GO:0005215 closure)
curl -sIL 'https://rest.uniprot.org/uniprotkb/search?query=(database:tcdb)+AND+(reviewed:true)+NOT+(go:0005215)&size=0' | grep -i x-total-results
```

`tcdb_go_probe.py --gap` automates this. **UniProt's `go:<id>` query field expands
to descendants**, so these counts are already ontology-closure-filtered *on the GO
side* (verified: `go:0005215` root returns more entries than the mid-level child
`go:0015075`).

### Why an entry falls through the cracks

1. **No pipeline.** The dominant cause here, unlike RHEA. A transporter with no
   EC (most secondary transporters) and no informative InterPro2GO term has no
   automated route to a transport MF term.
2. **Specificity mismatch (confounder — not a true gap).** The entry may carry a
   *more specific* transport MF child, or a transport **BP** term
   (`transmembrane transport`) / channel **CC** term, none of which the exact
   `GO:0005215`-MF-closure count credits.
3. **Family poly-specificity.** Even a hypothetical family-level `tc2go` would
   often supply only a generic parent; the substrate-specific child needs the
   4/5-level TC id.

### The closure caveat is mandatory

The gap headline in [TCDB.md](../TCDB.md) is **exact-match against the
`GO:0005215` MF branch**, so `pct_missing` is an **upper bound**. The honest next
step is a cross-branch closure filter: subtract entries carrying any transport MF
descendant, any transport-process BP term, or any transporter/channel-complex CC
term before calling an annotation a true gap. This is the identical lesson the
RHEA, CAZy, and SPKW projects learned: **naive counts overstate the signal.**

## Reproducibility & limitations

- Everything is fetched live: `go.py` from TCDB, the MF closure from QuickGO, the
  gap counts from UniProt REST. The go.py dump is cached to
  [`data/tcdb_go.tsv`](data/tcdb_go.tsv) for offline re-analysis; delete it (or
  pass a refresh) to re-fetch.
- No `~/repos/go-db` DuckDBs are required (unlike the RHEA forward
  cross-organism scan) — the whole probe runs anywhere with network access.
- The generated SSSOM aggregates to the **3-level TC family**; poly-specific
  families therefore emit multiple `narrowMatch` rows. A subfamily-level (4/5)
  rebuild is a follow-up target (see parent page).
- GO label validation uses the repo's pinned ontology cache; when GO renames a
  term (e.g. `GO:0008982` sugar→carbohydrate phosphotransferase) the cache is
  refreshed to the current `rdfs:label`. Validate with `just validate-tcdb-mappings`.
