---
title: "NCBIFAM / CDD -> GO Methodology Notes"
---

# NCBIFAM / CDD → GO Methodology Notes

**Parent project:** [NCBIFam.md](../NCBIFam.md)

## The one route, and the one that is missing

NCBIFAM and CDD are **InterPro member databases**. In GOA they reach GO through a
single pipeline — InterPro integration → `interpro2go` → `GO_REF:0000002` — and
*nothing else*. There is **no public `ncbifam2go` or `cdd2go`** external2go file
(both 403 on `current.geneontology.org`; only `interpro2go` is served). So a
member signature contributes GO **only if it is integrated into an InterPro entry
that itself carries an `interpro2go` mapping.**

```bash
# the only GOA route for these sources
curl -sIL https://current.geneontology.org/ontology/external2go/interpro2go   # 200
curl -sIL https://current.geneontology.org/ontology/external2go/ncbifam2go    # 403 (does not exist)
curl -sIL https://current.geneontology.org/ontology/external2go/cdd2go        # 403 (does not exist)
```

| Direction | Question | Source of truth | Analog |
|-----------|----------|-----------------|--------|
| **Forward (contribution)** | Where is a `GO_REF:0000002` row carried by an InterPro entry whose evidence is an NCBIFAM/CDD signature, and is it informative? | GOA `GO_REF:0000002` rows + InterPro member integration | [SPKW](../SPKW/SPKW-METHODOLOGY.md), [RHEA](../RHEA/RHEA-METHODOLOGY.md) |
| **Reverse (gap)** | Where does NCBIFAM/CDD assert a function (GO/EC, or a precise family name) that never reaches GO? | NCBIFAM PGAP HMM metadata; unintegrated signatures | [RHEA](../RHEA.md) reverse gap |

## Masking — the GOA `GO_REF:0000002` row hides which member DB fired

This is the NCBIFAM/CDD analog of RHEA's "masked by EC". In a GOA row the
`WITH/FROM` field names the **integrated InterPro entry** (`InterPro:IPRnnnnnn`),
**not** the underlying member signature (`NCBIfam:TIGRnnnnn` / `NF.nnnnnn` or
`CDD:cdnnnnn`). Verified directly on this repo's gene set:

```bash
# every interpro2go row points at an IPR id, never at the member signature
grep -rhE "GO_REF:0000002" genes/ --include=*-goa.tsv | head    # WITH/FROM = InterPro:IPR...
grep -rhoE "(TIGR[0-9]{5}|NF[0-9]{6}|cd[0-9]{5})" genes/ --include=*-goa.tsv   # -> 0 hits
# yet the same proteins' UniProt records DO carry the signatures
grep -rhE "^DR   NCBIfam" genes/ --include=*-uniprot.txt | wc -l   # 1160
grep -rhE "^DR   CDD"     genes/ --include=*-uniprot.txt | wc -l   # 2174
```

So you cannot, from GOA alone, tell whether a `GO_REF:0000002` annotation owes to
an NCBIFAM equivalog (high-quality, 1:1 function-grounded) or to a broad CDD
domain — they are flattened into the same `InterPro:IPR…` provenance. Attributing
contribution to the member DB requires re-joining each annotation's InterPro entry to
its `member_databases` (InterPro API `entry/interpro/<IPR>`). This is **implemented**
in [`interpro_member_attribution.py`](interpro_member_attribution.py) and run over the
repo's gene set — see the [attribution result](../NCBIFam.md#un-masking-member-db-attribution-on-this-repos-annotations)
(NCBIFAM backs 13%, CDD 8%, of the repo's `GO_REF:0000002` rows; sole signature for
250 / 116).

## NCBIFAM has its own curated GO/EC that GO does not ingest

Unlike CDD (a domain/architecture resource), **NCBIFAM ships NCBI-curated
function on each model** — the reverse-gap goldmine. The PGAP HMM metadata
exposes `go_terms`, `ec_numbers`, `pmids`, `family_type`, and `product_name`
columns:

```bash
curl -sL https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv -o hmm_PGAP.tsv
head -1 hmm_PGAP.tsv | tr '\t' '\n' | nl   # cols 14=ec_numbers 15=go_terms 16=pmids
```

`family_type` is the curation-quality signal that makes this tractable:
**`equivalog`** (13,253 models) means *every* member has the same function, so
GO/EC transfer is safe — the ideal substrate for a curated `ncbifam2go` mapping,
exactly as RHEA's reviewed enzymes back the `rhea2go` gap-fill. `domain` /
`subfamily` models are weaker and need altitude care.

## The coverage gap — unintegrated signatures cannot propagate

A member signature that InterPro has **not** integrated has, by construction, no
`interpro2go` row and therefore contributes **zero** GO to GOA — the
NCBIFAM/CDD analog of RHEA's "no `rhea2go` line" reactions. Computed live from the
InterPro API:

```bash
for db in ncbifam cdd; do for s in "" integrated/ unintegrated/; do
  curl -sL "https://www.ebi.ac.uk/interpro/api/entry/${s}${db}/?page_size=1" \
    | grep -oE '"count":[0-9]+'; done; done
```

- **NCBIFAM: 7,447 / 18,511 integrated (40%); 11,064 unintegrated.**
- **CDD: 5,059 / 19,902 integrated (25%); 14,843 unintegrated.**

The unintegrated majority is the upper bound on the coverage gap; the curation
question is how many of those signatures carry a *real, GO-mappable* function
(for NCBIFAM, read it straight from the metadata `go_terms`/`product_name`).

## Reproducible probe

[`ncbifam_cdd_probe.py`](ncbifam_cdd_probe.py) computes every number above live
(stdlib `urllib` only, no go-db, no auth):

```bash
uv run python ncbifam_cdd_probe.py --stats              # all sections
uv run python ncbifam_cdd_probe.py --ncbifam-go          # PGAP GO/EC coverage
uv run python ncbifam_cdd_probe.py --interpro-coverage   # integration status
uv run python ncbifam_cdd_probe.py --interpro2go         # the GOA route
```

## Limitations in the web container

- The forward closure-filtered cross-organism contribution scan (which member DB
  is the *unique* source of a `GO_REF:0000002` term) needs the
  `~/repos/go-db/db/*.ddb` DuckDBs used by [UniPathway](../UNIPATHWAY.md)/[RHEA](../RHEA.md);
  these are **not present** in the web container, so that table is **staged**. The
  PGAP-metadata, InterPro-integration, and `interpro2go` numbers are computed live.
- InterPro ingests only a curated **subset** of NCBIFAM, so the InterPro
  "ncbifam" total (18,511) is smaller than the full PGAP HMM collection (34,351);
  the two totals are not directly subtractable without joining on accession
  (a staged follow-up).
