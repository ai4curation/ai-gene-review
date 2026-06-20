---
title: "NCBIFAM → GO Annotation Gain"
---

# NCBIFAM → GO Annotation Gain

**Parent project:** [NCBIFam.md](../NCBIFam.md)

How many GO annotations would be **gained** if NCBIFAM's own NCBI-curated
`go_terms` (from `hmm_PGAP.tsv`) were ingested as an `ncbifam2go` mapping and
propagated to every UniProtKB entry that already carries the family signature?
This is the NCBIFAM analog of [RHEA-ANNOTATION-GAIN.md](../RHEA/RHEA-ANNOTATION-GAIN.md),
computed live by [`ncbifam_go_gain.py`](ncbifam_go_gain.py).

## Method

For each NCBIFAM model with a GO term:

```
gain = N(xref:ncbifam-<id>) − N(xref:ncbifam-<id> AND go:<id>)
```

against the UniProtKB REST API (`x-total-results`, no records fetched). UniProt's
`go:` query is **closure-aware** (matches the term *and its descendants*), so a
family whose GO term is already covered by a more specific child counts as **no
gain** — the gain is closure-filtered, not naive exact-match. Gain is reported for
**Swiss-Prot (reviewed)** — the curation-relevant, trustworthy number — and for
all of UniProtKB (mostly automated TrEMBL) as context.

## Headline: the gain is real but lives in TrEMBL, not Swiss-Prot

Two deterministic samples of `equivalog` models with a single GO term:

| Sample | Models | Σ gain reviewed (Swiss-Prot) | Σ gain all UniProtKB |
|--------|-------:|----------------------------:|---------------------:|
| 25-model | 25 | 4 | 8,385 |
| 60-model | 60 | 19 | 26,578 |

**The curation-relevant (reviewed) gain is small; the all-UniProtKB gain is
large.** This is the opposite emphasis from RHEA (which gained ~42 *reviewed*
annotations). The reason is structural: NCBIFAM is **prokaryote-heavy**, and
Swiss-Prot's curated prokaryotic enzymes already carry the GO term (often added by
hand or via the InterPro route), whereas the millions of **unreviewed TrEMBL**
entries carrying the same signature do not. So ingesting `ncbifam2go` would mostly
improve automated annotation depth, with a modest but non-zero curated-entry gain
concentrated in newer biology.

⚠️ The all-UniProtKB numbers inherit the reliability of automated annotation and
should not be extrapolated naively to "true gaps" — they are an upper bound on
propagation volume, not a count of curation-ready additions.

## Where the gap concentrates — mobile elements, defense, secretion, division

Top propagation gaps in the 60-model `equivalog` sample (`gain_all` = entries
carrying the signature that lack the GO term or any descendant):

| Family | GO | N(sig) | gain (all) | gain (rev) | What it is |
|--------|----|-------:|-----------:|-----------:|------------|
| NCBIFAM:NF033545 | GO:0004803 transposase activity | 18,881 | 18,874 | 2 | IS630 family transposase |
| NCBIFAM:TIGR00439 | GO:0000910 cytokinesis | 3,306 | 3,304 | 5 | permease-like cell division protein FtsX |
| NCBIFAM:NF041162 | GO:0140737 encapsulin nanocompartment | 901 | 897 | 0 | family 2A encapsulin shell protein |
| NCBIFAM:TIGR03744 | GO:0005524 ATP binding | 706 | 694 | 0 | conjugative transfer ATPase |
| NCBIFAM:TIGR02165 | GO:0043571 …CRISPR… | 432 | 432 | 0 | type I-G CRISPR protein Csb2 |
| NCBIFAM:TIGR02878 | GO:0030436 sporulation | 298 | 298 | 1 | sporulation protein YpjB |
| NCBIFAM:TIGR02791 | GO:0043684 type IV secretion system complex | 298 | 298 | 4 | P-type DNA transfer protein VirB5 |
| NCBIFAM:NF042963 | GO:0051607 defense response to virus | 151 | 151 | 0 | anti-phage DUF1156 protein |

The pattern is consistent: **transposases / IS elements, conjugation and type
III/IV/VI secretion, CRISPR and anti-phage defense, sporulation, encapsulins, cell
division** — the mobile-genetic-element and microbial-defense biology where
InterPro integration of the NCBIFAM signature lags, so NCBIFAM's own GO assignment
never propagates. Several even show a **reviewed** gap (FtsX 5, VirB5 4), i.e.
Swiss-Prot entries that are missing the term too — the cleanest gap-fill targets.

## The verification caveat is mandatory

NCBIFAM's `go_terms` are NCBI-assigned and **not** automatically current or correct.
Three distinct failure modes turned up while building the 28-row seed, each of which
a naive bulk ingest would have propagated:

- **Obsolete** — `GO:0009448` on a GABA transaminase is an obsolete id.
- **Outright wrong** — the diacylglycerol-kinase model **NF009874** (EC 2.7.1.107)
  is tagged `GO:0003951 NAD+ kinase activity`; the correct term `GO:0004143
  ATP-dependent diacylglycerol kinase activity` exists. A wrong-MF assignment, not
  just an altitude issue — excluded.
- **Altitude-broad** — several sit far above the family's real function, up to the
  ontology **near-root** `GO:0003824 catalytic activity` (enoyl-CoA hydratase
  NF005804, spermidine synthase TIGR00417), or a class parent (dGTPase NF002326 →
  `GO:0016793` when `GO:0008832 dGTPase activity` exists). Demoted to `broadMatch`
  with the specific child named.

So an `ncbifam2go` build must, like the curated seed in
[`ncbifam2go.sssom.yaml`](ncbifam2go.sssom.yaml):

1. drop obsolete **and incorrect** GO ids (check against EC where available),
2. prefer the specific child where the NCBI term is a broad parent (`broadMatch`),
3. EC-bridge-confirm enzyme rows via `ec2go`.

## Reproduce

```bash
uv run python ncbifam_go_gain.py --family-type equivalog --single-go --sample 60
uv run python ncbifam_go_gain.py --accessions NF033545.0,TIGR02791.1,TIGR00439.2
```
